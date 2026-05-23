# FondamentalWork

Research repository for GUP phase-space models, UV/IR holographic relations,
dark-energy constraints, public-data tests, speculative twin-sector extensions
and cold-atom quantum-sensor applications.

This repository is not a single finished theory. It is organized as a set of
research tracks with explicit status labels: verified algebra, numerical tests,
observational constraints, candidate conjectures, rejected mechanisms and
engineering proposals.

## Start here

- `docs/REPOSITORY_STRUCTURE.md` explains the repository organization and file
  policy.
- `docs/PUBLICATION_CATALOG.md` gives the recommended reading order and status
  of each track.
- `docs/RESEARCH_WORKFLOW.md` defines how new work should move from idea to
  derivation, test and publication artifact.
- `docs/SCIENTIFIC_CONSOLIDATION_PLAN.md` turns the current technical review
  into a concrete action plan: literature positioning, quantitative result
  tables, falsifiability and robust-vs-speculative separation.

## Current research tracks

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

## Main results by category

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

## Generated artifacts

Generated PDFs, LaTeX build files, CSV tables, PNG figures and JSON summaries are
reproducible outputs. They are normally excluded from Git unless intentionally
published as release artifacts.

Source files, scripts, tests and Markdown reports are the primary review
artifacts.

## Editorial policy

This repository uses explicit scientific status labels:

- `verified algebra`
- `numerically reproduced`
- `observationally constrained`
- `candidate conjecture`
- `rejected as primary mechanism`
- `engineering proposal`

The goal is to keep professional separation between what is derived, what is
tested, what is excluded, what is conjectural and what is an applied design
proposal.
