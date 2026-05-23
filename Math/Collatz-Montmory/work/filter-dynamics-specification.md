# Specification du filtre M et de la dynamique locale mu_q

Date: 2026-05-23  
Statut: specification de recherche, non verifiee

## 1. Objectif

Cette note fixe deux objets candidats avant experimentation:

1. un filtre direct `M(p,p+2)` sur les paires de premiers jumeaux;
2. une dynamique locale modulo `q` produisant une loi `mu_q` et des facteurs locaux mixtes.

Le but est d'eviter la calibration a posteriori: les definitions ci-dessous doivent etre testees telles quelles sur des donnees hors echantillon.

## 2. Filtre direct M: version canonique figee

### 2.1. Transformation

On utilise la transformation Collatz acceleree:

```math
T(n)=
\begin{cases}
n/2, & n\equiv0\pmod2,\\
(3n+1)/2, & n\equiv1\pmod2.
\end{cases}
```

On fixe le seuil:

```math
B=89.
```

### 2.2. Temps d'arret

Pour `n>B`, on definit:

```math
\tau_B(n)=\min\{t\ge0:T^t(n)\le B\}.
```

Pour `n<=B`, on pose `tau_B(n)=0`.

### 2.3. Score d'un entier

Pour `n>B`:

```math
\kappa_B(n)=\frac{\log_2 n}{\tau_B(n)}.
```

Pour `n<=B`, le score n'est pas utilise dans les tests asymptotiques.

### 2.4. Score d'une paire

Pour une paire de jumeaux `(p,p+2)` avec `p>B`, on definit:

```math
S_B(p)=\min\left(\kappa_B(p),\kappa_B(p+2)\right).
```

Le minimum est choisi avant test, car il impose que les deux membres de la paire soient compressifs.

### 2.5. Filtre fige

Pour un seuil `alpha`, on definit:

```math
M_\alpha(p,p+2)=1
\quad\Longleftrightarrow\quad
S_B(p)\ge\alpha.
```

La constante cible correspondrait a une densite relative:

```math
\rho_M=0.08178598968002706089.
```

Le seuil `alpha` ne fait pas partie de la constante tant qu'il n'est pas fixe par une regle reproductible.

## 3. Regle de calibration autorisee

Une seule calibration est autorisee:

1. choisir une borne d'entrainement `X_train`;
2. calculer les paires de jumeaux `p,p+2` avec `p<=X_train`;
3. calculer les scores `S_B(p)`;
4. prendre `alpha_train` comme le quantile superieur qui selectionne la proportion `rho_M` sur l'entrainement;
5. geler `alpha_train`;
6. tester sans modification sur `X_test > X_train`.

Cette procedure ne prouve rien. Elle sert uniquement a rendre le test hors echantillon bien defini.

## 4. Dynamique locale mu_q: candidate A, affine Collatz aleatoire

### 4.1. Espace d'etats

Pour un premier impair `q>=3`, l'espace d'etats est:

```math
\mathcal X_q=\mathbb Z/q\mathbb Z.
```

### 4.2. Transitions

On definit deux applications affines:

```math
f_0(x)=2^{-1}x,
\qquad
f_1(x)=2^{-1}(3x+1)
\pmod q.
```

La chaine choisit `f_0` ou `f_1` avec probabilite `1/2` a chaque pas:

```math
X_{t+1}=f_{\varepsilon_t}(X_t),
\qquad
\varepsilon_t\sim\mathrm{Bernoulli}(1/2).
```

### 4.3. Probleme de stationnarite

Comme `f_0` et `f_1` sont des bijections modulo `q`, la loi uniforme est stationnaire:

```math
u_q=u_q.
```

Cette dynamique ne peut produire un biais local non trivial si l'on part de l'uniforme et si le melange est complet. Elle est donc principalement un controle negatif: elle doit redonner Hardy-Littlewood.

### 4.4. Facteur local associe

Pour une loi stationnaire ou empirique `mu_q`, on definit:

```math
\Sigma_q=1-\mu_q(0)-\mu_q(-2).
```

