# 只能选两样 · 

> 从来不及、会忘记到说不清——六个核心，看懂复杂世界的取舍
>
> **DOI**：10.5281/zenodo.24239808　·　概念 DOI：10.5281/zenodo.23440905　·　185 页 / 5 部分 / 19 章

看得见的世界背后，都有一张看不见的账单；这张账单只有三个价格——看得准、拼得上、传得下去，最多付得起两个。本书用“看见、记住、跟上、选择、讲述、临界”六个核心，把同一系列六本学术专著（《区分的语言》《遗忘的边界》《错位的时间》《选择的代价》《诠释的权衡》《涌现的临界》）的思想，写成一本从十岁到专家都能读完的通俗读本：每一部都配生活故事、公式直觉、可带走的做法与专家的证据边界，并配以可作图的图解与五分钟小实验；另设“十二个常见误解”“给老师、家长和孩子的一页”“一天里的六个核心”，让同一套尺子可以被课堂、家庭和一个人自己直接使用。这一版的共同地基写在卷首《总纲　现实中不存在无限》：不是先观察到六个领域都在取舍，而是有限承载者必须在描述、组合、传递之间分配同一份预算；六个核心是这一事实的六种显影。

---

## 结构

| 部分 | 标题 | 章数 | 起 → 止 |
|---|---|---:|---|
| 1 | 第一部分　六个核心 | 6 | 看见：一切从划一道线开始 → 临界：什么时候会变天 |
| 2 | 第二部分　把它们合起来看 | 3 | 一天里的六个核心 → 六个人生决定：同一套尺子，六个路口 |
| 3 | 第三部分　常问与常误解 | 3 | 大白话问答：三十一个“为什么” → 与五种批评对话 |
| 4 | 第四部分　用在日子里 | 4 | 二十五个真实的人 → 一场三个人的谈话 |
| 5 | 第五部分　边界与复盘 | 3 | 给老师、家长和孩子的一页 → 一年之后：一次诚实的复盘 |

每章八段：主提问 → 场景开篇 → 导论 → 机制 → 表/图 → 反例 → 本章小结 → 一句话带走。
每个部分有满栏插图扉页（`assets/svg/part-NN.svg`）、一段部分导语与一段部分小结。

## 证据与自检

- 结论标注 **A/B/C** 证据等级与甲/乙/丙概念等级；结论强度不超过证据强度。
- 可证伪登记簿：`docs/preregistration/checkups.csv`（append-only）。
- 结构校阅：系列 lint 24 条规则，本书 **error 0 / warn 0**（见 `_series/lint/REPORT.md`）。

## 文件

| 路径 | 是什么 |
|---|---|
| `source/` | **唯一正文来源**（HTML）；`book.json` 元数据、`parts.json` 结构 |
| `analysis/` | 图表、统计、抓取脚本（可重跑） |
| `assets/` | 封面、SVG 图、CSS |
| `scripts/build.sh` | audit → 印刷 PDF → 电子版 → EPUB → Markdown |
| `docs/` | 方法、数据来源、缺口与登记簿 |

产物（`output/`、`release/`）不入库，可由 `source/` 重建。

## 引用

```
只能选两样：从来不及、会忘记到说不清——六个核心，看懂复杂世界的取舍。李毅芃，2026。10.5281/zenodo.23888220
```

## 系列（九本书）

