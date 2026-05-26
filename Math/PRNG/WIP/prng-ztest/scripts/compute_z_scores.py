import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import chi2, kstest


SIGMA2 = {
    "identity": 1 / 12,
    "sin": 1 / 2,
    "quadratic": 4 / 45,
    "rare_099": 0.01 * 0.99,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compute calibrated seed-conditioned variance diagnostics Z_s."
    )
    parser.add_argument("--input", default="data/public_prng_estimates.csv")
    parser.add_argument("--out-table", default="results/z_scores_table.csv")
    parser.add_argument("--out-summary", default="results/z_summary.csv")
    return parser.parse_args()


def safe_ratio(values: np.ndarray) -> float:
    positive = values[values > 0]
    if len(positive) == 0:
        return float("inf")
    return float(np.max(values) / np.min(positive))


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.input)

    missing = {"generator", "backend", "seed", "integrand", "replicate", "N", "estimate"} - set(df)
    if missing:
        raise ValueError(f"missing required columns: {sorted(missing)}")

    rows = []
    grouped = df.groupby(["generator", "backend", "seed", "integrand", "N"], sort=True)
    for (generator, backend, seed, integrand, n_draws), group in grouped:
        if integrand not in SIGMA2:
            raise ValueError(f"unknown integrand {integrand!r}; expected one of {sorted(SIGMA2)}")

        values = group.sort_values("replicate")["estimate"].to_numpy(dtype=float)
        r_count = len(values)
        if r_count < 2:
            continue

        v_s = float(np.var(values, ddof=1))
        sigma2 = SIGMA2[integrand]
        t_s = (r_count - 1) * v_s / (sigma2 / n_draws)
        z_s = float(chi2.cdf(t_s, df=r_count - 1))
        n_eff = float(sigma2 / v_s) if v_s > 0 else float("inf")

        rows.append(
            {
                "generator": generator,
                "backend": backend,
                "seed": seed,
                "integrand": integrand,
                "N": n_draws,
                "R": r_count,
                "V_s": v_s,
                "sigma2": sigma2,
                "T_s": t_s,
                "Z_s": z_s,
                "N_eff": n_eff,
                "N_eff_ratio": n_eff / n_draws,
            }
        )

    zdf = pd.DataFrame(rows)
    Path(args.out_table).parent.mkdir(parents=True, exist_ok=True)
    zdf.to_csv(args.out_table, index=False)

    summary = []
    for (generator, backend, integrand), group in zdf.groupby(["generator", "backend", "integrand"], sort=True):
        z = group["Z_s"].to_numpy(dtype=float)
        v = group["V_s"].to_numpy(dtype=float)
        n_eff_ratio = (
            group["N_eff_ratio"]
            .replace([np.inf, -np.inf], np.nan)
            .dropna()
            .to_numpy(dtype=float)
        )

        ks = kstest(z, "uniform")
        extreme_rate = float(np.mean((z < 0.01) | (z > 0.99)))
        verdict = "compatible"
        if extreme_rate > 0.06:
            verdict = "tail_anomaly"
        elif ks.pvalue < 0.05:
            verdict = "calibration_drift"

        summary.append(
            {
                "generator": generator,
                "backend": backend,
                "integrand": integrand,
                "rho_max_min": safe_ratio(v),
                "rho_q95_q05": float(np.quantile(v, 0.95) / np.quantile(v, 0.05)),
                "Z_KS_stat": float(ks.statistic),
                "Z_KS_pvalue": float(ks.pvalue),
                "Z_extreme_rate_001": extreme_rate,
                "N_eff_ratio_q05": float(np.quantile(n_eff_ratio, 0.05)),
                "N_eff_ratio_median": float(np.median(n_eff_ratio)),
                "N_eff_ratio_q95": float(np.quantile(n_eff_ratio, 0.95)),
                "verdict": verdict,
            }
        )

    sdf = pd.DataFrame(summary)
    sdf.to_csv(args.out_summary, index=False)
    print(sdf.to_string(index=False))
    print(f"written {args.out_table}")
    print(f"written {args.out_summary}")


if __name__ == "__main__":
    main()
