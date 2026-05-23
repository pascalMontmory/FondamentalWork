#!/usr/bin/env python3
"""Generate large-N curve data for prime-pattern terminal signatures.

Outputs CSV plus lightweight SVG curves for:

- D_B(pattern, control) for twin/cousin/sexy patterns;
- terminal filter mass nu_{B,P_H,N}(A).

The output is diagnostic. It does not prove terminal limits.
"""
from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

from mathclass_common import INF, build_samples, terminal_entry, tv


PATTERN_TO_NON_PATTERN = {
    "twin": "prime_non_twin",
    "cousin": "prime_non_cousin",
    "sexy": "prime_non_sexy",
}


def parse_ints(raw: str) -> list[int]:
    return [int(part) for part in raw.split(",") if part.strip()]


def parse_states(raw: str) -> set[str]:
    return {part.strip() for part in raw.split(",") if part.strip()}


def project_state(state: str, low_bound: int, max_steps: int) -> str:
    if state == INF:
        return INF
    value = int(state)
    if value <= low_bound:
        return state
    return terminal_entry(value, low_bound, max_steps)


def laws_for_values(values: list[int], bounds: list[int], max_steps: int) -> dict[int, dict[str, float]]:
    high = max(bounds)
    counts = {bound: Counter() for bound in bounds}
    for n in values:
        high_state = terminal_entry(n, high, max_steps)
        for bound in bounds:
            state = high_state if bound == high else project_state(high_state, bound, max_steps)
            counts[bound][state] += 1

    total = len(values)
    if total == 0:
        return {bound: {} for bound in bounds}
    return {
        bound: {state: count / total for state, count in counter.items()}
        for bound, counter in counts.items()
    }


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    headers = ["kind", "pattern", "control", "bound", "N", "value", "sample_size"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def svg_polyline(points: list[tuple[float, float]], color: str) -> str:
    if not points:
        return ""
    return (
        f'<polyline fill="none" stroke="{color}" stroke-width="2" points="'
        + " ".join(f"{x:.2f},{y:.2f}" for x, y in points)
        + '" />'
    )


def write_svg(path: Path, rows: list[dict[str, str]], kind: str, title: str) -> None:
    width = 980
    height = 520
    margin_left = 70
    margin_right = 30
    margin_top = 50
    margin_bottom = 70
    plot_width = width - margin_left - margin_right
    plot_height = height - margin_top - margin_bottom

    selected = [row for row in rows if row["kind"] == kind]
    if kind == "distance":
        selected = [row for row in selected if row["control"] == PATTERN_TO_NON_PATTERN[row["pattern"]]]
    if not selected:
        path.write_text("<svg xmlns=\"http://www.w3.org/2000/svg\"></svg>\n", encoding="utf-8")
        return

    ns = sorted({int(row["N"]) for row in selected})
    values = [float(row["value"]) for row in selected]
    max_value = max(values) if values else 1.0
    max_value = max(max_value, 1e-12)
    min_n = min(ns)
    max_n = max(ns)
    span_n = max(max_n - min_n, 1)

    colors = {"twin": "#1f77b4", "cousin": "#d62728", "sexy": "#2ca02c"}
    lines: list[str] = []
    legend: list[str] = []
    for idx, pattern in enumerate(["twin", "cousin", "sexy"]):
        pattern_rows = [row for row in selected if row["pattern"] == pattern]
        pattern_rows.sort(key=lambda row: int(row["N"]))
        points = []
        for row in pattern_rows:
            x = margin_left + (int(row["N"]) - min_n) / span_n * plot_width
            y = margin_top + (1.0 - float(row["value"]) / max_value) * plot_height
            points.append((x, y))
        color = colors[pattern]
        lines.append(svg_polyline(points, color))
        legend_y = margin_top + 20 * idx
        legend.append(
            f'<line x1="{width - 170}" y1="{legend_y}" x2="{width - 145}" y2="{legend_y}" '
            f'stroke="{color}" stroke-width="3" />'
            f'<text x="{width - 138}" y="{legend_y + 5}" font-size="13">{pattern}</text>'
        )

    x_labels = "\n".join(
        f'<text x="{margin_left + (n - min_n) / span_n * plot_width:.2f}" y="{height - 30}" '
        f'font-size="11" text-anchor="middle">{n}</text>'
        for n in ns
    )
    y_labels = "\n".join(
        f'<text x="{margin_left - 10}" y="{margin_top + (1 - frac) * plot_height + 4:.2f}" '
        f'font-size="11" text-anchor="end">{frac * max_value:.3f}</text>'
        for frac in [0.0, 0.25, 0.5, 0.75, 1.0]
    )
    grid = "\n".join(
        f'<line x1="{margin_left}" y1="{margin_top + frac * plot_height:.2f}" '
        f'x2="{width - margin_right}" y2="{margin_top + frac * plot_height:.2f}" '
        f'stroke="#ddd" stroke-width="1" />'
        for frac in [0.0, 0.25, 0.5, 0.75, 1.0]
    )

    path.write_text(
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<rect width="100%" height="100%" fill="white" />
<text x="{width / 2}" y="28" font-size="18" text-anchor="middle">{title}</text>
{grid}
<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{height - margin_bottom}" stroke="#333" />
<line x1="{margin_left}" y1="{height - margin_bottom}" x2="{width - margin_right}" y2="{height - margin_bottom}" stroke="#333" />
{x_labels}
{y_labels}
{"".join(lines)}
{"".join(legend)}
<text x="{width / 2}" y="{height - 8}" font-size="12" text-anchor="middle">N</text>
</svg>
''',
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limits", default="300000,1000000,3000000")
    parser.add_argument("--bounds", default="27,89,127")
    parser.add_argument("--terminal-set", default="14,23,61,89")
    parser.add_argument("--output-dir", default="Math/MathClass/reports/large-scan-2026-05-23")
    parser.add_argument("--max-steps", type=int, default=10_000)
    args = parser.parse_args()

    limits = parse_ints(args.limits)
    bounds = parse_ints(args.bounds)
    terminal_set = parse_states(args.terminal_set)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, str]] = []
    for limit in limits:
        samples = build_samples(limit)
        needed = set(["prime", "admissible_210", "admissible_2310"])
        needed.update(PATTERN_TO_NON_PATTERN)
        needed.update(PATTERN_TO_NON_PATTERN.values())

        laws = {
            name: laws_for_values(samples[name].values, bounds, args.max_steps)
            for name in sorted(needed)
        }
        for pattern, non_pattern in PATTERN_TO_NON_PATTERN.items():
            sample_size = str(len(samples[pattern].values))
            for bound in bounds:
                for control in ["prime", non_pattern, "admissible_210", "admissible_2310"]:
                    value = tv(laws[pattern][bound], laws[control][bound])
                    rows.append(
                        {
                            "kind": "distance",
                            "pattern": pattern,
                            "control": control,
                            "bound": str(bound),
                            "N": str(limit),
                            "value": f"{value:.17g}",
                            "sample_size": sample_size,
                        }
                    )
                mass = sum(laws[pattern][bound].get(state, 0.0) for state in terminal_set)
                rows.append(
                    {
                        "kind": "filter_mass",
                        "pattern": pattern,
                        "control": args.terminal_set,
                        "bound": str(bound),
                        "N": str(limit),
                        "value": f"{mass:.17g}",
                        "sample_size": sample_size,
                    }
                )
        print(f"completed N={limit}")

    csv_path = output_dir / "prime_pattern_terminal_curves.csv"
    write_csv(csv_path, rows)
    write_svg(
        output_dir / "distance_to_non_pattern_control.svg",
        rows,
        "distance",
        "D_B(pattern, prime non-pattern control)",
    )
    write_svg(
        output_dir / "terminal_filter_mass.svg",
        rows,
        "filter_mass",
        f"Terminal filter mass A={{{args.terminal_set}}}",
    )

    print(csv_path)
    print(output_dir / "distance_to_non_pattern_control.svg")
    print(output_dir / "terminal_filter_mass.svg")


if __name__ == "__main__":
    main()
