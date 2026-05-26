# Generated Figures

This directory contains versioned `Z_s` figures for the calibrated PRNG variance diagnostic.

The ECDF figures are the preferred visual diagnostic because they compare the empirical distribution of `Z_s` directly to the uniform diagonal `F(z)=z`.

| Integrand | ECDF figure |
|---|---|
| `identity` | ![Z_s ECDF identity](ecdf_Zs_identity.svg) |
| `sin` | ![Z_s ECDF sin](ecdf_Zs_sin.svg) |
| `quadratic` | ![Z_s ECDF quadratic](ecdf_Zs_quadratic.svg) |
| `rare_099` | ![Z_s ECDF rare_099](ecdf_Zs_rare_099.svg) |

Histogram figures are also supported by the pipeline:

```bash
python scripts/plot_z_histograms.py \
  --input results/z_scores_table.csv \
  --outdir figures
```

ECDF figures are generated with:

```bash
python scripts/plot_z_ecdf.py \
  --input results/z_scores_table.csv \
  --outdir figures
```

The current reference run uses `N=50000`, `R=8`, and `1000` seeds per generator. The full `z_scores_table.csv` is a derived artifact and can be regenerated from the scripts.
