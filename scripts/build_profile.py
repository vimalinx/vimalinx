#!/usr/bin/env python3
"""Build self-contained, script-free SVG artwork for the GitHub profile."""
from base64 import b64encode
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'


def image_uri(name, mime):
    return 'data:' + mime + ';base64,' + b64encode((ASSETS / name).read_bytes()).decode()


def svg(width, height, title, body, defs='', styles=''):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title">
<title id="title">{escape(title)}</title>
<defs>{defs}</defs>
<style>
text{{font-family:'Noto Sans',Arial,sans-serif}}
.mono{{font-family:'DejaVu Sans Mono',monospace}}
.serif{{font-family:Georgia,'Noto Serif',serif}}
{styles}
@media(prefers-reduced-motion:reduce){{.motion,.slide{{animation:none!important}}.slide{{opacity:0}}.slide.first{{opacity:1}}}}
</style>
{body}
</svg>'''


flower = image_uri('flower-avatar.png', 'image/png')
hero_defs = '''
<radialGradient id="ambient"><stop stop-color="#746391" stop-opacity=".25"/><stop offset="1" stop-color="#111016" stop-opacity="0"/></radialGradient>
<clipPath id="avatarCircle"><circle cx="260" cy="260" r="208"/></clipPath>
<linearGradient id="rule"><stop stop-color="#C7B5DE" stop-opacity=".65"/><stop offset="1" stop-color="#C7B5DE" stop-opacity="0"/></linearGradient>
'''
hero_styles = '''
@keyframes breathe{0%,100%{transform:translateY(0) rotate(-1deg)}50%{transform:translateY(-9px) rotate(1.4deg)}}
@keyframes glow{0%,100%{opacity:.45}50%{opacity:.95}}
@keyframes drift{from{stroke-dashoffset:0}to{stroke-dashoffset:-160}}
.bloom{animation:breathe 11s ease-in-out infinite;transform-origin:260px 260px}
.halo{animation:glow 9s ease-in-out infinite}
.orbit{animation:drift 32s linear infinite}
'''


def flower_layer(x, y, scale=1):
    return f'''<g transform="translate({x} {y}) scale({scale})">
<circle class="motion halo" cx="260" cy="260" r="280" fill="url(#ambient)"/>
<circle cx="260" cy="260" r="221" fill="none" stroke="#A893BB" stroke-opacity=".15"/>
<circle class="motion orbit" cx="260" cy="260" r="247" fill="none" stroke="#D6C6E9" stroke-opacity=".38" stroke-width="1" stroke-dasharray="2 18 28 32"/>
<g class="motion bloom"><image x="52" y="52" width="416" height="416" preserveAspectRatio="xMidYMid meet" href="{flower}" clip-path="url(#avatarCircle)"/></g>
<circle cx="477" cy="142" r="3.5" fill="#E3CB87"/>
<circle cx="44" cy="399" r="2" fill="#C7B5DE"/>
</g>'''


hero_body = f'''
<rect width="1200" height="520" rx="18" fill="#111016"/>
<path d="M36 54H1164" stroke="#C7B5DE" stroke-opacity=".17"/>
<text class="mono" x="48" y="35" fill="#BAABC6" font-size="12" letter-spacing="2">VIMALINX / PERSONAL LAB</text>
<text class="mono" x="1152" y="35" text-anchor="end" fill="#BAABC6" font-size="12" letter-spacing="2">INDEPENDENT · OPEN SOURCE</text>
{flower_layer(688, 8, .94)}
<text class="serif" x="44" y="214" fill="#F8F2EB" font-size="126" letter-spacing="-6">Vimalinx<tspan fill="#CDB5E5">.</tspan></text>
<text x="53" y="265" fill="#D4C3E3" font-size="25" letter-spacing="7">七叶怀瑾</text>
<path d="M53 303H530" stroke="url(#rule)"/>
<text x="53" y="351" fill="#F3EBF8" font-size="25">Building VimalinxOS.</text>
<text x="53" y="387" fill="#AFA6BA" font-size="18">AI agents, Linux &amp; useful little things.</text>
<path d="M36 454H1164" stroke="#C7B5DE" stroke-opacity=".17"/>
<circle class="motion halo" cx="54" cy="486" r="4" fill="#C4D8AF"/>
<text class="mono" x="72" y="491" fill="#D3C7DC" font-size="13" letter-spacing="1">IDEAS INTO WORKING THINGS</text>
<text class="serif" x="1152" y="491" text-anchor="end" font-style="italic" fill="#BBAACB" font-size="18">A little code. A little curiosity.</text>
'''
(ASSETS / 'profile-hero.svg').write_text(svg(1200, 520, 'Vimalinx / 七叶怀瑾 — a flower, a personal lab, and VimalinxOS.', hero_body, hero_defs, hero_styles))

mobile_body = f'''
<rect width="720" height="650" rx="18" fill="#111016"/>
<text class="mono" x="38" y="42" fill="#BAABC6" font-size="14" letter-spacing="2">PERSONAL LAB / OPEN SOURCE</text>
<path d="M36 62H684" stroke="#C7B5DE" stroke-opacity=".2"/>
{flower_layer(254, 233, .54)}
<text class="serif" x="30" y="170" fill="#F8F2EB" font-size="112" letter-spacing="-5">Vimalinx<tspan fill="#CDB5E5">.</tspan></text>
<text x="40" y="218" fill="#D4C3E3" font-size="24" letter-spacing="6">七叶怀瑾</text>
<text x="40" y="539" fill="#F3EBF8" font-size="27">Building VimalinxOS.</text>
<path d="M36 570H684" stroke="#C7B5DE" stroke-opacity=".2"/>
<circle class="motion halo" cx="43" cy="610" r="4" fill="#C4D8AF"/>
<text class="mono" x="61" y="616" fill="#D3C7DC" font-size="16" letter-spacing=".7">IDEAS INTO WORKING THINGS</text>
'''
(ASSETS / 'profile-hero-mobile.svg').write_text(svg(720, 650, 'Vimalinx / 七叶怀瑾 — Building VimalinxOS.', mobile_body, hero_defs, hero_styles))

map_styles = '''
@keyframes flow{to{stroke-dashoffset:-160}}
@keyframes signal{0%,100%{opacity:.35}50%{opacity:1}}
.flow{animation:flow 14s linear infinite}
.signal{animation:signal 5s ease-in-out infinite}
'''
map_defs = '''<linearGradient id="mapBg" x2="1" y2="1"><stop stop-color="#201B2C"/><stop offset="1" stop-color="#121018"/></linearGradient>
<linearGradient id="beam"><stop stop-color="#B8D5A8"/><stop offset=".5" stop-color="#D1B6E5"/><stop offset="1" stop-color="#E0C386"/></linearGradient>'''
map_body = '''
<rect width="1200" height="330" rx="16" fill="url(#mapBg)"/>
<text class="mono" x="40" y="40" fill="#C7B5D9" font-size="13" letter-spacing="2">01 / THE MAIN PROJECT</text>
<text class="serif" x="37" y="119" fill="#FAF5EF" font-size="64" letter-spacing="-2">VimalinxOS</text>
<text x="43" y="164" fill="#D2C7DD" font-size="20">让 AI 能在自己的电脑上，把事情做完。</text>
<text x="43" y="199" fill="#A99DB9" font-size="16">独立组件，清晰的能力入口。</text>
<text class="mono" x="43" y="270" fill="#DDC38B" font-size="14" letter-spacing="2">EXPLORE THE ECOSYSTEM →</text>
<path d="M615 145H1120" stroke="#C2AED8" stroke-opacity=".15" stroke-width="2"/>
<path class="motion flow" d="M615 145H1120" fill="none" stroke="url(#beam)" stroke-width="2" stroke-dasharray="10 30"/>
'''
for i, (x, label, zh, color) in enumerate([(625, 'DISCOVER', '发现', '#B8D5A8'), (790, 'OPERATE', '操作', '#D3BCE8'), (955, 'VERIFY', '验证', '#B8C8E4'), (1120, 'RECOVER', '恢复', '#E0C386')]):
    map_body += f'''<circle cx="{x}" cy="145" r="27" fill="#1B1722" stroke="{color}" stroke-opacity=".55"/>
