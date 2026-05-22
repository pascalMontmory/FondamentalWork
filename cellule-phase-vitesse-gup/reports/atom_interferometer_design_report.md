# Design proxy: interferometre atomique Rb87

Ce modele n'est pas un instrument complet. Il montre pourquoi la formulation
position--vitesse est utile: la temperature fixe la dispersion de vitesse,
donc l'expansion du nuage, donc le temps d'interrogation exploitable.

| T [K] | temps [s] | eta | rayon [mm] | fraction detectee | delta a [m/s2] |
|---:|---:|---:|---:|---:|---:|
| 1.0e-08 | 1 | 6.568e+00 | 1.399e+00 | 1.000e+00 | 6.208e-11 |
| 1.0e-07 | 1 | 2.077e-01 | 3.251e+00 | 9.932e-01 | 6.229e-11 |
| 1.0e-06 | 0.25 | 6.568e-03 | 2.651e+00 | 9.995e-01 | 9.935e-10 |
| 1.0e-06 | 1 | 6.568e-03 | 9.832e+00 | 3.016e-01 | 1.130e-10 |
| 1.0e-05 | 0.25 | 2.077e-04 | 7.795e+00 | 5.955e-01 | 1.147e-09 |

Figure: `reports/figures/atom_interferometer_design_tradeoff.png`

Verdict: l'application concrete est un outil de dimensionnement de source
froide, pas une nouvelle loi de propulsion.
