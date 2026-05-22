# Simulation: qualite de phase pour capteurs atomiques

Le lien industriel le plus fort des formules position--vitesse est la source
d'atomes froids pour gravimetres, gyroscopes et navigation inertielle.

| Espece | n [m^-3] | T [K] | eta | sigma_v [m/s] | rayon apres 1s [m] |
|---|---:|---:|---:|---:|---:|
| Rb87 | 1.0e+18 | 1.0e-08 | 6.568e+00 | 9.781e-04 | 1.399e-03 |
| Rb87 | 1.0e+18 | 1.0e-07 | 2.077e-01 | 3.093e-03 | 3.251e-03 |
| Rb87 | 1.0e+18 | 1.0e-06 | 6.568e-03 | 9.781e-03 | 9.832e-03 |
| Rb87 | 1.0e+18 | 1.0e-05 | 2.077e-04 | 3.093e-02 | 3.095e-02 |

Figure: `reports/figures/cold_atom_sensor_phase_space.png`

Verdict: ici la formule n'est pas un gadget. Elle exprime directement
la qualite de source que l'industrie cherche a optimiser.
