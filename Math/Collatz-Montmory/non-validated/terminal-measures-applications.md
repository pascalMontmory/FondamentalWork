# Application directe des mesures terminales Collatz

> Statut : application mathematique et computationnelle non validee.
>
> Verifie : definitions, push-forward terminal exact, contraction TV par projection, protocole de test fini.
>
> Non verifie : existence des limites terminales, existence d'une resonance arithmetique, role special de `B=89`, valeur predictive de `C_Montmory`.

## 0. Objectif

Ce document presente l'application directe du cadre des mesures d'entree terminale pour les trajectoires de Collatz.

L'objectif n'est pas de prouver Collatz, mais de fournir un outil mathematique et computationnel propre pour tester, comparer et falsifier des signaux de type "resonance" dans differentes familles arithmetiques.

La contribution utilisable est :

```math
\text{mesure terminale}
+\text{push-forward exact}
+\text{distance mesurable}
+\text{tests de stabilite}.
```

## 1. Mesure terminale

On considere la carte acceleree de Collatz :

```math
T(n)=
\begin{cases}
n/2,& n\equiv 0 \pmod 2,\\
(3n+1)/2,& n\equiv 1 \pmod 2.
\end{cases}
```

Pour une borne `B\ge 1`, on definit le temps d'entree :

```math
\tau_B(n)=\inf\{t\ge 0:T^t(n)\le B\}.
```

Si ce temps n'existe pas, on pose :

```math
\tau_B(n)=\infty.
```

Le point d'entree terminal est :

```math
E_B(n)=
\begin{cases}
T^{\tau_B(n)}(n),&\tau_B(n)<\infty,\\
\infty,&\tau_B(n)=\infty.
\end{cases}
```

Donc :

```math
E_B(n)\in X_B=\{1,\ldots,B\}\cup\{\infty\}.
```

Cette definition evite de supposer la conjecture globale de Collatz.

Pour une famille arithmetique `\mathcal F\subseteq \mathbb N`, on definit :

```math
\mathcal F_N=\mathcal F\cap[1,N].
```

Si `\mathcal F_N\ne\varnothing`, la mesure terminale empirique est :

```math
\nu_{B,\mathcal F,N}(y)
=
\frac{
|\{n\in\mathcal F_N:E_B(n)=y\}|
}{
|\mathcal F_N|
},
\qquad y\in X_B.
```

Elle mesure la distribution des premiers points d'entree dans la zone terminale `\{1,\ldots,B\}`, avec un etat `\infty` pour les trajectoires non entrees.

## 2. Tester proprement les resonances

Avant ce cadre, dire qu'un centre comme `B=89` semblait special restait ambigu.

Avec les mesures terminales, une resonance devient une difference mesurable entre distributions :

```math
\nu_{B,\mathcal F}
\quad\text{et}\quad
\nu_{B,\mathcal G}.
```

Par exemple, pour les premiers jumeaux et un groupe de controle :

```math
D_B
=
\|\nu_{B,\mathrm{twin}}-\nu_{B,\mathrm{control}}\|_{\mathrm{TV}}.
```

Au niveau fini, on teste plutot :

```math
D_{B,N}
=
\|\nu_{B,\mathrm{twin},N}-\nu_{B,\mathrm{control},N}\|_{\mathrm{TV}}.
```

Si :

```math
D_{B,N}\to 0
```

quand `N\to\infty`, il n'y a pas de resonance specifique detectable dans ce test.

Si `D_{B,N}` reste positif et stable hors echantillon, alors il existe un candidat signal terminal arithmetique. Cela reste un diagnostic tant qu'une limite asymptotique n'est pas prouvee.

### Application pratique

Ce cadre permet de tester proprement des centres candidats :

```math
B=27,\ 31,\ 63,\ 89,\ 127,\ldots
```

et de decider s'ils correspondent a :

1. un effet reel de dynamique terminale ;
2. un artefact numerique ;
3. un effet de choix de fenetre ;
4. une resonance arithmetique specifique.

## 3. Comparaison de familles arithmetiques

