# Generated Input Data

This directory is reserved for generated Monte Carlo estimate CSV files.

The canonical generated file is:

```text
data/public_prng_estimates.csv
```

It is produced by:

```bash
python scripts/generate_public_prng_estimates.py --N 50000 --R 8 --seeds 100
```

For the HAL v1.2 target run, use `--N 1000000` after the protocol is frozen.

The CSV schema is:

```csv
generator,backend,seed,integrand,replicate,N,estimate
```

The generated CSV is intentionally not committed in this WIP bundle until the target run is fixed, because it is a derived artifact and can be regenerated from the scripts.
