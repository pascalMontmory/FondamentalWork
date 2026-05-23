# Scientific Consolidation Plan

This document turns the current technical review of the repository into a
concrete consolidation plan. The goal is to move `FondamentalWork` from a
well-organized research notebook toward a professional research program with
clear claims, comparisons, numerical outputs and falsifiability criteria.

## Current diagnosis

The repository has a coherent conceptual chain:

```text
GUP
-> deformed phase-space cell
-> UV regularization
-> UV/IR holographic projection
-> dark-energy constraint
-> public-data tests
-> cosmological and sensor applications
```

The strongest current asset is not a single final theory. It is the systematic
separation of:

- local UV regularization;
- IR/holographic gravitational projection;
- observational constraints on a universal local `beta0`;
- applied phase-space engineering for cold-atom sensors.

The main weakness is that several documents still read as internal derivations
or candidate notes. The project now needs explicit literature positioning,
quantitative summary tables and sharper falsifiability statements.

## Priority 1 - Separate robust results from conjectures

Create a top-level scientific status table that classifies each claim.

| Claim | Current status | Needed upgrade |
|---|---|---|
| GUP cell makes UV density integrals finite | verified algebra | show derivation and limiting cases in one canonical paper |
| Direct `rho_reg = rho_DE` requires huge `beta0` | robust no-go under stated assumptions | publish compact derivation and numerical value table |
| Huge universal local `beta0` is constrained by public data | observationally constrained | add visible bound table: FIRAS, BBN, atoms, fermions, CMB |
| UV/IR projection can lower the effective gravitational density | candidate mechanism | compare explicitly with holographic dark-energy literature |
| `alpha--Lambda` logarithmic relation is close numerically | candidate conjecture | add uncertainty and look-elsewhere discussion |
| Twin-sector / zero-mode scenario can mimic homogeneous Lambda | speculative | keep isolated from core framework unless it predicts an observable |
| Cold-atom phase-space CAD is useful engineering | applied proposal | continue with benchmarked noise budgets and reproducible scripts |
| Atom-interferometer `G` measurement may improve reliability | applied metrology proposal | add source-mass geometry simulator and uncertainty budget |

## Priority 2 - Add quantitative result tables

Every major README should expose the numbers that support its verdict. The
repository should not require a reader to inspect scripts to find the main
bounds.

Minimum tables to add:

1. `beta0` and length-scale table

```text
track: contrainte-energie-noire-gup
columns: assumption, formula, beta0, Delta x_min, verdict
```

2. Public-data exclusion table

```text
track: tests-donnees-publiques-gup-uvir
columns: probe, observable, assumed beta0, bound, pass/fail, reason
```

3. UV/IR relation table

```text
track: relations-uv-ir-holographie-gup
columns: equation, known identity vs conjecture, literature analogue, status
```

4. `alpha--Lambda` table

```text
track: constante-structure-fine-uvir
columns: input constants, predicted alpha^-1, CODATA alpha^-1, absolute error, relative error, sigma tension
```

5. Sensor benchmark table

```text
track: cellule-phase-vitesse-gup
columns: scenario, Ti, T_cycle, dominant noise, model microGal/sqrtHz, published/reference microGal/sqrtHz
```

## Priority 3 - Literature positioning

The next professional pass should add explicit comparison sections to the main
papers. The key references to position against are:

- GUP phase-space and density-of-states literature, especially Kempf, Mangano
  and Mann style formulations;
- UV/IR and holographic dark-energy literature, including Cohen-Kaplan-Nelson,
  Hsu and Li-type arguments;
- observational constraints on GUP-like dispersion or phase-space deformations;
- atom-interferometry gravimetry and Newton `G` measurements.

For each comparison, state:

```text
What is standard?
What is reused?
What is changed?
What does the present framework add?
What remains unproven?
```

This is essential because the current work is close to known ideas in several
places. The novelty must be framed as integration, filtering, no-go separation,
or applied CAD, not as rediscovery of established concepts.

## Priority 4 - Falsifiability and predictions

The project should distinguish three levels of falsifiability.

### Level A - Already falsifiable under current assumptions

- Universal local `beta0` large enough to directly produce dark energy.
- Naive horizon choice `L = c/H(t)` if it predicts unacceptable variation of
  `alpha` or vacuum density.

### Level B - Testable with public or near-public data

- Low-ell CMB signatures in the twin/zero-mode scenario.
- Cosmic birefringence signatures if the Moebius/CPT extension is made explicit.
- Deviations in public cosmological fits if `w(a)` departs from `-1`.
- Bounds from BBN, FIRAS, atomic spectroscopy and dense fermion systems.

### Level C - Engineering falsifiability

- Cold-atom source budget fails if vibration, detection or cycle time dominates
  beyond target sensitivity.
- Newton `G` metrology concept fails if geometry/systematics cannot beat the
  atom-interferometer reference uncertainty scale.

A professional paper should contain at least one Level A or Level B falsification
criterion. Engineering proposals should contain Level C failure criteria.

## Priority 5 - Canonical paper set

The repository should converge toward a smaller set of canonical papers:

1. `Paper I - GUP phase-space cell and vacuum-energy no-go`
   - combine deformed cell, finite UV density and direct dark-energy failure;
   - include explicit `beta0` table and public-data tension summary.

2. `Paper II - UV/IR holographic projection and cosmological constraints`
   - separate identities from conjectures;
   - compare with holographic dark energy literature;
   - define exactly what the model predicts beyond Lambda-CDM.

3. `Paper III - Fine-structure and electromagnetic consequences`
   - present `alpha--Lambda` as conjectural;
   - include sigma tension and non-variation constraints.

4. `Paper IV - Twin-sector zero-mode extension`
   - keep speculative;
   - require a distinct observable before elevating it to the core framework.

5. `Paper V - Phase-space CAD for cold-atom quantum sensors`
   - applied, benchmarked, reproducible;
   - includes noise budget and Newton `G` metrology proposal.

## Priority 6 - Repository actions

Immediate actions:

- add `docs/CLAIMS_MATRIX.md` with all major claims and statuses;
- add `docs/LITERATURE_POSITIONING.md` with side-by-side comparison against key
  prior work;
- add `docs/NUMERICAL_RESULTS_INDEX.md` with the main numerical values and
  where they are generated;
- update every major README with a `Main numbers` section;
- avoid new speculative branches until the existing claims matrix is complete.

Medium-term actions:

- build a single command that runs all public-data tests;
- make generated Markdown reports deterministic;
- decide which PDFs are release artifacts and keep all other PDFs ignored;
- create a `release/` or GitHub Releases workflow for publication snapshots.

## Editorial verdict

The project is serious and coherent, but its current impact is limited by
presentation and consolidation rather than by lack of ideas. The next scientific
step is not to add more conjectures. It is to expose the quantitative core,
compare it explicitly with the literature and state exactly what would falsify
each claim.
