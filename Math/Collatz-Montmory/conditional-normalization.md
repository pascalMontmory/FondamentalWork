# Normalisation conditionnelle Hardy-Littlewood pour une constante Montmory filtree

Version: 0.2 conditional-normalization draft  
Date: 2026-05-23  
Statut: note mathematique conditionnelle et verifiable

```math
\boxed{\text{Valide : normalisation et implications conditionnelles.}}
```

```math
\boxed{\text{Non valide : existence de }M,\ \rho_M,\ B_M,\ C_{\rm Montmory}.}
```

## Resume

Cette note fixe une normalisation mathematiquement coherente pour une constante candidate `C_Montmory = 0.107983974916` associee a un sous-ensemble filtre de paires de premiers jumeaux. Elle ne prouve ni la conjecture des nombres premiers jumeaux, ni l'existence inconditionnelle de la constante. Les resultats presentes sont limites a des identites, implications conditionnelles, normalisations Hardy-Littlewood, et bornes de stabilite multiplicative.

La contribution principale est la separation entre:

1. un coefficient asymptotique filtre direct;
2. une densite relative par rapport a Hardy-Littlewood;
3. une formulation par biais locaux mixtes;
4. les conditions exactes necessaires pour que la valeur `0.107983974916` devienne verifiable.

## 1. Notation Hardy-Littlewood

On note `pi_2(x)` le nombre de paires de premiers jumeaux `(p,p+2)` avec `p <= x`.

La conjecture de Hardy-Littlewood pour les premiers jumeaux predit:

```math
\pi_2(x) \sim 2C_2\frac{x}{\log^2 x},
```

ou:

```math
C_2=\prod_{p>2}\left(1-\frac{1}{(p-1)^2}\right).
```

Numeriquement:

```math
C_2 \approx 0.66016181584686957392781211001455577843,
```

et donc:

```math
2C_2 \approx 1.32032363169373914785562422002911155687.
```

## 2. Definition d'un comptage Montmory filtre

Soit `M` un predicat booleen fixe sur les paires d'entiers:

```math
M(p,p+2)\in\{0,1\}.
```

On definit le comptage filtre:

```math
N_M(x)=\#\{p\le x: p,p+2\text{ sont premiers et }M(p,p+2)=1\}.
```

Cette definition est purement formelle tant que `M` n'est pas specifie. Elle suffit cependant a etablir les implications conditionnelles ci-dessous.

## 3. Exemple jouet de filtre M

L'exemple suivant sert uniquement a montrer comment le formalisme s'applique. Il n'est pas propose comme filtre Montmory final.

Fixons un module `r >= 3` et un sous-ensemble `A subset Z/rZ`. On definit:

```math
M_A(p,p+2)=1
\quad\Longleftrightarrow\quad
p\bmod r\in A.
```

Alors:

```math
N_{M_A}(x)=\#\{p\le x:p,p+2\text{ premiers et }p\bmod r\in A\}.
```

Sous une hypothese d'equirepartition des premiers jumeaux admissibles modulo `r`, on aurait une densite relative:

```math
\rho_A=\frac{\#\{a\in A:a(a+2)\not\equiv0\pmod r\}}
{\#\{a\in Z/rZ:a(a+2)\not\equiv0\pmod r\}}.
```

Cet exemple montre la structure logique requise: le filtre doit etre fixe avant les tests, puis sa densite relative doit etre etablie ou estimee hors echantillon.

## 4. Convention directe pour C_Montmory

On adopte la convention suivante:

```math
N_M(x)\sim C_{\mathrm{Montmory}}\frac{x}{\log^2x}.
```

La valeur candidate etudiee est:

```math
C_{\mathrm{Montmory}}=0.107983974916.
```

Cette valeur n'est pas supposee prouvee dans cette note. Elle est traitee comme coefficient cible.

## 5. Densite relative induite

