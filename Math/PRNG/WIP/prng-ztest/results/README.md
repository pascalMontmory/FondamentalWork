# Generated Results

This directory contains or documents the derived outputs of the calibrated PRNG Z-test pipeline.

The committed summary files are:

```text
results/z_summary.csv
results/binomial_rare_event_summary.csv
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

Regenerate the exact/randomized binomial rare-event PIT table with:

```bash
python scripts/compute_binomial_rare_event_z.py \
  --input data/public_prng_estimates.csv \
  --out-table results/binomial_rare_event_table.csv \
  --out-summary results/binomial_rare_event_summary.csv
```

`z_scores_table.csv` contains one row per `(generator, backend, seed, integrand, N)` with:

```text
V_s, sigma2, T_s, Z_s, N_eff, N_eff_ratio
```

The WIP repository commits the lightweight audit summaries. The complete seed-level CSV files remain generated artifacts and may be archived separately as release artifacts.
