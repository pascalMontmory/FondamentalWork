# Jumeau V1: extraction utile et correction des facteurs locaux mixtes

Date: 2026-05-23

Objet: analyser le document `Jumeau V1 — Facteurs locaux mixtes et estimation de pi_2(x)` et separer ce qui est recuperable de ce qui doit etre corrige.

## 1. Verdict court

Le document contient une idee exploitable:

```text
construire un estimateur de pi_2(x) en remplacant certains facteurs locaux Hardy-Littlewood par des facteurs locaux mesures par une dynamique Montmory.
```

Mais la normalisation des facteurs locaux est incorrecte dans la version fournie. La quantite:

```math
\Sigma_q = 1 - \mu_q(0) - \mu_q(-2)
```

est une probabilite locale de non-exclusion modulo `q`. Elle ne doit pas etre comparee directement a:

```math
1 - \frac{1}{(q-1)^2},
```

qui est le facteur Hardy-Littlewood deja normalise par la densite brute des entiers copremiers.

## 2. Rappel du facteur Hardy-Littlewood correct

Pour le motif jumeau `H={0,2}` et un premier impair `q >= 3`, les classes interdites sont:

```math
0, -2 \pmod q.
```

Donc, sous la loi uniforme modulo `q`, la probabilite locale de non-exclusion est:

```math
\Sigma_q^{\mathrm{unif}} = 1 - \frac{2}{q} = \frac{q-2}{q}.
```

Le facteur local Hardy-Littlewood est:

```math
L_q^{\mathrm{HL}}
=
\frac{1-2/q}{(1-1/q)^2}
=
\frac{q(q-2)}{(q-1)^2}
=
1-\frac{1}{(q-1)^2}.
```

Conclusion: si `Sigma_q` est une probabilite, le facteur local dynamique correct est:

```math
L_q^{\mathrm{dyn}}
=
\frac{\Sigma_q}{(1-1/q)^2}.
```

## 3. Erreur dans la formule V1

La V1 propose:

```math
K_2^{\mathrm{mix}}(Q)
=
2\prod_{q\le Q}\frac{\Sigma_q}{1-1/(q-1)^2}
\cdot
\prod_{q>Q}\left(1-\frac{1}{(q-1)^2}\right).
```

Cette expression melange une probabilite `Sigma_q` avec un facteur HL normalise.

Elle donne aussi une equivalence incorrecte:

```math
K_2^{\mathrm{mix}}(Q)
=
2C_2\prod_{q\le Q}\frac{\Sigma_q}{1-1/(q-1)^2}.
```

Cette equivalence ne suit pas de la formule precedente.

## 4. Formule corrigee

La version mathematiquement coherente est:

```math
K_2^{\mathrm{mix}}(Q)
=
2
\prod_{3\le q\le Q}
\frac{\Sigma_q}{(1-1/q)^2}
\cdot
\prod_{q>Q}
\left(1-\frac{1}{(q-1)^2}\right),
```

ou, de facon equivalente:

```math
K_2^{\mathrm{mix}}(Q)
=
2C_2
\prod_{3\le q\le Q}
\frac{\Sigma_q}{1-2/q}.
```

La deuxieme forme montre clairement que le biais dynamique est mesure par rapport a la probabilite uniforme de non-exclusion `1-2/q`, pas par rapport au facteur HL normalise.

## 5. Reduction correcte a Hardy-Littlewood

Si la dynamique Montmory est uniforme modulo `q`, alors:

```math
\Sigma_q = 1-\frac{2}{q}.
```

Dans ce cas:

```math
\frac{\Sigma_q}{1-2/q}=1
```

et donc:

```math
K_2^{\mathrm{mix}}(Q)=2C_2.
```

C'est la bonne version de la Proposition 4.1.

## 6. Stability theorem corrige

On definit le biais local relatif:

```math
\varepsilon_q
=
\frac{\Sigma_q}{1-2/q}-1.
```

Alors:

```math
K_2^{\mathrm{mix}}(Q)=2C_2\prod_{3\le q\le Q}(1+\varepsilon_q).
```

Si `|epsilon_q| <= 1/2`, alors:

```math
\left|\log\frac{K_2^{\mathrm{mix}}(Q)}{2C_2}\right|
\le
\sum_{3\le q\le Q}\frac{|\varepsilon_q|}{1-|\varepsilon_q|}
\le
2\sum_{3\le q\le Q}|\varepsilon_q|.
```

Cette partie est recuperable apres correction de la definition de `epsilon_q`.

## 7. Queue eulerienne: correction de l'inegalite

La V1 ecrit une chaine d'inegalites avec une direction incorrecte.

Pour `0<a_q<1`, on a:

