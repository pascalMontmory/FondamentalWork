# FondamentalWork

Research repository organized around two top-level intellectual namespaces:

```text
COSMO/  # GUP, UV/IR, holography, cosmology, dark-energy constraints, sensors
Math/   # reusable mathematical foundations, including VDF and PRNG workstreams
```

The current cosmology tracks still live mostly at the repository root for
compatibility with existing LaTeX and script paths. `COSMO/` is now the target
namespace and index for their staged migration. `Math/` is the home for reusable
mathematical structures and algorithms that support this and other repositories.

## Executive Overview

The central COSMO result is a conditional no-go and separation principle:

```text
local GUP phase-space regularization can make UV vacuum integrals finite,
but direct identification with observed dark energy requires beta0 ~ 10^60,
which is not viable as a universal local parameter under public photon,
radiation and dense-fermion constraints.
```

The viable research direction is therefore not "GUP alone explains Lambda". It
is a two-layer framework:

```text
local UV regularization
+ IR/holographic gravitational projection
+ explicit observational constraints
```

The strongest applied COSMO direction is separate and more mature: the same
phase-space language gives a useful engineering budget for cold-atom quantum
sensors, gravimetry and a proposed differential atom-interferometer route to
measuring Newton's `G`.

The Math namespace starts with:

- `Math/VDF/` for the underlying VDF mathematics shared across repositories;
- `Math/PRNG/` for the mathematical and algorithmic structure of your PRNG.

Both should be defined as reusable mathematics first, then linked to COSMO or
software projects only where they are actually used.

This repository is not a single finished theory. It is organized as research
tracks with explicit status labels: verified algebra, numerical tests,
observational constraints, candidate conjectures, rejected mechanisms,
engineering proposals and reusable mathematical foundations.

## Key Numbers

| Result | Value | Status |
|---|---:|---|
| Dark-energy density used in synthesis | `5.253229e-10 J/m^3` | reproduced from public constants/cosmology inputs |
| Direct GUP match to dark energy | `beta0_Lambda(g=1) = 2.363228e60` | robust no-go value under direct `rho_reg = rho_DE` |
| FIRAS photon-sector bound | `beta0 <= 3.72e58` | excludes `beta0_Lambda` as universal photon parameter |
| BBN/radiation bound | `beta0 <= 2.64e41` | excludes `beta0_Lambda` in primordial radiation sector |
| Dense-fermion bound | `beta0 <= 1.66e38` | excludes `beta0_Lambda` for dense fermions |
| Proposed `alpha^-1` relation | `137.036063742708` vs CODATA `137.035999177` | numerically close conjecture, not confirmed |
| Sr88 sensor nominal result | `11.52 microGal/sqrtHz` | first-order technical-noise model, vibration dominated |
| NIM-like gravimeter benchmark | `19.72` model vs `20.5 microGal/sqrtHz` reference | sanity check |
| Atom-interferometer `G` milestone | `<150 ppm` first target | engineering proposal, not yet simulated end-to-end |

See `docs/NUMERICAL_RESULTS_INDEX.md` for the longer table and source locations.

## Start Here

- `COSMO/README.md` defines the target namespace for the cosmology/fundamental
  physics corpus.
- `Math/README.md` defines the reusable mathematics namespace.
- `Math/VDF/README.md` starts the VDF mathematical workstream.
- `Math/PRNG/README.md` starts the PRNG mathematical and algorithmic workstream.
- `docs/NAMESPACE_MIGRATION_PLAN.md` explains how root-level tracks will move
  into `COSMO/` without breaking scripts or LaTeX builds.
- `docs/CLAIMS_MATRIX.md` classifies the major claims by status and limitation.
- `docs/NUMERICAL_RESULTS_INDEX.md` lists the main numerical values and where
  they are generated.
- `docs/REPOSITORY_STRUCTURE.md` explains the repository organization and file
  policy.
- `docs/PUBLICATION_CATALOG.md` gives the recommended reading order and status
  of each track.
- `docs/RESEARCH_WORKFLOW.md` defines how new work should move from idea to
  derivation, test and publication artifact.
- `docs/SCIENTIFIC_CONSOLIDATION_PLAN.md` turns the current technical review
  into a concrete action plan: literature positioning, quantitative result
  tables, falsifiability and robust-vs-speculative separation.

## Current Research Tracks

These tracks are currently root-level for compatibility. Their target namespace
is `COSMO/`.

