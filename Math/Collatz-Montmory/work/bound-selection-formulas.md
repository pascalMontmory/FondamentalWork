# Formules pour determiner les bornes Collatz-Montmory

Date: 2026-05-23  
Statut: note mathematique de travail, formules conditionnelles

## 1. Objectif

Cette note ne cherche pas a choisir une borne `B` par simulation. Elle formule le probleme mathematiquement.

L'idee centrale est que deux bornes `B_1 < B_2` ne different que par une correction terminale de temps d'arret. Une borne est admissible si cette correction terminale ne deforme pas la queue du score normalise.

## 2. Transformation et temps d'arret

On utilise la transformation Collatz acceleree:

```math
T(n)=
\begin{cases}
n/2, & n\equiv0\pmod2,\\
(3n+1)/2, & n\equiv1\pmod2.
\end{cases}
```

Pour une borne `B`, on definit:

```math
\tau_B(n)=\min\{t\ge0:T^t(n)\le B\}.
```

Pour une paire `(p,p+2)`:

```math
S_B(p)=\min\left(
\frac{\log_2 p}{\tau_B(p)},
\frac{\log_2(p+2)}{\tau_B(p+2)}
\right).
```

La derive moyenne du modele aleatoire accelere est:

```math
d=1-\frac12\log_2 3.
```

Le score normalise est:

```math
Z_B(p)=\left(S_B(p)-d\right)\log_2 p.
```

## 3. Correction terminale entre deux bornes

Soient deux bornes:

```math
B_1<B_2.
```

On pose:

```math
y_{B_2}(n)=T^{\tau_{B_2}(n)}(n)\le B_2.
```

La correction terminale pour descendre de `B_2` a `B_1` est:

```math
\Delta_{B_1,B_2}(n)
=\tau_{B_1}\left(y_{B_2}(n)\right).
```

Alors on a l'identite exacte:

```math
\tau_{B_1}(n)=\tau_{B_2}(n)+\Delta_{B_1,B_2}(n).
```

Cette identite est la formule cle. Elle montre que changer de borne ne modifie que la fin de trajectoire.

## 4. Effet sur le score d'un entier

Posons:

```math
L(n)=\log_2 n,
\qquad
K_B(n)=\frac{L(n)}{\tau_B(n)}.
```

Avec `B_1<B_2`, en notant:

```math
\tau=\tau_{B_2}(n),
\qquad
\Delta=\Delta_{B_1,B_2}(n),
```

on a exactement:

```math
K_{B_1}(n)
=\frac{L}{\tau+\Delta}
=K_{B_2}(n)\frac{\tau}{\tau+\Delta}.
```

Donc:

```math
K_{B_1}(n)-K_{B_2}(n)
=-\frac{L\Delta}{\tau(\tau+\Delta)}.
```

Si `\tau` est grand et `\Delta` borne, alors:

```math
K_{B_1}(n)-K_{B_2}(n)
=-\frac{L\Delta}{\tau^2}+O\left(\frac{L\Delta^2}{\tau^3}\right).
```

Sous l'heuristique:

```math
\tau_B(n)\sim\frac{\log_2 n}{d},
```

on obtient:

```math
K_{B_1}(n)-K_{B_2}(n)
\approx -\frac{d^2\Delta_{B_1,B_2}(n)}{\log_2 n}.
```

## 5. Effet sur le score normalise

Comme:

```math
Z_B(n)=(K_B(n)-d)\log_2 n,
```

la formule precedente donne:

```math
Z_{B_1}(n)-Z_{B_2}(n)
\approx -d^2\Delta_{B_1,B_2}(n).
```

Plus precisement, si:

```math
\tau_{B_2}(n)=\frac{L}{d}+r(n),
```

alors:

```math
Z_{B_1}(n)-Z_{B_2}(n)
= -d^2\Delta_{B_1,B_2}(n)
+O\left(\frac{|r(n)|\Delta_{B_1,B_2}(n)+\Delta_{B_1,B_2}(n)^2}{L}\right).
```

Cette formule explique pourquoi une bande de bornes peut exister: si la correction terminale `\Delta` reste bornee et stable en distribution, changer `B` translate surtout le score `Z_B` par une quantite bornee.

## 6. Definition formelle d'une bande admissible

Fixons une densite cible:

```math
\rho\in(0,1).
```

Pour une population `P` de nombres premiers ou de paires de jumeaux, soit `F_B` la loi limite conjecturale de `Z_B`:

```math
Z_B \Rightarrow F_B.
```

La queue associee au seuil `\alpha` est:

```math
Q_B(\alpha)=1-F_B(\alpha).
```

Une borne `B` est admissible pour la densite `\rho` s'il existe un seuil `\alpha_B` tel que:

