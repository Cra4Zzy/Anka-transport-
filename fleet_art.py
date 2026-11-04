"""Draw ANKA's four illustrative vehicle profiles as lightweight SVG assets."""

VEHICLES = {
    # Box left edge, width, roof height, cab position, cab roof, and visible axles.
    "7-5": (106, 308, 96, 436, 122, (194, 515)),
    "12": (75, 365, 81, 458, 109, (179, 537)),
    "18": (51, 424, 68, 490, 99, (164, 222, 569)),
    "Sattelzug": (30, 427, 61, 489, 88, (133, 187, 241, 492, 570)),
}

DEFS = """
<defs>
  <linearGradient id="box" x2="0" y2="1" gradientUnits="objectBoundingBox">
    <stop stop-color="#646f7c"/><stop offset=".14" stop-color="#48525e"/>
    <stop offset=".68" stop-color="#293441"/><stop offset="1" stop-color="#1c2530"/>
  </linearGradient>
  <linearGradient id="cab" x2="0" y2="1" gradientUnits="objectBoundingBox">
    <stop stop-color="#f3f5f4"/><stop offset=".48" stop-color="#d4d9dc"/>
    <stop offset=".75" stop-color="#a9b3bd"/><stop offset="1" stop-color="#6f7d8b"/>
  </linearGradient>
  <linearGradient id="front" x2="0" y2="1" gradientUnits="objectBoundingBox">
    <stop stop-color="#aab6bf"/><stop offset=".54" stop-color="#697583"/>
    <stop offset="1" stop-color="#3f4c59"/>
  </linearGradient>
  <linearGradient id="glass" x2="1" y2="1" gradientUnits="objectBoundingBox">
    <stop stop-color="#77919e"/><stop offset=".34" stop-color="#344d61"/>
    <stop offset="1" stop-color="#102231"/>
  </linearGradient>
  <linearGradient id="amber" x2="1" y2="1" gradientUnits="objectBoundingBox">
    <stop stop-color="#ffb365"/><stop offset=".42" stop-color="#f1892d"/>
    <stop offset="1" stop-color="#cc5417"/>
  </linearGradient>
  <radialGradient id="tyre">
    <stop offset=".49" stop-color="#3d4650"/><stop offset=".76" stop-color="#1d252d"/>
    <stop offset="1" stop-color="#0a0e13"/>
  </radialGradient>
  <linearGradient id="hub" x2="0" y2="1" gradientUnits="objectBoundingBox">
    <stop stop-color="#d5dce0"/><stop offset="1" stop-color="#5a6977"/>
  </linearGradient>
  <radialGradient id="shadow">
    <stop stop-color="#000" stop-opacity=".9"/><stop offset=".72" stop-color="#000" stop-opacity=".58"/>
    <stop offset="1" stop-color="#000" stop-opacity="0"/>
  </radialGradient>
</defs>
"""


def wheel(x, radius, y=244):
    bolts = ''.join(
        f'<circle cx="{bx}" cy="{by}" r="1.3"/>'
        for bx, by in [(0, -8), (7, -4), (7, 4), (0, 8), (-7, 4), (-7, -4)]
    )
    return f'''<g transform="translate({x} {y})">
  <circle r="{radius + 2}" fill="#0c1218" stroke="#4e5c6b" stroke-width="1.4"/>
  <circle r="{radius}" fill="url(#tyre)" stroke="#101821" stroke-width="1"/>
  <circle r="{radius - 5}" fill="none" stroke="#818b94" stroke-opacity=".27" stroke-width=".8"/>
  <circle r="{radius - 9}" fill="url(#hub)" stroke="#252e38" stroke-width="1.8"/>
  <g fill="#374550">{bolts}</g>
  <circle r="4.8" fill="#485661" stroke="#acb6bd" stroke-width="1"/>
</g>'''