Sous uniforme:

```math
\Sigma_q=1-2/q.
```

Donc:

```math
B_q=\frac{\Sigma_q}{1-2/q}=1.
```

Conclusion: la candidate A est utile comme test de normalisation, mais elle ne peut pas expliquer `C_Montmory < 2C_2` sans condition non uniforme ou sans dynamique differente.

## 5. Dynamique locale mu_q: candidate B, projection de trajectoires entieres

La candidate B est plus proche de l'intuition Collatz-Montmory.

### 5.1. Definition empirique

Pour une borne `R`, on considere les trajectoires reelles:

```math
n, T(n), T^2(n), ..., T^R(n)
```

pour des graines `n` dans un ensemble `G_X`, par exemple:

```math
G_X=\{p:p,p+2\text{ premiers}, p\le X\}
```

ou un ensemble de controle:

```math
G_X^{ctrl}=\{n\le X:n\text{ impair}, n+2\text{ impair}\}.
```

On projette les trajectoires modulo `q` et on definit:

```math
\mu_{q;X,R}(a)=
\frac{1}{|G_X|(R+1)}
\#\{(n,t):n\in G_X,0\le t\le R,T^t(n)\equiv a\pmod q\}.
```

Puis:

```math
\Sigma_{q;X,R}=1-\mu_{q;X,R}(0)-\mu_{q;X,R}(-2).
```

### 5.2. Biais local empirique

```math
B_{q;X,R}=\frac{\Sigma_{q;X,R}}{1-2/q}.
```

Cette candidate peut produire un biais non trivial, mais elle est empirique et depend de `X`, `R`, et du choix des graines.

### 5.3. Regle anti-fuite de donnees

Si `G_X` utilise les jumeaux eux-memes, il faut separer:

- `X_train` pour choisir `R`, `Q`, et les options de dynamique;
- `X_test` pour mesurer la stabilite;
- un controle `G_X^{ctrl}` pour verifier que le biais n'est pas un artefact de selection.

## 6. Coefficient dynamique teste

Pour la candidate B, on definit:

```math
\widehat B_M(Q;X,R)=\prod_{3\le q\le Q}B_{q;X,R}.
```

et:

```math
\widehat C_{dyn}(Q;X,R)=2C_2\widehat B_M(Q;X,R).
```

La cible est:

```math
\widehat C_{dyn}(Q;X,R)\approx0.107983974916.
```

ou equivalent:

```math
\widehat B_M(Q;X,R)\approx0.08178598968002706089.
```

## 7. Hypothese de decorrelation precise

La forme minimale d'une hypothese testable est la suivante.

### Hypothese D_Montmory

Il existe une constante `B_M in (0,1)` telle que, pour une suite de parametres `Q=Q(X)`, `R=R(X)` avec `Q(X)->infty`, `R(X)->infty`, on ait:

```math
\prod_{3\le q\le Q(X)}
\frac{\Sigma_{q;X,R(X)}}{1-2/q}
\longrightarrow B_M.
```

De plus, le meme produit estime sur des fenetres hors echantillon doit avoir la meme limite.

La constante Montmory serait alors:

```math
C_{Montmory}=2C_2B_M.
```

La valeur cible impose:

```math
B_M=0.08178598968002706089.
```

## 8. Ce qui invaliderait l'hypothese

L'hypothese doit etre rejetee si:

1. `alpha_train` ou `B_M(Q;X,R)` derive fortement hors echantillon;
2. les controles impairs aleatoires produisent le meme biais;
3. le produit depend fortement de `R` sans plateau;
4. le produit depend fortement de quelques petits modules `q` instables;
5. la valeur cible n'apparait qu'apres ajustement de parametres.

## 9. Prochaine etape algorithmique

Implementer deux commandes separees:

1. `evaluate_montmory_filter.py`: deja disponible pour le filtre direct;
2. `evaluate_local_dynamics.py`: a creer pour calculer `mu_{q;X,R}`, `Sigma_q`, `B_q`, et `C_dyn`.

Les deux commandes doivent produire des CSV reproductibles.