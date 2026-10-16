# -*- coding: utf-8 -*-
"""make_figures.py — 《只能选两样》全部矢量插图（确定性生成）。

输出：assets/svg/fig-*.svg
风格与系列一致：白底、微软雅黑、标题居中、统一配色。
"""
import math
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "assets", "svg")

INK = "#1a1a1a"
GRY = "#666666"
BLU = "#2f6db0"
GRN = "#2e7d32"
ORG = "#ef6c00"
RED = "#c62828"
GLD = "#b8862f"
PNK = "#8e5a9c"
FONT = "Microsoft YaHei, PingFang SC, SimHei, sans-serif"


def head(w, h, title, sub=None):
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
         f'font-family="{FONT}">',
         f'<rect width="{w}" height="{h}" fill="#ffffff"/>',
         f'<text x="{w/2:.0f}" y="38" text-anchor="middle" font-size="22" font-weight="bold" fill="{INK}">{title}</text>']
    if sub:
        s.append(f'<text x="{w/2:.0f}" y="62" text-anchor="middle" font-size="14" fill="{GRY}">{sub}</text>')
    return s


def box(x, y, w, h, fill, stroke, rx=8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.4"/>'


def txt(x, y, t, size=14, fill=INK, anchor="middle", weight="normal", style=""):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="{fill}" '
            f'font-weight="{weight}"{(" " + style) if style else ""}>{t}</text>')


def arrow(x1, y1, x2, y2, color=GRY, w=2.0, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{color}" '
            f'stroke-width="{w}"{d} marker-end="url(#ah)"/>')


DEFS = (f'<defs><marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="3" '
        f'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 z" fill="{GRY}"/></marker>'
        f'<marker id="ahg" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" '
        f'markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 z" fill="{GLD}"/></marker></defs>')


def save(name, parts):
    svg = "\n".join(parts + ["</svg>"])
    with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote", name + ".svg")


# ----------------------------------------------------------------- 图 1 五核关系
def fig_five_core():
    W, H = 1000, 640
    s = head(W, H, "五个核心：同一笔账单的五个项目",
             "看见 · 记住 · 跟上 → 选择（至多取二）→ 讲述 → 元学习")
    s.append(DEFS)
    # 三个输入
    inputs = [("看见", "对象", "区分 / 二次型", 90, BLU),
              ("记住", "预算", "容量 / 压缩", 380, GRN),
              ("跟上", "时钟", "多尺度 / τ", 670, ORG)]
    for name, role, sub, x, col in inputs:
        s.append(box(x, 100, 240, 110, "#f5f7fa", col))
        s.append(txt(x + 120, 140, f"{name}（{role}）", 20, col, weight="bold"))
        s.append(txt(x + 120, 172, sub, 14, GRY))
        s.append(arrow(x + 120, 212, x + 120, 268, col))
    # 选择
    s.append(box(250, 270, 500, 120, "#fff8e1", GLD))
    s.append(txt(500, 312, "选择：C-A-T 不可能三角", 22, GLD, weight="bold"))
    s.append(txt(500, 342, "看得准（C）· 拼得上（A）· 传得下去（T）", 15, INK))
    s.append(txt(500, 372, "有限复杂度下，至多同时满足两个", 14, GRY))
    s.append(arrow(500, 392, 500, 446, GLD))
    # 讲述
    s.append(box(250, 450, 500, 80, "#f3e9f7", PNK))
    s.append(txt(500, 484, "讲述：诠释 ＝ 给竞争命题分配置信度", 19, PNK, weight="bold"))
    s.append(txt(500, 512, "把坐标系反过来，用在“我们如何讲述”上", 13, GRY))
    s.append(arrow(500, 532, 500, 580, GRY))
    s.append(box(150, 584, 700, 46, "#eef2f6", BLU))
    s.append(txt(500, 614, "元学习：观察 → 抽象 → 建模 → 应用 → 反馈 → 更新", 15, BLU))
    save("fig-five-core-map", s)


