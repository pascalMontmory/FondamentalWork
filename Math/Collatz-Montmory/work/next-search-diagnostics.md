# Diagnostics de recherche suivants pour C_Montmory

Date: 2026-05-23  
Statut: note de travail, non verifiee

## 1. Question traitee

On cherche si la valeur candidate:

```math
C_{Montmory}=0.107983974916
```

peut provenir d'un mecanisme arithmetique stable plutot que d'une calibration a posteriori.

Avec la normalisation Hardy-Littlewood:

```math
2C_2 \approx 1.3203236316937391,
```

la densite relative cible est:

```math
\rho_M=\frac{C_{Montmory}}{2C_2}
\approx 0.08178598968002705.
```

Cela signifie que tout filtre Montmory final doit retenir environ `8.1786%` de la masse Hardy-Littlewood des premiers jumeaux.

## 2. Diagnostic etendu du filtre Collatz direct

Filtre teste:

```text
T(n) = n/2        si n est pair
T(n) = (3n+1)/2  si n est impair
B = 89
tau_B(n) = premier t tel que T^t(n) <= B
kappa_B(n) = log2(n) / tau_B(n)
score(p,p+2) in {min, geo, harm} de kappa_B(p), kappa_B(p+2)
M_alpha = score >= alpha
```

Les seuils `alpha` ont ete calibres sur une borne basse pour selectionner la proportion cible `rho_M`, puis testes hors echantillon jusqu'a `10^7`.

### Mode min

Calibration sur `10^5`:

```text
alpha = 0.5500968685322026
x        twin_count  selected  selected_ratio  coefficient_estimate
100000   1216        100       0.0822368421    0.1325474528
300000   2986        149       0.0498995311    0.0789952726
1000000  8161        255       0.0312461708    0.0486714247
3000000  20924       469       0.0224144523    0.0347733891
10000000 58972       927       0.0157193244    0.0240828118
```

Calibration sur `10^6`:

```text
alpha = 0.4560177187432752
x        twin_count  selected  selected_ratio  coefficient_estimate
1000000  8161        668       0.0818527141    0.1275000458
3000000  20924       1345      0.0642802523    0.0997232587
10000000 58972       2985      0.0506172421    0.0775482127
```

### Modes geo et harm

Les modes `geo` et `harm` montrent la meme derive hors echantillon, souvent plus forte que le mode `min`.

Exemples avec calibration sur `10^6`:

```text
mode geo, alpha = 0.5149490296253010
1000000  ratio 0.0818527141  coefficient 0.1275000458
3000000  ratio 0.0564423628  coefficient 0.0875636941
10000000 ratio 0.0378484705  coefficient 0.0579857993

mode harm, alpha = 0.4980479184695207
1000000  ratio 0.0818527141  coefficient 0.1275000458
3000000  ratio 0.0601223475  coefficient 0.0932727579
10000000 ratio 0.0417147121  coefficient 0.0639090798
```

## 3. Interpretation du diagnostic direct

Ce test ne soutient pas encore le filtre direct `score >= alpha` comme source stable de `C_Montmory`.

Le comportement observe est:

1. le seuil calibre sur une borne basse ne conserve pas la proportion cible hors echantillon;
2. la proportion selectionnee diminue quand `x` augmente;
3. le coefficient estime tombe sous `0.107983974916` a `10^7` pour les calibrations testees;
4. les variantes `min`, `geo`, `harm` ne corrigent pas la derive.

Conclusion prudente: le verrou n'est pas seulement numerique. Il faut soit un filtre plus structurel, soit une justification probabiliste du seuil, soit abandonner ce filtre comme candidat principal.

## 4. Recherche d'une provenance locale simple du nombre cible

On teste si la densite relative cible ressemble a un produit local elementaire.

Produit brut de survie aux classes interdites `0` et `-2` modulo les petits premiers:

```math
P(y)=\prod_{3\le q\le y}\left(1-\frac{2}{q}\right).
```

Valeurs:

```text
y=3   P(y)=0.3333333333333334
5     P(y)=0.2000000000000000
7     P(y)=0.1428571428571429
11    P(y)=0.1168831168831169
13    P(y)=0.0989010989010989
17    P(y)=0.0872656755009696
19    P(y)=0.0780798149219202
```

La cible:

```text
rho_M = 0.0817859896800271
```

se situe entre les troncatures `y=17` et `y=19`:

```text
P(17) = 0.0872656755009696
P(19) = 0.0780798149219202
```

En coefficient direct:

```text
2C2 * P(17) = 0.1152189335996476
2C2 * P(19) = 0.1030906247996847
C_Montmory  = 0.1079839749160000
```

## 5. Ce que cette observation apporte

Cette proximite ne prouve rien. Elle donne seulement une piste de provenance possible:

- `C_Montmory` pourrait numeriquement ressembler a un coefficient Hardy-Littlewood multiplie par une densite de survie imposee par quelques petits modules;
- si c'est le cas, la constante devrait etre expliquee par un filtre modulaire fixe, pas par une propriete Collatz asymptotique vague;
- cette piste est testable: il faut identifier des congruences precises qui donnent exactement ou naturellement une densite proche de `0.08178598968`.

## 6. Risque d'overfitting

La proximite avec `P(17)` et `P(19)` peut etre accidentelle. Il est facile de fabriquer une constante proche en tronquant un produit eulerien ou en ajustant un petit module.

Pour que cette piste devienne scientifique, il faut:

1. definir le filtre modulaire avant test;
2. calculer sa densite exacte parmi les classes admissibles;
3. montrer pourquoi ce filtre est impose par la dynamique Montmory, et non choisi pour approcher la cible;
4. verifier hors echantillon que le filtre predit une proportion stable parmi les jumeaux.

## 7. Prochaine piste concrete

Tester des filtres hybrides fixes:

```math
M(p,p+2)=1
\quad\Longleftrightarrow\quad
p\bmod W \in A
\quad\text{et}\quad
S_B(p)\ge \alpha(W,A),
```

ou `W` est un primorial petit, par exemple:

```text
W = 3*5*7*11*13*17
```

Mais la regle de choix de `A` doit venir d'une definition Montmory explicite. Si `A` est choisi pour atteindre `rho_M`, la piste perd toute valeur predictive.

## 8. Conclusion de travail

A ce stade, les tests apportent une valeur negative mais utile:

- le filtre Collatz direct a seuil unique ne tient pas encore;
- la dynamique locale empirique initiale ne tient pas encore;
- le nombre cible ressemble davantage a une densite locale tronquee qu'a un coefficient deja explique par les tests Collatz.

La prochaine avance devra donc etre une definition naturelle et fixe d'un filtre modulaire ou dynamique qui produit `rho_M` sans calibration apres coup.