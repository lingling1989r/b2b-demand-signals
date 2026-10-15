# 交付字段

核心字段：lead_id、platform、topic、evidence_type、parent_post_id、parent_published_at、post_or_comment_id、source_url、comment_locator、raw_text、published_at_raw、published_at、timestamp_precision、collected_at、as_of、window_start、window_end、window_applied_by、account_id、account_name、account_homepage、bio、public_business_contact、contact_source、account_status、demand_summary、demand_strength、service_fit、closed、account_inactive、grade、grade_reason、age_days、bucket、missing_fields、reply_draft、outreach_status。

时间过滤要记录原生参数与实际核对/本地过滤，不能只凭传参判定成功。账号是评论者时独立记录父帖作者。平台计数和实际读取条数分开。

## 默认Excel页

1. 近期回复工作台：窗口内A/B，等级后按日期倒序，含链接、原话、主页、回复、等级理由。
2. 线索与原文：完整证据和判断。
3. 账号与联系入口：工作相关公开资料，未知标未返回。
4. 历史候选与日期待核：旧B类与日期未知独立标记。
5. 排除与归档：C类原因分清过期/关闭/注销/不适配。
6. 查询与覆盖：关键词、排序、时间参数、页/游标、实际读取和失败。
7. 方法与口径：执行时刻、窗口、规则、能力边界、未发布状态。

媒体可加配图页；邮件/DM合作入口按任务需要增加。公开链接可点击；无评论直达链接时给父视频链接＋评论ID＋昵称＋原话。没有邮箱不猜。长文另放Markdown，不把固定行高当全文展示保证。

## 脚本输入

JSON数组，lead_id唯一；以下仅虚构离线样例：

```json
[{"lead_id":"demo-1","published_at":"2026-10-14T09:00:00+08:00","demand_strength":"explicit","service_fit":"direct","closed":false,"account_inactive":false}]
```

demand_strength只用explicit/general/noise；service_fit只用direct/indirect/none。必须先读原文完成标签，缺标签直接报错，不自动凑A级。published_at缺省表示未知；日期字符串按--timezone解释。完整时间须有时区。