# ----------------------------------------------------------------- 图 2 三角与三张账单
def fig_triangle():
    W, H = 900, 680
    s = head(W, H, "不可能三角：三张账单",
             "完备 C / 可组合 A / 传递 T —— 至多同时满足两个")
    s.append(DEFS)
    cx, cy, R = 450, 290, 150

    def pt(deg):
        a = math.radians(deg)
        return cx + R * math.cos(a), cy + R * math.sin(a)
    xc, yc = pt(-90)
    xa, ya = pt(150)
    xt, yt = pt(30)
    s.append(f'<polygon points="{xc:.0f},{yc:.0f} {xa:.0f},{ya:.0f} {xt:.0f},{yt:.0f}" '
             f'fill="#f7f9fc" stroke="#9aa4b2" stroke-width="2"/>')
    s.append(f'<circle cx="{xc:.0f}" cy="{yc:.0f}" r="10" fill="{BLU}"/>')
    s.append(f'<circle cx="{xa:.0f}" cy="{ya:.0f}" r="10" fill="{GRN}"/>')
    s.append(f'<circle cx="{xt:.0f}" cy="{yt:.0f}" r="10" fill="{ORG}"/>')
    s.append(txt(xc, yc - 34, "完备 C（看得准）", 18, BLU, weight="bold"))
    s.append(txt(xa, ya + 42, "可组合 A（拼得上）", 17, GRN, weight="bold"))
    s.append(txt(xt, yt + 42, "传递 T（传得下去）", 17, ORG, weight="bold"))
    s.append(txt(cx, cy + 10, "至多取二", 26, GLD, weight="bold"))
    # 三张账单卡片（三角形下方一行，互不重叠）
    cards = [("要 C + A → 让出 T", "账单：离散→连续 的 1/3 缺口", BLU),
             ("要 C + T → 让出 A", "账单：子模性，能力不能相加", GRN),
             ("要 A + T → 让出 C", "账单：τ 发散，预测失效", ORG)]
    cw, gap = 268, 22
    x0 = (W - (cw * 3 + gap * 2)) / 2
    for i, (t1, t2, col) in enumerate(cards):
        x = x0 + i * (cw + gap)
        s.append(box(x, 500, cw, 86, "#fbfcfe", col))
        s.append(txt(x + cw / 2, 534, t1, 16, col, weight="bold"))
        s.append(txt(x + cw / 2, 562, t2, 13, GRY))
    save("fig-triangle-bills", s)


# ----------------------------------------------------------------- 图 3 容量级联
def fig_capacity_cascade():
    W, H = 920, 520
    s = head(W, H, "容量级联：从毫秒到一生，约 10⁹ 倍",
             "容量决定“必须忘”，时间尺度决定“忘在哪一层”")
    s.append(DEFS)
    layers = [("工作记忆", "秒", "#e3f0fb", BLU),
              ("短期记忆", "分钟—小时", "#e7f4ea", GRN),
              ("长期巩固", "小时—年", "#fff5e6", ORG),
              ("终身整合", "年—一生", "#f6ecf7", PNK)]
    x0, y0, bw, bh, gap = 120, 100, 640, 70, 18
    for i, (name, tscale, fill, col) in enumerate(layers):
        y = y0 + i * (bh + gap)
        s.append(box(x0, y, bw, bh, fill, col))
        s.append(txt(x0 + 140, y + 44, name, 20, col, weight="bold"))
        s.append(txt(x0 + 430, y + 44, tscale, 16, INK))
        if i < len(layers) - 1:
            s.append(f'<line x1="{x0+bw/2:.0f}" y1="{y+bh:.0f}" x2="{x0+bw/2:.0f}" y2="{y+bh+gap:.0f}" '
                     f'stroke="{GRY}" stroke-width="2" marker-end="url(#ah)"/>')
    # 侧边：压缩 / 遗忘
    s.append(txt(x0 + bw + 40, y0 + 30, "快的层→选", 14, GRY, anchor="start"))
    s.append(arrow(x0 + bw + 10, y0 + 45, x0 + bw + 10, y0 + 210, GRY))
    s.append(txt(x0 + bw + 40, y0 + 360, "慢的层→固", 14, GRY, anchor="start"))
    s.append(f'<text x="{x0+bw+120}" y="{y0+40}" font-size="13" fill="{RED}" '
             f'transform="rotate(90 {x0+bw+120} {y0+40})">压缩 · 干扰 · 遗忘</text>')
    s.append(txt(W / 2, H - 30, "容量 K 有限：多层分工不是奢侈，而是“既要适应又要稳定”的数学解", 14, GRY))
    save("fig-capacity-cascade", s)


