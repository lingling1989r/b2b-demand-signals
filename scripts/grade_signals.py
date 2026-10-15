"""Apply freshness caps to human-reviewed signals. No network or external writes."""
import argparse
import datetime as dt
import json
from pathlib import Path
from zoneinfo import ZoneInfo


def bounds(value, zone):
    if not value:
        return None
    if len(value) == 10:
        day = dt.date.fromisoformat(value)
        start = dt.datetime.combine(day, dt.time(), zone)
        return start, start + dt.timedelta(days=1) - dt.timedelta(microseconds=1)
    instant = dt.datetime.fromisoformat(value.replace('Z', '+00:00'))
    if instant.tzinfo is None:
        raise ValueError('full timestamp requires timezone')
    return instant, instant


def grade(row, as_of, zone, window_days=7, archive_days=30, fastlane_hours=4):
    if row.get('demand_strength') not in {'explicit', 'general', 'noise'}:
        raise ValueError('demand_strength must be explicit/general/noise')
    if row.get('service_fit') not in {'direct', 'indirect', 'none'}:
        raise ValueError('service_fit must be direct/indirect/none')
    for flag in ['closed', 'account_inactive']:
        if flag in row and not isinstance(row[flag], bool):
            raise ValueError(flag + ' must be boolean')
    result = dict(row, as_of=as_of.isoformat(), age_days=None, age_hours=None, fastlane=False)
    def emit(g, bucket, reason):
        if g == 'A' and result['age_hours'] is not None:
            result['fastlane'] = result['age_hours'] <= fastlane_hours
        return dict(result, grade=g, bucket=bucket, grade_reason=reason)
    if row.get('closed') or row.get('account_inactive'):
        return emit('C', 'excluded', '需求已关闭或账号注销；排除联系')
    if row['demand_strength'] == 'noise' or row['service_fit'] == 'none':
        return emit('C', 'excluded', '噪声或核心需求不适配')
    try:
        span = bounds(row.get('published_at'), zone)
    except (ValueError, TypeError, AttributeError):
        return emit('C', 'date_pending', '日期无效或完整时间缺少时区；待核')
    if span is None:
        return emit('B', 'date_pending', '无可核实的信号日期，不宣称近期')
    earliest, latest = span
    if earliest == latest:
        result['age_hours'] = (as_of - earliest).total_seconds() / 3600
    if earliest > as_of:
        return emit('C', 'date_pending', '日期晚于执行时刻；待核')
    latest = min(latest, as_of)
    result['age_days'] = round((as_of - earliest).total_seconds() / 86400, 4)
    start = as_of - dt.timedelta(days=window_days)
    archive_start = as_of - dt.timedelta(days=archive_days)
    if earliest < start <= latest:
        return emit('B', 'date_pending', '只有日期且跨窗口边界；需核时刻')
    if earliest < archive_start <= latest:
        return emit('C', 'date_pending', '只有日期且跨归档边界；需核时刻')
    if latest < archive_start:
        return emit('C', 'archive', '超过历史截止；旧信号归档')
    if latest < start:
        return emit('B', 'historical_candidates', '超过近期窗口，降级并单列历史候选')
    if row['demand_strength'] == 'explicit' and row['service_fit'] == 'direct':
        return emit('A', 'recent_workbench', '窗口内明确具体需求，直接适配且未关闭')
    return emit('B', 'recent_workbench', '窗口内一般求助或间接适配，先确认')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('--as-of', required=True, help='ISO timestamp with timezone')
    parser.add_argument('--timezone', default='Asia/Shanghai')
    parser.add_argument('--window-days', type=int, default=7)
    parser.add_argument('--archive-days', type=int)
    parser.add_argument('--fastlane-hours', type=float, default=4)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    archive_days = args.archive_days if args.archive_days is not None else max(30, 4 * args.window_days)
    if not 0 < args.fastlane_hours < float('inf'):
        parser.error('fastlane-hours must be finite and positive')
    if args.window_days <= 0 or archive_days < args.window_days:
        parser.error('window must be positive; archive must be >= window')
    try:
        as_of = dt.datetime.fromisoformat(args.as_of.replace('Z', '+00:00'))
        if as_of.tzinfo is None:
            raise ValueError('--as-of requires timezone')
        zone = ZoneInfo(args.timezone)
        rows = json.loads(args.input.read_text())
        if not isinstance(rows, list):
            raise ValueError('input must be a JSON array')
        ids = [r.get('lead_id') for r in rows]
        if any(not i for i in ids) or len(set(ids)) != len(ids):
            raise ValueError('lead_id must be present and unique')
        ranked = [grade(r, as_of, zone, args.window_days, archive_days, args.fastlane_hours) for r in rows]
    except (ValueError, TypeError, KeyError) as exc:
        parser.error(str(exc))
    ranked.sort(key=lambda r: (r['grade'], r['age_days'] is None,
                               r['age_days'] if r['age_days'] is not None else float('inf')))
    result = {'as_of': as_of.isoformat(), 'timezone': args.timezone,
              'window_start': (as_of - dt.timedelta(days=args.window_days)).isoformat(),
              'window_end': as_of.isoformat(), 'window_days': args.window_days,
              'archive_days': archive_days, 'fastlane_hours': args.fastlane_hours, 'rows': ranked}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps({'rows': len(ranked), 'grades': {g: sum(r['grade'] == g for r in ranked)
                                                  for g in ['A', 'B', 'C']}}, ensure_ascii=False))


if __name__ == '__main__':
    main()
