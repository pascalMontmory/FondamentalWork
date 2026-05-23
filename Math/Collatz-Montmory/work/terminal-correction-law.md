# Loi de correction terminale pour les bornes Collatz-Montmory

Date: 2026-05-23  
Statut: note mathematique conditionnelle, sans validation numerique

## 1. Objectif

On veut determiner les bornes admissibles `B` par des formules, pas par ajustement numerique.

Le principe est:

```text
Une borne B est admissible si changer B ne fait qu'ajouter une correction terminale stable au score normalise.
```

La structure mathematique est donc une loi de correction terminale.

## 2. Transformation et entree dans la zone terminale

On travaille avec la transformation Collatz acceleree:

```math
T(n)=
\begin{cases}
n/2, & n\equiv0\pmod2,\\
(3n+1)/2, & n\equiv1\pmod2.
\end{cases}
```

Pour `B>=1`, on definit le temps d'entree:

```math
\tau_B(n)=\min\{t\ge0:T^t(n)\le B\}.
```

Le point d'entree dans la zone terminale est:

```math
E_B(n)=T^{\tau_B(n)}(n)\in\{1,2,\dots,B\}.
```

`E_B` est la variable importante: elle dit ou la trajectoire entre dans le petit graphe terminal.

## 3. Loi d'entree

Pour une population arithmetique `\mathcal P` (entiers impairs, premiers, premiers jumeaux projetes sur `p`, etc.), on definit la loi empirique d'entree:

```math
\nu_{B,x}^{\mathcal P}(y)
=
\frac{\#\{n\le x:n\in\mathcal P, E_B(n)=y\}}
{\#\{n\le x:n\in\mathcal P\}},
\qquad 1\le y\le B.
```

Hypothese d'entree terminale:

```math
\nu_{B,x}^{\mathcal P}\Longrightarrow \nu_B^{\mathcal P}
\qquad (x\to\infty).
```

Cette hypothese est le premier verrou theorique. Elle transforme le choix de `B` en une question sur une mesure finie:

```math
\nu_B^{\mathcal P}\in\mathcal P(\{1,\dots,B\}).
```

## 4. Correction terminale entre deux bornes

Soient:

```math
B_1<B_2.
```

La correction terminale finie est la fonction:

```math
\delta_{B_1,B_2}(y)=\tau_{B_1}(y),
\qquad 1\le y\le B_2.
```

Pour tout `n`, on a l'identite exacte:

```math
\tau_{B_1}(n)=\tau_{B_2}(n)+\delta_{B_1,B_2}(E_{B_2}(n)).
```

Donc la variable de correction est:

```math
\Delta_{B_1,B_2}(n)=\delta_{B_1,B_2}(E_{B_2}(n)).
```

Si la loi d'entree existe, alors la loi limite de correction est le push-forward:

```math
\mathcal L(\Delta_{B_1,B_2})
=
(\delta_{B_1,B_2})_*\nu_{B_2}^{\mathcal P}.
```

C'est la formule centrale.

## 5. Loi de correction pour les paires

Pour les jumeaux, le score utilise deux trajectoires. On doit donc regarder la loi jointe:

```math
\nu_{B,x}^{(2)}(y_0,y_2)
=
\frac{\#\{p\le x:p,p+2\text{ premiers},
E_B(p)=y_0,
E_B(p+2)=y_2\}}
{\pi_2(x)}.
```

Hypothese jointe:

```math
\nu_{B,x}^{(2)}\Longrightarrow\nu_B^{(2)}.
```

Pour `B_1<B_2`, les corrections terminales des deux membres sont:

```math
\Delta_0=\delta_{B_1,B_2}(E_{B_2}(p)),
\qquad
\Delta_2=\delta_{B_1,B_2}(E_{B_2}(p+2)).
```

Leur loi limite est:

```math
\mathcal L(\Delta_0,\Delta_2)
=
(\delta_{B_1,B_2}\times\delta_{B_1,B_2})_*\nu_{B_2}^{(2)}.
```

Cette formule remplace une simulation par un objet mathematique fini: la loi d'entree jointe dans `\{1,\dots,B_2\}^2`.

## 6. Effet exact sur le score d'un entier

Posons:

```math
L(n)=\log_2 n,
\qquad
K_B(n)=\frac{L(n)}{\tau_B(n)}.
```

Avec:

```math
\tau=\tau_{B_2}(n),
\qquad
\Delta=\Delta_{B_1,B_2}(n),
```

on a:

```math
K_{B_1}(n)=\frac{L}{\tau+\Delta}.
```

Donc:

```math
K_{B_2}(n)-K_{B_1}(n)
=
\frac{L\Delta}{\tau(\tau+\Delta)}.
```