# ----------------------------------------------------------------- 图 4 六个钟
def fig_six_clocks():
    W, H = 940, 480
    s = head(W, H, "现代社会不是一个钟，而是许多个转速不同的钟",
             "横轴为“做成一件事”所需时间的量级（对数）")
    s.append(DEFS)
    data = [("金融市场", "秒—分", 1.0, ORG),
            ("信息传播", "分—时", 1.6, ORG),
            ("政治决策", "周—月", 2.6, GRN),
            ("基础设施", "年—十年", 3.6, BLU),
            ("社会信任", "年", 3.9, BLU),
            ("生态环境", "十年—百年", 4.8, PNK)]
    x0, y0, bw, bh, gap = 230, 100, 620, 46, 22
    for i, (name, tscale, val, col) in enumerate(data):
        y = y0 + i * (bh + gap)
        w = max(46, bw * (val / 5.0))
        s.append(txt(x0 - 20, y + 30, name, 17, INK, anchor="end"))
        s.append(box(x0, y, w, bh, col, col, rx=6))
        s.append(f'<rect x="{x0}" y="{y}" width="{w:.0f}" height="{bh}" rx="6" fill="{col}" opacity="0.18"/>')
        s.append(txt(x0 + w + 14, y + 30, tscale, 13, GRY, anchor="start"))
    s.append(txt(200, 92, "制造冲击", 14, ORG, anchor="start", weight="bold"))
    s.append(txt(860, 92, "必须回应", 14, PNK, anchor="start", weight="bold"))
    s.append(txt(W / 2, H - 26, "快的一方可几小时定价，慢的一方要几年重建信任——错位是结构性的", 14, GRY))
    save("fig-six-clocks", s)


# ----------------------------------------------------------------- 图 5 τ 曲线
def fig_tau():
    W, H = 880, 500
    s = head(W, H, "时间错配越大，可控性越低、判断越模糊", "τ = 需要的时间 ÷ 你有的时间；可控性 C = 1/τ")
    s.append(DEFS)
    ox, oy, w, h = 110, 380, 620, 290
    s.append(f'<line x1="{ox}" y1="{oy}" x2="{ox+w}" y2="{oy}" stroke="#333" stroke-width="2"/>')
    s.append(f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy-h}" stroke="#333" stroke-width="2"/>')
    s.append(f'<text x="{ox+w/2:.0f}" y="{oy+44}" text-anchor="middle" font-size="14" fill="{INK}">τ（越大越糟）→</text>')
    s.append(f'<text x="{ox-70}" y="{oy-h/2:.0f}" text-anchor="middle" font-size="14" fill="{INK}" '
             f'transform="rotate(-90 {ox-70} {oy-h/2:.0f})">可控性 C</text>')
    # regions（tau: 0.1—100，log）
    s.append(f'<rect x="{ox}" y="{oy-h}" width="{w*0.333:.0f}" height="{h}" fill="#e8f5e9"/>')
    s.append(f'<rect x="{ox+w*0.333:.0f}" y="{oy-h}" width="{w*0.233:.0f}" height="{h}" fill="#fff8e1"/>')
    s.append(f'<rect x="{ox+w*0.566:.0f}" y="{oy-h}" width="{w*0.434:.0f}" height="{h}" fill="#ffebee"/>')
    # curve C = 1/tau
    pts = []
    for i in range(101):
        u = i / 100
        tau = 0.1 * (1000 ** u)
        C = 1.0 / tau
        x = ox + w * u
        y = oy - h * min(C / 10.0, 1.0)
        pts.append((x, y))
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    s.append(f'<path d="{d}" fill="none" stroke="{RED}" stroke-width="3.2"/>')
    s.append(f'<line x1="{ox}" y1="{oy-h*0.1:.0f}" x2="{ox+w}" y2="{oy-h*0.1:.0f}" stroke="#333" stroke-width="1.6" stroke-dasharray="7,5"/>')
    s.append(txt(ox + 100, oy - h + 24, "来得及", 14, GRN, weight="bold"))
    s.append(txt(ox + 300, oy - h + 24, "勉强", 14, ORG, weight="bold"))
    s.append(txt(ox + 500, oy - h + 24, "来不及 → 优雅降级", 14, RED, weight="bold"))
    for tau, lab in [(0.5, "τ≈0.5"), (3.5, "τ≈3.5"), (30, "τ≈30")]:
        u = math.log(tau / 0.1) / math.log(1000)
        x = ox + w * u
        y = oy - h * min((1.0 / tau) / 10.0, 1.0)
        s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="6" fill="{RED}"/>')
        s.append(txt(x, oy + 24, lab, 13, INK))
    # 置信区间注释（图外下方）
    s.append(txt(W / 2, H - 16, "τ 越大，置信区间越宽（±0.10 → ±0.60）；τ 只做事后诊断，不做事前预测", 13, GRY))
    save("fig-tau-curve", s)


