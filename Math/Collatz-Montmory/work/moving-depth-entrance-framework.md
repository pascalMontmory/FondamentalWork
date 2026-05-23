# Cadre a profondeur mobile pour les mesures d'entree Collatz

Date: 2026-05-23  
Statut: correction mathematique et reformulation du verrou

## 1. Correction importante

Un point doit etre fixe clairement.

Pour une borne `B`, un terminal `y<=B` et une profondeur fixe `k`, l'ensemble:

```math
\mathcal A_B^{(k)}(y)
```

est fini. En effet, il est obtenu par les mots inverses de longueur `k` appliques a `y`, et il y a au plus `2^k` mots.

Donc, pour la population des entiers ordinaires:

```math
\#(\mathcal A_B^{(k)}(y)\cap[1,x])\le 2^k,
```

et par consequent, pour `k` fixe:

```math
\frac{\#(\mathcal A_B^{(k)}(y)\cap[1,x])}{x}
\longrightarrow0.
```

La meme obstruction vaut pour les premiers ou les jumeaux: a profondeur fixe, les cylindres inverses ne peuvent pas porter une densite positive.

Conclusion:

```text
La loi d'entree ne peut pas etre obtenue par des densites fixes en k.
Elle doit etre formulee avec des profondeurs k qui croissent avec log x.
```

## 2. Decomposition exacte par profondeur

On garde la decomposition exacte:

```math
\mathcal A_B(y)=\bigsqcup_{k\ge0}\mathcal A_B^{(k)}(y).
```

Pour une population `\mathcal P`, la mesure empirique d'entree est:

```math
\nu_{B,x}^{\mathcal P}(y)
=
\frac{\#(\mathcal P\cap\mathcal A_B(y)\cap[1,x])}
{\#(\mathcal P\cap[1,x])}.
```

Donc:

```math
\nu_{B,x}^{\mathcal P}(y)
=
\sum_{k\ge0}
\frac{\#(\mathcal P\cap\mathcal A_B^{(k)}(y)\cap[1,x])}
{\#(\mathcal P\cap[1,x])}.
```

Mais la masse utile vient de `k` dependant de `x`.

## 3. Profondeur typique

Sous l'heuristique de derive Collatz acceleree:

```math
d=1-\frac12\log_2 3,
```

on attend:

```math
\tau_B(n)\approx\frac{\log_2 n}{d}.
```

Donc, pour `n<=x`, la profondeur pertinente est de taille:

```math
k\asymp\frac{\log_2 x}{d}.
```

La bonne variable n'est donc pas `k` fixe, mais une profondeur centree ou rescalee.

## 4. Mesure jointe entree-profondeur

On definit la mesure empirique jointe:

```math
\mu_{B,x}^{\mathcal P}(y,k)
=
\frac{\#\{n\le x:n\in\mathcal P,
E_B(n)=y,
\tau_B(n)=k\}}
{\#\{n\le x:n\in\mathcal P\}}.
```

Alors:

```math
\nu_{B,x}^{\mathcal P}(y)=\sum_{k\ge0}\mu_{B,x}^{\mathcal P}(y,k).
```

This identity is exact.

## 5. Fenetre mobile de profondeur

Pour une fenetre `I_x subset N`, on pose:

```math
\nu_{B,x}^{\mathcal P}(y;I_x)
=
\sum_{k\in I_x}\mu_{B,x}^{\mathcal P}(y,k).
```

Une fenetre naturelle est:

```math
I_x(a,b)=
\left\{k:
 a\le k-\frac{\log_2 x}{d}\le b
\right\}.
```

Une autre est une fenetre rescalee:

```math
I_x(\alpha,\beta)=
\left\{k:
 \alpha\log x\le k\le \beta\log x
\right\}.
```

La loi d'entree limite devrait etre etudiee par ces fenetres mobiles, pas par `k` fixe.

## 6. Formulation correcte de l'hypothese d'entree

Une hypothese robuste doit porter sur la famille de mesures:

```math
\mu_{B,x}^{\mathcal P}(y,k).
```

Par exemple, on peut demander l'existence d'une loi limite centree:

```math
\left(E_B(n),\ \tau_B(n)-\frac{\log_2 n}{d}\right)
\Longrightarrow
\Lambda_B^{\mathcal P},
```

pour `n` tire dans `\mathcal P` jusqu'a `x`.

Si cette limite existe, alors:

```math
\nu_B^{\mathcal P}(y)
=
\Lambda_B^{\mathcal P}(\{y\}\times\mathbb R).
```

C'est la bonne forme de l'hypothese.

## 7. Formulation par score normalise

Le score utilise:

```math
K_B(n)=\frac{\log_2 n}{\tau_B(n)}.
```

Le score centre-log est:

