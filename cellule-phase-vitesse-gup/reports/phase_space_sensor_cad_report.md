# Phase-space CAD pour capteurs quantiques

Ce rapport transforme la cellule de phase `D^3 v^3 ~ h^3/m^3` en outil
de conception. L'objectif n'est pas de remplacer un simulateur complet
d'instrument, mais de fournir un budget physique minimal: temperature,
densite, expansion balistique, nombre d'atomes detectes et bruit de tir.

## Formules utilisees

```text
eta = n lambda_th^3
lambda_th = h / sqrt(2 pi m k_B T)
sigma_v = sqrt(k_B T / m)
R(t) = sqrt(R0^2 + sigma_v^2 t^2)
delta a ~= 1 / (k_eff T_i^2 sqrt(N_detected))
delta Omega ~= 1 / (2 k_eff v T_i^2 sqrt(N_detected))
```

## Meilleurs points trouves par scenario

| scenario | espece | T [K] | Ti [s] | eta | rayon [mm] | survie | N det. | bruit a [m/s2] | bruit Omega [rad/s] | score |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| gps_denied_inertial_accelerometer | Rb87 | 1.00e-07 | 0.05 | 2.08e-01 | 0.81 | 1.00 | 1.00e+06 | 2.48e-08 | inf | 0.974 |
| field_gravimeter | Rb87 | 5.01e-08 | 0.25 | 2.93e-01 | 1.32 | 1.00 | 2.00e+06 | 7.02e-10 | inf | 0.980 |
| compact_atomic_gyroscope | Cs133 | 1.00e-07 | 0.1 | 8.79e-02 | 0.74 | 1.00 | 8.00e+05 | 7.58e-09 | 3.79e-09 | 0.960 |
| space_gravity_gradiometer_source | Sr88 | 1.00e-08 | 1 | 1.29e+00 | 1.79 | 1.00 | 1.00e+06 | 2.74e-11 | inf | 1.000 |

## Interpretation

- La variable vraiment industrielle est `sigma_v`: elle fixe la taille de
  l'instrument apres expansion libre.
- `eta` n'est pas seulement un indicateur de degenerate quantique; c'est un
  indicateur de qualite de source atomique a densite et temperature donnees.
- Le meilleur produit n'est pas une propulsion nouvelle. C'est un logiciel
  de pre-dimensionnement pour capteurs inertiels, gravimetres, gyroscopes
  et gradiometres atomiques.
- Un score eleve ne prouve pas qu'un instrument est realisable: il signifie
  seulement que le budget d'espace des phases ne l'interdit pas deja.

## Limites a ajouter dans une version industrielle

- bruit laser et bruit de phase optique;
- vibrations et strategie de rejet classique/quantique;
- aberrations de front d'onde;
- collisions froides, pertes et densite maximale exploitable;
- temps mort, cadence, Allan deviation;
- modele complet de detection et bruit technique.

Donnees: `reports/data/phase_space_sensor_cad.csv`

Figure: `reports/figures/phase_space_sensor_cad.png`