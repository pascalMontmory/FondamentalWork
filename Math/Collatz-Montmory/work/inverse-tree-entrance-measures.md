# Mesures d'entree par arbres inverses Collatz

Date: 2026-05-23  
Statut: note mathematique de travail, formules exactes et correction du cadre

## 1. Objectif

Cette note decrit les branches inverses et les bassins d'entree de la transformation Collatz acceleree. Elle corrige explicitement un point important: les cylindres inverses a profondeur fixe ont une densite asymptotique nulle. La loi d'entree doit donc etre etudiee avec des profondeurs qui croissent comme `log x`.

Le cadre corrige est developpe dans:

```text
moving-depth-entrance-framework.md
```

## 2. Transformation acceleree

On utilise:

```math
T(n)=
\begin{cases}
n/2, & n\equiv0\pmod2,\\
(3n+1)/2, & n\equiv1\pmod2.
\end{cases}
```

Pour `B>=1`, lorsque le temps d'entree existe:

```math
\tau_B(n)=\min\{t\ge0:T^t(n)\le B\},
\qquad
E_B(n)=T^{\tau_B(n)}(n).
```

## 3. Branches inverses exactes

Soit `y` un entier positif.

La branche paire existe toujours:

```math
U_0(y)=2y.
```

La branche impaire est obtenue en resolvant:

```math
\frac{3n+1}{2}=y.
```

Donc:

```math
U_1(y)=\frac{2y-1}{3}.
```

Elle existe si et seulement si:

```math
y\equiv2\pmod3.
```

Ainsi:

```math
T^{-1}(y)=\{2y\}\cup
\begin{cases}
\{(2y-1)/3\}, & y\equiv2\pmod3,\\
\varnothing, & y\not\equiv2\pmod3.
\end{cases}
```

Ces formules sont exactes et classiques.

## 4. Bassins d'entree

Pour `1<=y<=B`, on definit:

```math
\mathcal A_B(y)=\{n:E_B(n)=y\}.
```

Le niveau zero est:

```math
\mathcal A_B^{(0)}(y)=\{y\}.
```

Pour `k>=0`:

```math
\mathcal A_B^{(k+1)}(y)
=
\{m>B:T(m)\in\mathcal A_B^{(k)}(y)\}.
```

Alors:

```math
\mathcal A_B(y)=\bigsqcup_{k\ge0}\mathcal A_B^{(k)}(y).
```

La condition `m>B` impose la premiere entree dans la zone terminale.

## 5. Mots inverses

Pour un mot:

```math
w=(\varepsilon_1,\dots,\varepsilon_k)\in\{0,1\}^k,
```

ou `0` designe `U_0` et `1` designe `U_1`, on pose:

```math
U_w=U_{\varepsilon_k}\circ\cdots\circ U_{\varepsilon_1},
```

lorsque toutes les branches impaires sont admissibles.

Tout element de `\mathcal A_B^{(k)}(y)` est de la forme:

```math
n=U_w(y)
```

pour un mot admissible de longueur `k`, avec condition de premiere entree.

## 6. Forme affine-rationnelle

Soit:

```math
r(w)=\#\{j:\varepsilon_j=1\}.
```

Alors, pour tout mot admissible, il existe un entier `c_w>=0` tel que:

```math
U_w(y)=\frac{2^k y-c_w}{3^{r(w)}}.
```

On peut definir `c_w` recursivement:

```math
c_\varnothing=0,
\qquad r(\varnothing)=0.
```

Ajout d'une branche paire:

```math
c_{w0}=2c_w,
\qquad r(w0)=r(w).
```

Ajout d'une branche impaire:

```math
c_{w1}=2c_w+3^{r(w)},
\qquad r(w1)=r(w)+1.
```

La condition d'integralite finale est:

```math
2^k y-c_w\equiv0\pmod{3^{r(w)}}.
```

Les conditions intermediaires encodent l'existence successive des branches `U_1`.

## 7. Correction: les profondeurs fixes ne suffisent pas

Pour `k` fixe, il y a au plus `2^k` mots de longueur `k`. Donc:

```math
\#\mathcal A_B^{(k)}(y)\le2^k.
```

En particulier:

```math
\frac{\#(\mathcal A_B^{(k)}(y)\cap[1,x])}{x}
\longrightarrow0
\qquad(x\to\infty)
```

pour tout `k` fixe.

Ainsi, une hypothese de densite positive pour chaque niveau fixe `k` serait fausse pour la population des entiers, et inadaptee pour les premiers ou les jumeaux.

La masse asymptotique vient de profondeurs `k` qui croissent avec `x`, typiquement:

```math
k\asymp\frac{\log_2 x}{d},
\qquad
 d=1-\frac12\log_2 3.
```

## 8. Mesure d'entree correcte

Pour une population `\mathcal P`, la mesure empirique d'entree reste:

```math
\nu_{B,x}^{\mathcal P}(y)
=
\frac{\#(\mathcal P\cap\mathcal A_B(y)\cap[1,x])}
{\#(\mathcal P\cap[1,x])}.
```

Mais il faut l'etudier via la mesure jointe entree-profondeur:

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

La limite doit etre formulee avec `k` mobile, pas avec `k` fixe.

## 9. Verrou mathematique corrige

Le bon verrou est l'existence d'une loi limite jointe:

```math
\left(E_B(n),\ \tau_B(n)-\frac{\log_2 n}{d}\right)
\Longrightarrow
\Lambda_B^{\mathcal P}.
```

Si cette limite existe, alors:

```math
\nu_B^{\mathcal P}(y)
=
\Lambda_B^{\mathcal P}(\{y\}\times\mathbb R).
```

Pour les jumeaux, il faudrait une version jointe:

```math
\left(E_B(p),E_B(p+2),
\tau_B(p)-\frac{\log_2 p}{d},
\tau_B(p+2)-\frac{\log_2(p+2)}{d}
\right)
\Longrightarrow
\Lambda_B^{(2)}.
```

## 10. Ce qui est verifie ici

Verifie par calcul formel:

1. les deux branches inverses exactes;
2. la condition `y\equiv2 mod 3` pour la branche impaire;
3. la recursion des bassins d'entree;
4. la representation affine-rationnelle des mots inverses;
5. la densite nulle des niveaux fixes `k` dans les entiers.

Non verifie:

1. existence de la loi limite mobile `\Lambda_B`;
2. convergence de `\nu_{B,x}^{\mathcal P}`;
3. convergence jointe pour les jumeaux;
4. lien avec `C_Montmory`;
5. choix non calibre de `alpha`.

## 11. Conclusion

Les arbres inverses Collatz sont classiques. Le point a etudier dans le cadre Montmory est la loi mobile:

```math
\boxed{
\left(E_B(n),\ \tau_B(n)-\frac{\log_2 n}{d}\right)
\Longrightarrow
\Lambda_B^{\mathcal P}
}
```

C'est cette formulation, et non les cylindres de profondeur fixe, qui peut soutenir une theorie des bornes et du score normalise.