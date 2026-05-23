# Protocole de determination des bornes Collatz-Montmory

Date: 2026-05-23  
Statut: note de travail, protocole experimental non verifie comme theorie

## 1. Probleme

Le seuil `B=89` n'est pas necessairement unique. La question correcte n'est donc pas:

```text
Pourquoi exactement 89 ?
```

mais plutot:

```text
Existe-t-il une bande de bornes B donnant la meme densite de queue Collatz normalisee ?
```

Si oui, `89` peut etre traite comme un representant d'une zone stable. Si non, `89` serait probablement un parametre ajuste.

## 2. Score teste

Pour une borne `B`, on definit:

```math
\tau_B(n)=\min\{t\ge0:T^t(n)\le B\},
```

avec la transformation Collatz acceleree:

```math
T(n)=
\begin{cases}
n/2, & n\equiv0\pmod2,\\
(3n+1)/2, & n\equiv1\pmod2.
\end{cases}
```

Puis:

```math
\kappa_B(n)=\frac{\log_2 n}{\tau_B(n)}.
```

Pour une paire `(p,p+2)`:

```math
S_B(p)=\min(\kappa_B(p),\kappa_B(p+2)).
```

On centre par la derive moyenne du modele aleatoire accelere:

```math
d=1-\frac12\log_2 3
\approx0.20751874963942196.
```

Score normalise:

```math
Z_B(p)=\left(S_B(p)-d\right)\log_2 p.
```

## 3. Critere de determination d'une bande admissible

On fixe une densite cible:

```math
\rho_M\approx0.08178598968002705.
```

Pour chaque `B`:

1. calibrer `alpha_B` sur les paires de jumeaux jusqu'a `X_train=10^6` pour garder la proportion `rho_M`;
2. geler `alpha_B`;
3. mesurer la proportion selectionnee sur des fenetres disjointes:

```text
(10^6,3*10^6]
(3*10^6,10^7]
```

4. calculer:

```math
E_B=\max_i |\widehat\rho_B(I_i)-\rho_M|.
```

Une borne `B` est admissible experimentalement si `E_B` reste petite et si les fenetres ne montrent pas de derive monotone forte.

## 4. Balayage preliminaire jusqu'a 10^7

Balayage effectue avec `X_train=10^6`.

```text
B,alpha,cum1e7,win1,win2,max_window_abs_err
7,2.310310818,0.094886672,0.092141346,0.098585997,0.016800007
15,2.696836322,0.087659473,0.090025856,0.088099243,0.008239866
27,3.060467309,0.083706569,0.081250490,0.084919050,0.003133060
31,3.464809592,0.083757465,0.082739168,0.084498528,0.002712538
45,3.706562776,0.081993078,0.080937084,0.082369638,0.000848906
63,4.173269857,0.082654723,0.081172138,0.083315812,0.001529822
75,4.273314732,0.082824376,0.080310272,0.083867746,0.002081756
89,4.412400011,0.082366314,0.079448406,0.083447225,0.002337584
95,4.648039913,0.081348398,0.081563896,0.081160639,0.000625350
111,4.810039495,0.079855456,0.078899945,0.079741379,0.002886045
127,4.987841315,0.078260722,0.079448406,0.077086838,0.004699152
159,5.222352824,0.077802660,0.077019510,0.077191968,0.004766480
191,5.454042824,0.076004343,0.074825668,0.075141926,0.006960322
223,5.664741821,0.075003393,0.072945232,0.074222035,0.008840757
255,5.832553693,0.074070304,0.073258638,0.072671362,0.009114627
319,6.159652640,0.071983578,0.070359633,0.070411060,0.011426356
383,6.500102020,0.068912866,0.068400846,0.066310976,0.015475014
511,7.090785071,0.063263436,0.061427564,0.059898024,0.021887966
767,7.950049768,0.058699783,0.056491421,0.054483810,0.027302180
1023,8.632272321,0.053762894,0.050301653,0.048911901,0.032874089
```

## 5. Interpretation du balayage

Le resultat ne pointe pas vers une borne unique. Il pointe vers une zone de stabilite.

A ce stade, la bande experimentale plausible est approximativement:

```text
27 <= B <= 111
```

avec une zone plus stable:

```text
45 <= B <= 95
```

Dans cette zone, les erreurs par fenetres restent proches de la cible. Au-dela de `B=127`, les proportions commencent a decroitre. Pour `B>=255`, le decrochage est net.

## 6. Pourquoi une bande peut avoir du sens

La borne `B` sert a couper la fin de trajectoire, c'est-a-dire la partie ou les dynamiques tombent dans le petit graphe Collatz. Si `B` est trop petit, le score incorpore trop de bruit de fin de trajectoire. Si `B` est trop grand, le temps d'arret devient trop court et perd une partie de l'information asymptotique.

Donc une bonne borne devrait etre:

1. assez grande pour eviter les artefacts minuscules du cycle final;
2. assez petite pour conserver la descente longue de la trajectoire;
3. situee dans une zone ou la densite de queue ne varie pas fortement avec `B`.

Dans cette lecture, `89` n'est pas une constante fondamentale. C'est un representant raisonnable d'une bande de stabilite.

## 7. Regle de selection proposee

Pour eviter la calibration a posteriori, on peut definir une regle de selection de borne:

1. choisir une grille prepubliee de bornes `B`;
2. choisir des fenetres d'entrainement et de validation prepubliees;
3. retenir la bande maximale de `B` telle que `E_B <= epsilon`, par exemple `epsilon=0.003`;
4. choisir comme representant le plus petit `B` dans la bande qui est superieur au coeur terminal Collatz juge trop petit, ou le centre logarithmique de la bande;
5. ne plus modifier `B` apres validation hors echantillon.

Avec le balayage actuel et `epsilon=0.003`, une selection prudente donnerait une bande proche de:

```text
31 <= B <= 111
```

Avec `epsilon=0.0025`, elle donnerait plutot:

```text
45 <= B <= 95
```

## 8. Statut de 89

`89` reste acceptable experimentalement parce qu'il est dans la zone stable `45..95` et parce qu'il n'est pas isole. Mais il ne doit pas etre presente comme demontre.

Formulation prudente:

```text
B=89 est un representant de la bande experimentale de stabilite des bornes Collatz-Montmory.
```

Formulation a eviter:

```text
89 est la borne universelle demontree.
```

## 9. Prochains tests

Avant diffusion scientifique, il faut:

1. refaire ce balayage a `10^8`;
2. tester des fenetres disjointes plus nombreuses;
3. comparer jumeaux et premiers non jumeaux pour chaque `B`;
4. estimer l'incertitude statistique sur `E_B`;
5. verifier que la bande stable ne se deplace pas quand `X_train` augmente.

## 10. Conclusion

La bonne approche n'est pas de chercher une borne unique par intuition. Il faut definir une bande stable de bornes par un protocole reproductible. Les donnees jusqu'a `10^7` soutiennent l'idee que `89` appartient a une bande stable, mais ne prouvent pas que `89` soit fondamental.