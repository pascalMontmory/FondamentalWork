# Claims Matrix

This matrix is the main guardrail against presenting a research notebook as a
finished theory. Each claim is classified by status, evidence and required next
step.

## Status scale

| Status | Meaning |
|---|---|
| `robust within assumptions` | Follows from the stated equations and checks |
| `observationally constrained` | Compared against public bounds or data |
| `candidate conjecture` | Coherent but not yet established |
| `speculative extension` | Conceptual extension requiring separate evidence |
| `engineering proposal` | Design or metrology proposal not yet experimentally built |
| `rejected as primary mechanism` | Negative result under tested assumptions |

## Core claims

| Claim | Status | Evidence in repo | Main limitation | Next step |
|---|---|---|---|---|
| The deformed GUP phase-space cell regularizes UV state counting. | robust within assumptions | `cellule-phase-deformee-gup/`, `synthese-travaux-confirmes-gup-uvir/` | Depends on chosen deformation and power law | Consolidate into Paper I with limiting cases |
| Direct identification `rho_reg = rho_DE` requires `beta0 ~ 10^60`. | robust within assumptions | `contrainte-energie-noire-gup/`, value `2.363228e60` for `g=1` | Assumes local universal GUP regulator is directly responsible for dark energy | Publish compact no-go derivation and table |
| A universal local `beta0 ~ 10^60` is not viable for photons, radiation and dense fermions. | observationally constrained | `tests-donnees-publiques-gup-uvir/`, FIRAS/BBN/fermion bounds | Bounds are model-dependent and use simplified public constraints | Add visible bounds in each README and generated report |
| The viable direction is local UV regularization plus IR/holographic gravitational projection. | candidate conjecture | `relations-uv-ir-holographie-gup/`, `theorie-holographique-uvir-cellule-phase-deformee/` | Needs explicit comparison with holographic dark-energy literature and dynamics | Add literature positioning and falsifiable prediction |
| The `alpha--Lambda` logarithmic relation is numerically close. | candidate conjecture | `constante-structure-fine-uvir/`, predicted `137.036063742708` vs CODATA `137.035999177` | Difference is far above CODATA uncertainty; look-elsewhere issue remains | Add sigma tension and parameter-choice discussion |
| Twin-sector / Moebius / zero-mode structure may reinterpret homogeneous dark energy. | speculative extension | `univers-jumeau-masse-negative-temps-inverse/` | Degenerate with Lambda-CDM in homogeneous zero-mode limit | Require distinct observable such as low-ell or birefringence signature |
| Phase-space source metrics are useful for cold-atom sensor design. | engineering proposal | `cellule-phase-vitesse-gup/` scripts and reports | Not a full instrument model | Continue benchmarked noise and geometry models |
| Atom-interferometer metrology may improve the reliability of `G` measurements. | engineering proposal | `PUBLICATION_MESURE_G_ATOMIQUE.md` | Source-mass geometry and systematics not yet simulated | Add `simulate_newton_G_atom_interferometer.py` |

## Robust negative results

| Negative result | Why it matters | Status |
|---|---|---|
| GUP vacuum regularization alone does not naturally explain observed dark energy with `beta0 ~ 1`. | Prevents overstating the GUP mechanism | robust within assumptions |
| Tuning `beta0` to dark energy gives `beta0 = 2.363228e60`, too large to be universal locally. | Forces sector separation or IR projection | observationally constrained |
| Hot industrial gases are deeply classical in phase-space density. | Rejects propulsion-style overclaim | robust within assumptions |
| Cold-atom GUP corrections are negligible even for deliberately large `beta0=1e26`. | Keeps sensor application in the standard `beta -> 0` regime | robust within assumptions |

## What is not claimed

The repository does not currently claim:

- an experimentally confirmed theory of quantum gravity;
- a derivation of Newton's `G` from first principles;
- a direct measurement of GUP corrections in cold atoms;
- a confirmed explanation of `alpha`;
- a confirmed alternative to Lambda-CDM;
- a built instrument for measuring `G`.

Those distinctions should remain visible in publication drafts.