<circle class="motion signal" cx="{x}" cy="145" r="6" fill="{color}" style="animation-delay:{-i*1.2}s"/>
<text class="mono" x="{x}" y="203" text-anchor="middle" fill="{color}" font-size="12" letter-spacing="1">{label}</text>
<text x="{x}" y="229" text-anchor="middle" fill="#B8ADCA" font-size="16">{zh}</text>'''
map_body += '<text x="876" y="287" text-anchor="middle" fill="#93879F" font-size="13">能力分工示意 · 组件各自开发与发布</text>'
(ASSETS / 'ecosystem.svg').write_text(svg(1200, 330, 'VimalinxOS — Discover, operate, verify, recover. A capability illustration, not a live execution trace.', map_body, map_defs, map_styles))

slides = [('router-overview.jpg','运行概览 / Overview'), ('router-services.jpg','服务与渠道 / Services'), ('router-agents.jpg','Agent 工作台 / Agents')]
carousel_styles = '''
@keyframes cycle{0%,30%{opacity:1}33.333%,96.667%{opacity:0}100%{opacity:1}}
.slide{opacity:0;animation:cycle 18s linear infinite}
.slide.first{opacity:1}
'''
carousel_body = '''
<rect width="1200" height="855" rx="16" fill="#15121C"/>
<text class="mono" x="38" y="39" fill="#B4A0CD" font-size="13" letter-spacing="2">02 / IN THE APP</text>
<text x="37" y="94" fill="#FAF6FF" font-size="39" font-weight="700" letter-spacing="-1">LocalRouter</text>
<text x="38" y="130" fill="#C0B2CD" font-size="19">模型、服务和 Agent 调用，在自己的机器上管理。</text>
<rect x="24" y="162" width="1152" height="684" rx="8" fill="#F7F7FC"/>
'''
for i, (name, label) in enumerate(slides):
    delay = [0, -12, -6][i]
    carousel_body += f'''<g class="slide {'first' if i == 0 else ''}" style="animation-delay:{delay}s">
<image x="24" y="162" width="1152" height="684" preserveAspectRatio="xMidYMid meet" href="{image_uri(name, 'image/jpeg')}"/>
<rect x="824" y="45" width="334" height="49" rx="24" fill="#2A2238"/>
<text x="991" y="76" text-anchor="middle" fill="#E9DCF7" font-size="17">{escape(label)}</text>
</g>'''
(ASSETS / 'localrouter-showcase.svg').write_text(svg(1200, 855, 'LocalRouter public demo screenshots: overview, services and Agent workbench. Example data is fictional.', carousel_body, styles=carousel_styles))
print('Built 4 self-contained SVG assets with reduced-motion support.')