Cette quantite est positive: descendre vers une borne plus petite augmente le temps d'arret et diminue le score.

## 7. Effet sur le score normalise

On pose:

```math
d=1-\frac12\log_2 3,
\qquad
Z_B(n)=(K_B(n)-d)L(n).
```

Alors:

```math
Z_{B_1}(n)-Z_{B_2}(n)
=
-\frac{L(n)^2\Delta_{B_1,B_2}(n)}
{\tau_{B_2}(n)(\tau_{B_2}(n)+\Delta_{B_1,B_2}(n))}.
```

Si:

```math
\tau_{B_2}(n)=\frac{L(n)}{d}+r(n),
```

alors:

```math
Z_{B_1}(n)-Z_{B_2}(n)
=
-d^2\Delta_{B_1,B_2}(n)
+O\left(
\frac{|r(n)|\Delta_{B_1,B_2}(n)+\Delta_{B_1,B_2}(n)^2}{L(n)}
\right).
```

Donc, au premier ordre, changer de borne translate le score normalise par:

```math
-d^2\Delta_{B_1,B_2}.
```

## 8. Effet sur le score de paire

Pour une paire `(p,p+2)`, posons:

```math
K_{B,i}=K_B(p+i),
\qquad i\in\{0,2\}.
```

Le score de paire est:

```math
S_B(p)=\min(K_{B,0},K_{B,2}).
```

Pour `B_1<B_2`, on definit:

```math
R_i(p)=K_{B_2,i}-K_{B_1,i}
=\frac{L_i^2\Delta_i}{L_i\tau_{B_2,i}(\tau_{B_2,i}+\Delta_i)},
```

ou plus simplement:

```math
R_i(p)=\frac{L_i\Delta_i}{\tau_{B_2,i}(\tau_{B_2,i}+\Delta_i)},
\qquad L_i=\log_2(p+i).
```

Alors:

```math
S_{B_1}(p)=\min(K_{B_2,0}-R_0,
K_{B_2,2}-R_2).
```

On a toujours l'encadrement exact:

```math
S_{B_2}(p)-\max(R_0,R_2)
\le
S_{B_1}(p)
\le
S_{B_2}(p)-\min(R_0,R_2).
```

Si l'indice minimisant est stable, c'est-a-dire si le meme membre de la paire realise le minimum pour `B_1` et `B_2`, alors:

```math
S_{B_1}(p)-S_{B_2}(p)=-R_{i_*}(p),
```

avec:

```math
i_*\in\arg\min_{i\in\{0,2\}}K_{B_2,i}.
```

Dans ce cas:

```math
Z_{B_1}(p)-Z_{B_2}(p)
\approx -d^2\Delta_{i_*}.
```

Sans stabilite de l'indice minimisant, on conserve l'encadrement par `min` et `max` des deux corrections.

## 9. Definition de l'equivalence de bornes

Soit `\mathcal P` une population et soit `F_B^{\mathcal P}` la loi limite de `Z_B` sur cette population.

La queue est:

```math
Q_B^{\mathcal P}(\alpha)=1-F_B^{\mathcal P}(\alpha).
```

Deux bornes `B_1<B_2` sont equivalentes pour la queue si la loi de correction terminale agit comme une translation au voisinage de la queue d'interet.

Une definition quantitative est:

```math
D_{\mathcal P}(B_1,B_2)
=
\inf_{c\in\mathbb R}
W_1\left(
\mathcal L(Z_{B_1}^{\mathcal P}),
\mathcal L(Z_{B_2}^{\mathcal P}+c)
\right),
```

ou `W_1` est la distance de Wasserstein-1.

On pose:

```math
B_1\sim_\varepsilon B_2
\quad\Longleftrightarrow\quad
D_{\mathcal P}(B_1,B_2)\le\varepsilon.
```

Grace aux formules precedentes, une approximation calculable de cette distance est donnee par la loi de:

```math
d^2\Delta_{B_1,B_2}.
```

Plus la loi de `\Delta` est concentree autour d'une constante, plus les bornes sont equivalentes.

## 10. Critere de bande admissible

Une bande de bornes `I` est admissible si:

```math
\sup_{B_1,B_2\in I}D_{\mathcal P}(B_1,B_2)\le\varepsilon.
```

Un representant canonique peut etre choisi par minimax:

```math
B_*=
\arg\min_{B\in I}
\sup_{B'\in I}D_{\mathcal P}(B,B').
```

Ce choix ne depend pas de `C_Montmory`. Il depend seulement de la stabilite terminale des temps d'arret.

## 11. Formule inverse pour la loi d'entree

