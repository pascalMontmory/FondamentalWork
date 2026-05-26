# Generated Input Data

This directory is reserved for generated Monte Carlo estimate CSV files.

The canonical generated file is:

```text
data/public_prng_estimates.csv
```

It is produced by:

```bash
python scripts/generate_public_prng_estimates.py --N 50000 --R 8 --seeds 1000
```

The HAL `hal-05633702v1` public baseline uses `N=50000`, `R=8`, and `1000` seeds per generator.

The CSV schema is:

```csv
generator,backend,seed,integrand,replicate,N,estimate
```

The generated CSV is intentionally not committed in this WIP bundle because it is a large derived artifact and can be regenerated from the scripts. It may be archived separately as a release artifact.
