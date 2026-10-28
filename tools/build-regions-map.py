#!/usr/bin/env python3
"""Regenerate images/regions-map.svg from Natural Earth 1:50m Admin 0 countries (GeoJSON).

Usage: python3 tools/build-regions-map.py ne_50m_admin_0_countries.geojson images/regions-map.svg
"""
import json, math, sys

W, H = 1040, 660
LON0, LON1 = 66.0, 142.0
LAT_TOP = 36.5
K = W / ((LON1 - LON0) * math.cos(math.radians(10)))  # px per degree

ACTIVE = {"India", "Philippines", "Indonesia", "Malaysia", "Singapore"}
# label, anchor (lon, lat), label centre (lon, lat)
LABELS = [
    ("INDIA", (78.5, 22.0), (78.5, 22.0), 112),
    ("PHILIPPINES", (122.0, 13.0), (127.5, 19.0), 172),
    ("INDONESIA", (113.5, -1.5), (113.5, -1.5), 150),
    ("MALAYSIA", (102.0, 4.2), (92.5, 7.5), 140),
    ("SINGAPORE", (103.82, 1.35), (97.5, -5.5), 150),
]


def project(lon, lat):
    return ((lon - LON0) * K * math.cos(math.radians(10)), (LAT_TOP - lat) * K)


def path(rings):
    d = []
    for ring in rings:
        pts = [project(x, y) for x, y in ring]
        if all(p[0] < -20 or p[0] > W + 20 or p[1] < -20 or p[1] > H + 20 for p in pts):
            continue
        d.append("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + "Z")
    return "".join(d)


def polys(geom):
    if geom["type"] == "Polygon":
        return [geom["coordinates"]]
    return geom["coordinates"]


data = json.load(open(sys.argv[1]))
base, active = [], []
for f in data["features"]:
    name = f["properties"]["ADMIN"]
    if name == "Antarctica":
        continue
    rings = [r for p in polys(f["geometry"]) for r in p]
    d = path(rings)
    if not d:
        continue
    (active if name in ACTIVE else base).append(d)

out = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="map-title map-desc">',
    '<title id="map-title">Bahtera regional coverage</title>',
    '<desc id="map-desc">Map of Asia. India, the Philippines, Indonesia, Malaysia, and Singapore are highlighted as Bahtera’s operating countries.</desc>',
    f'<defs><clipPath id="frame"><rect x="0" y="0" width="{W}" height="{H}" rx="18"/></clipPath></defs>',
    '<g clip-path="url(#frame)">',
    f'<rect width="{W}" height="{H}" fill="#f1eadb"/>',
    '<g stroke="#d8d0bf" stroke-width="1" opacity=".55">',
]
for lon in range(70, 142, 10):
    x = project(lon, 0)[0]
    out.append(f'<path d="M{x:.1f} 0V{H}"/>')
for lat in range(-10, 40, 10):
    y = project(0, lat)[1]
    out.append(f'<path d="M0 {y:.1f}H{W}"/>')
out.append("</g>")
for d in base:
    out.append(f'<path d="{d}" fill="#dbd3c3" stroke="#bcb4a4" stroke-width="1.3" fill-rule="evenodd" stroke-linejoin="round"/>')
for d in active:
    out.append(f'<path d="{d}" fill="#193656" stroke="#f1eadb" stroke-width="1.3" fill-rule="evenodd" stroke-linejoin="round"/>')
for text, anchor, centre, w in LABELS:
    ax, ay = project(*anchor)
    cx, cy = project(*centre)
    if (ax, ay) != (cx, cy):
        out.append(f'<path d="M{ax:.1f} {ay:.1f}L{cx:.1f} {cy:.1f}" stroke="#b18d54" stroke-width="1.5"/>')
        out.append(f'<circle cx="{ax:.1f}" cy="{ay:.1f}" r="5" fill="#b18d54" stroke="#f8f4e8" stroke-width="2"/>')
    out.append(
        f'<g><rect x="{cx - w / 2:.1f}" y="{cy - 16:.1f}" width="{w}" height="32" rx="16" fill="#f8f4e8"/>'
        f'<text x="{cx:.1f}" y="{cy + 5:.1f}" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="700" letter-spacing="1.5" fill="#172b4d">{text}</text></g>'
    )
out.append("</g></svg>")
open(sys.argv[2], "w").write("\n".join(out))
