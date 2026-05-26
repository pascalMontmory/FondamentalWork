import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Plot Z_s histograms by integrand and generator.")
    parser.add_argument("--input", default="results/z_scores_table.csv")
    parser.add_argument("--outdir", default="figures")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    for integrand in sorted(df["integrand"].unique()):
        plt.figure(figsize=(9, 5))

        for generator in sorted(df["generator"].unique()):
            group = df[(df["integrand"] == integrand) & (df["generator"] == generator)]
            if group.empty:
                continue
            plt.hist(
                group["Z_s"].to_numpy(dtype=float),
                bins=10,
                histtype="step",
                linewidth=1.5,
                label=generator,
            )

        plt.title(f"Z_s histogram - {integrand}")
        plt.xlabel("Z_s")
        plt.ylabel("count")
        plt.legend()
        plt.tight_layout()

        path = outdir / f"hist_Zs_{integrand}.png"
        plt.savefig(path, dpi=160)
        plt.close()
        print(f"written {path}")


if __name__ == "__main__":
    main()
