# Mesures d'entree par arbres inverses Collatz

Date: 2026-05-23  
Statut: note mathematique de travail, formules exactes et hypotheses separees

## 1. Objectif

On veut etudier les mesures d'entree:

```math
\nu_{B,x}^{\mathcal P}(y)
=
\frac{\#\{n\le x:n\in\mathcal P,E_B(n)=y\}}
{\#\{n\le x:n\in\mathcal P\}},
\qquad 1\le y\le B.
```

Le but est de remplacer l'observation numerique par une description exacte des bassins d'entree via les arbres inverses de la transformation acceleree.

## 2. Transformation acceleree

On utilise:

```math
T(n)=
\begin{cases}
n/2, & n\equiv0\pmod2,\\
(3n+1)/2, & n\equiv1\pmod2.
\end{cases}
```

Pour `B>=1`:

```math
\tau_B(n)=\min\{t\ge0:T^t(n)\le B\},
\qquad
E_B(n)=T^{\tau_B(n)}(n).
```

## 3. Branches inverses exactes

Soit `y` un entier positif. Les preimages de `y` par `T` sont:

### Branche paire

```math
U_0(y)=2y.
```

Elle existe pour tout `y`.

### Branche impaire

On resout:

```math
\frac{3n+1}{2}=y.
```

Donc:

```math
n=\frac{2y-1}{3}.
```

Cette branche existe si et seulement si:

```math
2y-1\equiv0\pmod3,
```

c'est-a-dire:

```math
y\equiv2\pmod3.
```

Dans ce cas:

```math
U_1(y)=\frac{2y-1}{3},
```

et `U_1(y)` est automatiquement impair.

Conclusion:

```math
T^{-1}(y)=\{2y\}\cup
\begin{cases}
\left\{\frac{2y-1}{3}\right\}, & y\equiv2\pmod3,\\
\varnothing, & y\not\equiv2\pmod3.
\end{cases}
```

Cette formule est exacte.

## 4. Bassins d'entree dans une borne B

Pour `1<=y<=B`, on definit le bassin d'entree:

```math
\mathcal A_B(y)=\{n:E_B(n)=y\}.
```

Les bassins `\mathcal A_B(y)` sont disjoints. Pour tout `n` dont `\tau_B(n)` existe:

```math
n\in\bigsqcup_{1\le y\le B}\mathcal A_B(y).
```

La mesure d'entree s'ecrit donc:

```math
\nu_{B,x}^{\mathcal P}(y)
=
\frac{\#(\mathcal P\cap\mathcal A_B(y)\cap[1,x])}
{\#(\mathcal P\cap[1,x])},
```

si tous les elements de `\mathcal P\cap[1,x]` consideres ont un temps d'entree defini. Sinon, on doit ajouter explicitement une masse d'echappement.

## 5. Recursion exacte des bassins

Pour `y<=B`, le niveau zero est:

```math
\mathcal A_B^{(0)}(y)=\{y\}.
```

Pour `k>=0`, on definit:

```math
\mathcal A_B^{(k+1)}(y)
=
\{m>B:T(m)\in\mathcal A_B^{(k)}(y)\}.
```

Alors:

```math
\mathcal A_B(y)=\bigsqcup_{k\ge0}\mathcal A_B^{(k)}(y).
```

La condition `m>B` est essentielle: elle garantit que `y` est le premier point d'entree dans `\{1,\dots,B\}`.

## 6. Representation par mots inverses

Soit un mot:

```math
w=(\varepsilon_1,\dots,\varepsilon_k)\in\{0,1\}^k,
```

ou `0` designe la branche paire `U_0` et `1` la branche impaire `U_1`.

On pose:

```math
U_w=U_{\varepsilon_k}\circ\cdots\circ U_{\varepsilon_1},
```

lorsque toutes les branches impaires sont admissibles.

Tout element de `\mathcal A_B^{(k)}(y)` est de la forme:

```math
n=U_w(y)
```

pour un mot admissible `w` de longueur `k`, avec tous les intermediaires avant `y` strictement superieurs a `B`.

## 7. Forme affine-rationnelle d'un mot inverse

Soit:

```math
r(w)=\#\{j:\varepsilon_j=1\}.
```

