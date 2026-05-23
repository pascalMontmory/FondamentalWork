# Programme de preuve pour les lois terminales Collatz-Montmory

> Statut : programme de preuve non valide.
>
> Verifie dans ce document : definitions, projectivite finie, contraction de la distance en variation totale par projection, et consequences conditionnelles algebriques.
>
> Non verifie : existence generale des limites terminales, loi limite `Lambda_B`, loi terminale pour les premiers ou les jumeaux, resonance specifique de `B = 89`.

## 0. Objet et verrou mathematique

Ce document formalise un programme de preuve autour des mesures d'entree terminale de Collatz. L'objectif est de passer d'observations numeriques sur des bornes terminales a une theorie probabiliste structuree des lois limites :

```math
\nu_{B,\mathcal F,N} \longrightarrow \nu_{B,\mathcal F}.
```

Ici :

- `B` est une borne terminale ;
- `\mathcal F \subset \mathbb N` est une famille arithmetique ;
- `\nu_{B,\mathcal F,N}` est la mesure empirique des points d'entree terminale sous la borne `B`.

Le verrou mathematique reel est l'existence des limites :

```math
\nu_{B,\mathcal F,N} \to \nu_{B,\mathcal F}
```

pour des familles arithmetiques non triviales. La structure projective, elle, est exacte au niveau fini.

## 1. Carte acceleree de Collatz

On considere la carte acceleree :

```math
T(n)=
\begin{cases}
n/2,& n\equiv 0\pmod 2,\\
(3n+1)/2,& n\equiv 1\pmod 2.
\end{cases}
```

Pour une borne `B \ge 1`, on definit le temps d'entree :

```math
\tau_B(n)=\inf\{t\ge 0:T^t(n)\le B\}.
```

Si l'orbite ne rencontre jamais `[1,B]`, on pose :

```math
\tau_B(n)=\infty.
```

L'entree terminale est :

```math
E_B(n)=
\begin{cases}
T^{\tau_B(n)}(n),& \tau_B(n)<\infty,\\
\infty,& \tau_B(n)=\infty.
\end{cases}
```

Ainsi :

```math
E_B(n)\in X_B=\{1,\ldots,B\}\cup\{\infty\}.
```

L'ajout de `\infty` permet de formuler les resultats sans supposer la conjecture de Collatz globale.

## 2. Mesure terminale empirique

Soit `\mathcal F\subset\mathbb N` une famille arithmetique. On pose :

```math
\mathcal F_N=\mathcal F\cap[1,N].
```

Si `\mathcal F_N\ne\varnothing`, on definit la mesure uniforme empirique :

```math
\mu_{\mathcal F,N}
=
\frac{1}{|\mathcal F_N|}
\sum_{n\in\mathcal F_N}\delta_n.
```

La mesure d'entree terminale sous la borne `B` est :

```math
\nu_{B,\mathcal F,N}
=
(E_B)_\#\mu_{\mathcal F,N}.
```

Autrement dit, pour `y\in X_B`,

```math
\nu_{B,\mathcal F,N}(y)
=
\frac{
|\{n\in\mathcal F_N:E_B(n)=y\}|
}{
|\mathcal F_N|
}.
```

La question centrale est :

```math
\nu_{B,\mathcal F,N}
\overset{?}{\longrightarrow}
\nu_{B,\mathcal F}
\qquad (N\to\infty).
```

## 3. Theoreme exact de projectivite terminale

Soient `B_1 < B_2`. On definit la projection terminale :

```math
\delta_{B_1,B_2}:X_{B_2}\to X_{B_1}
```

par :

```math
\delta_{B_1,B_2}(\infty)=\infty,
```

et, pour `y\in\{1,\ldots,B_2\}`,

```math
\delta_{B_1,B_2}(y)=E_{B_1}(y).
```

### Proposition 3.1 : projectivite finie

Pour tout `n\in\mathbb N`,

```math
E_{B_1}(n)
=
\delta_{B_1,B_2}(E_{B_2}(n)).
```

En consequence, pour toute famille `\mathcal F` telle que `\mathcal F_N\ne\varnothing`,

```math
\nu_{B_1,\mathcal F,N}
=
(\delta_{B_1,B_2})_\#\nu_{B_2,\mathcal F,N}.
```