| 书 | 仓库 |
|---|---|
| 区分的语言 | [distinction-evolution](https://github.com/lyp0746/distinction-evolution) |
| 遗忘的边界 | [capacity-cascade](https://github.com/lyp0746/capacity-cascade) |
| 错位的时间 | [entropy-spiral](https://github.com/lyp0746/entropy-spiral) |
| 选择的代价 | [impossibility-triangle](https://github.com/lyp0746/impossibility-triangle) |
| 诠释的权衡 | [interpretation-tradeoff](https://github.com/lyp0746/interpretation-tradeoff) |
| 涌现的临界 | [emergence-critical](https://github.com/lyp0746/emergence-critical) |
| 心灵的分岔 | [mind-forks](https://github.com/lyp0746/mind-forks) |
| 热点的账单 | [hotspot-bills](https://github.com/lyp0746/hotspot-bills) |

十四篇工作论文与全部条目的 DOI 见 [series-workspace](https://github.com/lyp0746/series-workspace)。

## 许可

正文与图件 CC BY 4.0；脚本 MIT。

<!-- viz-console -->
## 可视化阅读台 ｜ Reading console

这一件配了两个**离线单文件**：双击就能开，断网可用，零外部依赖、零服务器、零 API 账单。
Two offline single-file entries ship with this item. Double-click and it runs — no network, no server, no API bill.

| 入口 | 文件 | 体积 | 里面是什么 |
|---|---|---|---|
| 阅读页 | `assets/knowledge-tradeoffs-reader.html` | 522 KB | 三档切换（**骨架**＝只留标题与高亮框／**阅读**＝正文全显、表与证据折叠／**全展**＝全部展开，可用 Ctrl+F 搜全书表格）＋ **19 张章末审问卡** |
| 结构地图 | `assets/knowledge-tradeoffs-explorer.html` | 149 KB | 章际引用的 3D 螺旋、部 × 部矩阵、附录原表台账（按表号/章/单元格搜索）、图件账（SVG 内联，不缺图） |

- **审问卡**四行全部原文摘录，一个字不增写：`带走`（一句话带走／本章小结末句）／`打脸条件`（表 F.1、附录登记簿、或「反例与边界」节首段）／`封顶`（本章标过的 A/B/C 等级，没有就不印）／`动手`（【动手试试】）。右上角一键复制，粘到自己的 AI 里当严苛伴读。
  The audit card quotes four things verbatim — takeaway, falsification condition, evidence ceiling, hands-on prompt — and offers a one-click copy for your own AI, with the discipline written into the clipboard.
- **两页互跳**：阅读页顶部「结构地图 →」，结构地图工具栏「正文阅读页 →」，螺旋上点第 N 章直接落到 `#chN`。
- **算式装置**：12 站背包客（3¹² 穷举，页内跑出 473,721／0.58／2.16）。滑块上没有一个是编的系数，式子照抄正文，页内按钮可当场复算。
- **已验证**：`375px` 窄屏与桌面均无横向溢出；0 个 JS 报错；三档切换 10–40 ms（纯 CSS class，不遍历 DOM）。
- **Computational bench** — three sliders-plus-recompute devices (stationarity, entry equilibrium, ebb half-life) and a ten-limit degeneration table; every parameter is quoted from the text.
- 本件规模：正文 **19 章**；审问卡 **19 张**。
  Size: **19 chapters**, **19** audit cards.


## 可视化阅读台 / Reading console

`只能选两样` 每件都有两个入口，**离线单文件、断网可开、零外部依赖**：

| 入口 | 文件 | 里面是什么 |
|---|---|---|
| 阅读页 | [`assets/knowledge-tradeoffs-reader.html`](assets/knowledge-tradeoffs-reader.html) | 三档切换（骨架／阅读／全展）＋ 每章末尾「审问卡」（带走／打脸条件／封顶／动手，四行全部原文摘录，可一键复制给自己的 AI 当严苛伴读） |
| 结构地图 | [`assets/knowledge-tradeoffs-explorer.html`](assets/knowledge-tradeoffs-explorer.html) | 章际引用的 3D 螺旋、部 × 部矩阵、附录原表台账（可搜）、图件账 |

另含 **12 站背包客复算沙盘**（3¹² 穷举，页内当场跑出 473,721 / 0.58 / 2.16）。

两个页面顶部互跳；`375px` 窄屏与桌面都验过，0 外部请求。

Every item ships two offline single-file entries: a **reading console** (three density levels + a per-chapter audit card quoting the text verbatim) and a **structure map** (chapter-citation spiral, part × part matrix, appendix ledgers). No server, no external requests — double-click and it runs.

