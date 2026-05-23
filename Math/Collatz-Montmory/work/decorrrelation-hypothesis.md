# Hypothese de decorrelation Montmory

Date: 2026-05-23  
Statut: hypothese de recherche falsifiable

## 1. Objet

Cette note formule une hypothese precise reliant la dynamique Montmory empirique et les facteurs locaux de Hardy-Littlewood.

Elle ne prouve pas `C_Montmory`. Elle donne une cible mathematique claire pour les tests.

## 2. Donnees

Pour chaque borne `X`, on fixe:

- un ensemble de graines `G_X`;
- une profondeur de trajectoire `R(X)`;
- un seuil de modules `Q(X)`;
- des modules premiers impairs `3 <= q <= Q(X)`.

Pour chaque `q`, on calcule la mesure empirique:

```math
\mu_{q;X,R}(a)=
\frac{1}{|G_X|(R+1)}
\#\{(n,t):n\in G_X,0\le t\le R,T^t(n)\equiv a\pmod q\}.
```

Puis:

```math
\Sigma_{q;X,R}=1-\mu_{q;X,R}(0)-\mu_{q;X,R}(-2),
```

```math
B_{q;X,R}=\frac{\Sigma_{q;X,R}}{1-2/q}.
```

## 3. Produit de biais locaux

On definit:

```math
B_M(X)=\prod_{3\le q\le Q(X)}B_{q;X,R(X)}.
```

et:

```math
C_{dyn}(X)=2C_2B_M(X).
```

La cible Montmory est:

```math
B_*=\frac{0.107983974916}{2C_2}
\approx0.08178598968002706089.
```

## 4. Hypothese D1: convergence des biais

Il existe des choix fixes de `G_X`, `R(X)` et `Q(X)`, definis avant test, tels que:

```math
B_M(X)\to B_*
```

quand `X -> infinity`.

Si cette hypothese est vraie, alors:

```math
C_{dyn}(X)\to0.107983974916.
```

## 5. Hypothese D2: stabilite hors echantillon

Pour une suite de bornes d'entrainement `X_train` et de test `X_test>X_train`, les parametres fixes sur `X_train` doivent satisfaire:

```math
B_M(X_test)-B_M(X_train)\to0.
```

Une derive systematique invalide l'interpretation predictive.

## 6. Hypothese D3: non-trivialite face aux controles

Soit `G_X^{ctrl}` un ensemble de controle, par exemple les entiers impairs ou des paires impaires non filtrees. On calcule:

```math
B_M^{ctrl}(X).
```

Le signal Montmory est non trivial seulement si:

```math
B_M(X)-B_M^{ctrl}(X)
```

ne s'annule pas par simple effet de la dynamique Collatz commune.

## 7. Criteres de rejet

Rejeter l'hypothese si:

1. `B_M(X)` ne s'approche pas de `B_*`;
2. `B_M(X)` varie fortement avec `R` ou `Q` sans plateau;
3. quelques petits modules dominent tout le produit;
4. le controle produit la meme limite;
5. la cible n'apparait qu'apres changement de parametres post-test.

## 8. Theoreme conditionnel associe

Si Hardy-Littlewood jumeaux est vraie et si l'hypothese D1 est vraie, alors l'estimateur dynamique:

```math
\widehat\pi_2^{dyn}(x)
=
2C_2B_M(x)\frac{x}{\log^2x}
```

possede le coefficient limite:

```math
0.107983974916.
```

Cette conclusion reste conditionnelle aux hypotheses; elle ne prouve pas la constante.