### Preuve

Si `E_{B_2}(n)=\infty`, l'orbite de `n` ne rencontre jamais `[1,B_2]`. Comme `[1,B_1]\subset[1,B_2]`, elle ne rencontre jamais `[1,B_1]`, donc `E_{B_1}(n)=\infty`.

Si `E_{B_2}(n)=y\le B_2`, alors l'orbite de `n` atteint d'abord `y` sous la borne `B_2`. Pour atteindre ensuite la borne plus basse `B_1`, il suffit de poursuivre l'orbite a partir de `y`. Donc l'entree sous `B_1` est exactement `E_{B_1}(y)`. La relation de push-forward suit en appliquant cette identite point par point sous la mesure empirique.

## 4. Programme de preuve

Le programme se decompose en trois niveaux croissants de difficulte.

## Niveau A : classes residuelles

Le premier objectif raisonnable est de traiter les familles arithmetiques simples :

```math
\mathcal F_{a,q}=\{n\in\mathbb N:n\equiv a\pmod q\}.
```

On cherche a prouver l'existence de :

```math
\nu_{B,a,q}
=
\lim_{N\to\infty}\nu_{B,\mathcal F_{a,q},N}.
```

### Objectif A1 : existence

Pour une borne fixee `B`, prouver que pour tout `a,q` admissible :

```math
\nu_{B,\mathcal F_{a,q},N}
\longrightarrow
\nu_{B,a,q}.
```

### Objectif A2 : compatibilite projective

Si les limites existent, la projectivite finie implique automatiquement :

```math
\nu_{B_1,a,q}
=
(\delta_{B_1,B_2})_\#\nu_{B_2,a,q}.
```

### Objectif A3 : biais residuel

Comparer :

```math
\nu_{B,a,q}
```

a la loi terminale globale :

```math
\nu_{B,\mathbb N}.
```

Un premier resultat possible serait de montrer que certaines classes residuelles ne biaisent pas la loi terminale :

```math
\nu_{B,a,q}=\nu_{B,\mathbb N},
```

ou bien qu'elles la biaisent par des poids locaux explicites.

## Niveau B : familles a densite naturelle

Soit `\mathcal F\subset\mathbb N` une famille possedant une densite naturelle positive :

```math
d(\mathcal F)
=
\lim_{N\to\infty}\frac{|\mathcal F\cap[1,N]|}{N}
>0.
```

L'objectif est de comprendre quand la loi terminale existe :

```math
\nu_{B,\mathcal F}
=
\lim_{N\to\infty}\nu_{B,\mathcal F,N}.
```

### Hypothese B1 : equidistribution relative dans les fibres terminales

Pour chaque `y\in X_B`, on considere la fibre terminale :

```math
A_y(B)=\{n:E_B(n)=y\}.
```

Une condition suffisante naturelle est :

```math
\lim_{N\to\infty}
\frac{|A_y(B)\cap\mathcal F\cap[1,N]|}
{|A_y(B)\cap[1,N]|}
=
d(\mathcal F)
```

pour toute fibre de densite terminale positive. Les fibres de densite nulle doivent etre traitees separement.

Si cette equidistribution relative vaut pour tout `y` de masse positive, et si la loi globale `\nu_{B,\mathbb N}` existe, alors :

```math
\nu_{B,\mathcal F}
=
\nu_{B,\mathbb N}.
```

### Objectif B2 : familles biaisees

Si l'egalite precedente echoue, on cherche des poids locaux :

```math
w_y(\mathcal F)
```

tels que :

```math
\nu_{B,\mathcal F}(y)
=
\frac{w_y(\mathcal F)\nu_{B,\mathbb N}(y)}
{\sum_{z\in X_B}w_z(\mathcal F)\nu_{B,\mathbb N}(z)}.
```

Cela donnerait une theorie des biais terminaux.

## Niveau C : premiers et jumeaux

Le niveau le plus difficile concerne les familles arithmetiques fines :

```math
\mathcal P=\{p:p\text{ premier}\},
```

et :

```math
\mathcal T=\{p:p,p+2\text{ premiers}\}.
```

On definit :

```math
\nu_{B,\rm prime,N}(y)
=
\frac{
|\{p\le N:p\text{ premier},\ E_B(p)=y\}|
}{
|\{p\le N:p\text{ premier}\}|
},
```