# ----------------------------------------------------------------- 图 6 相似性=二次型
def fig_similarity():
    W, H = 800, 500
    s = head(W, H, "“像不像”其实是一个数：相似度＝二次型", "把每个东西画成一个点；两点之差平方相加，就是距离")
    s.append(DEFS)
    ox, oy, w, h = 120, 400, 560, 300
    s.append(f'<line x1="{ox}" y1="{oy}" x2="{ox+w}" y2="{oy}" stroke="#333" stroke-width="1.6"/>')
    s.append(f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy-h}" stroke="#333" stroke-width="1.6"/>')
    s.append(txt(ox + w / 2, oy + 36, "大小 →", 14, INK))
    s.append('<text x="70" y="250" font-size="14" fill="#1a1a1a" transform="rotate(-90 70 250)" text-anchor="middle">甜度 →</text>')
    P = {"甲": (0.55, 0.62), "乙": (0.57, 0.60), "丙": (0.42, 0.52), "丁": (0.20, 0.30)}
    for name, (u, v) in P.items():
        x, y = ox + w * u, oy - h * v
        s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="8" fill="{BLU if name=="甲" else GRN}"/>')
        s.append(txt(x + 16, y - 8, name, 15, INK, anchor="start", weight="bold"))
    xa, ya = ox + w * P["甲"][0], oy - h * P["甲"][1]
    for name in ["乙", "丙", "丁"]:
        x, y = ox + w * P[name][0], oy - h * P[name][1]
        s.append(f'<line x1="{xa:.0f}" y1="{ya:.0f}" x2="{x:.0f}" y2="{y:.0f}" stroke="{GRY}" '
                 f'stroke-width="1.3" stroke-dasharray="5,4"/>')
    s.append(txt(ox + w * 0.42, oy - h * 0.30, "距离 = (Δ甜度)² + (Δ大小)²", 14, GRY))
    s.append(box(560, 92, 200, 70, "#eef4fb", BLU))
    s.append(txt(660, 120, "xᵀ M x", 20, BLU, weight="bold"))
    s.append(txt(660, 146, "方差 / Hessian / 图能量 / 内积 / 度量", 11, GRY))
    save("fig-similarity-quadratic", s)


