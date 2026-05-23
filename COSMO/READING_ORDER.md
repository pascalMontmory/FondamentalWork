# COSMO Reading Order

This file explains how to read the COSMO area without getting lost in the number of folders.

## 1. What COSMO Is For

`COSMO/` contains the fundamental-physics side of the repository:

1. GUP and deformed phase-space cells;
2. UV/IR and holographic relations;
3. vacuum-energy and dark-energy constraints;
4. public-data and observational checks;
5. applied sensor/noise-budget work.

It is separate from `Math/`, which contains reusable mathematical foundations such as Collatz-Montmory, VDF, and PRNG work.

## 2. Recommended Reading Path

Read in this order:

1. `COSMO/README.md`: track overview and status policy.
2. `COSMO/synthese-travaux-confirmes-gup-uvir/`: strongest consolidated claims, if maintained as confirmed.
3. `COSMO/theorie-holographique-uvir-cellule-phase-deformee/`: master UV/IR and holographic framework.
4. `COSMO/relations-uv-ir-holographie-gup/`: scaling relations and UV/IR mechanisms.
5. `COSMO/contrainte-energie-noire-gup/`: dark-energy constraint track.
6. `COSMO/tests-donnees-publiques-gup-uvir/`: public-data tests and observational checks.
7. `COSMO/cellule-phase-vitesse-gup/`: sensor-oriented phase-space formulation.
8. `COSMO/cellule-phase-deformee-gup/`: deformed phase-cell formalism and supporting derivations.
9. `COSMO/non-validated/programme-tests-experimentaux-uvir/`: proposed tests and protocols, kept non-validated until each test is tied to a reproducible data source and decision threshold.
10. `COSMO/non-validated/constante-structure-fine-uvir/` and `COSMO/non-validated/consequences-alpha-uvir-electromagnetisme/`: alpha/electromagnetic conjectures.
11. `COSMO/non-validated/conclusions-cosmologiques-gup-uvir/`: interpretations and open theoretical blocks.

## 3. Status Interpretation

Use this hierarchy:

| Status | Reader interpretation |
|---|---|
| verified | derivation/check is present and reproducible |
| conditional | follows from stated assumptions only |
| computationally bounded | finite-range numerical result, not asymptotic proof |
| non-validated | hypothesis, draft, conjecture, or incomplete analysis |
| old/superseded | preserved for history only |

If a document does not state its status, treat it as **non-validated**.

## 4. The Main Scientific Pipeline

The intended logic is:

```text
Deformed phase cell
  -> GUP deformation
  -> UV/IR or holographic relation
  -> vacuum-density regularization
  -> dark-energy/cosmology constraint
  -> public-data tests
  -> experimental/sensor consequences
```

A strong COSMO document should make clear which step of this pipeline it supports.

## 5. Where New Material Goes

- Polished verified or explicitly conditional summaries: relevant COSMO track root.
- Hypotheses, draft papers, speculative derivations: `COSMO/non-validated/`.
- Scripts and reproducibility helpers: `COSMO/work/scripts/`.
- Data provenance: `COSMO/work/data-notes/`.
- Old versions retained only for history: `COSMO/old/` if created later.

## 6. First Cleanup Pass Completed

The following tracks have been moved to `COSMO/non-validated/` because their README/status identifies them as conjectural, interpretive, programmatic, or not independently validated:

- `constante-structure-fine-uvir/`
- `consequences-alpha-uvir-electromagnetisme/`
- `programme-tests-experimentaux-uvir/`
- `conclusions-cosmologiques-gup-uvir/`

This move does not mean the material is useless. It means it should be read as hypothesis, draft, program, or conditional interpretation until promoted by proof, reproducible bounded computation, or a clearly stated conditional theorem.

## 7. Remaining Cleanup

The current folders were preserved from earlier work. They are named by theme, but not all files inside them necessarily have the same scientific status.

Next cleanup pass should classify each document into one of:

- `verified-facing`;
- `conditional-facing`;
- `non-validated`;
- `old/superseded`;
- `script/reproducibility`.
