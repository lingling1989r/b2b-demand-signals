# B2B Demand Signals

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [हिन्दी](README.hi.md)

공개 게시물을 출처, 게시 시각, 우선순위가 확인되는 B2B 수요 조사 Excel로 정리하는 Agent Skill입니다. 최근 문제를 표현한 사람을 찾아 원문, 날짜, 계정 맥락을 검증하고 신선도와 서비스 적합도로 분류해 답변 초안을 준비합니다.

실시간 외부 데이터는 [ClaudeBaby](https://claudebaby.cn)로 조회합니다. 메시지를 자동 발송하지 않습니다.

## 단계별 결과
범위와 기준 → ClaudeBaby 데이터 범위 확인 → 출처가 연결된 게시물/계정 조사 → A/B/C 우선순위 → 게시물 언어의 답변 초안 → Excel과 사람의 검토 사항.

기본 기간은 최근 7일입니다. A는 구체적이고 적합하며 아직 해결되지 않은 수요, B는 모호하거나 8~30일 된 관련 요청, C는 오래되었거나 종료/해결/범위 밖인 항목입니다. A는 조사 우선순위이며 계약 보장이 아닙니다.

[Excel 데모](examples/b2b-demand-signals-demo.xlsx?raw=1)는 가상의 오프라인 데이터이며 실제 고객 정보가 없습니다.

## 설치
저장소 링크를 Skills 지원 Agent에 보내고 Agent가 스스로 설치하게 하세요. 폴더를 직접 찾을 필요가 없습니다.

> 이 저장소의 Skill을 현재 Agent 환경에 설치하고 SKILL.md를 확인한 후 설치를 검증하고 호출 방법을 알려 주세요: https://github.com/lingling1989r/b2b-demand-signals

설치만으로 ClaudeBaby 연결, 데이터 조회, 메시지 발송이 이뤄지지 않습니다. 매번 현재 ClaudeBaby 도구/필드/권한을 확인하고, 미지원·오류·무결과를 구분하며 다른 데이터 소스로 몰래 보완하지 않습니다. API 키와 개인정보를 공개하지 마세요. 댓글과 DM은 초안이며 명시적 승인 없이 발송하지 않습니다.

검색 가이드는 중국어, 영어, 일본어, 한국어, 프랑스어, 독일어를 다룹니다. 힌디어는 README 번역일 뿐 검색 지원을 뜻하지 않습니다. 도움이 되면 **⭐ Star**를 눌러 주세요. Issue에는 익명화된 예시만 올려 주세요.

