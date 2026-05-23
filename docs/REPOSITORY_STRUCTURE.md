# Repository Structure

FondamentalWork uses a two-namespace layout.

## Top-Level Directories

| Directory | Rule |
| --- | --- |
| `COSMO/` | Fundamental physics, cosmology, GUP, UV/IR, holography, observational tests, and sensor-related applications. |
| `Math/` | Reusable mathematical foundations shared with other repositories or theory tracks. |
| `docs/` | Repository-level documentation and process notes. |

## Root Policy

The repository root should stay small. Keep only:

- root `README.md`;
- top-level namespaces;
- repository-level configuration;
- cross-cutting documentation in `docs/`.

New research tracks should not be added directly at root. Put them under the closest namespace.

## Math Policy

Mathematical material should separate:

- definitions;
- verified lemmas or theorems;
- computational evidence;
- conjectures;
- open problems.

This separation matters because the repository mixes mature derivations, numerical checks, and exploratory research. The directory name alone must not imply that a result is proven.

## COSMO Migration

The following root directories were moved under `COSMO/` without changing their internal content:

- `cellule-phase-deformee-gup/`
- `cellule-phase-vitesse-gup/`
- `conclusions-cosmologiques-gup-uvir/`
- `consequences-alpha-uvir-electromagnetisme/`
- `constante-structure-fine-uvir/`
- `contrainte-energie-noire-gup/`
- `programme-tests-experimentaux-uvir/`
- `relations-uv-ir-holographie-gup/`
- `synthese-travaux-confirmes-gup-uvir/`
- `tests-donnees-publiques-gup-uvir/`
- `theorie-holographique-uvir-cellule-phase-deformee/`