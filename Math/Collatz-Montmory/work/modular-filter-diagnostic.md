# Diagnostic des filtres modulaires pour C_Montmory

Date: 2026-05-23  
Statut: note de travail, non verifiee comme theorie Montmory

## 1. Objectif

Cette note examine une piste naturelle apres les diagnostics negatifs du filtre Collatz direct: la constante cible pourrait-elle venir d'un filtre de congruences modulo un petit primorial ?

La densite relative cible reste:

```math
\rho_M=\frac{0.107983974916}{2C_2}
\approx 0.08178598968002705.
```

## 2. Classes admissibles pour les jumeaux modulo W

Soit:

```math
W=\prod_{q\in P}q
```

ou `P` est un ensemble fini de premiers impairs.

Pour le motif `(n,n+2)`, les classes interdites modulo `q` sont:

```math
0, -2 \pmod q.
```

Donc le nombre de classes admissibles modulo `q` est `q-2`, et le nombre total de classes admissibles modulo `W` est:

```math
A(W)=\prod_{q\mid W}(q-2).
```

Sous l'heuristique Hardy-Littlewood renforcee d'equirepartition dans les classes admissibles modulo `W`, tout sous-ensemble fixe `A` de ces classes aurait une densite relative:

```math
\rho_A=\frac{|A|}{A(W)}.
```

## 3. Consequence importante

Un filtre modulaire peut produire une densite relative stable, mais seulement rationnelle de la forme:

```math
\frac{m}{\prod_{q\mid W}(q-2)}.
```

Cette observation est mathematiquement utile, mais elle cree aussi un risque d'overfitting: en prenant `W` assez grand, on peut approximer presque n'importe quelle valeur cible par un choix arbitraire de `m` classes.

## 4. Approximation rationnelle de la cible par primoriaux

Pour les primoriaux impairs successifs, le denominateur admissible est `prod(q-2)`. La meilleure densite `m/A(W)` proche de `rho_M` donne:

```text
P<=7   denom=15          nearest=1          density=0.0666666666666667  relerr=-1.85e-1
P<=11  denom=135         nearest=11         density=0.0814814814814815  relerr=-3.72e-3
P<=13  denom=1485        nearest=121        density=0.0814814814814815  relerr=-3.72e-3
P<=17  denom=22275       nearest=1822       density=0.0817957351290685  relerr= 1.19e-4
P<=19  denom=378675      nearest=30970      density=0.0817851719812504  relerr=-1.00e-5
P<=23  denom=7952175     nearest=650377     density=0.0817860522435686  relerr= 7.65e-7
P<=29  denom=214708725   nearest=17560166   density=0.0817859916964250  relerr= 2.47e-8
P<=31  denom=6226553025  nearest=509244801  density=0.0817859896085925  relerr=-8.73e-10
```

Conclusion: le fait qu'une densite modulaire puisse approximer `rho_M` n'est pas une preuve de structure. C'est attendu des grands denominateurs. Il faut une regle naturelle pour choisir les classes, pas seulement le bon nombre de classes.

## 5. Test de correlation entre score Collatz et petits modules

On a teste si les paires avec les meilleurs scores Collatz, selectionnees au quantile cible `rho_M`, etaient concentrees dans certaines classes admissibles modulo les petits premiers.

Pour chaque `X`, on calibre le seuil `alpha(X)` pour garder environ `rho_M` des paires jusqu'a `X`, puis on compare la distribution des residues des paires selectionnees avec la distribution de toutes les paires de jumeaux jusqu'a `X`.

### Resultat synthetique

A `X=10^7`, les differences maximales entre frequence selectionnee et frequence de base sont petites:

```text
q   max_abs_difference
5   0.012
7   0.005
11  0.010
13  0.006
17  0.006
19  0.010
23  0.006
29  0.007
31  0.006
```

Interpretation: le haut du score Collatz ne semble pas correspondre a un fort filtre de congruences modulo les petits premiers `5..31`. Les ecarts observes diminuent avec la taille et ressemblent davantage a du bruit d'echantillonnage qu'a une structure modulaire stable.

## 6. Impact sur le programme Montmory

Cette note restreint les pistes plausibles:

1. un filtre modulaire arbitraire peut approximer `rho_M`, mais ce serait non predictif;
2. le score Collatz direct ne semble pas cacher un petit filtre modulaire evident;
3. si une structure modulaire existe, elle doit etre definie par une regle Montmory explicite plus profonde que `score >= alpha`;
4. sinon, la piste modulaire doit etre traitee comme un controle negatif.

## 7. Criteres pour qu'un filtre modulaire devienne recevable

Un filtre modulaire `A subset (Z/WZ)_admissible` ne devrait etre considere que si:

1. `W` est fixe par une definition theorique avant le test;
2. les classes `A` sont determinees par une regle simple, non par ajustement de la cardinalite;
3. la densite exacte `|A|/A(W)` est calculee;
4. le comptage des jumeaux dans ces classes est teste hors echantillon;
5. la meme regle continue de fonctionner lorsque `W` est agrandi ou lorsque les donnees augmentent.

## 8. Conclusion de travail

La piste modulaire apporte une clarification importante: elle fournit un cadre ou une densite relative stable serait mathematiquement naturelle, mais elle montre aussi pourquoi approcher `0.08178598968` n'est pas suffisant.

Pour avancer, il faut maintenant une regle Montmory explicite qui choisit les classes admissibles. Sans cette regle, un bon accord numerique avec `rho_M` serait probablement une calibration a posteriori.