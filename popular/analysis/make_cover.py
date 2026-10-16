# -*- coding: utf-8 -*-
"""make_cover.py — 生成《只能选两样》满版封面 SVG（A4 比例 1000×1414）。

系列统一版式：暗色渐变、顶部金线、标题/副标题/作者/英文行的位置与字号，
仅中心线描母题因书而异。母题：一个三条边的三角形，三个顶点分别写着
看得准（C）、拼得上（A）、传得下去（T）；其中一个顶点被点亮、一个被虚化，
题字“至多取二”。
"""
import math
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "assets", "svg", "cover.svg")


def build():
    W, H = 1000, 1414
    ink = "#e8e6df"
    dim = "#9aa0a6"
    gold = "#b8862f"
    layers = []

    cx, cy = 500, 820
    R = 210

    def pt(deg):
        a = math.radians(deg)
        return cx + R * math.cos(a), cy + R * math.sin(a)

    xc, yc = pt(-90)      # C 顶点（上）
    xa, ya = pt(150)      # A 顶点（左下）
    xt, yt = pt(30)       # T 顶点（右下）

    # 三角形三条边
    layers.append(f'<polygon points="{xc:.0f},{yc:.0f} {xa:.0f},{ya:.0f} {xt:.0f},{yt:.0f}" '
                  f'fill="none" stroke="#7d8a99" stroke-width="1.6" opacity="0.55"/>')
    # 被“让出”的顶点：C 用红色虚线圈
    layers.append(f'<circle cx="{xc:.0f}" cy="{yc:.0f}" r="34" fill="none" stroke="#c94f4f" '
                  f'stroke-width="1.6" stroke-dasharray="6,5" opacity="0.75"/>')
    # 被保住的两个顶点：金色实心点
    for (x, y) in [(xa, ya), (xt, yt)]:
        layers.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="12" fill="{gold}" opacity="0.85"/>')
    layers.append(f'<circle cx="{xc:.0f}" cy="{yc:.0f}" r="5" fill="#c94f4f" opacity="0.8"/>')

    # 顶点标签
    layers.append(f'<text x="{xc:.0f}" y="{yc-52:.0f}" text-anchor="middle" class="vl">看得准 C</text>')
    layers.append(f'<text x="{xa-6:.0f}" y="{ya+58:.0f}" text-anchor="middle" class="vl">拼得上 A</text>')
    layers.append(f'<text x="{xt+6:.0f}" y="{yt+58:.0f}" text-anchor="middle" class="vl">传得下去 T</text>')
    # 中心题字
    layers.append(f'<text x="{cx}" y="{cy+8}" text-anchor="middle" class="mid">至多取二</text>')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#0e1117"/><stop offset="0.55" stop-color="#151a23"/>
<stop offset="1" stop-color="#0b0e14"/>
</linearGradient>
</defs>
<rect x="0" y="0" width="{W}" height="{H}" fill="url(#bg)"/>
<rect x="0" y="0" width="{W}" height="8" fill="{gold}" opacity="0.85"/>
{chr(10).join(layers)}
<style>
text{{font-family:'Microsoft YaHei','SimHei',Arial,sans-serif;}}
.ttl{{font-size:112px;font-weight:700;letter-spacing:14px;fill:{ink};}}
.sub{{font-size:28px;fill:{dim};letter-spacing:2px;}}
.eng{{font-size:20px;fill:{dim};letter-spacing:1px;}}
.au{{font-size:30px;fill:{ink};letter-spacing:2px;}}
.rule{{stroke:{dim};stroke-width:1;opacity:0.6;}}
.vl{{font-size:24px;fill:#cfd6de;letter-spacing:1px;}}
.mid{{font-size:34px;fill:{gold};letter-spacing:8px;font-weight:700;}}
.sm{{font-size:20px;fill:#9aa0a6;letter-spacing:2px;}}
</style>
<text x="80" y="176" class="eng">PICK TWO</text>
<text x="80" y="300" class="ttl">只能选两样</text>
<line x1="84" y1="344" x2="700" y2="344" class="rule"/>
<text x="84" y="396" class="sub">从来不及、会忘记到说不清：</text>
<text x="84" y="440" class="sub">五个核心，看懂复杂世界的取舍</text>
<text x="84" y="500" class="eng">看见 · 记住 · 跟上 · 选择 · 讲述</text>
<text x="80" y="1180" class="au">李毅芃　著</text>
<text x="80" y="1232" class="eng">Five Ideas for Understanding a Complicated World</text>
<text x="80" y="1274" class="eng">通俗读本 · 2026</text>
</svg>
'''
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote", OUT)


if __name__ == "__main__":
    build()
