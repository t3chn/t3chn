#!/usr/bin/env python3
"""Generate the light and dark control-plane profile artwork."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"

THEMES = {
    "dark": {
        "background": "#0B0F14",
        "surface": "#111821",
        "ink": "#E6EDF3",
        "muted": "#91A4B7",
        "active": "#4DB4FF",
        "proof": "#45D483",
        "guard": "#F2B84B",
        "border": "#2A3746",
        "track": "#1A2531",
    },
    "light": {
        "background": "#F6F8FA",
        "surface": "#FFFFFF",
        "ink": "#15202B",
        "muted": "#536477",
        "active": "#0969DA",
        "proof": "#16833C",
        "guard": "#9A5B00",
        "border": "#C8D1DC",
        "track": "#E7ECF1",
    },
}

SYSTEMS = (
    ("SIGNUM", "contract-first proof gate", "ACTIVE", "proof"),
    ("HERALD", "local-first news intelligence", "ACTIVE", "active"),
    ("ARBITER", "independent AI review routing", "ACTIVE", "active"),
    ("PUNK", "bounded work kernel", "EXPERIMENTAL", "guard"),
)


def system_row(x: int, y: int, item: tuple[str, str, str, str], colors: dict[str, str]) -> str:
    name, description, status, status_color = item
    return f"""
    <line x1="{x}" y1="{y - 25}" x2="{x + 395}" y2="{y - 25}" class="rule" />
    <circle cx="{x + 7}" cy="{y}" r="5" fill="{colors[status_color]}" class="status-dot" />
    <text x="{x + 24}" y="{y + 5}" class="system-name">{name}</text>
    <text x="{x + 24}" y="{y + 27}" class="system-copy">{description}</text>
    <text x="{x + 395}" y="{y + 5}" text-anchor="end" class="system-status" fill="{colors[status_color]}">{status}</text>
    """


def render(theme_name: str, colors: dict[str, str]) -> str:
    rows = "".join(
        (
            system_row(50, 360, SYSTEMS[0], colors),
            system_row(50, 435, SYSTEMS[1], colors),
            system_row(515, 360, SYSTEMS[2], colors),
            system_row(515, 435, SYSTEMS[3], colors),
        )
    )

    nodes = (
        (95, "INTENT", colors["active"]),
        (285, "CONTRACT", colors["active"]),
        (480, "AGENT WORK", colors["guard"]),
        (680, "PROOF", colors["proof"]),
        (865, "OUTCOME", colors["proof"]),
    )
    node_markup = "".join(
        f"""
        <circle cx="{x}" cy="267" r="9" fill="{color}" />
        <circle cx="{x}" cy="267" r="18" fill="none" stroke="{color}" stroke-opacity=".25" />
        <text x="{x}" y="305" text-anchor="middle" class="node-label">{label}</text>
        """
        for x, label, color in nodes
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="960" height="560" viewBox="0 0 960 560" role="img" aria-labelledby="title description">
  <title id="title">t3chn control plane</title>
  <desc id="description">Vitaly D. builds bounded, inspectable agent systems where humans own outcomes.</desc>
  <defs>
    <marker id="arrow-{theme_name}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 Z" fill="{colors['muted']}" />
    </marker>
    <style>
      text {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace; }}
      .frame {{ fill: {colors['surface']}; stroke: {colors['border']}; }}
      .rule {{ stroke: {colors['border']}; stroke-width: 1; }}
      .brand {{ fill: {colors['ink']}; font-size: 46px; font-weight: 760; letter-spacing: -1px; }}
      .control {{ fill: {colors['active']}; font-size: 13px; font-weight: 700; letter-spacing: 1.8px; }}
      .role {{ fill: {colors['ink']}; font-size: 19px; font-weight: 650; }}
      .mission {{ fill: {colors['muted']}; font-size: 15px; }}
      .label {{ fill: {colors['muted']}; font-size: 11px; font-weight: 700; letter-spacing: 1.4px; }}
      .principle {{ fill: {colors['ink']}; font-size: 16px; font-weight: 650; }}
      .principle.guard {{ fill: {colors['guard']}; }}
      .node-label {{ fill: {colors['muted']}; font-size: 11px; font-weight: 700; letter-spacing: .7px; }}
      .system-name {{ fill: {colors['ink']}; font-size: 16px; font-weight: 750; letter-spacing: .5px; }}
      .system-copy {{ fill: {colors['muted']}; font-size: 13px; }}
      .system-status {{ font-size: 10px; font-weight: 750; letter-spacing: 1px; }}
      .footer {{ fill: {colors['muted']}; font-size: 12px; }}
      .flow {{ stroke: {colors['muted']}; stroke-width: 1.5; stroke-dasharray: 7 7; animation: flow 6s linear infinite; }}
      .status-ring {{ transform-origin: 893px 31px; animation: pulse 2.4s ease-out infinite; }}
      .status-dot {{ animation: breathe 2.8s ease-in-out infinite; }}
      @keyframes flow {{ to {{ stroke-dashoffset: -56; }} }}
      @keyframes pulse {{ 0% {{ opacity: .55; transform: scale(.65); }} 70%, 100% {{ opacity: 0; transform: scale(1.45); }} }}
      @keyframes breathe {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: .55; }} }}
      @media (prefers-reduced-motion: reduce) {{
        .flow, .status-ring, .status-dot {{ animation: none; }}
      }}
    </style>
  </defs>

  <rect width="960" height="560" rx="13" fill="{colors['background']}" />
  <rect x="1" y="1" width="958" height="558" rx="12" class="frame" />

  <line x1="1" y1="57" x2="959" y2="57" class="rule" />
  <circle cx="29" cy="29" r="5" fill="{colors['guard']}" />
  <text x="45" y="34" class="control">T3CHN / CONTROL PLANE</text>
  <text x="846" y="35" class="label">ONLINE</text>
  <circle cx="893" cy="31" r="6" fill="{colors['proof']}" />
  <circle cx="893" cy="31" r="11" fill="none" stroke="{colors['proof']}" class="status-ring" />
  <text x="916" y="35" text-anchor="middle" class="footer">V1</text>

  <text x="50" y="123" class="brand">t3chn</text>
  <text x="52" y="157" class="role">Vitaly D. — agent systems builder</text>
  <text x="52" y="187" class="mission">I build systems where agents can act,</text>
  <text x="52" y="210" class="mission">and humans still own the outcome.</text>

  <line x1="580" y1="88" x2="580" y2="210" class="rule" />
  <text x="620" y="103" class="label">OPERATING PRINCIPLE</text>
  <text x="620" y="139" class="principle">Bound the work.</text>
  <text x="620" y="166" class="principle">Inspect the evidence.</text>
  <text x="620" y="193" class="principle guard">Own the outcome.</text>

  <text x="50" y="248" class="label">CONTROL LOOP</text>
  <line x1="114" y1="267" x2="266" y2="267" class="flow" marker-end="url(#arrow-{theme_name})" />
  <line x1="304" y1="267" x2="461" y2="267" class="flow" marker-end="url(#arrow-{theme_name})" />
  <line x1="499" y1="267" x2="661" y2="267" class="flow" marker-end="url(#arrow-{theme_name})" />
  <line x1="699" y1="267" x2="846" y2="267" class="flow" marker-end="url(#arrow-{theme_name})" />
  {node_markup}

  <text x="50" y="326" class="label">ACTIVE SYSTEMS</text>
  {rows}

  <line x1="50" y1="495" x2="910" y2="495" class="rule" />
  <text x="50" y="527" class="footer">machine-first infrastructure / bounded autonomy / proof-bearing work</text>
  <text x="910" y="527" text-anchor="end" class="footer">AUTOMATE THE WORK · OWN THE OUTCOME</text>
</svg>
"""


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    for theme_name, colors in THEMES.items():
        output = ASSETS / f"control-plane-{theme_name}.svg"
        svg = "\n".join(line.rstrip() for line in render(theme_name, colors).splitlines()) + "\n"
        output.write_text(svg, encoding="utf-8")
        print(output.relative_to(ROOT))


if __name__ == "__main__":
    main()
