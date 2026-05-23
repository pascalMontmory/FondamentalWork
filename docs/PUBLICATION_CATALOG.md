# Publication Catalog

This catalog gives the repository a professional reading order. It separates
core claims, constraints, speculative extensions and applied engineering work.

For the fastest external review path, read first:

1. `README.md` for the executive overview and key numbers.
2. `docs/CLAIMS_MATRIX.md` for robust vs conjectural claims.
3. `docs/NUMERICAL_RESULTS_INDEX.md` for the quantitative values and source
   locations.
4. This catalog for the track-by-track reading order.

## Recommended reading order

1. `cellule-phase-deformee-gup/`
   - Type: `core`
   - Status: `verified algebra`, `candidate conjecture`
   - Role: introduces the deformed phase-space cell and UV saturation logic.

2. `contrainte-energie-noire-gup/`
   - Type: `constraint`
   - Status: `verified algebra`, `rejected as primary mechanism`
   - Key number: `beta0_Lambda(g=1) = 2.363228e60`.
   - Role: shows that direct GUP vacuum regularization requires an enormous
     universal `beta0` if identified with dark energy.

3. `tests-donnees-publiques-gup-uvir/`
   - Type: `test`
   - Status: `numerically reproduced`, `observationally constrained`
   - Key bounds: FIRAS `3.72e58`, BBN `2.64e41`, dense fermions `1.66e38`.
   - Role: tests the local universal `beta0` hypothesis against public bounds.

4. `relations-uv-ir-holographie-gup/`
   - Type: `core`, `constraint`
   - Status: `verified algebra`, `candidate conjecture`
   - Role: separates exact Planck-Hubble identities from candidate UV/IR and
     holographic relations.

5. `theorie-holographique-uvir-cellule-phase-deformee/`
   - Type: `synthesis`, `core`
   - Status: `candidate conjecture`
   - Role: master framework combining GUP cell, no-go result and holographic
     UV/IR projection.

6. `constante-structure-fine-uvir/`
   - Type: `application`, `candidate conjecture`
   - Status: `numerically reproduced`, `candidate conjecture`
   - Key number: `alpha^-1_pred = 137.036063742708` vs CODATA
     `137.035999177`.
   - Role: tests the proposed `alpha--Lambda` logarithmic relation.

7. `consequences-alpha-uvir-electromagnetisme/`
   - Type: `constraint`, `application`
   - Status: `verified algebra`
   - Role: separates algebraic consequences from independent predictions.

8. `univers-jumeau-masse-negative-temps-inverse/`
   - Type: `speculative`
   - Status: `candidate conjecture`
   - Role: analyzes a twin-sector / zero-mode / Moebius-time extension without
     mixing it with the robust GUP no-go results.

9. `cellule-phase-vitesse-gup/`
   - Type: `application`, `engineering proposal`
   - Status: `verified algebra`, `numerically reproduced`, `engineering proposal`
   - Key sensor number: Sr88 nominal `11.52 microGal/sqrtHz`.
   - Role: converts the position-velocity phase-space language into cold-atom
     sensor CAD, gravimetry, atom interferometry and a proposed route for more
     reliable measurement of Newton's `G`.

10. `synthese-travaux-confirmes-gup-uvir/`
    - Type: `synthesis`
    - Status: `verified algebra`, `observationally constrained`
    - Role: summarizes what is confirmed inside the framework and what remains
      speculative.

## Publication tracks

| Track | Primary artifact | Status | Notes |
|---|---|---|---|
| Deformed phase-space cell | `cellule-phase-deformee-gup/main.tex` | foundation | Mathematical basis |
| GUP dark-energy constraint | `contrainte-energie-noire-gup/main.tex` | no-go | Direct local `beta0` is not viable |
| Public-data tests | `tests-donnees-publiques-gup-uvir/main.tex` | tests | Quantitative public constraints |
| UV/IR holographic relations | `relations-uv-ir-holographie-gup/main.tex` | candidate | Requires clear separation of identities and conjectures |
| Master UV/IR framework | `theorie-holographique-uvir-cellule-phase-deformee/main.tex` | synthesis | Best single entry for theory |
| Fine-structure conjecture | `constante-structure-fine-uvir/main.tex` | candidate | Numerically close, not established |
| Twin-sector scenario | `univers-jumeau-masse-negative-temps-inverse/PUBLICATION.md` | speculative | Keep separate from core no-go |
| Cold-atom quantum sensors | `cellule-phase-vitesse-gup/PAPER_QUANTUM_SENSOR_PHASE_SPACE.md` | application | Strongest industrial direction |
| Phase-space sensor CAD | `cellule-phase-vitesse-gup/PHASE_SPACE_CAD_QUANTUM_SENSORS.md` | engineering proposal | Reproducible sensor design budget |
| Newton `G` metrology | `cellule-phase-vitesse-gup/PUBLICATION_MESURE_G_ATOMIQUE.md` | engineering proposal | Differential atom-interferometer route |

## Editorial rule

Every publication should clearly state:

- what is mathematically derived;
- what is numerically reproduced;
- what is experimentally constrained;
- what is only a conjecture;
- what has been rejected as a primary mechanism.

This is the main difference between a professional research repository and a
personal notebook.
