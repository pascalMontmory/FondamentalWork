# COSMO

This namespace is the target home for the cosmology and fundamental-physics
research tracks currently developed in the repository root.

It groups the work around:

```text
GUP phase-space cell
-> UV regularization
-> UV/IR holographic projection
-> dark-energy no-go and constraints
-> public-data tests
-> cosmological synthesis
-> speculative twin-sector extensions
-> cold-atom sensor applications derived from the same phase-space language
```

## Current status

The physical migration is intentionally staged. The existing research folders
remain at the repository root for now because many LaTeX files, scripts and
reports use relative paths.

This `COSMO/` directory is therefore an index and migration target first. Track
folders should be moved here only after their commands and links have been
checked.

## Tracks to migrate here

| Current root track | Target path | Role |
|---|---|---|
| `cellule-phase-deformee-gup/` | `COSMO/cellule-phase-deformee-gup/` | GUP phase-space cell and UV saturation |
| `contrainte-energie-noire-gup/` | `COSMO/contrainte-energie-noire-gup/` | dark-energy no-go for direct local GUP matching |
| `relations-uv-ir-holographie-gup/` | `COSMO/relations-uv-ir-holographie-gup/` | UV/IR and holographic relations |
| `conclusions-cosmologiques-gup-uvir/` | `COSMO/conclusions-cosmologiques-gup-uvir/` | cosmological conclusions |
| `theorie-holographique-uvir-cellule-phase-deformee/` | `COSMO/theorie-holographique-uvir-cellule-phase-deformee/` | master UV/IR framework |
| `constante-structure-fine-uvir/` | `COSMO/constante-structure-fine-uvir/` | alpha--Lambda conjecture |
| `consequences-alpha-uvir-electromagnetisme/` | `COSMO/consequences-alpha-uvir-electromagnetisme/` | electromagnetic consequences |
| `tests-donnees-publiques-gup-uvir/` | `COSMO/tests-donnees-publiques-gup-uvir/` | public-data constraints |
| `programmes-verification-publique-uvir/` | `COSMO/programmes-verification-publique-uvir/` | public verification pipeline |
| `programme-tests-experimentaux-uvir/` | `COSMO/programme-tests-experimentaux-uvir/` | experimental test program |
| `univers-jumeau-masse-negative-temps-inverse/` | `COSMO/univers-jumeau-masse-negative-temps-inverse/` | speculative twin-sector extension |
| `synthese-travaux-confirmes-gup-uvir/` | `COSMO/synthese-travaux-confirmes-gup-uvir/` | confirmed-results synthesis |
| `cellule-phase-vitesse-gup/` | `COSMO/cellule-phase-vitesse-gup/` | sensor and metrology applications |

## Canonical review path

Before the physical migration, use the root-level documentation:

- `../README.md`
- `../docs/CLAIMS_MATRIX.md`
- `../docs/NUMERICAL_RESULTS_INDEX.md`
- `../docs/PUBLICATION_CATALOG.md`
- `../docs/SCIENTIFIC_CONSOLIDATION_PLAN.md`

## Migration rule

A track can be moved into `COSMO/` when:

1. its README links are updated;
2. its LaTeX builds still compile from the new path;
3. its Python scripts still run from the new path;
4. generated artifacts remain ignored or reproducible;
5. the PR shows only intentional path changes.