Les mesures terminales permettent de comparer plusieurs familles :

```math
\mathbb N,\quad
2\mathbb N+1,\quad
\mathbb P,\quad
\{p:p,p+2\text{ premiers}\},\quad
\{n:n\equiv a\pmod q\}.
```

On peut tester :

```math
\nu_{B,\mathbb P}
\stackrel{?}{=}
\nu_{B,\mathbb N},
```

ou encore :

```math
\nu_{B,\mathrm{twin}}
\stackrel{?}{=}
\nu_{B,\mathrm{prime\ non\ twin}}.
```

La question precise devient :

```math
\boxed{
\text{La dynamique de Collatz voit-elle certaines structures arithmetiques ?}
}
```

## 4. Reduction des tests multi-bornes

Si `B_1<B_2`, on a une application terminale :

```math
\delta_{B_1,B_2}:X_{B_2}\to X_{B_1},
```

definie par :

```math
\delta_{B_1,B_2}(\infty)=\infty,
```

et, pour `y\le B_2`,

```math
\delta_{B_1,B_2}(y)=E_{B_1}(y).
```

Alors :

```math
E_{B_1}
=
\delta_{B_1,B_2}\circ E_{B_2}.
```

Donc les mesures verifient exactement, a `N` fini :

```math
\boxed{
\nu_{B_1,\mathcal F,N}
=
(\delta_{B_1,B_2})_\#\nu_{B_2,\mathcal F,N}.
}
```

Cela signifie qu'une loi terminale a une borne haute determine automatiquement toutes les lois terminales aux bornes plus basses.

### Consequence pratique

Il n'est pas necessaire de recalculer toute la dynamique pour chaque borne basse. On peut calculer a une borne `B_2`, puis projeter vers `B_1`.

Le script :

```text
Math/Collatz-Montmory/work/scripts/compute_terminal_measures.py
```

implemente cette verification de projectivite finie.

## 5. Controle d'erreur

Le push-forward contracte la distance en variation totale :

```math
\|(\delta_\#\mu)-(\delta_\#\nu)\|_{\mathrm{TV}}
\le
\|\mu-\nu\|_{\mathrm{TV}}.
```

Donc, si :

```math
\|\nu_{B_2,\mathcal F,N}-\nu_{B_2,\mathcal F}\|_{\mathrm{TV}}
\le \varepsilon(N),
```

alors :

```math
\|\nu_{B_1,\mathcal F,N}-\nu_{B_1,\mathcal F}\|_{\mathrm{TV}}
\le \varepsilon(N).
```

Les erreurs ne s'amplifient pas lorsqu'on projette vers une borne plus basse. Cela donne un outil de stabilite numerique.

## 6. Detection d'artefacts numeriques

Une "resonance" qui disparait :

1. quand `N` augmente ;
2. quand on change de borne ;
3. quand on applique la projection exacte ;
4. quand on compare a un controle approprie ;

doit etre consideree comme suspecte.

Le cadre des mesures terminales agit donc comme un filtre anti-faux-signal.

Il permet de distinguer :

```math
\boxed{\text{signal structurel}}
```

de :

```math
\boxed{\text{artefact de borne, de fenetre ou d'echantillonnage}.}
```

## 7. Protocole experimental Collatz

Le script standard ajoute au depot est :

```text
Math/Collatz-Montmory/work/scripts/compute_terminal_measures.py
```

Il produit, pour chaque borne, famille et seuil `N` :

```text
kind
family
B
N
state
count
probability
```

et, si plusieurs bornes sont donnees, des lignes de verification :

```text
kind=projection
family
B_high
B_low
tv_error
verdict
```

Avec l'option `--pairwise-tv`, il ajoute aussi des distances TV entre familles a borne fixee.

Familles supportees :

```text
all
odd
prime
twin-prime-start
prime-non-twin
mod-class
```

Sorties mathematiques :

```math
\nu_{B,\mathcal F,N},
```

```math
D_B(\mathcal F,\mathcal G),
```

```math
D_B(N_1,N_2),
```

et stabilite en `N`.

## 8. Formulation d'une conjecture testable