Alors, pour tout mot admissible, il existe un entier `c_w>=0` tel que:

```math
U_w(y)=\frac{2^k y-c_w}{3^{r(w)}}.
```

La constante `c_w` est definie recursivement:

```math
c_\varnothing=0,
\qquad r(\varnothing)=0.
```

Si on ajoute une branche paire:

```math
c_{w0}=2c_w,
\qquad r(w0)=r(w).
```

Si on ajoute une branche impaire:

```math
c_{w1}=2c_w+3^{r(w)},
\qquad r(w1)=r(w)+1.
```

La condition d'admissibilite du mot est:

```math
2^k y-c_w\equiv0\pmod{3^{r(w)}}
```

avec les conditions de congruence intermediaires equivalentes a l'existence successive des branches `U_1`.

## 8. Consequence: la loi d'entree n'est pas binaire uniforme

L'arbre inverse n'est pas un arbre binaire complet. La branche impaire n'existe que lorsque l'etat courant vaut `2 mod 3`.

Donc une formule naive du type:

```math
\nu_B(y)\propto 2^{-k}
```

ou une marche inverse binaire uniforme n'est pas justifiee.

La loi d'entree depend de:

1. la frequence des mots admissibles;
2. les congruences modulo les puissances de `3`;
3. la population `\mathcal P` consideree: entiers, impairs, premiers, ou premiers jumeaux;
4. la condition de premiere entree `m>B` avant le terminal.

## 9. Operateur de transfert exact sur les ensembles

Pour un ensemble `A` d'entiers positifs, la preimage exacte est:

```math
T^{-1}(A)=2A\cup U_1(A\cap(2+3\mathbb Z)),
```

ou:

```math
2A=\{2a:a\in A\},
```

et:

```math
U_1(A\cap(2+3\mathbb Z))
=
\left\{\frac{2a-1}{3}:a\in A,
 a\equiv2\pmod3\right\}.
```

La recursion des bassins peut donc s'ecrire:

```math
\mathcal A_B^{(k+1)}(y)
=
\left(T^{-1}\mathcal A_B^{(k)}(y)\right)\cap\{B+1,B+2,
\dots\}.
```

Cette formule est exacte.

## 10. Version mesure: operateur pousse sur les densites conditionnelles

Si une population `\mathcal P` possede des densites naturelles dans les classes de congruence necessaires, on peut definir un operateur formel `\mathcal L_{\mathcal P}` par:

```math
\nu_{k+1}(A)
=
\nu_k(T(A))
```

ou plus concretement par les deux branches inverses ci-dessus avec les poids induits par les densites de `\mathcal P` dans les classes residue.

Mais ces poids ne sont pas universels. Pour les premiers, ils dependraient de l'equirepartition des premiers dans des progressions arithmetiques compatibles avec les congruences imposees par les mots inverses. Pour les jumeaux, ils dependraient d'une version Hardy-Littlewood locale dans ces memes progressions.

Donc l'operateur de transfert devient rigoureux seulement sous des hypotheses explicites de repartition arithmetique.

## 11. Hypothese d'equirepartition des cylindres inverses

Pour un mot admissible `w` et un terminal `y<=B`, definissons le cylindre inverse:

```math
C(w,y)=\{U_w(y)\}
```

comme point exact, et plus globalement le cylindre de profondeur `k`:

```math
\mathcal C_k(y)=\{U_w(y):|w|=k,
 w\text{ admissible et premiere entree en }y\}.
```

Pour une population `\mathcal P`, l'hypothese minimale de loi d'entree est l'existence de poids `\omega_{B}^{\mathcal P}(k,y)` tels que:

```math
\frac{\#(\mathcal P\cap\mathcal A_B^{(k)}(y)\cap[1,x])}
{\#(\mathcal P\cap[1,x])}
\longrightarrow
\omega_B^{\mathcal P}(k,y),
```

et:

```math
\sum_{y=1}^B\sum_{k\ge0}\omega_B^{\mathcal P}(k,y)=1.
```

Alors:

```math
\nu_B^{\mathcal P}(y)
=
\sum_{k\ge0}\omega_B^{\mathcal P}(k,y).
```

