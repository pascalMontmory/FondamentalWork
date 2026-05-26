import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Plot Z_s ECDF curves against the uniform diagonal.")
    parser.add_argument("--input", default="results/z_scores_table.csv")
    parser.add_argument("--outdir", default="figures")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    for integrand in sorted(df["integrand"].unique()):
        fig, ax = plt.subplots(figsize=(6.5, 5.5))
        ax.plot([0, 1], [0, 1], linestyle="--", linewidth=1.2, color="0.4", label="Uniform diagonal")

        for generator in sorted(df["generator"].unique()):
            group = df[(df["integrand"] == integrand) & (df["generator"] == generator)]
            if group.empty:
                continue
            z = np.sort(group["Z_s"].to_numpy(dtype=float))
            y = np.arange(1, len(z) + 1, dtype=float) / len(z)
            ax.step(z, y, where="post", linewidth=1.5, label=generator)

        ax.set_title(f"Z_s ECDF vs uniform - {integrand}")
        ax.set_xlabel("Z_s")
        ax.set_ylabel("Empirical CDF")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.grid(True, alpha=0.25)
        ax.legend()
        fig.tight_layout()

        for ext in ("png", "svg"):
            path = outdir / f"ecdf_Zs_{integrand}.{ext}"
            fig.savefig(path, dpi=160 if ext == "png" else None)
            print(f"written {path}")

        plt.close(fig)


if __name__ == "__main__":
    main()
