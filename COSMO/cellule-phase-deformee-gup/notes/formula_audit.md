# Audit mathematique initial

Date : 22 mai 2026

## Formules verifiees

- Integrale maitresse : `I_s(gamma) = 1/2 beta^{-s/2} B(s/2, gamma-s/2)`, valide pour `gamma > s/2`.
- Pour `gamma = 3` : `int_0^inf p^2 dp/(1+beta p^2)^3 = pi/(16 beta^{3/2})`.
- Pour `gamma = 3` : `int_0^inf p^3 dp/(1+beta p^2)^3 = 1/(4 beta^2)`.
- Densite maximale de modes : `n_max = g pi^2/(4 h^3 beta^{3/2})`.
- Cumul exact : `N(p) = g pi V/(2 h^3 beta^{3/2}) [atan(q) - q(1-q^2)/(1+q^2)^2]`, avec `q = sqrt(beta) p`.
- Coefficient de Wien a premier ordre : `x_max = x0 - 18.2282675 gamma epsilon + O(epsilon^2)`, avec `x0 = 2.821439372...` et `epsilon = beta (k_B T)^2/c^2`.
- Correction Stefan-Boltzmann : `u(T)=aT^4[1 - gamma (40 pi^2/21) beta k_B^2 T^2/c^2 + ...]`.

## Corrections conceptuelles importantes

- Une densite finie de modes ne donne pas une energie thermique maximale pour un gaz bosonique. A haute temperature, le gaz de photons verifie plutot `u(T) ~ n_max k_B T`.
- Les bornes `rho_max` et `P_max` sont valables pour un secteur a occupation bornee, typiquement un gaz fermionique degenere a temperature nulle, sous l'hypothese `E=pc`.
- L'energie du vide devient finie dans le modele, mais cela ne resout pas la constante cosmologique sans mecanisme additionnel.
- L'equation de rebond de type `H^2 = (8 pi G/3) rho (1-rho/rho_max)` est une hypothese effective, pas une consequence directe de la mesure de phase.
- La loi holographique ne decoule pas de la mesure GUP seule. Il faut ajouter une contrainte gravitationnelle d'effondrement.

## Points a verifier dans une version publication

- Derivation de la mesure de Liouville depuis une algebre deformee precise.
- Formulation covariante ou choix explicite d'un repere physique.
- Relation de dispersion et definition operationnelle de la vitesse de groupe.
- Equation d'etat massive avec interactions pour les objets compacts.
- Perturbations cosmologiques et stabilite du rebond.
- Contraintes observationnelles sur `beta_0`.