Si Hardy-Littlewood est vraie et si `N_M(x)` admet une densite relative parmi les jumeaux, alors on pose:

```math
\rho_M=\lim_{x\to\infty}\frac{N_M(x)}{\pi_2(x)}.
```

Dans ce cas, les coefficients sont lies par:

```math
C_{\mathrm{Montmory}}=2C_2\rho_M.
```

Donc, pour la valeur candidate:

```math
\rho_M=\frac{0.107983974916}{2C_2}.
```

Numeriquement:

```math
\rho_M\approx0.08178598968002706089.
```

Cela signifie que le filtre Montmory devrait retenir environ `8.1786%` de la masse Hardy-Littlewood attendue des premiers jumeaux.

## 6. Theoreme conditionnel fondamental

### Theoreme 1

Supposons:

1. Hardy-Littlewood jumeaux:

```math
\pi_2(x)\sim2C_2\frac{x}{\log^2x}.
```

2. Existence d'une densite relative Montmory:

```math
\frac{N_M(x)}{\pi_2(x)}\to\rho_M.
```

Alors:

```math
N_M(x)\sim2C_2\rho_M\frac{x}{\log^2x}.
```

En particulier, si:

```math
\rho_M=\frac{0.107983974916}{2C_2},
```

alors:

```math
N_M(x)\sim0.107983974916\frac{x}{\log^2x}.
```

### Preuve

On ecrit l'identite:

```math
N_M(x)=\frac{N_M(x)}{\pi_2(x)}\pi_2(x).
```

En passant a la limite avec les deux hypotheses:

```math
\frac{N_M(x)}{\pi_2(x)}\to\rho_M,
\qquad
\pi_2(x)\sim2C_2\frac{x}{\log^2x}.
```

Donc:

```math
N_M(x)\sim\rho_M\,2C_2\frac{x}{\log^2x}.
```

## 7. Consequence logique d'une preuve inconditionnelle

### Proposition 2

Si l'on prouve inconditionnellement:

```math
N_M(x)\sim C\frac{x}{\log^2x}
```

avec `C>0`, alors il existe une infinite de premiers jumeaux.

### Preuve

Comme:

```math
C\frac{x}{\log^2x}\to\infty,
```

on a:

```math
N_M(x)\to\infty.
```

Or chaque objet compte par `N_M(x)` est une paire de premiers jumeaux. Il existe donc une infinite de paires de premiers jumeaux.

### Consequence

Une preuve inconditionnelle de `C_Montmory>0` dans cette convention serait au moins aussi forte qu'une preuve d'infinite de premiers jumeaux. La note presente donc seulement des resultats conditionnels ou algebriques.

## 8. Risque de calibration a posteriori

Le filtre `M` doit etre defini avant la comparaison avec la valeur `0.107983974916`.

Si `M` est choisi apres observation des donnees pour forcer:

```math
\frac{N_M(x)}{\pi_2(x)}\approx0.08178598968002706,
```

alors `C_Montmory` perd sa signification predictive. Le resultat devient un ajustement retrospectif, non une constante arithmetique.

Pour eviter ce biais, toute etude doit distinguer:

1. une zone d'entrainement pour fixer les parametres du filtre;
2. une zone hors echantillon pour tester la stabilite;
3. une regle de promotion qui interdit de modifier `M` apres lecture des resultats hors echantillon.

## 9. Formulation par facteurs locaux mixtes

On considere maintenant une deuxieme formulation, utile pour l'experimentation.

Pour un premier impair `q>=3`, les classes interdites pour le motif `(n,n+2)` sont:

```math
0, -2 \pmod q.
```

Soit `mu_q` une loi de probabilite sur `Z/qZ`. On definit:

```math
\Sigma_q=1-\mu_q(0)-\mu_q(-2).
```

Sous la loi uniforme:

```math
\Sigma_q^{\mathrm{unif}}=1-\frac{2}{q}.
```

