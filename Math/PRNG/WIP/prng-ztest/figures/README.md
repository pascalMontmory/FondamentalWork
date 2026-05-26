# Generated Figures

This directory is reserved for the generated `Z_s` histogram figures.

The expected files are:

```text
figures/hist_Zs_identity.png
figures/hist_Zs_sin.png
figures/hist_Zs_quadratic.png
figures/hist_Zs_rare_099.png
```

Regenerate them with:

```bash
python scripts/plot_z_histograms.py \
  --input results/z_scores_table.csv \
  --outdir figures
```

The figures are derived artifacts. They should be committed once the final HAL v1.2 target run is fixed, preferably with `N=1000000` or the selected publication configuration.
