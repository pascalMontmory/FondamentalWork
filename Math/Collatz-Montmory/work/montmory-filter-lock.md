# Verrou du filtre Montmory

Date: 2026-05-23

Objet: definir professionnellement le critere `M(p,p+2)` necessaire pour donner un sens verifiable a `C_Montmory = 0.107983974916` comme coefficient asymptotique Hardy-Littlewood filtre.

## 1. Probleme exact

La constante candidate est interpretee comme coefficient direct:

```math
N_M(x) \sim C_{\mathrm{Montmory}}\frac{x}{\log^2 x},
\qquad
C_{\mathrm{Montmory}}=0.107983974916.
```

Avec Hardy-Littlewood jumeaux:

```math
\pi_2(x)\sim 2C_2\frac{x}{\log^2x},
```

cela impose une densite relative cible:

```math
\rho_M
=
\frac{C_{\mathrm{Montmory}}}{2C_2}
\approx 0.08178598968002706089.
```

Le verrou est donc:

```math
\text{definir }M(p,p+2)\text{ tel que }
\frac{N_M(x)}{\pi_2(x)}\to\rho_M.
```

## 2. Regle anti-surajustement

Un filtre Montmory admissible doit etre fixe avant les tests asymptotiques. Il ne doit pas etre defini par la phrase:

```text
M selectionne les 8.1786% de jumeaux qui donnent la constante voulue.
```

Cela serait tautologique.

Un filtre admissible doit donc fournir:

1. une transformation dynamique exacte;
2. un temps d'arret exact;
3. un score exact sur un entier;
4. une regle exacte sur la paire `(p,p+2)`;
5. des parametres declares avant calcul;
6. une implementation deterministe;
7. un protocole de test reproductible.

## 3. Dynamique canonique proposee

On fixe la transformation Collatz acceleree:

```math
T(n)=
\begin{cases}
n/2, & n\equiv 0\pmod 2,\\
(3n+1)/2, & n\equiv 1\pmod 2.
\end{cases}
```

Cette version est compatible avec les applications affines `x -> x/2` et `x -> (3x+1)/2` deja presentes dans les notes.

On fixe aussi le seuil:

```math
B_M=89.
```

Le temps d'arret est:

```math
\tau_B(n)=\min\{t\ge0:T^t(n)\le B_M\}.
```

Il est conditionnellement fini pour tout `n` sous la conjecture de Collatz. Pour les tests bornes, il est simplement calcule avec une limite d'iteration explicite.

## 4. Score compressif canonique

Pour `n>B_M`, on definit:

```math
\kappa_B(n)=\frac{\log_2 n}{\tau_B(n)}.
```

Ce score mesure le nombre moyen de bits compresses par etape avant entree dans la zone basse `<=B_M`.

Pour une paire de jumeaux `(p,p+2)`, on definit trois scores de paire:

```math
\kappa_{\min}(p)=\min(\kappa_B(p),\kappa_B(p+2)),
```

```math
\kappa_{\mathrm{geo}}(p)=\sqrt{\kappa_B(p)\kappa_B(p+2)},
```

```math
\kappa_{\mathrm{harm}}(p)=\frac{2}{\kappa_B(p)^{-1}+\kappa_B(p+2)^{-1}}.
```

Le score `min` est le plus conservateur: une paire n'est compressive que si ses deux membres le sont.

## 5. Famille de filtres admissibles

### Filtre seuil haut

Pour un score de paire `s(p)` et un seuil `alpha`, on definit:

```math
M_{s,\alpha}^{\ge}(p,p+2)=1
\quad\Longleftrightarrow\quad
s(p)\ge\alpha.
```

### Filtre fenetre autour de `K_Montmory`

Avec:

```math
K_M=0.291333547788,
```

on definit:

```math
M_{s,\Delta}^{\mathrm{win}}(p,p+2)=1
\quad\Longleftrightarrow\quad
|s(p)-K_M|\le\Delta.
```

Ce filtre est plus proche de l'intuition `K_Montmory`, mais il introduit un parametre `Delta`. Il doit donc etre justifie independamment ou calibre sur un jeu d'apprentissage puis teste hors echantillon.

### Filtre quantile interdit pour preuve

On peut definir experimentalement un seuil `alpha_x` tel que le filtre retienne exactement `rho_M` des jumeaux jusqu'a `x`. Ce filtre est utile pour diagnostic, mais il est interdit comme definition mathematique de la constante, car il encode la reponse.