Le facteur local Hardy-Littlewood correspondant est:

```math
L_q^{\mathrm{HL}}
=\frac{1-2/q}{(1-1/q)^2}
=1-\frac{1}{(q-1)^2}.
```

Ainsi, le biais local relatif naturel est:

```math
B_q=\frac{\Sigma_q}{1-2/q}.
```

## 10. Constante mixte corrigee

Pour un seuil `Q`, on definit:

```math
K_2^{\mathrm{mix}}(Q)
=2C_2\prod_{3\le q\le Q}B_q
=2C_2\prod_{3\le q\le Q}\frac{\Sigma_q}{1-2/q}.
```

Cette formule est normalisee pour reduire a Hardy-Littlewood lorsque `mu_q` est uniforme pour tout `q<=Q`.

### Proposition 3: reduction uniforme

Si:

```math
\Sigma_q=1-\frac{2}{q}
```

pour tout `3<=q<=Q`, alors:

```math
K_2^{\mathrm{mix}}(Q)=2C_2.
```

### Preuve

Dans ce cas:

```math
B_q=\frac{1-2/q}{1-2/q}=1.
```

Donc:

```math
K_2^{\mathrm{mix}}(Q)=2C_2\prod_{3\le q\le Q}1=2C_2.
```

## 11. Stabilite multiplicative

On pose:

```math
\varepsilon_q=B_q-1=\frac{\Sigma_q}{1-2/q}-1.
```

Alors:

```math
K_2^{\mathrm{mix}}(Q)=2C_2\prod_{3\le q\le Q}(1+\varepsilon_q).
```

### Theoreme 4

Si:

```math
|\varepsilon_q|\le\frac12
```

pour tout `3<=q<=Q`, alors:

```math
\left|\log\frac{K_2^{\mathrm{mix}}(Q)}{2C_2}\right|
\le
\sum_{3\le q\le Q}\frac{|\varepsilon_q|}{1-|\varepsilon_q|}
\le
2\sum_{3\le q\le Q}|\varepsilon_q|.
```

### Preuve

On utilise:

```math
\log\frac{K_2^{\mathrm{mix}}(Q)}{2C_2}
=
\sum_{3\le q\le Q}\log(1+\varepsilon_q).
```

Pour `|u|<1`:

```math
|\log(1+u)|\le\frac{|u|}{1-|u|}.
```

La premiere borne suit par sommation. Si `|epsilon_q|<=1/2`, alors:

```math
\frac{|\varepsilon_q|}{1-|\varepsilon_q|}\le2|\varepsilon_q|.
```

## 12. Queue du produit Hardy-Littlewood

### Proposition 5

On a:

```math
\prod_{q>Q}\left(1-\frac{1}{(q-1)^2}\right)=1+O\left(\frac1Q\right).
```

### Preuve

Pour `q>=3`, posons:

```math
a_q=\frac{1}{(q-1)^2}.
```

Alors:

```math
\sum_{q>Q}a_q
\le
\sum_{n>Q}\frac{1}{(n-1)^2}
=O\left(\frac1Q\right).
```

Comme:

```math
\log(1-a_q)=-a_q+O(a_q^2),
```

et:

```math
\sum_{q>Q}a_q^2=O\left(\frac{1}{Q^3}\right),
```

on obtient:

```math
\sum_{q>Q}\log(1-a_q)=O\left(\frac1Q\right).
```

En exponentiant:

```math
\prod_{q>Q}(1-a_q)=1+O\left(\frac1Q\right).
```

## 13. Coefficient limite par biais locaux

Si le produit des biais locaux converge:

```math
B_M=\lim_{Q\to\infty}\prod_{3\le q\le Q}B_q,
```

alors le coefficient dynamique associe serait:

```math
C_{\mathrm{dyn}}=2C_2B_M.
```

Pour identifier ce coefficient a la valeur Montmory candidate, il faudrait:

