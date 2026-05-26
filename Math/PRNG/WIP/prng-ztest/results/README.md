# Generated Results

This directory contains or documents the derived outputs of the calibrated PRNG Z-test pipeline.

The committed summary file is:

```text
results/z_summary.csv
```

The full seed-level table is generated as:

```text
results/z_scores_table.csv
```

Regenerate it with:

```bash
python scripts/compute_z_scores.py \
  --input data/public_prng_estimates.csv \
  --out-table results/z_scores_table.csv \
  --out-summary results/z_summary.csv
```

`z_scores_table.csv` contains one row per `(generator, backend, seed, integrand, N)` with:

```text
V_s, sigma2, T_s, Z_s, N_eff, N_eff_ratio
```

The WIP repository commits `z_summary.csv` as the lightweight audit summary. The complete `z_scores_table.csv` remains a generated artifact until the target HAL v1.2 run is fixed.