```math
\log\prod_{q>Q}(1-a_q)
=
\sum_{q>Q}\log(1-a_q)
=
-O\left(\sum_{q>Q}a_q\right),
```

avec:

```math
a_q=\frac{1}{(q-1)^2}.
```

Comme:

```math
\sum_{q>Q}\frac{1}{(q-1)^2}
\le
\sum_{n>Q}\frac{1}{(n-1)^2}
=O(1/Q),
```

on obtient:

```math
\prod_{q>Q}\left(1-\frac{1}{(q-1)^2}\right)
=
1+O(1/Q).
```

C'est la conclusion correcte. La preuve doit eviter d'ecrire une borne superieure du type `<= exp(-1/Q)`, qui ne donne pas l'erreur relative souhaitee et inverse une comparaison intermediaire.

## 8. Monte Carlo: correction de la concentration

La V1 cite Hoeffding comme si les observations post burn-in etaient independantes.

Pour une chaine de Markov, ce n'est pas automatique. Il faut choisir une des options suivantes:

1. prouver une inegalite de concentration pour chaine de Markov avec gap spectral ou temps de melange;
2. utiliser une taille effective d'echantillon `N_eff` estimee par autocorrelation;
3. faire des repetitions independantes et estimer la variance inter-chaines;
4. utiliser Hoeffding seulement si les echantillons sont effectivement independants.

Donc l'idee d'intervalle de confiance est bonne, mais la justification doit etre modifiee.

## 9. Estimateur de pi_2(x) corrige

Une version coherente est:

```math
\widehat{\pi_2}(x;Q)
=
K_2^{\mathrm{mix}}(Q)
\frac{x}{\log^2x}
\left(1+\frac{2}{\log x}+\frac{6}{\log^2x}\right).
```

avec:

```math
K_2^{\mathrm{mix}}(Q)
=
2C_2\prod_{3\le q\le Q}\frac{\widehat\Sigma_q}{1-2/q}.
```

Ce n'est pas une preuve de Hardy-Littlewood; c'est un estimateur calibre.

## 10. Lien avec C_Montmory

Cette V1 est utile pour `C_Montmory`, mais pas directement comme preuve.

Si on obtient un biais moyen stable:

```math
B_M(Q)
=
\prod_{3\le q\le Q}\frac{\Sigma_q}{1-2/q}
\to B_M,
```

alors le coefficient asymptotique dynamique serait:

```math
C_{\mathrm{dyn}}=2C_2 B_M.
```

Pour retrouver:

```math
C_{\mathrm{Montmory}}=0.107983974916,
```

il faudrait:

```math
B_M
=
\frac{C_{\mathrm{Montmory}}}{2C_2}
\approx 0.08178598968002706.
```

Donc Jumeau V1 fournit une deuxieme voie vers la constante: non plus par un filtre direct sur les paires, mais par un produit de biais locaux Montmory.

## 11. Interet scientifique de cette voie

La voie `facteurs locaux mixtes` est peut-etre plus professionnelle que le filtre direct si l'on peut definir une vraie dynamique stationnaire `mu_q`.

Elle permet de separer:

1. les faits algebriques sur les produits;
2. les estimations statistiques de `Sigma_q`;
3. l'hypothese dynamique de stationnarite;
4. la comparaison a Hardy-Littlewood.

Mais elle exige une definition complete de la transition Montmory modulo `q`.

## 12. Verrou restant

Le nouveau verrou est:

```text
definir transition_Montmory sur Z/qZ de facon canonique, ergodique, apériodique, et non calibree apres coup.
```

Sans cette transition, `Sigma_q` est seulement un symbole.

## 13. Formulation recommandee

Formulation correcte:

```text
Jumeau V1 propose un estimateur experimental de pi_2(x) par facteurs locaux dynamiques. Apres normalisation, le facteur local dynamique doit etre Sigma_q/(1-1/q)^2, ou equivalemment le biais relatif Sigma_q/(1-2/q). Si le produit des biais relatifs converge, il definit un coefficient dynamique C_dyn = 2C_2 B_M. La valeur C_Montmory correspondrait au cas B_M ~= 0.08178598968.
```

Formulation a eviter:

```text
La formule V1 prouve ou estime correctement pi_2(x) telle quelle.
```

## 14. Ce qu'on peut en tirer

On peut en tirer trois choses solides:

1. un squelette d'estimateur experimental;
2. un theoreme de stabilite multiplicative apres correction de normalisation;
3. une nouvelle interpretation de `C_Montmory` comme produit limite de biais locaux Montmory.

Ce qui n'est pas encore disponible:

1. une dynamique Montmory canonique modulo `q`;
2. une preuve d'ergodicite/apériodicite;
3. des estimations reproductibles de `Sigma_q`;
4. une preuve ou evidence forte que le produit converge vers `0.08178598968`.
