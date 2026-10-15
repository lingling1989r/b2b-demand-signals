# 多语言检索与回复

默认工作语言中文；未指定市场时先中文、英文，全球需求再按预算分批补日、韩、法、德。用户指定语言优先。语言覆盖仅代表实际执行查询的语言，不代表对应国家或市场已覆盖。

| 语言 | 求工具/服务 | 替代或变化 | 具体需求检索例 |
|---|---|---|---|
| 中文 zh | 求推荐、有没有好用的、需要、有偿求 | 替代、换供应商、交期不行 | 达人建联 工具 求推荐；1688 数据 API 求助 |
| 英文 en | looking for、any recommendations for、need help with | alternative to、switching from、got burned by | influencer discovery tool recommendations; product review data API |
| 日语 ja | おすすめ、探しています、教えてください | 乗り換え、代替、納期の遅れ | インフルエンサー リスト ツール おすすめ；商品レビュー データ 取得 |
| 韩语 ko | 추천해주세요、찾고 있습니다、필요합니다 | 대안、갈아타기、납기 지연 | 인플루언서 섭외 툴 추천；상품 리뷰 데이터 수집 |
| 法语 fr | je cherche、vous recommandez quoi、besoin de | alternative à、changer de fournisseur、retard de livraison | outil pour trouver des influenceurs; API avis produits |
| 德语 de | suche、kann jemand empfehlen、brauche | Alternative zu、Anbieter wechseln、Lieferverzug | Tool zur Influencer-Suche; Produktbewertungen Daten API |

先选真实买家所在社区，再把业务词与意图词组合。以上是可调整的自然语言词库，不是已验证的平台高级搜索语法。不要把外语整句或OR组合盲当接口运算符。搜索引擎/平台不支持语言过滤时用原文判断语言；无结果先查词义与覆盖，不直接宣布当地无需求。

1688补充阿里巴巴中文站、Chinese wholesale、1688 sourcing等当地常用写法，但供应链选品咨询不自动等于数据采购。KOL补充creator、influencer、UGC、达人/红人及当地自然表达。B2B补充lead generation、営業リード、잠재고객、prospection B2B、B2B-Kundengewinnung；泛泛销售经验和推广贴不能当本人需求。

每条保留source_language、query_language、reply_language、raw_text、translation_zh、translation_uncertainty、target_market、market_evidence。原文是证据，中文译文只方便阅读；预算币种、否定词、期限、已解决、求职与求服务区别要核。跨语言转帖用原始链接/ID去重，相似文案保留疑似模板标记。

多语言统一用同一as_of与7天/4小时窗口，不以本地日历天代替滚动窗口。保留原时区及规范化时间。翻译不提高ABC等级，无法判断关键意图时最多B待核；没有精确时间不进4小时快线。

回复优先原帖语言，先回应一两个具体问题，再提出匹配能力。给中文对照方便用户审核；不声称母语者身份，不夸大当地经验。专有产品名和URL保留。各语言采用适合社区的称呼与语气，不把中文销售口头禅逐字翻译。公开付费服务推广被禁的社区只给帮助，不塞链接；未核规则先标记。默认拟稿，语言覆盖不产生发送授权。

验收按语言报告：查询数、命中数、唯一记录、A/B/C、失败和截断。某语种失败或未检索必须单列，不能用其他语种结果填补。每条译文、等级、原文与回复可相互追回。
