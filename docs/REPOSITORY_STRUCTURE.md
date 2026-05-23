# Repository Structure

FondamentalWork uses domain namespaces plus status-specific subdirectories.

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

## Status Policy

Research material should separate:

- definitions;
- verified lemmas or derivations;
- computational evidence;
- conditional statements;
- conjectures;
- open problems;
- old or superseded drafts.

The directory name alone must not imply that a result is proven.

## Standard Topic Layout

Where practical, each domain or topic should follow this pattern:

```text
<topic>/README.md          Entry point and status policy.
<topic>/non-validated/     Hypotheses, draft articles, speculative claims, negative diagnostics.
<topic>/work/              Scripts, run notes, data provenance, temporary work products.
<topic>/old/               Optional historical/superseded material.
```

## COSMO Layout

`COSMO/` now has explicit status areas:

```text
COSMO/README.md
COSMO/READING_ORDER.md
COSMO/non-validated/
COSMO/work/
COSMO/<track>/
```

`COSMO/non-validated/` is the correct place for unverified theoretical claims, candidate publications, speculative derivations, and analyzed but non-confirmed results.

`COSMO/work/` is the correct place for scripts, run manifests, data notes, and reproducibility helpers.

## Math Policy

Mathematical material should separate:

- exact definitions;
- verified lemmas or theorems;
- computational evidence;
- conjectures;
- open problems.

This separation matters because the repository mixes mature derivations, numerical checks, and exploratory research.

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

This migration did not validate any scientific claim by itself. Each track still needs per-file status review.

In the first COSMO status cleanup, these tracks were then moved under
`COSMO/non-validated/` because their own summaries describe them as conjectural,
programmatic, interpretive, or dependent on unverified assumptions:

- `conclusions-cosmologiques-gup-uvir/`
- `consequences-alpha-uvir-electromagnetisme/`
- `constante-structure-fine-uvir/`
- `programme-tests-experimentaux-uvir/`
