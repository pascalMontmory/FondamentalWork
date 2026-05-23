# Positionnement bibliographique du programme Lambda_B

Date: 2026-05-23  
Statut: note de positionnement, a consolider avant publication

## 1. Position courte

La contribution ne doit pas etre presentee comme une nouveaute sur les arbres inverses Collatz ou sur les temps d'arret eux-memes.

Formulation prudente:

```text
Nous ne revendiquons pas la nouveaute des arbres inverses Collatz ni des temps d'arret.
La contribution proposee est la loi mobile Lambda_B et son usage comme mecanisme de filtrage arithmetique.
```

Formulation mathematique:

```math
\left(E_B(n),\tau_B(n)-\frac{\log_2 n}{d}\right)
\Longrightarrow
\Lambda_B^{\mathcal P},
\qquad
 d=1-\frac12\log_2 3.
```

L'usage propose est ensuite:

```math
\Lambda_B
\longrightarrow
\text{classes de bornes}
\longrightarrow
\text{queue normalisee}
\longrightarrow
C=2C_2\rho.
```

## 2. Ce qui est classique

### 2.1. Temps d'arret Collatz

Les temps d'arret sont un objet classique du probleme `3x+1`, en particulier depuis Terras.

Reference minimale:

```text
R. Terras, A stopping time problem on the positive integers,
Acta Arithmetica 30 (1976), 241-252.
```

Terras introduit et etudie des fonctions de distribution de temps d'arret, dans un cadre qui est devenu standard pour les travaux probabilistes sur Collatz.

### 2.2. Arbres inverses

Les arbres inverses Collatz et les branches inverses sont classiques. Pour la transformation acceleree:

```math
T(n)=n/2\quad(n\text{ pair}),
\qquad
T(n)=(3n+1)/2\quad(n\text{ impair}),
```

les preimages sont:

```math
2y,
\qquad
\frac{2y-1}{3}\quad\text{si }y\equiv2\pmod3.
```

Ces formules ne doivent pas etre revendiquees comme nouvelles.

### 2.3. Modeles probabilistes et derive moyenne

L'heuristique de derive logarithmique moyenne est classique. Dans le modele parites aleatoires, la derive descendante moyenne pour la carte acceleree est:

```math
d=1-\frac12\log_2 3.
```

Cette valeur sert ici de centrage, mais son origine probabiliste n'est pas nouvelle.

### 2.4. Bibliographies et surveys

References de cadrage:

```text
J. C. Lagarias, The 3x+1 Problem: An Annotated Bibliography (1963-1999), arXiv:math/0309224.
J. C. Lagarias, The 3x+1 Problem: An Annotated Bibliography, II (2000-2009), arXiv:math/0608208.
M. Chamberland, An Update on the 3x+1 Problem, survey.
```

Ces references doivent etre consultees avant toute revendication forte de nouveaute.

## 3. Travaux recents a surveiller

Des travaux recents et preprints etudient les distributions de temps d'arret, les modeles probabilistes, les structures modulaires et les phenomenes statistiques Collatz.

A citer seulement apres verification bibliographique precise:

```text
- travaux sur les distributions empiriques des temps d'arret;
- modeles probabilistes ou bayesiens des temps d'arret;
- travaux sur les structures modulaires, notamment modulo petites puissances;
- travaux sur les fonctions de stopping time coefficient / odd-step density.
```

Ces travaux peuvent recouvrir une partie de l'analyse statistique de `tau_B`, mais pas necessairement l'usage arithmetique propose ici.

## 4. Ce que le programme Lambda_B propose de specifique

La proposition specifique est de ne pas regarder seulement le temps d'arret, mais la loi jointe mobile:

```math
\Lambda_B^{\mathcal P}
=\lim_{x\to\infty}
\mathcal L\left(
E_B(n),\tau_B(n)-\frac{\log_2 n}{d}
\right),
\qquad n\in\mathcal P\cap[1,x].
```

La population `\mathcal P` peut etre:

```text
- entiers impairs;
- nombres premiers;
- premiers p avec p+2 non premier;
- premiers jumeaux projetes sur p.
```

Le point distinctif est l'association de deux informations:

1. le point d'entree terminal `E_B(n)`;
2. la fluctuation centree du temps d'arret.

La contribution potentielle est l'usage de cette loi pour definir un filtre arithmetique stable.

