#!/usr/bin/env python3
"""Generate the density and cumulative saturation figure for gamma=3."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "figures" / "gup_density_saturation.png"


def main() -> None:
    q = np.linspace(0.0, 8.0, 1000)
    density = q**2 / (1.0 + q**2) ** 3
    density /= density.max()

    cumulative = (2.0 / np.pi) * (
        np.arctan(q) - q * (1.0 - q**2) / (1.0 + q**2) ** 2
    )

    FIGURE.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8.5, 4.8))
    plt.plot(q, density, label="densite normalisee")
    plt.plot(q, cumulative, label="cumul N(q)/Nmax")
    plt.xlabel(r"$q=\sqrt{\beta}p$")
    plt.ylabel("valeur normalisee")
    plt.xlim(0, 8)
    plt.ylim(0, 1.05)
    plt.grid(True, alpha=0.28)
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIGURE, dpi=180)


if __name__ == "__main__":
    main()
