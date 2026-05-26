import argparse
from pathlib import Path

import numpy as np
import pandas as pd


INTEGRANDS = {
    "identity": lambda u: u,
    "sin": lambda u: np.sin(2 * np.pi * u),
    "quadratic": lambda u: u * u,
    "rare_099": lambda u: (u > 0.99).astype(float),
}

BITGENS = {
    "PCG64": np.random.PCG64,
    "MT19937": np.random.MT19937,
    "Philox": np.random.Philox,
    "SFC64": np.random.SFC64,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate seed/replicate Monte Carlo estimates for public NumPy PRNGs."
    )
    parser.add_argument("--N", type=int, default=50_000)
    parser.add_argument("--R", type=int, default=8)
    parser.add_argument("--seeds", type=int, default=1000)
    parser.add_argument("--out", default="data/public_prng_estimates.csv")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = []

    for generator_name, bitgen_cls in BITGENS.items():
        for seed in range(args.seeds):
            for replicate in range(args.R):
                derived_seed = seed * 1_000_003 + replicate * 9_176 + 12_345
                rng = np.random.Generator(bitgen_cls(derived_seed))
                u = rng.random(args.N)

                for integrand_name, func in INTEGRANDS.items():
                    rows.append(
                        {
                            "generator": generator_name,
                            "backend": "cpu",
                            "seed": seed,
                            "integrand": integrand_name,
                            "replicate": replicate,
                            "N": args.N,
                            "estimate": float(np.mean(func(u))),
                        }
                    )

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(out, index=False)
    print(f"written {out}")


if __name__ == "__main__":
    main()
