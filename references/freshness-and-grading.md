# 时间与ABC分级

记录as_of、时区、请求窗口、原始时间、规范化时间、日期来源与精度。不要从帖子ID或更新时间猜发布时间。相对时间必须保存获取时刻；无法可靠换算则待核。

默认7天窗口。配套脚本接受window-days；历史截止默认max(30,4×窗口天数)，默认7天时为30天，也可显式设置archive-days，但不得短于窗口。用户改变窗口时，A/B时间边界和“近一周”标签要同步更新。

仅日期无时刻时视为一天的区间：跨越窗口边界最多B、待核；未来日期C、待核。完整时间缺时区不默认当UTC。缺日期的明确需求最多B，不宣称近期。

先判断排除条件：closed=true或account_inactive=true直接C/excluded；noise广告口令或service_fit=none也C/excluded。已解决、已有服务商、停止招募、注销须有原文/接口依据。

| 时间和适配 | 等级 | bucket |
|---|---|---|
| 窗口内，explicit具体需求，direct直接适配 | A | recent_workbench |
| 窗口内，general一般求助或indirect间接适配 | B | recent_workbench |
| 超窗口但未超历史截止，仍有需求且匹配 | B | historical_candidates |
| 无日期或边界精度待核 | B | date_pending |
| 未来/无效日期 | C | date_pending |
| 超历史截止 | C | archive |

explicit应能定位具体问题、目标或场景，不要求已有预算；direct指当前服务确实能帮这条问题，不是泛泛想象“这个人以后也许会需要”。两项由读原文后判断，脚本不推断。

示例：昨天求按关键词导出帖子，数据已核覆盖→A；两天前只问外贸怎么找客户→B；18天前明确找设备类YouTube名单→B历史；45天前有偿求助→C历史；三天前找SEO但已编辑为不需要→C排除；一年前主帖下两天前新评论可独立评级。