| Track | Type | Status | Purpose |
|---|---|---|---|
| `cellule-phase-deformee-gup/` | core | verified algebra, candidate conjecture | Deformed phase-space cell, density of states and UV saturation |
| `contrainte-energie-noire-gup/` | constraint | verified algebra, rejected primary mechanism | Shows why direct GUP vacuum regularization requires an enormous universal `beta0` |
| `relations-uv-ir-holographie-gup/` | core | verified algebra, candidate conjecture | Separates Planck-Hubble identities, black-hole bounds and candidate UV/IR equations |
| `conclusions-cosmologiques-gup-uvir/` | synthesis | conditional conclusion | Summarizes cosmological implications and the need for UV/IR projection |
| `theorie-holographique-uvir-cellule-phase-deformee/` | synthesis | candidate framework | Master framework: GUP cell, no-go result, holographic projection and alpha-Lambda conjecture |
| `constante-structure-fine-uvir/` | application | numerically reproduced, candidate conjecture | Tests the logarithmic `alpha--Lambda` relation |
| `consequences-alpha-uvir-electromagnetisme/` | constraint | verified algebra | Separates algebraic consequences from independent electromagnetic predictions |
| `tests-donnees-publiques-gup-uvir/` | test | observationally constrained | Tests the local universal `beta0` hypothesis against public bounds |
| `programmes-verification-publique-uvir/` | test | reproducibility program | Public verification scripts and verdict matrix |
| `programme-tests-experimentaux-uvir/` | test plan | proposed program | Experimental and observational test roadmap |
| `univers-jumeau-masse-negative-temps-inverse/` | speculative | candidate conjecture | Twin-sector, negative effective mass, zero-mode and Moebius-time analysis |
| `cellule-phase-vitesse-gup/` | application | engineering proposal | Position-velocity phase-space, cold-atom sensors, gravimetry and Newton `G` metrology |
| `synthese-travaux-confirmes-gup-uvir/` | synthesis | curated status | Separates confirmed internal results from speculative extensions |

## Math Tracks

| Track | Type | Status | Purpose |
|---|---|---|---|
| `Math/VDF/` | mathematical foundation | workstream to formalize | Define the VDF objects, notation, lemmas and links to other repositories |
| `Math/PRNG/` | mathematical algorithm | workstream to formalize | Define PRNG state transition, output function, period/statistical/security claims and reference vectors |

## Main Results by Category

### Robust negative results

- A direct local GUP regularization of vacuum energy does not naturally produce
  observed dark energy unless `beta0` is made enormous.
- A universal local `beta0` of that size is strongly constrained by public
  photon, plasma, fermion and cosmological bounds.
- Hot chemical-engine gases are far too classical for the phase-space cell
  `h^3` to provide a direct propulsion lever.

### Candidate theoretical structure

- The viable direction is a separation between local UV regularization and an
  IR/holographic gravitational projection.
- The `alpha--Lambda` relation is numerically close and algebraically clean, but
  it remains a conjecture rather than an established prediction.
- Twin-sector / Moebius / zero-mode ideas are kept separate from the core no-go
  results and treated as speculative extensions.

### Applied engineering direction

The strongest practical track is cold-atom quantum sensing:

- phase-space source quality;
- velocity dispersion and cloud expansion;
- atom-number and detection budgets;
- vibration, laser, QPN, photon-shot, thermal and Johnson-Nyquist noise;
- gravimetry, inertial sensing and a proposed differential route to measuring
  Newton's `G` with atom interferometry.

The current sensor track includes a nominal Sr88 case around `T_i = 0.102 s`
with estimated sensitivity `11.52 microGal/sqrtHz`, dominated by vibration in
the modeled setup.

## Reproducibility

Most tracks are self-contained. Typical commands are:

```bash
python3 -m py_compile scripts/*.py
python3 scripts/test_*.py
latexmk -pdf -interaction=nonstopmode main.tex
```

For the cold-atom sensor track:

```bash
cd cellule-phase-vitesse-gup
python3 -m py_compile scripts/*.py
python3 scripts/test_phase_space_sensor_cad.py
python3 scripts/test_atom_phase_space_budget.py
python3 scripts/test_sensor_noise_budget.py
python3 scripts/simulate_sensor_noise_budget.py
latexmk -pdf -interaction=nonstopmode phase_space_cad_quantum_sensors.tex
latexmk -pdf -interaction=nonstopmode paper_quantum_sensor_phase_space.tex
```

## Generated Artifacts

Generated PDFs, LaTeX build files, CSV tables, PNG figures and JSON summaries are
reproducible outputs. They are normally excluded from Git unless intentionally
published as release artifacts.

Source files, scripts, tests and Markdown reports are the primary review
artifacts.

## Editorial Policy

This repository uses explicit scientific status labels:

- `verified algebra`
- `numerically reproduced`
- `observationally constrained`
- `candidate conjecture`
- `rejected as primary mechanism`
- `engineering proposal`
- `mathematical foundation`
- `mathematical algorithm`

The goal is to keep professional separation between what is derived, what is
tested, what is excluded, what is conjectural, what is an applied design proposal
and what is reusable mathematics.
