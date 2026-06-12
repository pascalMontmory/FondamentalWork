# Audit mathematique des constantes Montmory

Date: 2026-05-23

Objet audite: `C_Montmory = 0.107983974916`, `K_Montmory = 0.291333547788`, `B_Montmory = 89`, fonctions `tau`, `K_X`, `gamma`, et extensions proposees autour des nombres premiers jumeaux, de Goldbach et de Collatz-Montmory.

## Verdict court

Les constantes et theoremes proposes ne sont pas verifies mathematiquement dans leur forme actuelle.

Le statut correct est:

| Element | Statut apres audit | Raison |
| --- | --- | --- |
| `C_Montmory` | non verifie | `f(x)` et l'ensemble compte ne sont pas definis. Si `f=pi_2`, la valeur contredit la constante attendue de Hardy-Littlewood. |
| `K_Montmory` | non verifie / incompatible avec la definition globale | Pour la dynamique Collatz standard, `K_X(n)=log2(n)/tau(n)` ne peut pas avoir la limite globale annoncee. |
| `B_Montmory=89` | observation experimentale seulement | Une borne globale dependrait d'un resultat de type Collatz, non demontre. |
| `gamma(alpha)` | conjectural | La limite, la mesure et le parametre `mu` ne sont pas etablis. |
| Theoreme jumeaux dans intervalles carres | non verifie | La formule asymptotique a la mauvaise echelle: elle manque un facteur d'ordre `n`. |
| Theoreme Goldbach dynamique | incompatible avec les definitions | Si `tau(n) ~ log2(n)/K`, alors `1/tau(n)` decroit comme `1/log n`, et ne croit pas comme `log n`. |
| Borne des jumeaux | fausse sous l'interpretation Collatz naturelle | Contre-exemple: `(107,109)` avec `tau(107)=81` pour descendre sous 89. |

## Definitions manquantes ou ambigues

Les formulations auditees ne permettent pas une verification complete parce que plusieurs objets ne sont pas fixes:

1. `f(x)` n'est pas defini dans `C_Montmory = lim f(x)/(x/log^2(x))`.
2. La base de `log(x)` n'est pas specifiee dans plusieurs formules.
3. `tau(n)` doit dire si l'on attend `n=89`, `n<=89`, `n=1`, ou l'entree dans un cycle.
4. La transformation exacte Collatz-Montmory n'est pas definie.
5. L'ensemble des structures dites compressibles n'est pas defini.
6. La notion de motif primaire ou de faible entropie algorithmique n'est pas formalisee.

Sans ces definitions, les constantes ne peuvent pas etre des constantes mathematiques immuables. Elles peuvent seulement etre des parametres experimentaux associes a un protocole donne.

## Audit de `C_Montmory`

La definition proposee est:

```text
C_Montmory = lim_{x -> infinity} f(x) / (x / log(x)^2)
```

Cette definition est incomplete parce que `f(x)` n'est pas defini.

Si `f(x)` designe le nombre de paires de premiers jumeaux `p,p+2 <= x`, la conjecture de Hardy-Littlewood predit:

```text
pi_2(x) ~ 2 C_2 x / log(x)^2
C_2 ~= 0.6601618158468696
2 C_2 ~= 1.3203236316937392
```

La valeur annoncee `C_Montmory = 0.107983974916` n'est donc pas compatible avec la constante asymptotique standard des premiers jumeaux. Le ratio est:

```text
0.107983974916 / 1.3203236316937392 ~= 0.08178598968
```

Donc l'une des deux choses doit etre vraie:

- soit `C_Montmory` ne compte pas tous les premiers jumeaux, mais un sous-ensemble compressif qui reste a definir;
- soit la normalisation est incorrecte.

Conclusion: `C_Montmory` ne doit pas etre publiee comme constante mathematique verifiee.

## Audit de `K_Montmory`

La definition proposee est:

```text
K_X(n) = log2(n) / tau(n)
K_Montmory = lim_{n -> infinity} K_X(n)
```

Sous l'interpretation naturelle ou `tau(n)` est le nombre d'etapes Collatz pour atteindre `n <= 89`, la limite globale annoncee est impossible.

En effet, pour `n = 2^m`, la trajectoire est seulement une suite de divisions par 2. Elle atteint `n <= 89` apres environ `m-6` etapes. Alors:

```text
K_X(2^m) = m / (m - 6) -> 1
```

Cette sous-suite force toute limite globale, si elle existait, a valoir `1`, pas `0.291333547788`.

Conclusion: avec la definition ecrite, `K_Montmory` n'est pas une limite globale sur les entiers naturels.

## Audit de `B_Montmory = 89`

La phrase `borne compressive universelle atteinte par tous les entiers testes` est experimentale. Elle ne prouve pas une borne universelle.

Si `tau(n)` signifie atteindre exactement `89`, la definition est fausse pour de nombreux entiers: beaucoup de trajectoires Collatz n'atteignent pas exactement 89.

Si `tau(n)` signifie atteindre `n <= 89`, alors l'existence de `tau(n)` pour tout entier positif depend d'un resultat global de type Collatz. Ce resultat n'est pas demontre.

Conclusion: `B_Montmory=89` peut etre un seuil experimental ou logiciel, pas une borne mathematique universelle prouvee.

## Contre-exemple a la borne des jumeaux

La borne proposee est:

```text
tau(p), tau(p+2) <= lambda log2(p)
lambda = 1 / K_Montmory ~= 3.4324917524695375
```