# ----------------------------------------------------------------- 图 7 谱决定性格
def fig_spectrum():
    W, H = 880, 460
    s = head(W, H, "系统的“性格”藏在谱里：谱决定长期行为", "短期的细节会互相抵消，长期的趋势只由特征值决定")
    s.append(DEFS)
    # 左：两个小圈子
    cx, cy = 210, 260
    A = [(90, 210), (150, 180), (150, 250), (110, 300)]
    B = [(300, 210), (340, 260), (290, 310), (330, 180)]
    for (x, y) in A:
        s.append(f'<circle cx="{x}" cy="{y}" r="9" fill="{BLU}"/>')
    for (x, y) in B:
        s.append(f'<circle cx="{x}" cy="{y}" r="9" fill="{GRN}"/>')
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if (i + j) % 2 == 0:
                s.append(f'<line x1="{A[i][0]}" y1="{A[i][1]}" x2="{A[j][0]}" y2="{A[j][1]}" stroke="{BLU}" stroke-width="1" opacity="0.5"/>')
    for i in range(len(B)):
        for j in range(i + 1, len(B)):
            if (i + j) % 2 == 0:
                s.append(f'<line x1="{B[i][0]}" y1="{B[i][1]}" x2="{B[j][0]}" y2="{B[j][1]}" stroke="{GRN}" stroke-width="1" opacity="0.5"/>')
    s.append(f'<line x1="180" y1="240" x2="270" y2="240" stroke="{RED}" stroke-width="1.6" stroke-dasharray="5,4"/>')
    s.append(txt(cx, 370, "两个小圈子：会不会裂开？", 14, GRY))
    s.append(txt(cx, 396, "看 λ₂（Fiedler 值）——越小越容易裂", 13, RED))
    # 右：谱
    bx, by, bw, bh = 470, 360, 360, 240
    s.append(f'<line x1="{bx}" y1="{by}" x2="{bx+bw}" y2="{by}" stroke="#333" stroke-width="1.6"/>')
    lambdas = [0.0, 0.6, 1.1, 1.7, 2.4, 3.2, 4.6, 6.0]
    for i, l in enumerate(lambdas):
        x = bx + 30 + i * 40
        hh = l / 6.0 * bh
        col = RED if i == 1 else BLU
        s.append(f'<rect x="{x}" y="{by-hh:.0f}" width="22" height="{hh:.0f}" fill="{col}" opacity="0.8"/>')
    s.append(txt(bx + bw / 2, by + 34, "拉普拉斯谱 λ₁ ≤ λ₂ ≤ … ≤ λₙ", 13, GRY))
    s.append(txt(bx + 70, by - bh - 6, "λ₂", 14, RED, weight="bold"))
    save("fig-spectrum", s)


# ----------------------------------------------------------------- 图 8 两阶段相变
def fig_two_stage():
    W, H = 900, 480
    s = head(W, H, "局部先醒，还是全局先醒？一场可复算的两阶段相变",
             "对称图：局部（高频）模式一定先于全局（Fiedler）模式增长")
    s.append(DEFS)
    ox, oy, w = 110, 300, 700
    s.append(f'<line x1="{ox}" y1="{oy}" x2="{ox+w}" y2="{oy}" stroke="#333" stroke-width="2"/>')
    s.append(f'<text x="{ox+w/2:.0f}" y="{oy+44}" text-anchor="middle" font-size="14" fill="{INK}">耦合强度 β（关系有多强）→</text>')
    b1, b2 = 0.34, 0.68
    x1, x2 = ox + w * b1, ox + w * b2
    s.append(f'<rect x="{ox}" y="{oy-230}" width="{x1-ox:.0f}" height="230" fill="#eceff1"/>')
    s.append(f'<rect x="{x1:.0f}" y="{oy-230}" width="{x2-x1:.0f}" height="230" fill="#e3f0fb"/>')
    s.append(f'<rect x="{x2:.0f}" y="{oy-230}" width="{ox+w-x2:.0f}" height="230" fill="#fff5e6"/>')
    s.append(f'<line x1="{x1:.0f}" y1="{oy-230}" x2="{x1:.0f}" y2="{oy}" stroke="{BLU}" stroke-width="1.6" stroke-dasharray="6,4"/>')
    s.append(f'<line x1="{x2:.0f}" y1="{oy-230}" x2="{x2:.0f}" y2="{oy}" stroke="{ORG}" stroke-width="1.6" stroke-dasharray="6,4"/>')
    s.append(txt((ox + x1) / 2, oy - 110, "全部衰减", 16, GRY, weight="bold"))
    s.append(txt((x1 + x2) / 2, oy - 130, "只有局部模式增长", 16, BLU, weight="bold"))
    s.append(txt((x1 + x2) / 2, oy - 100, "细碎的火苗", 13, GRY))
    s.append(txt((x2 + ox + w) / 2, oy - 110, "全局模式随后增长", 16, ORG, weight="bold"))
    s.append(txt((x2 + ox + w) / 2, oy - 80, "大火连成一片", 13, GRY))
    s.append(txt(x1, oy + 24, "β₁ = α/λₙ", 13, BLU, weight="bold"))
    s.append(txt(x2, oy + 24, "β₂ = α/λ₂", 13, ORG, weight="bold"))
    s.append(box(110, 380, 320, 76, "#e3f0fb", BLU))
    s.append(txt(270, 408, "Petersen 图：(0.200, 0.500)", 14, BLU))
    s.append(txt(270, 434, "环 C₁₀：(0.250, 2.618) → 中间隔了十倍！", 13, GRY))
    s.append(box(470, 380, 340, 76, "#eef7f0", GRN))
    s.append(txt(640, 408, "任意正对称边权下，顺序不可反转", 14, GRN))
    s.append(txt(640, 434, "有向图（不对称）可反转——一条真实反例", 13, GRY))
    save("fig-two-stage", s)


