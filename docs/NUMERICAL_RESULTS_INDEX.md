# Numerical Results Index

This index makes the main quantitative claims visible without requiring a reader
to inspect every script or LaTeX source.

## Cosmology and GUP regulator

| Quantity | Value | Source track | Status |
|---|---:|---|---|
| Dark-energy density used in synthesis | `5.253229e-10 J/m^3` | `synthese-travaux-confirmes-gup-uvir/` | reproduced from CODATA/NIST 2022 and Planck 2018 inputs |
| Direct dark-energy matching parameter | `beta0_Lambda(g=1) = 2.363228e60` | `contrainte-energie-noire-gup/` | no-go value under direct `rho_reg = rho_DE` assumption |
| Mixed UV/IR energy scale | `E_P / sqrt(beta0_Lambda) = 7.94 meV` | `tests-donnees-publiques-gup-uvir/` | derived scale, not a standalone prediction |
| FIRAS photon-sector bound | `beta0 <= 3.72e58` | `tests-donnees-publiques-gup-uvir/` | excludes `beta0_Lambda` as universal photon parameter |
| BBN/radiation bound | `beta0 <= 2.64e41` | `tests-donnees-publiques-gup-uvir/` | excludes `beta0_Lambda` in primordial radiation sector |
| Dense-fermion bound | `beta0 <= 1.66e38` | `tests-donnees-publiques-gup-uvir/` | excludes `beta0_Lambda` for dense fermions |
| Holographic dark-energy example | `w0 = -0.885` for `Omega_DE=0.685`, `c_hde=1` | `tests-donnees-publiques-gup-uvir/` | in tension with approximate `w=-1.03 +- 0.03` public constraint |

## Fine-structure relation

| Quantity | Value | Source track | Status |
|---|---:|---|---|
| CODATA 2022 `alpha^-1` | `137.035999177` | `constante-structure-fine-uvir/` | reference value |
| Proposed relation with `10 pi` factor | `137.036063742708` | `constante-structure-fine-uvir/` | numerically close conjecture |
| Absolute difference | `6.4565708e-5` | computed from values above | far above CODATA uncertainty; not a confirmed prediction |
| Relative difference | `4.7e-7` | `constante-structure-fine-uvir/README.md` | useful scale, not enough for confirmation |

## Cold-atom sensor application

| Quantity | Value | Source track | Status |
|---|---:|---|---|
| Sr88 nominal interrogation time | `T_i = 0.102 s` | `cellule-phase-vitesse-gup/reports/sensor_noise_budget_report.md` | modeled scenario |
| Sr88 nominal cycle time | `T_cycle = 1.253 s` | `cellule-phase-vitesse-gup/reports/sensor_noise_budget_report.md` | modeled scenario |
| Sr88 nominal sensitivity | `11.52 microGal/sqrtHz` | `cellule-phase-vitesse-gup/reports/sensor_noise_budget_report.md` | first-order technical-noise model |
| Dominant Sr88 nominal noise | `vibration` | `cellule-phase-vitesse-gup/reports/sensor_noise_budget_report.md` | model output |
| NIM-like model benchmark | `19.72 microGal/sqrtHz` vs `20.5` published | `cellule-phase-vitesse-gup/` | sanity check |
| Muquans/Exail-like model benchmark | `26.44 microGal/sqrtHz` vs `50` datasheet | `cellule-phase-vitesse-gup/` | same order, not fitted |
| Rb87 GUP epsilon at `1 microkelvin`, `beta0=1` | `4.68e-56` | `cellule-phase-vitesse-gup/` | negligible correction |
| Rb87 GUP epsilon at `1 microkelvin`, `beta0=1e26` | `4.68e-30` | `cellule-phase-vitesse-gup/` | still negligible |

## Newton G metrology proposal

| Quantity | Value | Source track | Status |
|---|---:|---|---|
| Published cold-atom `G` reference uncertainty | about `150 ppm` | `PUBLICATION_MESURE_G_ATOMIQUE.md` | target to beat for atom-interferometer class |
| Best modern torsion-class uncertainty scale | about `10-30 ppm` | `PUBLICATION_MESURE_G_ATOMIQUE.md` | global competitiveness target |
| Proposed first milestone | `< 150 ppm` | `PUBLICATION_MESURE_G_ATOMIQUE.md` | beat atom-interferometer reference |
| Competitive milestone | `< 50 ppm` | `PUBLICATION_MESURE_G_ATOMIQUE.md` | competitive with modern measurements |
| State-of-art milestone | `< 10 ppm` | `PUBLICATION_MESURE_G_ATOMIQUE.md` | very difficult; geometry/systematics dominate |

## How to use this index

A value in this document is not automatically a confirmed physical prediction.
Each row must be read with its status column. The current repository contains a
mix of:

- reproduced public-data constraints;
- internal algebraic consequences;
- candidate conjectures;
- applied engineering estimates.

The professional standard is to keep those categories separate.