Pour la paire de premiers jumeaux `(107,109)`, avec la dynamique Collatz standard et `tau(n)` defini comme le nombre d'etapes pour descendre sous ou egal a 89:

```text
tau(107) = 81
lambda log2(107) ~= 23.140029830367606
```

Donc:

```text
81 > 23.140029830367606
```

La borne est fausse sous cette interpretation naturelle.

## Audit de `gamma(alpha)`

La definition proposee est:

```text
gamma(alpha) = lim_{x -> infinity} #{p <= x | K_X(p) >= alpha} / pi(x)
gamma(alpha) ~= (1 - alpha / K_Montmory)^mu
```

Problemes:

1. La limite n'est pas prouvee.
2. `K_X(p)` depend d'une definition non stabilisee de `tau`.
3. La formule impose `gamma(K_Montmory)=0`, ce qui ne suit pas de la definition.
4. Le parametre `mu` n'est pas derive.

Conclusion: cette fonction est une conjecture de modele, pas un resultat.

## Audit de la densite compressive des jumeaux

La formule proposee est:

```text
pi_2^{>= alpha}(x) ~= 2 C_Montmory gamma(alpha)^2 x / log(x)^2
```

Elle peut etre une hypothese de modele pour un sous-ensemble de paires compressives, mais elle n'est pas demontree.

Si `alpha = 0` et `gamma(0)=1`, alors la formule donne un coefficient `2 C_Montmory ~= 0.215967949832`. Pour tous les premiers jumeaux, le coefficient conjectural standard est `2 C_2 ~= 1.320323631694`. Les deux ne coincident pas.

Conclusion: la formule doit preciser qu'elle concerne un sous-ensemble strict ou que sa normalisation est differente.

## Audit du theoreme Montmory-Legendre

Proposition:

```text
Il existe une infinite de n tels que l'intervalle (n^2, (n+1)^2) contient une paire de jumeaux.
```

Cette proposition implique l'existence d'une infinite de premiers jumeaux. Elle n'est pas demontree actuellement.

La forme asymptotique proposee est:

```text
pi_2(n^2, (n+1)^2) ~ (2 C_Montmory) / log(n)^2
```

Cette echelle est incorrecte pour un comptage dans un intervalle de longueur `(n+1)^2 - n^2 = 2n+1`.

Par heuristique Hardy-Littlewood, le nombre attendu de paires de jumeaux dans cet intervalle est plutot d'ordre:

```text
2 C_2 * (2n) / log(n^2)^2
= C_2 * n / log(n)^2
```

Il manque donc un facteur d'ordre `n` dans la formule proposee.

Conclusion: la formule Montmory-Legendre ecrite est mathematiquement incorrecte comme asymptotique de comptage.

## Audit du theoreme Goldbach dynamique

Formule proposee:

```text
(1 / N(n)) * sum_{p+q=n} (1/tau(p) + 1/tau(q)) ~ 2 K_Montmory log(n)
```

Mais si l'equation centrale dit:

```text
tau(n) * K_Montmory ~= log2(n)
```

alors:

```text
1/tau(n) ~= K_Montmory / log2(n)
```

La moyenne des inverses de trajectoires devrait donc decroitre comme `1/log(n)`, pas croitre comme `log(n)`.

Conclusion: la formule Goldbach dynamique est incompatible avec les definitions internes.

## Audit de la structure alternative `s(n)`

Formule proposee:

```text
s(n) = sum_{d | n} 1 / log(d)
K_Montmory ~= lim_{n -> infinity} log(n) / E[s(n)]
```

Probleme immediat: le diviseur `d=1` donne `1/log(1)`, qui est non defini car `log(1)=0`.

Il faut donc definir au minimum:

```text
s(n) = sum_{d | n, d > 1} 1 / log(d)
```

Meme apres cette correction, l'esperance `E[s(n)]`, la mesure de probabilite et le mode de passage a la limite ne sont pas definis.

Conclusion: cette formule n'est pas verifiable en l'etat.

## Commande de verification utilisee

Verification numerique minimale pour le contre-exemple `(107,109)`:

```python
import math
K = 0.291333547788

def tau_leq_B(n, B=89):
    t = 0
    while n > B:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        t += 1
    return t

p = 107
print(tau_leq_B(p))
print((1 / K) * math.log2(p))
```

Sortie attendue:

```text
81
23.140029830367606
```

## Classification recommandee

A publier comme verifie:

- uniquement les definitions elementaires une fois stabilisees;
- le contre-exemple a la borne des jumeaux sous la definition `tau = temps pour atteindre n <= 89`;
- les calculs numeriques bornes avec code et plage explicites.

A garder comme conjectural:

- `C_Montmory`;
- `K_Montmory`;
- `gamma(alpha)`;
- les formules de densite compressive;
- les extensions Goldbach et Legendre;
- les applications cryptographiques.

A corriger avant toute publication:

1. Definir rigoureusement la transformation Collatz-Montmory.
2. Definir `tau(n)` sans ambiguite.
3. Definir `f(x)` et l'ensemble compte par `C_Montmory`.
4. Preciser la base des logarithmes.
5. Remplacer les mots `theoreme` par `conjecture` tant qu'il n'y a pas de preuve.
6. Retirer `immuable` pour les constantes tant qu'elles dependent d'un protocole experimental non fixe.
7. Corriger l'asymptotique des intervalles carres en tenant compte de la longueur `2n+1`.
8. Corriger la formule Goldbach dynamique, car elle a actuellement la mauvaise croissance.