et :

```math
\nu_{B,\rm twin,N}(y)
=
\frac{
|\{p\le N:p,p+2\text{ premiers},\ E_B(p)=y\}|
}{
|\{p\le N:p,p+2\text{ premiers}\}|
}.
```

L'objectif est de prouver ou formuler conditionnellement :

```math
\nu_{B,\rm prime,N}\to\nu_{B,\rm prime},
```

et :

```math
\nu_{B,\rm twin,N}\to\nu_{B,\rm twin}.
```

## 5. Hypothese Hardy-Littlewood terminale

Pour les premiers jumeaux, on peut formuler une hypothese conditionnelle.

Pour chaque `y\in X_B`, soit :

```math
A_y(B)=\{n:E_B(n)=y\}.
```

On suppose que la densite relative parmi les debuts de paires jumelles existe :

```math
\rho_y^{\rm twin}(B)
=
\lim_{N\to\infty}
\frac{
|\{p\le N:p,p+2\text{ premiers},\ p\in A_y(B)\}|
}{
|\{p\le N:p,p+2\text{ premiers}\}|
}.
```

Alors :

```math
\nu_{B,\rm twin}(y)=\rho_y^{\rm twin}(B).
```

Si de plus les poids sont donnes par une loi locale explicite :

```math
\rho_y^{\rm twin}(B)
=
\frac{w_y}{\sum_{z\in X_B}w_z},
```

alors la loi terminale des jumeaux est explicite.

## 6. Theoreme conditionnel de loi terminale pour les jumeaux

### Enonce

Supposons que, pour chaque `y\in X_B`, l'asymptotique locale existe :

```math
|\{p\le N:p,p+2\text{ premiers},\ E_B(p)=y\}|
\sim
c_y(B)\frac{N}{\log^2 N}.
```

Supposons aussi que :

```math
C_B=\sum_{y\in X_B}c_y(B)
```

soit strictement positif et fini. Comme `X_B` est fini, cette somme ne pose pas de probleme de convergence.

Alors :

```math
\nu_{B,\rm twin,N}
\longrightarrow
\nu_{B,\rm twin},
```

avec :

```math
\nu_{B,\rm twin}(y)
=
\frac{c_y(B)}{C_B}.
```

### Preuve

Par definition :

```math
\nu_{B,\rm twin,N}(y)
=
\frac{
|\{p\le N:p,p+2\text{ premiers},\ E_B(p)=y\}|
}{
|\{p\le N:p,p+2\text{ premiers}\}|
}.
```

Sous l'hypothese locale :

```math
|\{p\le N:p,p+2\text{ premiers},\ E_B(p)=y\}|
\sim
c_y(B)\frac{N}{\log^2N}.
```

En sommant sur `y\in X_B`, on obtient :

```math
|\{p\le N:p,p+2\text{ premiers}\}|
\sim
C_B\frac{N}{\log^2N}.
```

Donc :

```math
\nu_{B,\rm twin,N}(y)
\to
\frac{c_y(B)}{C_B}.
```

Remarque : la conjecture de Hardy-Littlewood globale n'est pas suffisante a elle seule pour prouver cet enonce. Il faut des asymptotiques locales sur les fibres terminales `A_y(B)`. Inversement, ces asymptotiques locales impliquent deja une asymptotique globale pour les jumeaux, avec constante `C_B`.

## 7. Resonance terminale

Soient deux familles arithmetiques `\mathcal F,\mathcal G`. Si les lois terminales existent, on definit :

```math
D_B(\mathcal F,\mathcal G)
=
\|\nu_{B,\mathcal F}-\nu_{B,\mathcal G}\|_{\rm TV}.
```

On dit que `B` est une resonance terminale entre `\mathcal F` et `\mathcal G` si :

```math
D_B(\mathcal F,\mathcal G)>0,
```

et si les distances empiriques convergent vers cette valeur positive :

```math
D_{B,N}(\mathcal F,\mathcal G)
=
\|\nu_{B,\mathcal F,N}-\nu_{B,\mathcal G,N}\|_{\rm TV}
\longrightarrow
D_B(\mathcal F,\mathcal G)>0.
```

Pour les jumeaux, le test naturel est :