## 5. Lien avec les bornes

Pour deux bornes `B_1<B_2`, on a l'identite exacte:

```math
\tau_{B_1}(n)=\tau_{B_2}(n)+\Delta_{B_1,B_2}(n).
```

La correction terminale est:

```math
\Delta_{B_1,B_2}(n)
=\tau_{B_1}(E_{B_2}(n)).
```

Le programme propose de definir des classes de bornes par la stabilite distributionnelle de cette correction sous `\Lambda_B`.

Ce point peut etre formule comme contribution methodologique:

```text
La borne B n'est pas choisie comme constante isolee, mais comme representant d'une classe de bornes dont les corrections terminales preservent la loi de queue normalisee.
```

## 6. Lien avec Hardy-Littlewood

Sous Hardy-Littlewood jumeaux:

```math
\pi_2(x)\sim2C_2\frac{x}{\log^2x}.
```

Si une queue `Q_B(alpha)` definie par `Lambda_B` a une densite relative `rho`, et si cette queue est decorrelee de la condition `p+2` premier, alors on obtient conditionnellement:

```math
N_{B,\alpha}(x)
\sim
2C_2\rho\frac{x}{\log^2x}.
```

La valeur candidate devient:

```math
C_{Montmory}=2C_2\rho.
```

Cette partie n'est pas une preuve de Hardy-Littlewood ni une preuve de la constante. C'est un mecanisme conditionnel de filtrage.

## 7. Revendication publiable prudente

Une revendication prudente pourrait etre:

```text
We introduce a moving terminal-entrance law for accelerated Collatz stopping times,
combining the terminal entrance state E_B(n) with the centered stopping-time fluctuation
 tau_B(n)-log_2(n)/d. We use this law to define bound-equivalence classes and conditional
arithmetic filters compatible with Hardy-Littlewood asymptotics.
```

En francais:

```text
Nous introduisons une loi mobile d'entree terminale pour les temps d'arret Collatz acceleres,
associant l'etat terminal E_B(n) et la fluctuation centree tau_B(n)-log_2(n)/d. Nous utilisons
cette loi pour definir des classes de bornes et des filtres arithmetiques conditionnels compatibles
avec les asymptotiques de Hardy-Littlewood.
```

## 8. Ce qu'il ne faut pas revendiquer

A eviter:

```text
Nous decouvrons les arbres inverses Collatz.
```

A eviter:

```text
Nous prouvons C_Montmory.
```

A eviter:

```text
Nous prouvons une nouvelle constante des jumeaux.
```

A eviter:

```text
89 est une borne fondamentale unique.
```

## 9. Section bibliographique minimale pour un preprint

Une version preprint devrait contenir au minimum:

```text
Terras (1976) for stopping-time distribution.
Lagarias annotated bibliographies for historical coverage.
A modern survey such as Chamberland for terminology and state of the problem.
References on inverse trees / 3x+1 semigroups.
References on empirical or probabilistic stopping-time distributions.
Hardy-Littlewood / Bateman-Horn for the twin-prime asymptotic side.
```

## 10. Tests bibliographiques a faire avant soumission

Avant toute soumission, chercher explicitement:

```text
"Collatz" "terminal entrance" stopping time
"Collatz" "entrance distribution"
"3x+1" "stopping time distribution" "centered"
"Collatz" "inverse tree" "stopping time"
"Terras" "distribution function" "stopping time"
"Collatz" "Hardy-Littlewood" primes
```

Le but est de verifier si une loi equivalente a `Lambda_B` a deja ete definie sous un autre nom.

## 11. Statut actuel

Actuellement:

- les briques Collatz sont classiques;
- la formulation `Lambda_B` semble specifique au programme Montmory;
- le lien avec Hardy-Littlewood est conditionnel et probablement original dans ce depot;
- aucune preuve asymptotique complete n'est encore disponible;
- le positionnement bibliographique doit etre renforce avant diffusion.

## 12. Conclusion

La nouveaute defendable n'est pas dans Collatz inverse ou les temps d'arret. Elle est dans l'assemblage:

```math
\Lambda_B
\to
\text{classes de bornes}
\to
\text{queue normalisee}
\to
2C_2\rho.
```

C'est cette contribution qu'il faut proteger, clarifier et tester.