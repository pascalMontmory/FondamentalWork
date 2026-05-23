# Namespace Migration Plan

The repository should move toward two top-level intellectual namespaces:

```text
COSMO/  # GUP, UV/IR, holography, cosmology, sensors tied to the framework
Math/   # reusable mathematical foundations, including VDF
```

This document defines a non-breaking migration plan.

## Why not move everything immediately?

Many existing tracks contain LaTeX files, scripts, generated reports and relative
links. A mass move would make the repository look cleaner but could silently
break reproducibility.

The migration should be staged:

1. create `COSMO/` and `Math/` as explicit namespaces;
2. document the target mapping;
3. move one track at a time;
4. update links and commands;
5. run the track tests/compilation;
6. then remove the old root-level path.

## Target root layout

```text
FondamentalWork/
  README.md
  docs/
  COSMO/
    README.md
    cellule-phase-deformee-gup/
    contrainte-energie-noire-gup/
    relations-uv-ir-holographie-gup/
    theorie-holographique-uvir-cellule-phase-deformee/
    tests-donnees-publiques-gup-uvir/
    synthese-travaux-confirmes-gup-uvir/
    cellule-phase-vitesse-gup/
    ...
  Math/
    README.md
    VDF/
      README.md
      definitions.md
      notation.md
      lemmas.md
```

## COSMO migration order

Recommended order:

1. `synthese-travaux-confirmes-gup-uvir/`
2. `contrainte-energie-noire-gup/`
3. `tests-donnees-publiques-gup-uvir/`
4. `relations-uv-ir-holographie-gup/`
5. `theorie-holographique-uvir-cellule-phase-deformee/`
6. `constante-structure-fine-uvir/`
7. `consequences-alpha-uvir-electromagnetisme/`
8. `cellule-phase-deformee-gup/`
9. `conclusions-cosmologiques-gup-uvir/`
10. `programme-tests-experimentaux-uvir/`
11. `programmes-verification-publique-uvir/`
12. `univers-jumeau-masse-negative-temps-inverse/`
13. `cellule-phase-vitesse-gup/`

Reason: migrate the synthesis and no-go/test tracks first because they define
the review backbone. Migrate the large sensor track last because it has the most
scripts, reports and generated outputs.

## Math/VDF migration order

1. Write `Math/VDF/definitions.md`.
2. Write `Math/VDF/notation.md`.
3. Identify which COSMO formulas depend on VDF concepts.
4. Add `Math/VDF/links-to-repos.md`.
5. Only then start extracting mathematical material from COSMO notes into VDF.

## Acceptance checklist for each moved COSMO track

Before deleting the old root-level directory, verify:

```text
README links updated
LaTeX compiles from new path
Python scripts run from new path
reports still reproducible
relative references updated
root README points to new path
publication catalog points to new path
```

## Naming rule

Use uppercase only for broad namespaces:

```text
COSMO/
Math/
```

Keep research-track directories lowercase and hyphenated:

```text
contrainte-energie-noire-gup/
cellule-phase-vitesse-gup/
```

This keeps the repository readable without turning every path into a title.