```math
Q_B(\alpha_B)=\rho.
```

Deux bornes `B_1<B_2` sont equivalentes a tolerance `\varepsilon` si:

```math
\left|Q_{B_1}(\alpha_{B_2})-\rho\right|\le\varepsilon.
```

Avec la correction terminale, une condition suffisante heuristique est:

```math
\mathbb P\left(
\left|d^2\Delta_{B_1,B_2}-c_{B_1,B_2}\right|>\eta
\right)\le\varepsilon,
```

pour une constante de translation `c_{B_1,B_2}` et un petit `\eta`.

Autrement dit: les bornes sont equivalentes si leur correction terminale est presque une translation du score normalise.

## 7. Critere sans simulation de comptage de jumeaux

Le choix de `B` peut etre ramene a l'etude du graphe fini sous `B_2`.

Pour `B_1<B_2`, tous les etats terminaux possibles sont:

```math
\mathcal T(B_2)=\{1,2,\dots,B_2\}.
```

La correction terminale est une fonction finie:

```math
\delta_{B_1,B_2}(y)=\tau_{B_1}(y),
\qquad y\in\mathcal T(B_2).
```

Si `\nu_{B_2}` est la loi limite des points d'entree:

```math
y_{B_2}(n)=T^{\tau_{B_2}(n)}(n),
```

alors la correction terminale a pour loi:

```math
\Delta_{B_1,B_2}\sim (\delta_{B_1,B_2})_*\nu_{B_2}.
```

La selection des bornes se reduit donc a deux objets:

1. la fonction finie `\delta_{B_1,B_2}`;
2. la loi d'entree `\nu_{B_2}`.

Une bande stable de bornes est une bande ou ces lois de correction terminale sont proches, au sens de leur effet sur la queue de `Z_B`.

## 8. Formule de choix d'une borne representative

Soit une grille de bornes candidates `\mathcal B`. On peut definir une distance entre bornes:

```math
D(B_1,B_2)
=\inf_c\mathbb E_{\nu_{B_2}}
\left|d^2\delta_{B_1,B_2}(Y)-c\right|.
```

Ici `c` retire la translation moyenne du score. La distance mesure seulement la deformation restante.

Une bande admissible est alors:

```math
\mathcal I_\varepsilon
=\{B\in\mathcal B:D(B,B_0)\le\varepsilon\}
```

pour un representant provisoire `B_0`, ou plus symetriquement:

```math
\mathcal I_\varepsilon
=\{B\in\mathcal B:\sup_{B'\in\mathcal I_\varepsilon}D(B,B')\le\varepsilon\}.
```

Une borne representative peut etre choisie par minimax:

```math
B_*=
\arg\min_{B\in\mathcal I_\varepsilon}
\sup_{B'\in\mathcal I_\varepsilon}D(B,B').
```

Dans cette formulation, `B_*` n'est pas choisi pour approcher `C_Montmory`. Il est choisi pour minimiser la deformation terminale dans une bande stable.

## 9. Interpretation de 89

`89` peut etre defendu seulement si l'on montre qu'il appartient a une classe d'equivalence de bornes:

```math
B\sim B'
\quad\Longleftrightarrow\quad
D(B,B')\le\varepsilon.
```

La bonne phrase mathematique serait donc:

```text
89 est un representant de la classe de bornes dont la correction terminale preserve la queue normalisee.
```

et non:

```text
89 est la borne fondamentale unique.
```

## 10. Verrou theorique restant

Pour transformer ce protocole en theorie, il faut etablir:

1. l'existence d'une loi limite pour `Z_B` sur les premiers;
2. la stabilite de cette loi sous changement de borne dans une bande;
3. une decorrelation entre la queue `Z_B>=alpha` et la condition `p+2` premier;
4. une definition non calibree du seuil `alpha` ou de la quantile `rho`.

Sous ces hypotheses, on obtiendrait conditionnellement:

```math
N_{B,\alpha}(x)
\sim
2C_2\,\rho_{B,\alpha}\frac{x}{\log^2 x}.
```

La valeur candidate correspond au cas:

```math
\rho_{B,\alpha}
=\frac{0.107983974916}{2C_2}.
```

## 11. Conclusion

Les bornes doivent etre determinees par l'effet de la correction terminale sur le score normalise, pas par ajustement direct de la constante. La formule cle est:

```math
\tau_{B_1}(n)=\tau_{B_2}(n)+\Delta_{B_1,B_2}(n),
```

puis:

```math
Z_{B_1}(n)-Z_{B_2}(n)
\approx -d^2\Delta_{B_1,B_2}(n).
```

C'est cette correction terminale qui doit definir les bornes admissibles.