def truck_svg(key):
    left, width, top, cab, roof, axles = VEHICLES[key]
    right = left + width
    side_top = top + 14
    box_bottom = 216 if key != "Sattelzug" else 207
    radius = 24 if key == "7-5" else 27
    rear_y = 246 if key == "7-5" else 243
    contact_y = rear_y + radius + 1
    mid = (left + cab + 145) / 2
    rails = ''.join(f'<path d="M{x} {side_top + 8}v{box_bottom - side_top - 15}"/>' for x in range(left + 11, right - 5, 16))
    far = ''.join(f'<circle cx="{x+13}" cy="{rear_y-3}" r="{radius-1}" fill="#111820"/>' for x in axles)
    near = ''.join(wheel(x, radius, rear_y) for x in axles)
    markers = ''.join(f'<rect x="{x}" y="{box_bottom-7}" width="7" height="2.5" rx="1" fill="#f4ab64"/>' for x in range(left + 19, right, 68))
    underside = (
        f'<path d="M{right-36} 207v40m-8 1h16" stroke="#637080" stroke-width="4"/>'
        f'<path d="M{cab-16} 219h59v17h-59z" fill="#35424f"/>'
        if key == "Sattelzug" else
        f'<path d="M{left+25} 229H{cab+35}v8H{left+25}z" fill="#465461"/>'
        f'<rect x="{cab-67}" y="224" width="66" height="18" rx="5" fill="#687480"/>'
        f'<path d="M{cab-56} 224v18m42-18v18" stroke="#3e4a57" stroke-width="3"/>'
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="680" height="294" viewBox="0 0 680 294">
{DEFS}
<ellipse cx="{mid}" cy="{contact_y}" rx="{(cab+145-left)/2+22}" ry="15" fill="url(#shadow)"/>
{far}
<rect x="{left+3}" y="{box_bottom-3}" width="{width}" height="21" rx="2" fill="#222c36"/>
<path d="M{left-3} {side_top+6}v{box_bottom-side_top+21}h19" fill="none" stroke="#727f8b" stroke-width="5" stroke-linejoin="round"/>
<rect x="{left-5}" y="{box_bottom-17}" width="5" height="14" rx="1" fill="#dc593e"/>
{underside}
<path d="M{left} {side_top}l18 -14h{width}l-18 14z" fill="#788490"/>
<path d="M{right} {side_top}l18 -14V{box_bottom-12}l-18 12z" fill="#222e3a" stroke="#4c5b69" stroke-width="1"/>
<rect x="{left}" y="{side_top}" width="{width}" height="{box_bottom-side_top}" rx="3" fill="url(#box)" stroke="#83909b" stroke-width="1.4"/>
<g stroke="#c5d0d8" opacity=".07">{rails}</g>
<path d="M{left+2} {side_top+2}h{width-4}" stroke="#bac5ce" stroke-opacity=".52" stroke-width="1.5"/>
<path d="M{right-122} {box_bottom-11}h41l38 -67h-41z" fill="url(#amber)" opacity=".94"/>
<path d="M{right-76} {box_bottom-11}h16l38 -67h-16z" fill="#ee9b52" opacity=".38"/>
<text x="{left+27}" y="{side_top+45}" fill="#f4f5f2" font-family="Arial,sans-serif" font-size="34" font-weight="900" letter-spacing="2">ANKA</text>
<text x="{left+29}" y="{side_top+63}" fill="#eeb17f" font-family="Arial,sans-serif" font-size="10" font-weight="700" letter-spacing="4">TRANSPORT</text>
<rect x="{left+2}" y="{box_bottom-4}" width="{width-4}" height="3" rx="1" fill="#f18b38"/>
{markers}
<g transform="translate({cab} 0)">
 <path d="M-7 218h153v15H-7z" fill="#27313b"/>
 <path d="M4 224V{roof+24}Q5 {roof+7} 23 {roof+4}L67 {roof}Q86 {roof-1} 96 {roof+16}L116 {roof+63}V232H15Q4 230 4 224Z"
       fill="url(#cab)" stroke="#d3dbe0" stroke-width="1.15"/>
 <path d="M96 {roof+16}L123 {roof+24} 146 {roof+68}V223L116 232V{roof+63}Z"
       fill="url(#front)" stroke="#8795a2" stroke-width="1.2"/>
 <path d="M22 {roof+20}L69 {roof+16}Q79 {roof+15} 84 {roof+28}L101 {roof+62}H15V{roof+38}Q15 {roof+24} 22 {roof+20}Z"
       fill="url(#glass)" stroke="#1b2a37" stroke-width="2.8"/>
 <path d="M22 {roof+23}L69 {roof+19}Q76 {roof+18} 80 {roof+26}L25 {roof+36}Z" fill="#b5d1db" opacity=".28"/>
 <path d="M69 {roof+17}V{roof+61}" stroke="#a7b6c0" stroke-opacity=".64" stroke-width="2"/>
 <path d="M102 {roof+25}l19 6 19 35-23 -5Z" fill="url(#glass)" stroke="#25323e" stroke-width="2"/>
 <path d="M105 {roof+30}l17 6 4 7-18 -4Z" fill="#a7c4cf" opacity=".22"/>
 <path d="M14 {roof+69}h82v{204-roof-69}H14Z" fill="none" stroke="#667687" stroke-width="1.1" opacity=".74"/>
 <path d="M14 202h98v10H14Z" fill="url(#amber)"/>
 <rect x="25" y="181" width="15" height="3" rx="1.5" fill="#465362"/>
 <path d="M104 {roof+58}l12 -5" stroke="#303f4d" stroke-width="3" stroke-linecap="round"/>
 <rect x="111" y="{roof+37}" width="10" height="18" rx="3" fill="#1c2732" stroke="#72818e" stroke-width="1"/>
 <path d="M117 {roof+78}l28 2v{216-roof-80}l-28 5Z" fill="#202b36"/>
 <path d="M121 184l21 -1m-21 8 21 -2m-21 8 21 -2m-21 8 21 -2" stroke="#788591" stroke-width="1.35"/>
 <path d="M116 214l29 -6v9l-29 7z" fill="#151d26"/>
 <path d="M120 215l15 -3v4l-15 4z" fill="#ffedce"/>
 <path d="M138 211l7 -2v5l-7 2z" fill="#ffae60"/>
 <path d="M9 228h108l29 -9v7l-29 9H9Z" fill="#364553"/>
 <path d="M16 222h23v5H16z" fill="#5f707d"/>
</g>
{near}
</svg>
'''


def write_fleet_art(assets):
    for key in VEHICLES:
        (assets / f"fleet-{key.lower()}.svg").write_text(truck_svg(key), encoding="utf-8")