```math
Z_B(n)=\left(K_B(n)-d\right)\log_2 n.
```

Ecrivons:

```math
\tau_B(n)=\frac{L}{d}+u,
\qquad L=\log_2 n.
```

Alors:

```math
K_B(n)=\frac{L}{L/d+u}
=d\left(1+\frac{du}{L}\right)^{-1}.
```

Donc:

```math
Z_B(n)
=(K_B(n)-d)L
=-d^2u+O\left(\frac{u^2}{L}\right),
```

quand `u=o(L)`.

Ainsi, une loi limite de `Z_B` correspond essentiellement a une loi limite de la fluctuation:

```math
u_B^{time}(n)=\tau_B(n)-\frac{\log_2 n}{d}.
```

## 8. Nouveau verrou mathematique

Le verrou n'est plus:

```text
prouver des densites fixes des cylindres A_B^(k)(y)
```

car elles sont nulles a `k` fixe.

Le verrou correct est:

```text
prouver une loi limite jointe de l'entree terminale et de la fluctuation du temps d'arret.
```

Formule cible:

```math
\left(E_B(n),\ \tau_B(n)-\frac{\log_2 n}{d}\right)
\Longrightarrow
\Lambda_B^{\mathcal P}.
```

Pour les paires:

```math
\left(E_B(p),E_B(p+2),
\tau_B(p)-\frac{\log_2 p}{d},
\tau_B(p+2)-\frac{\log_2(p+2)}{d}
\right)
\Longrightarrow
\Lambda_B^{(2)}.
```

## 9. Relation avec les bornes

Pour `B_1<B_2`, la correction exacte reste:

```math
\tau_{B_1}(n)=\tau_{B_2}(n)+\Delta_{B_1,B_2}(n).
```

Donc les fluctuations centrees satisfont:

```math
\left(\tau_{B_1}(n)-\frac{\log_2 n}{d}\right)
=
\left(\tau_{B_2}(n)-\frac{\log_2 n}{d}\right)
+\Delta_{B_1,B_2}(n).
```

Si la loi jointe de:

```math
(E_{B_2}(n),\tau_{B_2}(n)-\log_2 n/d)
```

existe, alors la loi pour `B_1` est le push-forward par:

```math
(y,u)\mapsto
\left(E_{B_1}(y),\ u+\delta_{B_1,B_2}(y)\right),
```

avec `y=E_{B_2}(n)`.

C'est une formulation propre des classes de bornes.

## 10. Theoreme conditionnel corrige

### Theoreme

Fixons une population `\mathcal P` et une borne `B`. Supposons que la loi jointe centree existe:

```math
\left(E_B(n),\ \tau_B(n)-\frac{\log_2 n}{d}\right)
\Longrightarrow
\Lambda_B^{\mathcal P}.
```

Alors:

1. la mesure d'entree limite existe:

```math
\nu_B^{\mathcal P}(y)
=
\Lambda_B^{\mathcal P}(\{y\}\times\mathbb R);
```

2. si `u^2/log_2 n -> 0` en probabilite, le score normalise converge en loi vers le push-forward:

```math
Z_B(n)\Longrightarrow (-d^2\pi_2)_*\Lambda_B^{\mathcal P},
```

ou `\pi_2(y,u)=u` est la projection sur la fluctuation temporelle.

### Sens

Ce theoreme donne la bonne route: prouver une loi limite de fluctuation temporelle, pas sommer des densites de profondeurs fixes.

## 11. Consequence pour la nouveaute du programme

Les arbres inverses Collatz sont classiques. La reformulation potentiellement originale est:

```text
utiliser la loi jointe mobile (entree terminale, fluctuation du temps d'arret)
pour definir les classes de bornes et les queues normalisees.
```

C'est plus precis que la formulation precedente et evite l'erreur des cylindres fixes.

## 12. Statut

Verifie:

1. les cylindres fixes ont densite nulle dans les entiers;
2. la decomposition par profondeur est exacte;
3. la profondeur pertinente croit comme `log x` sous l'heuristique de derive;
4. la relation entre `Z_B` et la fluctuation `u=tau_B-log_2(n)/d` est une expansion algebrique.

Non verifie:

1. existence de la loi limite `Lambda_B`;
2. controle probabiliste de `u^2/log n`;
3. version sur les premiers;
4. version jointe sur les jumeaux;
5. lien final avec `C_Montmory`.

## 13. Conclusion

La bonne etude mathematique n'est pas une densite de cylindres inverses fixes, mais une loi limite a profondeur mobile:

```math
\boxed{
\left(E_B(n),\ \tau_B(n)-\frac{\log_2 n}{d}\right)
\Longrightarrow
\Lambda_B^{\mathcal P}
}
```

C'est ce verrou qui doit etre attaque pour donner une base theorique aux bornes et au score normalise.