# ----------------------------------------------------------------- 图 9 置信度分层
def fig_confidence():
    W, H = 880, 520
    s = head(W, H, "诠释＝给竞争命题分配置信度", "同一批材料，越往上层，置信度越低，分歧越难消除")
    s.append(DEFS)
    layers = [("因果", "这导致了……", 0.20, RED),
              ("诠释", "这标志一个时代……", 0.35, ORG),
              ("推理", "他因此被排挤……", 0.62, GLD),
              ("事实", "他确实说过这句话", 0.88, GRN)]
    y0, bw, bh, gap = 110, 380, 62, 14
    x = 90
    for i, (name, ex, conf, col) in enumerate(layers):
        y = y0 + i * (bh + gap)
        w = 120 + 260 * conf
        s.append(box(x, y, w, bh, col, col, rx=6))
        s.append(f'<rect x="{x}" y="{y}" width="{w:.0f}" height="{bh}" rx="6" fill="{col}" opacity="0.16"/>')
        s.append(txt(x + 34, y + 38, name, 18, INK, anchor="start", weight="bold"))
        s.append(txt(x + w - 20, y + 38, ex, 15, INK, anchor="end"))
    s.append(txt(x + 200, 88, "越往上：越容易各取所需", 13, GRY))
    # 右侧置信度条
    for i, (name, ex, conf, col) in enumerate(layers):
        y = y0 + i * (bh + gap)
        s.append(txt(600, y + 38, f"置信度 {int(conf*100)}%", 13, col, anchor="start", weight="bold"))
    s.append(box(600, 430, 240, 66, "#fff8e1", ORG))
    s.append(txt(720, 458, "材料增加", 14, ORG, weight="bold"))
    s.append(txt(720, 480, "主要提高下层；上层分歧照旧", 12, GRY))
    save("fig-confidence-layers", s)


# ----------------------------------------------------------------- 图 10 三种学者
def fig_three_scholars():
    W, H = 840, 520
    s = head(W, H, "三种学者，三个顶点", "谁也说服不了谁，因为各自让出了不同的顶点")
    s.append(DEFS)
    cx, cy, R = 420, 320, 180

    def pt(deg):
        a = math.radians(deg)
        return cx + R * math.cos(a), cy + R * math.sin(a)
    xc, yc = pt(-90)
    xa, ya = pt(150)
    xt, yt = pt(30)
    s.append(f'<polygon points="{xc:.0f},{yc:.0f} {xa:.0f},{ya:.0f} {xt:.0f},{yt:.0f}" '
             f'fill="#f7f9fc" stroke="#9aa4b2" stroke-width="2"/>')
    items = [((xc, yc), "清晰派", "C + T", "让出 A", BLU),
             ((xa, ya), "平衡派", "A + T", "让出 C", GRN),
             ((xt, yt), "细节派", "C + A", "让出 T", ORG)]
    for (x, y), name, keep, give, col in items:
        s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="10" fill="{col}"/>')
        dy = -30 if y < cy else 46
        s.append(txt(x, y + dy, name, 18, col, weight="bold"))
        s.append(txt(x, y + dy + 24, keep + "（" + give + "）", 14, INK))
    s.append(txt(cx, cy + 14, "同一场争论", 20, GLD, weight="bold"))
    s.append(txt(cx, cy + 42, "分歧多在“分配位置”，不在事实", 13, GRY))
    save("fig-three-scholars", s)


