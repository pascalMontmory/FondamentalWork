# HAL Metadata — `hal-05633702v1`

## Type

Pré-publication, Document de travail

## Title

TACM / PRNG Structural Diagnostics

## Subtitle

Empirical Measures, Seed-Conditioned Variance, Null Calibration and Reproducibility Boundaries

## Authors

Pascal Montmory

## Date

2026-05-26

## HAL Identifier

```text
hal-05633702v1
```

## Keywords

- pseudo-random number generators
- PRNG
- Monte Carlo simulation
- seed sensitivity
- empirical measures
- variance calibration
- probability integral transform
- null calibration
- TestU01
- BigCrush
- ECDF
- rare-event simulation
- reproducibility
- statistical diagnostics

## English Abstract

This manuscript introduces TACM, a structural diagnostic framework for pseudo-random number generators under finite Monte Carlo workloads. TACM is formulated around empirical measures of PRNG output, seed-conditioned replicated Monte Carlo estimators, null-calibrated variance diagnostics, ECDF interpretation, and exact rare-event calibration.

The central position is that TACM does not replace established PRNG batteries such as TestU01 or BigCrush. Instead, it adds a Monte Carlo workload-facing layer: it measures how seed-conditioned PRNG streams affect replicated Monte Carlo estimators. The core calibrated diagnostic is a probability-integral-transform score applied to seed-conditioned empirical variances.

A reproducible CPU-only baseline tests four public NumPy bit generators, four diagnostic integrands, 1000 seeds, 8 replicates, and 50000 draws per replicate. The results show that large raw max/min variance ratios can occur naturally, while null calibration separates raw dispersion alerts from compatible behaviour, mild calibration drift, and tail anomaly. Exact binomial rare-event checks are also reported for the rare-event integrand.

The manuscript explicitly separates definitions, reproducible evidence, reported evidence requiring archival raw logs for independent verification, and stated limitations. The contribution is methodological: TACM provides a calibrated and interpretable layer for assessing seed sensitivity in Monte Carlo workloads.

## French Abstract

Ce manuscrit introduit TACM, un cadre de diagnostic structurel pour les générateurs pseudo-aléatoires utilisés dans des workloads Monte Carlo finis. TACM est formulé autour des mesures empiriques du flux PRNG, des estimateurs Monte Carlo répliqués conditionnés par la seed, de diagnostics de variance calibrés sous loi nulle, de l’interprétation par ECDF et de la calibration exacte des événements rares.

La position centrale est que TACM ne remplace pas les batteries de tests établies telles que TestU01 ou BigCrush. Il ajoute plutôt une couche orientée workload Monte Carlo : il mesure comment les flux PRNG conditionnés par la seed affectent les estimateurs Monte Carlo répliqués. Le diagnostic calibré principal est un score par transformation intégrale de probabilité appliqué aux variances empiriques conditionnées par la seed.

Un baseline reproductible CPU-only teste quatre générateurs publics de NumPy, quatre intégrandes diagnostiques, 1000 seeds, 8 réplications et 50000 tirages par réplication. Les résultats montrent que de grands ratios bruts max/min de variance peuvent apparaître naturellement, tandis que la calibration sous loi nulle sépare les alertes de dispersion brute des comportements compatibles, des dérives légères de calibration et des anomalies de queue. Des contrôles exacts binomiaux sont également rapportés pour l’intégrande d’événement rare.

Le manuscrit sépare explicitement les définitions, les preuves reproductibles, les résultats rapportés nécessitant des logs bruts archivés pour vérification indépendante, et les limites déclarées. La contribution est méthodologique : TACM fournit une couche calibrée et interprétable pour évaluer la sensibilité aux seeds dans les workloads Monte Carlo.