Cette formule est conditionnelle mais precise.

## 12. Loi jointe pour les jumeaux

Pour les paires, il faut deux arbres inverses couples:

```math
E_B(p)=y_0,
\qquad
E_B(p+2)=y_2.
```

On definit:

```math
\mathcal A_B^{(2)}(y_0,y_2)
=
\{p:p,p+2\text{ premiers},
E_B(p)=y_0,
E_B(p+2)=y_2\}.
```

La loi jointe est:

```math
\nu_{B,x}^{(2)}(y_0,y_2)
=
\frac{\#(\mathcal A_B^{(2)}(y_0,y_2)\cap[1,x])}{\pi_2(x)}.
```

Une preuve de convergence de `\nu_{B,x}^{(2)}` demanderait une version tres forte de Hardy-Littlewood dans les cylindres inverses Collatz, c'est-a-dire des contraintes de primalite combinees avec des contraintes de congruence issues des mots inverses.

## 13. Theoreme conditionnel d'existence de la mesure d'entree

### Theoreme

Fixons `B` et une population `\mathcal P`. Supposons que:

1. les ensembles de premiere entree `\mathcal A_B^{(k)}(y)` forment une partition de `\mathcal P` a une masse asymptotique nulle pres;
2. pour tout `k>=0` et tout `1<=y<=B`, la densite relative

```math
\omega_B^{\mathcal P}(k,y)
=
\lim_{x\to\infty}
\frac{\#(\mathcal P\cap\mathcal A_B^{(k)}(y)\cap[1,x])}
{\#(\mathcal P\cap[1,x])}
```

existe;

3. la somme des masses vaut `1`:

```math
\sum_{y=1}^B\sum_{k\ge0}\omega_B^{\mathcal P}(k,y)=1.
```

Alors la mesure d'entree limite existe et vaut:

```math
\nu_B^{\mathcal P}(y)=\sum_{k\ge0}\omega_B^{\mathcal P}(k,y).
```

### Preuve

Par definition:

```math
\nu_{B,x}^{\mathcal P}(y)
=
\sum_{k\ge0}
\frac{\#(\mathcal P\cap\mathcal A_B^{(k)}(y)\cap[1,x])}
{\#(\mathcal P\cap[1,x])},
```

avec troncature finie pour `n<=x`. Sous les hypotheses d'existence des limites et de somme totale `1`, le passage a la limite donne la formule.

## 14. Ce que cette etude apporte

Elle identifie le vrai verrou:

```text
prouver des densites relatives dans les cylindres inverses Collatz.
```

Pour les entiers ordinaires, cela renvoie a la dynamique probabiliste de Collatz. Pour les premiers, cela renvoie a l'equirepartition des premiers dans les classes imposees par les mots inverses. Pour les jumeaux, cela renvoie a Hardy-Littlewood dans ces classes.

## 15. Ce qui est verifie ici

Verifie par calcul formel:

1. les deux branches inverses exactes;
2. la condition `y=2 mod 3` pour la branche impaire;
3. la recursion des bassins d'entree;
4. la representation affine-rationnelle des mots inverses;
5. le fait que la loi d'entree est une somme de masses de cylindres, si ces masses existent.

Non verifie:

1. existence effective des densites `\omega_B^{\mathcal P}(k,y)`;
2. convergence de `\nu_{B,x}^{\mathcal P}`;
3. convergence jointe pour les jumeaux;
4. lien avec `C_Montmory`;
5. choix non calibre de `alpha`.

## 16. Conclusion

L'etude des bornes doit maintenant passer par les arbres inverses:

```math
T^{-1}(y)=\{2y\}\cup
\begin{cases}
\{(2y-1)/3\}, & y\equiv2\pmod3,\\
\varnothing, & y\not\equiv2\pmod3.
\end{cases}
```

Les mesures d'entree `\nu_B` sont des mesures sur les bassins de premiere entree `\mathcal A_B(y)`. Leur existence n'est pas automatique: elle depend de la distribution arithmetique des cylindres inverses dans la population etudiee.

C'est le prochain probleme mathematique a attaquer avant toute affirmation forte sur une classe de bornes ou sur `C_Montmory`.