La loi d'entree `\nu_B` peut etre formulee par les branches inverses de `T`.

Les preimages accelerees de `y` sont:

```math
2y,
```

et, lorsque `y\equiv2\pmod3`,

```math
\frac{2y-1}{3}.
```

La seconde branche est l'inverse de l'etape impaire.

Ainsi, les arbres de preimages de la zone terminale `\{1,\dots,B\}` determinent les bassins d'entree. Formellement, pour `y<=B`:

```math
\mathcal A_B(y)=\{n:E_B(n)=y\}.
```

Alors:

```math
\nu_{B,x}^{\mathcal P}(y)
=
\frac{\#(\mathcal P\cap\mathcal A_B(y)\cap[1,x])}
{\#(\mathcal P\cap[1,x])}.
```

Cela montre que la loi terminale est un probleme de densite des arbres inverses `\mathcal A_B(y)` dans la population choisie.

## 12. Theoreme conditionnel de stabilite des bornes

### Theoreme

Fixons une population `\mathcal P`. Supposons que:

1. pour chaque `B` dans une bande `I`, la loi limite `F_B^{\mathcal P}` de `Z_B` existe;
2. pour tous `B_1<B_2` dans `I`, la loi d'entree `\nu_{B_2}^{\mathcal P}` existe;
3. les corrections terminales sont concentrees modulo translation:

```math
\inf_c
\mathbb E_{\nu_{B_2}^{\mathcal P}}
\left|d^2\delta_{B_1,B_2}(Y)-c\right|
\le\varepsilon;
```

4. les erreurs de temps d'arret satisfont:

```math
\frac{|r(n)|\Delta_{B_1,B_2}(n)+\Delta_{B_1,B_2}(n)^2}{\log_2 n}
\to0
```

en probabilite sur `\mathcal P`.

Alors les lois `F_B^{\mathcal P}` sont equivalentes modulo translation a erreur `O(\varepsilon)` sur la bande `I`.

En particulier, les queues:

```math
Q_B^{\mathcal P}(\alpha)=1-F_B^{\mathcal P}(\alpha)
```

sont stables apres ajustement du seuil `\alpha` par une translation dependante de `B`.

### Sens

Ce theoreme conditionnel justifie l'existence d'une bande de bornes admissibles. Il ne choisit pas `89`; il donne le critere pour dire que `89` appartient ou non a la meme classe que d'autres bornes.

## 13. Application conditionnelle aux jumeaux

Pour les jumeaux, on prend:

```math
\mathcal P_2=\{p:p,p+2\text{ premiers}\}.
```

Si la loi jointe d'entree `\nu_B^{(2)}` existe et si la correction terminale de paire est stable dans une bande `I`, alors le choix de `B` dans `I` ne change que le seuil de queue, pas la structure de la densite filtree.

Sous une hypothese supplementaire de decorrelation avec Hardy-Littlewood:

```math
\#\{p\le x:p,p+2\text{ premiers}, Z_B(p)\ge\alpha\}
\sim
\rho_{B,\alpha}\,2C_2\frac{x}{\log^2x}.
```

La constante candidate correspond a:

```math
\rho_{B,\alpha}
=
\frac{0.107983974916}{2C_2}.
```

## 14. Ce qui est verifie dans cette note

Les points suivants sont des identites ou definitions mathematiques:

1. `\tau_{B_1}=\tau_{B_2}+\Delta_{B_1,B_2}`;
2. la correction terminale est le push-forward `(\delta_{B_1,B_2})_*\nu_{B_2}`;
3. l'effet exact sur `K_B(n)`;
4. l'effet asymptotique `Z_{B_1}-Z_{B_2}\approx-d^2\Delta` sous l'heuristique de temps d'arret;
5. l'encadrement exact du score de paire par `min/max` des corrections;
6. la definition d'une classe d'equivalence de bornes.

Les points suivants restent conditionnels:

1. existence des lois limites `\nu_B`, `\nu_B^{(2)}`, `F_B`;
2. concentration des corrections terminales dans une bande;
3. decorrelation avec la condition de primalite jumelle;
4. identification non calibree du seuil `\alpha` donnant la valeur numerique cible.

## 15. Conclusion

La determination des bornes doit passer par la loi de correction terminale:

```math
\mathcal L(\Delta_{B_1,B_2})=(\delta_{B_1,B_2})_*\nu_{B_2}.
```

Une borne comme `89` est defendable seulement comme representant d'une classe de bornes pour laquelle cette loi de correction terminale preserve la queue du score normalise.

Le prochain verrou mathematique est donc l'etude des mesures d'entree `\nu_B` et `\nu_B^{(2)}` via les arbres inverses de la transformation acceleree.