Le cadre permet de remplacer les conjectures floues par une conjecture precise :

```math
\boxed{
\nu_{B,\mathcal F,N}\longrightarrow \nu_{B,\mathcal F}
\quad\text{quand }N\to\infty.
}
```

### Neutralite terminale

Une famille `\mathcal F` est terminalement neutre si :

```math
\nu_{B,\mathcal F}
=
\nu_{B,\mathbb N}.
```

### Resonance terminale

Une famille `\mathcal F` est terminalement resonante si :

```math
\nu_{B,\mathcal F}
\ne
\nu_{B,\mathbb N}.
```

Ou, plus quantitativement :

```math
\|\nu_{B,\mathcal F}-\nu_{B,\mathbb N}\|_{\mathrm{TV}}>0.
```

## 9. Application au filtre Montmory

Un filtre Montmory peut etre defini par une loi terminale.

Soit :

```math
A_B\subseteq \{1,\ldots,B\}.
```

On definit :

```math
M_B(n)=1
\quad\Longleftrightarrow\quad
E_B(n)\in A_B.
```

Pour les premiers jumeaux :

```math
N_M(x)
=
\#\{p\le x:p,p+2\text{ premiers et }E_B(p)\in A_B\}.
```

Si la loi terminale des jumeaux existe, la densite relative du filtre est :

```math
\rho_M
=
\nu_{B,\mathrm{twin}}(A_B).
```

Sous une asymptotique terminale compatible Hardy-Littlewood :

```math
N_M(x)
\sim
2C_2\,\nu_{B,\mathrm{twin}}(A_B)\,
\frac{x}{(\log x)^2}.
```

Dans la convention ou `C_Montmory` designe le coefficient devant `x/(\log x)^2`, on obtient donc conditionnellement :

```math
C_{\mathrm{Montmory}}
=
2C_2\,\nu_{B,\mathrm{twin}}(A_B).
```

Dans la convention ou `C_Montmory` designe seulement la fraction relative des jumeaux conserves par le filtre, on a plutot :

```math
C_{\mathrm{Montmory}}^{\rm rel}
=
\nu_{B,\mathrm{twin}}(A_B).
```

Cette distinction de normalisation est essentielle. Sans definition explicite du filtre `A_B` et sans test hors echantillon, une valeur numerique ajustee apres coup n'a pas de signification predictive.

## 10. Integration dans le repo

Ce cadre sert a :

1. tester proprement les centres candidats ;
2. retrograder les signaux non robustes ;
3. comparer premiers, jumeaux et controles ;
4. verifier la compatibilite entre bornes ;
5. definir des filtres Montmory par masses terminales ;
6. produire des conjectures mathematiques precises ;
7. separer resultats verifies, computationnels et non valides.

Il s'integre dans :

```text
Math/Collatz-Montmory/non-validated/
```

pour les notes d'hypotheses et d'application, et dans :

```text
Math/Collatz-Montmory/work/scripts/
```

pour les scripts de diagnostic reproductibles.

## 11. Ce que cela ne fait pas

Ce cadre ne prouve pas :

```math
\text{la conjecture de Collatz}.
```

Il ne prouve pas non plus :

```math
\text{l'existence d'une infinite de premiers jumeaux}.
```

Il ne prouve pas encore l'existence de :

```math
\nu_{B,\mathcal F}
```

pour des familles arithmetiques fines.

Mais il donne un langage propre pour formuler ces questions.

## Conclusion

L'application directe des mesures terminales est :

```math
\boxed{
\text{creer un outil rigoureux de detection, validation et elimination des resonances Collatz.}
}
```

Ce cadre remplace :

```math
\text{"ce centre semble special"}
```

par :

```math
\text{"cette famille possede une loi terminale distincte avec distance stable".}
```

La partie demontree est :

```math
\boxed{
\text{mesures terminales}
+\text{push-forward exact}
+\text{contraction TV}.
}
```

La partie encore ouverte est :

```math
\boxed{
\text{existence des limites}
+\text{resonance asymptotique}
+\text{interpretation arithmetique}.}
```
