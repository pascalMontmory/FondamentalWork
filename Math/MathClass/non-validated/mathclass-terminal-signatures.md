# MathClass: signatures terminales de classes arithmetiques

> Statut : note verifiee pour les identites structurelles finies et les
> implications conditionnelles explicites.
>
> Non prouve : existence des limites pour les premiers, jumeaux, cousins,
> sexy primes ; Hardy-Littlewood ; Collatz ; role special de `B=89`.

## 1. Idee

On fixe une application d'observation terminale :

```math
E_B:\mathbb N\to X_B.
```

Dans l'application Collatz :

```math
X_B=\{1,\ldots,B\}\cup\{\infty\},
```

et `E_B(n)` est le premier point d'entree de l'orbite acceleree de Collatz
dans `[1,B]`, ou `\infty` si l'entree n'a pas lieu.

Pour une classe arithmetique `\mathcal F\subseteq\mathbb N`, on definit :

```math
\mathcal F_N=\mathcal F\cap[1,N],
```

et, si `\mathcal F_N` est non vide :

```math
\nu_{B,\mathcal F,N}
=
(E_B)_\#\left(
\frac{1}{|\mathcal F_N|}
\sum_{n\in\mathcal F_N}\delta_n
\right).
```

Cette loi est la signature terminale finie de la classe `\mathcal F`.

## 2. Classes arithmetiques

Le cadre traite uniformement :

```math
\mathbb N,\quad 2\mathbb N+1,\quad
\{n:n\equiv a\pmod q\},\quad
\mathbb P,
```

ainsi que les motifs premiers :

```math
\mathcal P_H
=
\{p:p+h\text{ est premier pour tout }h\in H\}.
```

Exemples :

```math
H=\{0,2\}\quad\text{jumeaux},
```

```math
H=\{0,4\}\quad\text{cousins},
```

```math
H=\{0,6\}\quad\text{sexy primes}.
```

## 3. Resultat demontre A : decomposition des unions disjointes

Si `\mathcal F` et `\mathcal G` sont disjointes et si
`(\mathcal F\cup\mathcal G)_N` est non vide, alors :

```math
\nu_{B,\mathcal F\cup\mathcal G,N}
=
\alpha_N\nu_{B,\mathcal F,N}
+(1-\alpha_N)\nu_{B,\mathcal G,N},
```

avec :

```math
\alpha_N
=
\frac{|\mathcal F_N|}
{|\mathcal F_N|+|\mathcal G_N|}.
```

Cette identite est exacte a `N` fini.

## 4. Resultat demontre B : classes terminales pures

Pour `y\in X_B`, soit :

```math
A_y(B)=\{n:E_B(n)=y\}.
```

Si `A_y(B)\cap[1,N]` est non vide, alors :

```math
\nu_{B,A_y(B),N}=\delta_y.
```

Les fibres terminales sont donc des classes pures pour l'observation `E_B`.

Plus generalement, pour `A\subseteq X_B`, la classe :

```math
\mathcal C_A=E_B^{-1}(A)
```

verifie :

```math
\nu_{B,\mathcal C_A,N}(A)=1.
```

## 5. Resultat demontre C : pseudometrique de classes

Pour deux classes `\mathcal F,\mathcal G`, on definit :

```math
D_{B,N}(\mathcal F,\mathcal G)
=
\|\nu_{B,\mathcal F,N}-\nu_{B,\mathcal G,N}\|_{\rm TV}.
```

Alors `D_{B,N}` est une pseudometrique sur les classes ayant un echantillon
non vide a `N` :

```math
D_{B,N}(\mathcal F,\mathcal G)\ge 0,
```

```math
D_{B,N}(\mathcal F,\mathcal G)=D_{B,N}(\mathcal G,\mathcal F),
```

```math
D_{B,N}(\mathcal F,\mathcal H)
\le
D_{B,N}(\mathcal F,\mathcal G)
+D_{B,N}(\mathcal G,\mathcal H).
```

Elle est seulement une pseudometrique, car deux classes differentes peuvent
avoir la meme signature terminale.

## 6. Resultat demontre D : projection entre bornes

Pour `B_1<B_2`, on definit :

```math
\delta_{B_1,B_2}:X_{B_2}\to X_{B_1}
```

par :

```math
\delta_{B_1,B_2}(\infty)=\infty,
```

et :

```math
\delta_{B_1,B_2}(y)=E_{B_1}(y).
```

Alors :

```math
E_{B_1}
=
\delta_{B_1,B_2}\circ E_{B_2}.
```

Donc, pour toute classe `\mathcal F` :

```math
\nu_{B_1,\mathcal F,N}
=
(\delta_{B_1,B_2})_\#\nu_{B_2,\mathcal F,N}.
```

Cette identite est exacte a `N` fini.

## 7. Resultat demontre E : contraction de la distance

Pour toute application `f:X\to Y` et toutes probabilites `\mu,\nu` sur `X` :

```math
\|f_\#\mu-f_\#\nu\|_{\rm TV}
\le
\|\mu-\nu\|_{\rm TV}.
```

Applique a `f=\delta_{B_1,B_2}` :

```math
D_{B_1,N}(\mathcal F,\mathcal G)
\le
D_{B_2,N}(\mathcal F,\mathcal G).
```

Une difference entre deux classes peut donc disparaitre par projection vers
une borne plus basse, mais elle ne peut pas etre amplifiee par cette projection.

## 8. Resultat conditionnel F : passage aux limites

Si :

