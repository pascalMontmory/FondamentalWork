import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import binom, kstest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compute exact/randomized binomial PIT diagnostics for rare_099 estimates."
    )
    parser.add_argument("--input", default="data/public_prng_estimates.csv")
    parser.add_argument("--out-table", default="results/binomial_rare_event_table.csv")
    parser.add_argument("--out-summary", default="results/binomial_rare_event_summary.csv")
    parser.add_argument("--integrand", default="rare_099")
    parser.add_argument("--p-event", type=float, default=0.01)
    parser.add_argument("--rng-seed", type=int, default=123456789)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.input)
    required = {"generator", "backend", "seed", "integrand", "replicate", "N", "estimate"}
    missing = required - set(df)
    if missing:
        raise ValueError(f"missing required columns: {sorted(missing)}")

    rdf = df[df["integrand"] == args.integrand].copy()
    if rdf.empty:
        raise ValueError(f"no rows found for integrand={args.integrand!r}")

    rng = np.random.default_rng(args.rng_seed)
    rows = []
    for row in rdf.itertuples(index=False):
        n_draws = int(row.N)
        k_count = int(round(float(row.estimate) * n_draws))
        cdf_left = float(binom.cdf(k_count - 1, n_draws, args.p_event)) if k_count > 0 else 0.0
        pmf = float(binom.pmf(k_count, n_draws, args.p_event))
        z_rand = cdf_left + rng.random() * pmf
        z_midp = cdf_left + 0.5 * pmf
        rows.append(
            {
                "generator": row.generator,
                "backend": row.backend,
                "seed": row.seed,
                "replicate": row.replicate,
                "N": n_draws,
                "p_event": args.p_event,
                "K": k_count,
                "Z_bin_midp": z_midp,
                "Z_bin_rand": z_rand,
            }
        )

    out = pd.DataFrame(rows)
    Path(args.out_table).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.out_table, index=False)

    summary = []
    for (generator, backend, n_draws), group in out.groupby(["generator", "backend", "N"], sort=True):
        z_midp = group["Z_bin_midp"].to_numpy(dtype=float)
        z_rand = group["Z_bin_rand"].to_numpy(dtype=float)
        ks_midp = kstest(z_midp, "uniform")
        ks_rand = kstest(z_rand, "uniform")
        tail_rate = float(np.mean((z_rand < 0.01) | (z_rand > 0.99)))
        verdict = "tail_anomaly" if tail_rate > 0.06 else "compatible"
        summary.append(
            {
                "generator": generator,
                "backend": backend,
                "N": n_draws,
                "replicates_total": len(group),
                "p_event": args.p_event,
                "mean_K": float(group["K"].mean()),
                "KS_midp_stat": float(ks_midp.statistic),
                "KS_midp_pvalue": float(ks_midp.pvalue),
                "KS_rand_stat": float(ks_rand.statistic),
                "KS_rand_pvalue": float(ks_rand.pvalue),
                "tail_rate_rand_001": tail_rate,
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