# ----------------------------------------------------------------- 图 11 知识的一生
def fig_knowledge_life():
    W, H = 940, 520
    s = head(W, H, "知识的一生：一部不断重选三角的历史", "成熟不是终点，能周期性地回到起点才是")
    s.append(DEFS)
    stages = [("范式建立", "C + T", "少数大师的精妙理论", "难教学、难推广", BLU),
              ("教学化", "A + T", "教科书、标准课程", "磨平精妙与边界", GRN),
              ("工程化", "C + A", "标准流程、可复制产品", "对新情况反应慢", ORG),
              ("危机与革命", "重回 C + T", "新范式、新精妙理论", "旧的可教性中断", RED)]
    cxp, cyp, r = 470, 300, 150
    for i, (name, keep, what, cost, col) in enumerate(stages):
        ang = -90 + i * 90
        a = math.radians(ang)
        x = cxp + r * math.cos(a)
        y = cyp + r * math.sin(a)
        s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="58" fill="{col}" opacity="0.16" stroke="{col}" stroke-width="1.6"/>')
        s.append(txt(x, y - 6, name, 15, col, weight="bold"))
        s.append(txt(x, y + 16, keep, 14, INK))
    # 环上箭头
    for i in range(4):
        a0 = -90 + i * 90 + 24
        a1 = -90 + (i + 1) * 90 - 24
        x0 = cxp + r * math.cos(math.radians(a0))
        y0 = cyp + r * math.sin(math.radians(a0))
        x1 = cxp + r * math.cos(math.radians(a1))
        y1 = cyp + r * math.sin(math.radians(a1))
        s.append(arrow(x0, y0, x1, y1, GRY, 2.0))
    s.append(txt(cxp, cyp + 4, "不断重选", 16, GLD, weight="bold"))
    s.append(txt(cxp, cyp + 28, "三角", 16, GLD, weight="bold"))
    # 代价说明条
    s.append(box(60, 452, 820, 46, "#f7f9fc", "#c9d2dd"))
    s.append(txt(470, 480, "每一阶段都换来力量，也让出一个顶点；最危险的时刻，是“工程化得最好、却忘了自己丢了什么”的时候", 13, GRY))
    save("fig-knowledge-life", s)


# ----------------------------------------------------------------- 图 12 五张账单
def fig_bill():
    W, H = 980, 440
    s = head(W, H, "五张账单：看得见的世界背后，都有一张看不见的账单", "每个核心＝一笔代价；看懂账单，就看见了自己站在哪里")
    s.append(DEFS)
    cards = [("看见", "划线有成本", "区分＋二次型", BLU),
             ("记住", "遗忘是前提", "容量＋压缩", GRN),
             ("跟上", "来不及是结构", "多尺度＋τ", ORG),
             ("选择", "至多取二", "C-A-T 三角", GLD),
             ("讲述", "争吵在抢位置", "置信度分配", PNK)]
    cw, ch, gap = 172, 240, 14
    x0 = (W - (cw * 5 + gap * 4)) / 2
    for i, (name, line, sub, col) in enumerate(cards):
        x = x0 + i * (cw + gap)
        s.append(box(x, 100, cw, ch, "#fbfcfe", col))
        s.append(f'<rect x="{x}" y="{100}" width="{cw}" height="56" rx="8" fill="{col}" opacity="0.16"/>')
        s.append(txt(x + cw / 2, 138, name, 24, col, weight="bold"))
        s.append(txt(x + cw / 2, 196, line, 17, INK, weight="bold"))
        s.append(txt(x + cw / 2, 244, sub, 13, GRY))
        s.append(txt(x + cw / 2, 312, f"账单 {i+1}", 13, GRY))
    save("fig-bill", s)


def main():
    os.makedirs(OUT, exist_ok=True)
    for f in [fig_five_core, fig_triangle, fig_capacity_cascade, fig_six_clocks,
              fig_tau, fig_similarity, fig_spectrum, fig_two_stage,
              fig_confidence, fig_three_scholars, fig_knowledge_life, fig_bill]:
        f()
    print("all figures written to", OUT)


if __name__ == "__main__":
    main()
