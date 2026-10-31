# 只能选两样 · 

> 从来不及、会忘记到说不清——六个核心，看懂复杂世界的取舍
>
> **DOI**：10.5281/zenodo.23830302　·　概念 DOI：10.5281/zenodo.23440905　·　141 页 / 5 部分 / 19 章

看得见的世界背后，都有一张看不见的账单；这张账单只有三个价格——看得准、拼得上、传得下去，最多付得起两个。本书用“看见、记住、跟上、选择、讲述、临界”六个核心，把同一系列六本学术专著（《区分的语法》《遗忘的边界》《错位的时间》《选择的代价》《诠释的权衡》《涌现的临界》）的思想，写成一本从十岁到专家都能读完的通俗读本：每一部都配生活故事、公式直觉、可带走的做法与专家的证据边界，并配以可作图的图解与五分钟小实验；另设“十二个常见误解”“给老师、家长和孩子的一页”“一天里的六个核心”，让同一套尺子可以被课堂、家庭和一个人自己直接使用。这一版的共同地基写在卷首《总纲　现实中不存在无限》：不是先观察到六个领域都在取舍，而是有限承载者必须在描述、组合、传递之间分配同一份预算；六个核心是这一事实的六种显影。

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
只能选两样：从来不及、会忘记到说不清——六个核心，看懂复杂世界的取舍。李毅芃，2026。10.5281/zenodo.23830302
```

## 系列（九本书）

| 书 | 仓库 |
|---|---|
| 区分的语法 | [distinction-evolution](https://github.com/lyp0746/distinction-evolution) |
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
