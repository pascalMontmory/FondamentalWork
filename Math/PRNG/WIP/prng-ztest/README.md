# PRNG Z-Test Protocol

CPU-only reproducible protocol for the calibrated diagnostic:

```math
Z_s(f)=F_{\chi^2_{R-1}}\left(\frac{(R-1)V_s(f)}{\sigma_f^2/N}\right).
```

The goal is to decide whether a large raw seed-variance ratio is a true anomaly or a fluctuation compatible with the null model.

## Input Format

CSV with one row per Monte Carlo replicate:

```csv
generator,backend,seed,integrand,replicate,N,estimate
Philox,cpu,0,rare_099,0,1000000,0.00997
Philox,cpu,0,rare_099,1,1000000,0.01004
```

Required columns:

| Column | Meaning |
|---|---|
| `generator` | PRNG name |
| `backend` | CPU, CUDA, Metal, etc. |
| `seed` | tested seed |
| `integrand` | diagnostic function |
| `replicate` | replicate id |
| `N` | draws per replicate |
| `estimate` | Monte Carlo estimate |

Supported built-in integrands are `identity`, `sin`, `quadratic`, and `rare_099`.

## Run Public PRNG Benchmark

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python scripts/generate_public_prng_estimates.py --N 50000 --R 8 --seeds 100

python scripts/compute_z_scores.py \
  --input data/public_prng_estimates.csv \
  --out-table results/z_scores_table.csv \
  --out-summary results/z_summary.csv

python scripts/plot_z_histograms.py \
  --input results/z_scores_table.csv \
  --outdir figures
```

## Interpretation

The raw ratio

```math
\rho_f=\frac{\max_s V_s(f)}{\min_{s,V_s(f)>0}V_s(f)}
```

is only an alert. The calibrated diagnostic is `Z_s`.

Under the null model:

```math
Z_s(f)\sim U[0,1].
```

If the `Z_s` values are approximately uniform, the raw variance ratio should be relativized. If the `Z_s` values concentrate near 0 or 1, there is a signal of seed-conditioned instability.

The summary reports:

- `rho_max_min`
- `rho_q95_q05`
- `Z_KS_pvalue`
- `Z_extreme_rate_001`
- `N_eff_ratio_q05`, median, and q95
- `verdict`

## TACM Placement

This protocol is the bridge between raw seed-variance ratios and calibrated null-model diagnostics. In TACM v1.1, it belongs under:

```text
Calibrated seed-conditioned variance diagnostic
```

with `Z_s=F_0(V_s)` as the central formula.