```math
B_M=\frac{C_{\mathrm{Montmory}}}{2C_2}
\approx0.08178598968002706089.
```

## 14. Estimateur experimental formel

Une fois les `Sigma_q` estimes, on peut definir:

```math
\widehat K_2^{\mathrm{mix}}(Q)
=2C_2\prod_{3\le q\le Q}\frac{\widehat\Sigma_q}{1-2/q}.
```

Puis:

```math
\widehat\pi_2(x;Q)
=
\widehat K_2^{\mathrm{mix}}(Q)
\frac{x}{\log^2x}
\left(1+\frac{2}{\log x}+\frac{6}{\log^2x}\right).
```

Cette formule est un estimateur, pas un theoreme asymptotique.

## 15. Protocole experimental minimal

Un protocole acceptable doit fixer les objets avant test.

### Donnees

- `X_train`: borne d'entrainement pour fixer les parametres du filtre ou de la dynamique.
- `X_test`: bornes hors echantillon, par exemple `10 X_train`, `100 X_train`, puis la plus grande borne disponible.
- `Q_train`: seuil de modules utilise pour stabiliser les biais locaux.
- `Q_test`: seuils hors echantillon, avec `Q_test >= Q_train`.

### Mesures a reporter

Pour un filtre direct:

```math
\widehat\rho_M(X)=\frac{N_M(X)}{\pi_2(X)}.
```

Pour les facteurs locaux mixtes:

```math
\widehat K_2^{\mathrm{mix}}(Q),
\qquad
\widehat B_M(Q)=\prod_{3\le q\le Q}\frac{\widehat\Sigma_q}{1-2/q}.
```

Pour la constante:

```math
\widehat C_M(X)=\widehat\rho_M(X)\,2C_2
```

ou:

```math
\widehat C_{\mathrm{dyn}}(Q)=2C_2\widehat B_M(Q).
```

### Criteres de stabilite

Un resultat numerique est recevable seulement si:

1. les parametres fixes sur `X_train` ne sont pas modifies apres lecture de `X_test`;
2. `\widehat\rho_M(X)` ou `\widehat B_M(Q)` reste stable hors echantillon;
3. les ecarts diminuent ou se stabilisent quand `X` et `Q` augmentent;
4. les incertitudes Monte Carlo utilisent une taille effective ou des repetitions independantes;
5. les scripts, seeds, bornes et sorties attendues sont publies.

## 16. Ce qui est valide dans cette note

Les elements suivants sont valides:

1. la normalisation `C_Montmory = 2C_2 rho_M`;
2. la valeur numerique `rho_M ~= 0.08178598968002706`;
3. le theoreme conditionnel reliant Hardy-Littlewood, densite relative et coefficient filtre;
4. la consequence logique qu'une preuve inconditionnelle positive impliquerait une infinite de jumeaux;
5. la normalisation locale correcte `B_q = Sigma_q/(1-2/q)`;
6. la reduction a Hardy-Littlewood sous loi uniforme;
7. la stabilite multiplicative;
8. la queue `1+O(1/Q)` du produit Hardy-Littlewood.

## 17. Ce qui n'est pas valide sans hypothese supplementaire

Cette note ne prouve pas:

1. l'existence du filtre final `M`;
2. l'existence de la limite `rho_M`;
3. l'existence de la limite `B_M`;
4. la valeur `C_Montmory = 0.107983974916`;
5. une infinite de premiers jumeaux;
6. l'ergodicite d'une dynamique Montmory modulo `q`;
7. la convergence d'un estimateur Monte Carlo Markovien sans controle du melange.

## Conclusion

La constante candidate `C_Montmory` peut etre formulee proprement dans le cadre Hardy-Littlewood. La partie actuellement validable est une structure de normalisation et de propagation d'erreur, non une preuve de la constante. Le verrou scientifique reste la definition et la validation d'un filtre ou d'une dynamique Montmory non calibree apres coup.