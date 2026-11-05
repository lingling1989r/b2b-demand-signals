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

## 快线与阶段追踪扩展

Reddit任务按[快线参考](reddit-fastlane.md)增加四页底稿。字段增加query_id、record_id、duplicate_of、stage、stage_decision、stage_reason、raw_response_path、raw_record_locator、community、coverage_truncated、budget_quote、urgency_quote、replacement_quote、identity_match_evidence、fastlane、age_hours、first_seen_at、positive_reply_at、draft_ready_at、sent_at、response_due_at。每个阶段保留未通过与待核记录；公开演示文件继续只用虚构数据，实际原始底稿留在私有交付中。

脚本自动计算fastlane：A级、精确带时区时间且不超过4小时；可用--fastlane-hours调整。该字段只表示时效优先，不生成预算/身份判断或自动发送。

## 多语言字段

增加source_language、query_language、reply_language、translation_zh、translation_uncertainty、target_market、market_evidence。原文与译文分列，查询覆盖按语种拆开统计；语言不自动推断国家，外币预算保留原币种。

## URL 发现与主页池字段

使用[URL 发现与竞品池](url-discovery-and-pools.md)时，增加 discovery_method（用户/搜索/池内）、discovery_query、search_engine、discovered_at、discovery_url、search_snippet、pool_id、pool_role、identity_match_evidence、verification_status、verification_tool、verified_at、verification_error、coverage_truncated。摘要与已核验 raw_text 分列；失败候选不生成采购等级，保留在待核区。

主页池底稿记录来源、归属/市场证据、纳入理由、最近采集时间及可用游标。查询与覆盖页分别记录候选 URL 数、去重数、尝试/成功读取数、实际读取帖子数、已核验需求数、失败与未覆盖范围，避免把搜索命中数当客户数。
