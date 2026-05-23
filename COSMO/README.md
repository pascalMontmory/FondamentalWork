# COSMO

This namespace contains the fundamental-physics side of the repository: GUP, UV/IR, holography, cosmology, observational tests, and sensor-oriented applications.

The move into `COSMO/` was initially structural: formulas, scripts, and notes were preserved under their original directory names. The current cleanup adds explicit status discipline so a reader can distinguish consolidated work from hypotheses.

## Start Here

Read in this order:

1. [READING_ORDER.md](READING_ORDER.md) for the intended scientific pipeline and reading path.
2. `synthese-travaux-confirmes-gup-uvir/` for the strongest consolidated claims, if each document states its status.
3. `theorie-holographique-uvir-cellule-phase-deformee/` and `relations-uv-ir-holographie-gup/` for the core theoretical framework.
4. `contrainte-energie-noire-gup/` and `tests-donnees-publiques-gup-uvir/` for constraints and observational checks.
5. `programme-tests-experimentaux-uvir/` and `cellule-phase-vitesse-gup/` for experimental/sensor consequences.
6. [non-validated/README.md](non-validated/README.md) for hypotheses, draft articles, and non-verified claims.
7. [work/README.md](work/README.md) for scripts, reproducibility notes, and temporary work products.

## Scientific Pipeline

```text
Deformed phase cell
  -> GUP deformation
  -> UV/IR or holographic relation
  -> vacuum-density regularization
  -> dark-energy/cosmology constraint
  -> public-data tests
  -> experimental/sensor consequences
```

Each COSMO document should state which step of this pipeline it supports.

## Tracks

| Track | Purpose | Default status if unstated |
| --- | --- | --- |
| `cellule-phase-deformee-gup/` | Deformed phase-cell GUP formalism and UV regularization checks. | conditional |
| `cellule-phase-vitesse-gup/` | Position-velocity phase-space formulation and sensor-oriented consequences. | conditional |
| `contrainte-energie-noire-gup/` | Dark-energy constraint from the GUP-regulated vacuum-density hypothesis. | conditional |
| `relations-uv-ir-holographie-gup/` | UV/IR and holographic scaling relations. | conditional |
| `theorie-holographique-uvir-cellule-phase-deformee/` | Master holographic UV/IR framework. | conditional |
| `synthese-travaux-confirmes-gup-uvir/` | Consolidated status of the strongest GUP/UVIR results. | verify per file |
| `conclusions-cosmologiques-gup-uvir/` | Cosmological interpretation and open theoretical blocks. | non-validated unless stated |
| `constante-structure-fine-uvir/` | Fine-structure-constant conjecture and related checks. | non-validated unless stated |
| `consequences-alpha-uvir-electromagnetisme/` | Electromagnetic consequences of the alpha/UVIR conjecture. | non-validated unless stated |
| `tests-donnees-publiques-gup-uvir/` | Public-data testing program. | computationally bounded if reproducible |
| `programme-tests-experimentaux-uvir/` | Experimental and observational test plan. | non-validated plan |
| `non-validated/` | Hypotheses, draft articles, speculative claims, weakened claims, and negative diagnostics. | non-validated |
| `work/` | Scripts, run notes, data provenance, and reproducibility work products. | work product |

## Status Discipline

Use these labels when summarizing results:

- `verified`: derivation or numerical check is present and reproducible.
- `conditional`: result follows from stated assumptions, but those assumptions are not established.
- `computationally bounded`: finite numerical/observational result with reproducible command, data source, and uncertainty estimate.
- `non-validated`: hypothesis, conjecture, draft article, exploratory fit, or incomplete analysis.
- `old/superseded`: retained for history only.

If a document does not state its status, treat it as `non-validated` or at best `conditional`, not as confirmed.

## Placement Rule

- Put polished verified or explicitly conditional summaries in the relevant track folder.
- Put hypotheses, draft papers, speculative derivations, and unverified claims in `non-validated/`.
- Put scripts, data notes, and reproducibility helpers in `work/`.
- Do not commit large generated CSV/PNG/PDF files unless explicitly needed; prefer reproducible local outputs.
