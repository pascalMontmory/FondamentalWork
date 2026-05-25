# HAL Metadata

## Title

Structural Stability Diagnostics for Pseudo-Random Number Generators: Seed Sensitivity and Functional Variance Dispersion

## Authors

Pascal Montmory

## Affiliation

ENINCA Consulting

## Keywords

- PRNG
- Monte Carlo
- seed sensitivity
- functional stability
- cross-architecture reproducibility
- statistical diagnostics
- Monte Carlo methods
- random number generation
- reproducibility

## English Abstract

Classical statistical test batteries such as TestU01 BigCrush and PractRand are necessary but insufficient to assess the reliability of pseudo-random number generators (PRNGs) in Monte Carlo simulations. Generators compatible with these tests can still exhibit seed-dependent variations in functional variance, leading to unstable estimator behaviour across runs.

This paper introduces a structural diagnostic framework that complements traditional statistical tests by evaluating three properties: seed sensitivity, functional stability across representative integrands (identity, sinusoidal, quadratic, and rare-event), and bit-exact reproducibility across heterogeneous architectures (ARM64 CPU, Metal GPU, and CUDA GPU).

Using a controlled proprietary 64-bit PRNG as a test vehicle, the reported results show that common PRNGs can display inter-seed dispersion ratios up to approximately 25x on practical Monte Carlo integrands, despite passing full BigCrush. Imported BigCrush logs for seed 42 report 160/160 passed statistics for the test vehicle on CPU ARM, Metal GPU, and CUDA GPU backends.

These results suggest that seed-conditioned Monte Carlo stability should be treated as a first-class empirical criterion in PRNG evaluation for large-scale scientific and industrial applications. The current artifact is computational evidence, not a mathematical proof of generator quality, and identifies the additional artifacts required for independent verification.

## French Abstract

Cette note technique présente un cadre de diagnostic structurel pour l'évaluation des générateurs pseudo-aléatoires dans les simulations Monte Carlo. L'objectif n'est pas de remplacer les batteries statistiques classiques, comme TestU01 ou PractRand, mais de les compléter par des mesures de sensibilité à la seed, de dispersion de variance fonctionnelle et de reproductibilité inter-backend.

Un générateur propriétaire 64-bit est utilisé uniquement comme véhicule expérimental contrôlé. Sa récurrence interne, ses constantes et son code d'implémentation ne sont pas publiés dans cette note. La contribution principale porte sur la méthode d'évaluation et sur le protocole empirique.

Les logs BigCrush importés indiquent 160/160 statistiques passées pour la seed 42 sur CPU ARM, Metal GPU et CUDA GPU. Les diagnostics structurels rapportés montrent que des générateurs passant les batteries classiques peuvent néanmoins présenter une dispersion inter-seed importante de la variance Monte Carlo, notamment sur les événements rares.

Le document doit être lu comme une évidence computationnelle et méthodologique, pas comme une preuve mathématique de qualité, de période, de sécurité ou d'équidistribution.