## 6. Definition canonique recommandee pour le programme

La definition la plus propre pour commencer est:

```math
M_{\alpha}(p,p+2)=1
\quad\Longleftrightarrow\quad
\min(\kappa_B(p),\kappa_B(p+2))\ge\alpha.
```

Elle est:

- deterministe;
- symetrique en force compressive;
- plus stricte que la moyenne;
- simple a implementer;
- compatible avec une interpretation de sous-classe fortement compressive.

On definit alors:

```math
N_{M,\alpha}(x)=
\#\{p\le x:p,p+2\text{ premiers et }M_{\alpha}(p,p+2)=1\}.
```

et la fonction de densite relative:

```math
\rho(\alpha)=
\lim_{x\to\infty}\frac{N_{M,\alpha}(x)}{\pi_2(x)},
```

si cette limite existe.

Le verrou devient:

```math
\text{trouver un }\alpha_M\text{ naturel tel que }
\rho(\alpha_M)=0.08178598968002706089.
```

## 7. Ce qu'il faudrait demontrer

Pour obtenir `C_Montmory`, il faudrait demontrer les deux enonces suivants.

### Enonce A: existence de la densite filtrante

```math
\frac{N_{M,\alpha}(x)}{\pi_2(x)}\to\rho(\alpha).
```

### Enonce B: identification de la valeur

```math
\rho(\alpha_M)=\frac{0.107983974916}{2C_2}.
```

Alors, sous Hardy-Littlewood jumeaux:

```math
N_{M,\alpha_M}(x)
\sim
0.107983974916\frac{x}{\log^2x}.
```

## 8. Pourquoi c'est difficile

Une preuve inconditionnelle avec une constante positive impliquerait une infinite de premiers jumeaux. Il faut donc viser une des trois voies suivantes:

1. un resultat conditionnel a Hardy-Littlewood;
2. une heuristique probabiliste robuste avec verification numerique;
3. une reformulation qui ne compte pas des jumeaux premiers mais des candidats arithmetiques plus larges.

## 9. Strategie professionnelle recommandee

### Phase 1: gel des definitions

Fixer:

```text
T = Collatz accelere
B = 89
score = min(kappa_B(p), kappa_B(p+2))
filtre = score >= alpha
```

### Phase 2: calibration transparente

Calculer sur une plage d'apprentissage `x <= X_train` le seuil `alpha_train` tel que:

```math
N_{M,\alpha_{train}}(X_{train})/\pi_2(X_{train})\approx\rho_M.
```

Puis geler `alpha_train`.

### Phase 3: test hors echantillon

Tester si, pour `X > X_train`, le ratio:

```math
N_{M,\alpha_{train}}(X)/\pi_2(X)
```

reste proche de `rho_M` ou derive.

### Phase 4: modele probabiliste

Etudier la distribution de `\kappa_{\min}` parmi les paires de jumeaux et parmi des paires impaires aleatoires. Si les distributions coincident asymptotiquement, alors le filtre est probablement decorrele de la primalite. Si elles divergent, la constante peut contenir une vraie information arithmetique.

## 10. Criteres de succes

Le verrou est considere partiellement leve si:

1. `alpha_train` se stabilise quand `X_train` augmente;
2. le ratio hors echantillon reste proche de `rho_M`;
3. les ecarts diminuent avec `x`;
4. la definition ne change pas apres observation des resultats;
5. les scripts reproduisent les tableaux.

Il est considere mathematiquement leve seulement si une preuve conditionnelle ou inconditionnelle de la limite est donnee.

## 11. Formulation scientifique correcte

A ce stade, la formulation professionnelle est:

```text
Nous proposons une famille canonique de filtres Montmory sur les paires de premiers jumeaux, basee sur le temps d'arret Collatz accelere vers B=89. La constante C_Montmory est interpretee comme le coefficient Hardy-Littlewood filtre correspondant a une densite relative cible rho_M. Le probleme mathematique principal est l'existence et l'identification de la limite rho(alpha). La valeur 0.107983974916 devient une conjecture verifiable, non une constante prouvee.
```

## 12. Prochaine etape minimale

Implementer le calcul de:

```math
\tau_B(n),\quad \kappa_B(n),\quad \kappa_{\min}(p),\quad N_{M,\alpha}(x),\quad N_{M,\alpha}(x)/\pi_2(x).
```

Puis produire un tableau pour plusieurs `x` et plusieurs seuils `alpha`.