```math
\nu_{B,\mathcal F,N}\to\nu_{B,\mathcal F}
```

et :

```math
\nu_{B,\mathcal G,N}\to\nu_{B,\mathcal G},
```

alors :

```math
D_{B,N}(\mathcal F,\mathcal G)
\to
\|\nu_{B,\mathcal F}-\nu_{B,\mathcal G}\|_{\rm TV}.
```

Si les limites existent a `B_2`, alors elles existent par projection a toute
borne `B_1<B_2` et :

```math
\nu_{B_1,\mathcal F}
=
(\delta_{B_1,B_2})_\#\nu_{B_2,\mathcal F}.
```

## 9. Resultat demontre G : critere par densites naturelles

Pour `y\in X_B`, on note encore :

```math
A_y(B)=\{n:E_B(n)=y\}.
```

Supposons que `X_B` soit fini, que `\mathcal F` ait une densite naturelle
positive :

```math
d(\mathcal F)>0,
```

et que chaque intersection :

```math
\mathcal F\cap A_y(B)
```

ait une densite naturelle :

```math
d_y(\mathcal F,B)
=
d(\mathcal F\cap A_y(B)).
```

Alors la loi terminale limite existe et vaut :

```math
\nu_{B,\mathcal F}(y)
=
\frac{d_y(\mathcal F,B)}{d(\mathcal F)}.
```

La preuve est immediate :

```math
\nu_{B,\mathcal F,N}(y)
=
\frac{| \mathcal F\cap A_y(B)\cap[1,N]|/N}
{|\mathcal F\cap[1,N]|/N}
\longrightarrow
\frac{d_y(\mathcal F,B)}{d(\mathcal F)}.
```

Ce critere est un vrai theoreme conditionnel de densite. Il deplace le verrou :
il ne faut plus seulement observer une convergence numerique ; il faut prouver
les densites des intersections `\mathcal F\cap A_y(B)`.

## 10. Neutralite et biais de classes

Si la loi globale `\nu_{B,\mathbb N}` existe et si :

```math
d(\mathcal F\cap A_y(B))
=
d(\mathcal F)\,d(A_y(B))
```

pour tout `y`, alors :

```math
\nu_{B,\mathcal F}
=
\nu_{B,\mathbb N}.
```

La classe `\mathcal F` est alors terminalement neutre.

Plus generalement, si des poids `w_y(\mathcal F)` verifient :

```math
d(\mathcal F\cap A_y(B))
=
w_y(\mathcal F)\,d(\mathcal F)\,d(A_y(B)),
```

alors :

```math
\nu_{B,\mathcal F}(y)
=
\frac{w_y(\mathcal F)\nu_{B,\mathbb N}(y)}
{\sum_z w_z(\mathcal F)\nu_{B,\mathbb N}(z)}.
```

Cette formule donne une definition propre des biais terminaux.

## 11. Application aux motifs premiers

Soit un motif admissible :

```math
H=\{0,h_1,\ldots,h_k\}.
```

On pose :

```math
\mathcal P_H
=
\{p:p+h\text{ est premier pour tout }h\in H\}.
```

Si, pour chaque `y\in X_B`, on a une asymptotique locale :

```math
|\{p\le x:p\in\mathcal P_H,\ E_B(p)=y\}|
\sim
c_y(B,H)\frac{x}{(\log x)^{|H|}},
```

avec :

```math
C_B(H)=\sum_{y\in X_B}c_y(B,H)>0,
```

alors :

```math
\nu_{B,\mathcal P_H,N}(y)
\to
\frac{c_y(B,H)}{C_B(H)}.
```

Cela est un theoreme conditionnel elementaire : la profondeur est dans
l'asymptotique locale, pas dans le quotient.

## 12. Filtrage terminal et coefficient conditionnel

Soit `A\subseteq X_B`. Le filtre terminal est :

```math
M_A(n)=1
\quad\Longleftrightarrow\quad
E_B(n)\in A.
```

Pour un motif premier `H`, si la loi terminale limite existe :

```math
\rho_A(H)
=
\nu_{B,\mathcal P_H}(A).
```

Si en plus Hardy-Littlewood donne :

```math
|\mathcal P_H\cap[1,x]|
\sim
S(H)\frac{x}{(\log x)^{|H|}},
```

alors le sous-filtre terminal verifie conditionnellement :

```math
|\{p\le x:p\in\mathcal P_H,\ E_B(p)\in A\}|
\sim
S(H)\rho_A(H)\frac{x}{(\log x)^{|H|}}.
```

Pour les jumeaux, `S(H)=2C_2`, donc :

```math
C_{\rm Montmory}
=
2C_2\,\nu_{B,\rm twin}(A).
```

Cette formule est une normalisation conditionnelle. Elle ne prouve ni
Hardy-Littlewood, ni l'existence de la loi terminale des jumeaux.

## 13. Ce qui est vraiment demontre

Les resultats demontres forment deja une petite mathematique de classes :

```math
\boxed{
\mathcal F
\longmapsto
\nu_{B,\mathcal F,N}
}
```

avec :

```math
\boxed{
(\mathcal F,\mathcal G)
\longmapsto
D_{B,N}(\mathcal F,\mathcal G).
}
```

Cette mathematique est finie, exacte, projective et stable par contraction TV.

La nouveaute profonde, encore ouverte, serait de prouver l'existence des lois :

```math
\nu_{B,\mathcal F,N}\to\nu_{B,\mathcal F}
```

pour des classes arithmetiques non triviales.