```math
D_B({\rm twin},{\rm control})>0.
```

Le diagnostic computationnel actuel indique que `B=89` n'est pas valide comme resonance arithmetique specifique aux jumeaux dans les tests deja effectues.

## 8. Principe de contraction des resonances

Si `B_1<B_2`, alors :

```math
\nu_{B_1,\mathcal F}
=
(\delta_{B_1,B_2})_\#\nu_{B_2,\mathcal F},
```

et :

```math
\nu_{B_1,\mathcal G}
=
(\delta_{B_1,B_2})_\#\nu_{B_2,\mathcal G}.
```

La variation totale diminue par image directe :

```math
\|f_\#\mu-f_\#\nu\|_{\rm TV}
\le
\|\mu-\nu\|_{\rm TV}.
```

Donc :

```math
D_{B_1}(\mathcal F,\mathcal G)
\le
D_{B_2}(\mathcal F,\mathcal G).
```

Cela signifie qu'une resonance terminale peut etre detruite par projection vers une borne plus basse.

```math
\boxed{
\text{Une resonance doit etre cherchee a la bonne echelle de borne.}
}
```

## 9. Programme experimental associe

Les scripts ci-dessous sont des scripts proposes. Ils ne sont pas encore des preuves mathematiques.

### Script 1 : lois terminales par classes residuelles

```text
scripts/test_terminal_measures_residue_classes.py
```

Objectif :

```math
\nu_{B,a,q,N}
```

pour differents `a,q,B,N`, avec estimation de convergence.

### Script 2 : lois terminales des premiers

```text
scripts/test_terminal_measures_primes.py
```

Comparer :

```math
\nu_{B,\rm prime,N}
```

a :

```math
\nu_{B,\mathbb N,N}
```

et aux controles.

### Script 3 : lois terminales des jumeaux

```text
scripts/test_terminal_measures_twins.py
```

Comparer :

```math
\nu_{B,\rm twin,N}
```

a :

```math
\nu_{B,\rm prime,N},
\quad
\nu_{B,\rm odd,N},
\quad
\nu_{B,\mathbb N,N}.
```

### Script 4 : projectivite empirique

```text
scripts/test_terminal_projectivity.py
```

Verifier numeriquement :

```math
\nu_{B_1,\mathcal F,N}
=
(\delta_{B_1,B_2})_\#\nu_{B_2,\mathcal F,N}.
```

Ce test doit etre exact a erreur machine pres, car il reflete la proposition de projectivite finie.

### Script 5 : resonances terminales

```text
scripts/test_terminal_resonances.py
```

Calculer :

```math
D_B({\rm twin},{\rm control})
```

pour une plage de bornes `B`, et detecter les bornes ou une difference stable persiste.

## 10. Resultat mathematique vise

Le resultat ideal serait :

```math
\boxed{
\text{Pour certaines familles }\mathcal F,
\text{ les mesures }\nu_{B,\mathcal F,N}
\text{ convergent et forment un systeme projectif.}
}
```

Formellement :

```math
\nu_{B,\mathcal F,N}\to\nu_{B,\mathcal F},
```

et, pour `B_1<B_2`,

```math
\nu_{B_1,\mathcal F}
=
(\delta_{B_1,B_2})_\#\nu_{B_2,\mathcal F}.
```

Pour les jumeaux, un resultat conditionnel sous asymptotique Hardy-Littlewood terminale donnerait :

```math
\nu_{B,\rm twin}(y)
=
\frac{c_y(B)}{\sum_z c_z(B)}.
```

## 11. Conclusion

Le programme de preuve se resume ainsi :

```math
\boxed{
\textbf{Niveau A :}
\text{ prouver les lois terminales pour classes residuelles.}
}
```

```math
\boxed{
\textbf{Niveau B :}
\text{ etendre aux familles a densite naturelle.}
}
```

```math
\boxed{
\textbf{Niveau C :}
\text{ formuler et tester une loi terminale Hardy-Littlewood pour les premiers et jumeaux.}
}
```

La structure projective est deja exacte au niveau fini. Le verrou mathematique reel est donc :

```math
\boxed{
\text{Prouver l'existence des limites }\nu_{B,\mathcal F}
\text{ pour des familles arithmetiques non triviales.}
}
```
