# TACM — Formules diagnostiques PRNG v1.1

Statut : note de développement mathématique et opérationnel.

Objectif : formuler TACM comme un système cohérent de diagnostics dérivé d'un objet central : les mesures empiriques, unidimensionnelles et multidimensionnelles, du flux PRNG. Les formules ci-dessous ne constituent pas une preuve de hasard ni de sécurité cryptographique. Elles définissent un cadre d'audit reproductible, calibrable et exploitable pour la simulation Monte Carlo, la finance, le HPC et les backends GPU.

Cette note distingue :

- **Définitions** : objets mesurés directement.
- **Diagnostics** : scores empiriques calculables.
- **Approximations** : formules interprétables sous hypothèses explicites.
- **Quantités à calibrer** : constantes, seuils et poids ajustés expérimentalement.

---

## 1. Objet central : mesures empiriques du flux

Pour une seed `s`, un backend `b`, et un horizon `N`, un PRNG produit :

```math
u_{s,b,1},\ldots,u_{s,b,N}\in[0,1).
```

La mesure empirique marginale est :

```math
\mu^{(1)}_{s,b,N}
=
\frac1N\sum_{t=1}^{N}\delta_{u_{s,b,t}}.
```

L'idéal marginal est la mesure de Lebesgue `\lambda` sur `[0,1)`.

Les dépendances temporelles ne sont pas visibles dans `\mu^{(1)}`. On introduit donc les mesures empiriques de blocs :

```math
\mu^{(k)}_{s,b,N}
=
\frac1{N-k+1}
\sum_{t=1}^{N-k+1}
\delta_{(u_{s,b,t},\ldots,u_{s,b,t+k-1})},
\qquad k\geq2.
```

L'idéal `k`-dimensionnel est :

```math
\lambda^{\otimes k}.
```

Principe central :

```math
\boxed{
\text{Un bon flux PRNG produit des mesures empiriques stables selon la seed, le backend, les blocs temporels et le workload.}
}
```

TACM mesure donc :

```math
\mu^{(k)}_{s,b,N}\approx\lambda^{\otimes k},
```

au travers de bacs, transitions, intégrandes, lanes GPU, backends et observables financières.

---

## 2. Couverture marginale : diagnostic chi-carre

On découpe `[0,1)` en `m` bacs `I_1,\ldots,I_m`. Pour une seed `s` :

```math
O_i(s)=\#\{t:u_{s,t}\in I_i\},
\qquad
E_i=\frac Nm.
```

Le diagnostic classique est :

```math
\chi^2_s
=
\sum_{i=1}^{m}
\frac{(O_i(s)-E_i)^2}{E_i}.
```

Sous l'hypothèse de référence IID uniforme, et avec des effectifs attendus suffisants :

```math
\chi^2_s\approx\chi^2_{m-1}.
```

Version normalisée :

```math
\chi^2_{\rm norm}(s)=\frac{\chi^2_s}{m-1}.
```

Idéalement :

```math
\chi^2_{\rm norm}(s)\approx1.
```

Interprétation :

- `chi2_norm >> 1` : sur- ou sous-représentation de certains bacs.
- `chi2_norm << 1` : flux trop régulier, stratification artificielle, ou séquence quasi-déterministe.

Score borné avec garde-fou numérique :

```math
\Phi_\chi
=
\exp\left(-|\log(\max(\chi^2_{\rm norm},\varepsilon_\chi))|\right),
\qquad
\varepsilon_\chi>0.
```

Option plus statistique : remplacer `\Phi_\chi` par un score bilatéral dérivé de la p-value du test chi-carre. Ce choix doit être calibré selon `N`, `m` et la famille de générateurs.

Statut :

```math
\boxed{
\chi^2_{\rm norm}\text{ mesure la couverture marginale, pas le mélange temporel.}
}
```

---

## 3. Carte chi-carre bidimensionnelle

On observe les couples successifs :

```math
(u_t,u_{t+1}).
```

On découpe `[0,1)^2` en une grille `q x q`. Pour chaque cellule `(i,j)` :

```math
E_{ij}=\frac{N-1}{q^2},
```

```math
O_{ij}
=
\#\{t:(u_t,u_{t+1})\in I_i\times I_j\}.
```

Résidu standardisé :

```math
R_{ij}
=
\frac{O_{ij}-E_{ij}}{\sqrt{E_{ij}}}.
```

Score global :

```math
\chi^2_{2D}
=
\sum_{i,j}
\frac{(O_{ij}-E_{ij})^2}{E_{ij}},
\qquad
\chi^2_{2D,\rm norm}
=
\frac{\chi^2_{2D}}{q^2-1}.
```

Sous IID uniforme, `\chi^2_{2D}` est approximativement de loi chi-carre à `q^2-1` degrés de liberté, sous réserve d'effectifs attendus suffisants. Dans un PRNG déterministe, cette loi reste une référence de calibration, pas une garantie asymptotique automatique.

Statut :

```math
\boxed{
\text{La carte 2D visualise localement les défauts de }\mu^{(2)}_{s,b,N}.
}
```

---

## 4. Projection markovienne finie et lambda-gap

On définit un quantificateur :

```math
Q_q:[0,1)\to\{1,\ldots,q\}.
```

Chaque sortie devient :

```math
b_t=Q_q(u_t).
```

Convention TACM : la matrice de transition est **row-stochastic** :

```math
P_s(i,j)
=
\frac{
\#\{t:b_t=i,\ b_{t+1}=j\}
}{
\#\{t:b_t=i\}
}.
```

Chaque ligne somme à `1` lorsque l'état source est visité. Les lignes non visitées doivent être traitées explicitement : remplissage uniforme, exclusion documentée, ou lissage de Laplace. Le choix doit être enregistré dans l'audit.

Cette matrice n'est pas la dynamique interne du PRNG. C'est une projection markovienne empirique du flux observé.

Les valeurs propres de `P_s` sont :

```math
1=\lambda_1,\lambda_2,\ldots,\lambda_q.
```

On définit :

```math
\boxed{
\mathrm{Gap}_s
=
1-|\lambda_2(P_s)|.
}
```

Interprétation :

- `Gap_s` proche de `1` : mélange rapide dans la projection finie.
- `Gap_s` proche de `0` : mémoire persistante, structure lente, cycle visible ou mauvais mélange projeté.

Remarque d'implémentation : une matrice column-stochastic transposée a les mêmes valeurs propres. Les résultats spectraux sont donc invariants par transposition, mais l'API et les docs doivent exposer une convention unique.

---

## 5. Instabilité transitionnelle inter-seed

Pour un ensemble de seeds `B`, on calcule une matrice par seed :

```math
P_s,\qquad s\in\mathcal B.
```

Matrice moyenne :

```math
\bar P
=
\frac1{|\mathcal B|}
\sum_{s\in\mathcal B}P_s.
```

Instabilité transitionnelle :

```math
\boxed{
\epsilon_T(\mathcal B,N,q)
=
\max_{s\in\mathcal B}
\|P_s-\bar P\|_\infty.
}
```

Ici `||.||_infty` peut désigner :

```math
\|A\|_\infty=\max_i\sum_j |A_{ij}|,
```

ou, pour une lecture locale plus sévère :

```math
\|A\|_{\max}=\max_{i,j}|A_{ij}|.
```

La norme doit être indiquée dans le profil de calibration.

Statut :

```math
\boxed{
\epsilon_T\text{ mesure la stabilité des transitions projetées selon la seed.}
}
```

---

## 6. Entropie de mélange

Distribution empirique des bacs :

```math
\pi_s(i)
=
\frac{\#\{t:b_t=i\}}{N}.
```

Entropie :

```math
H_s
=
-\sum_{i=1}^q \pi_s(i)\log\pi_s(i).
```

Entropie normalisée :

```math
\boxed{
\tilde H_s
=
\frac{H_s}{\log q}.
}
```

Agrégations utiles :

```math
H_{\rm mix}^{Q5}
=
Q_5(\tilde H_s),
\qquad
\bar H_{\rm mix}
=
\frac1{|\mathcal B|}\sum_s \tilde H_s.
```

Statut :

```math
\boxed{
\tilde H_s\text{ mesure l'étalement marginal discret, complémentaire du lambda-gap.}
}
```

---

## 7. Stabilité fonctionnelle Monte Carlo

On choisit une famille d'intégrandes :

```math
\mathcal F=\{f_1,\ldots,f_k\}.
```

Exemples :

```math
f_1(u)=u,
\qquad
f_2(u)=\sin(2\pi u),
\qquad
f_3(u)=u^2,
\qquad
f_4(u)=\mathbf 1_{u>0.99}.
```

Pour une seed `s`, une réplication `r`, et une taille `N` :

```math
I_{s,r}(f)
=
\frac1N
\sum_{t=1}^N f(u_{s,r,t}).
```

Sur `R` réplications :

```math
\bar I_s(f)
=
\frac1R
\sum_{r=1}^{R}I_{s,r}(f).
```

Variance seed-conditionnée :

```math
\boxed{
V_s(f)
=
\frac1{R-1}
\sum_{r=1}^{R}
\left(
I_{s,r}(f)-\bar I_s(f)
\right)^2.
}
```

La définition suppose que les réplications sont construites par des sous-flux indépendants, des sauts contrôlés, ou des seeds dérivées de manière auditée. Ce point est critique pour les backends GPU.

Dispersion inter-seed :

```math
\rho_f
=
\frac{\max_s V_s(f)}
{\min_{s,V_s(f)>0}V_s(f)}.
```

Version robuste :

```math
\rho_f^{95/5}
=
\frac{Q_{95}(V_s(f))}
{Q_5(V_s(f))}.
```

---

## 8. GSQI : stabilité inter-seed

Score brut :

```math
\boxed{
GSQI(G;\mathcal B,\mathcal F)
=
\exp\left(
-\frac1{|\mathcal F|}
\sum_{f\in\mathcal F}
\log\rho_f
\right).
}
```

Version robuste :

```math
\boxed{
GSQI_{95/5}
=
\exp\left(
-\frac1{|\mathcal F|}
\sum_{f\in\mathcal F}
\log\rho_f^{95/5}
\right).
}
```

Interprétation :

- `GSQI` proche de `1` : faible dispersion inter-seed.
- `GSQI` faible : instabilité inter-seed.

Statut :

```math
\boxed{
GSQI\text{ est un score d'audit, pas une preuve de hasard ni de sécurité.}
}
```

---

## 9. Calibration statistique : Z_s = F_0(V_s)

Sous le modèle nul IID uniforme, pour un intégrande `f` :

```math
I_{s,r}(f)
\approx
\mathcal N
\left(
\mu_f,\frac{\sigma_f^2}{N}
\right).
```

Alors :

```math
T_s(f)
=
\frac{(R-1)V_s(f)}
{\sigma_f^2/N}
\sim
\chi^2_{R-1}.
```

On définit :

```math
\boxed{
Z_s(f)
=
F_{\chi^2_{R-1}}
\left(
T_s(f)
\right).
}
```

Sous le modèle nul :

```math
\boxed{
Z_s(f)\sim U[0,1].
}
```

Variances théoriques utiles :

| Integrande | Variance `sigma_f^2` |
|---|---:|
| `f(u)=u` | `1/12` |
| `f(u)=sin(2*pi*u)` | `1/2` |
| `f(u)=u^2` | `4/45` |
| `f(u)=1_{u>0.99}` | `0.01*0.99` |

Tests sur `Z_s(f)` :

```math
KS_f
=
\sup_z
\left|
\hat F_Z(z)-z
\right|.
```

Taux de valeurs extrêmes :

```math
Q_{\rm tail}(f)
=
\frac1{|\mathcal B|}
\#\{s:Z_s(f)<0.01\ \text{ou}\ Z_s(f)>0.99\}.
```

Sous uniformité :

```math
\mathbb E[Q_{\rm tail}]\approx0.02.
```

Un excès important signale des seeds ou sous-flux atypiques.

---

## 10. Nombre effectif de tirages

Sous Monte Carlo idéal :

```math
\mathrm{Var}(I_N(f))
=
\frac{\sigma_f^2}{N}.
```

Si l'on observe :

```math
V_s(f),
```

on définit :

```math
\boxed{
N_{\rm eff,s}^{\rm func}(f)
=
\frac{\sigma_f^2}{V_s(f)}.
}
```

Efficacité relative :

```math
\boxed{
\eta_s(f)
=
\frac{N_{\rm eff,s}^{\rm func}(f)}{N}
=
\frac{\sigma_f^2/N}{V_s(f)}.
}
```

Agrégation prudente :

```math
\eta_5(f)=Q_5(\eta_s(f)).
```

Score global :

```math
\boxed{
\eta_{\rm MC}
=
\exp\left(
\frac1{|\mathcal F|}
\sum_{f\in\mathcal F}
\log Q_5(\eta_s(f))
\right).
}
```

Pour un PRNG classique, on peut borner :

```math
\eta_s(f)\leftarrow \min(1,\eta_s(f)).
```

Pour une méthode QMC explicitement déclarée, un `N_eff>N` peut être conservé, mais doit être interprété comme un gain d'efficacité numérique, pas comme plus de tirages physiques.

---

## 11. Proxy structurel de N_eff

Proxy initial :

```math
N_{\rm eff}^{\rm struct}
=
N\cdot
\frac{\mathrm{Gap}}
\chi^2_{\rm norm}
\cdot
\frac1{c_{\rm mix}}.
```

Version opérationnelle bornée :

```math
\boxed{
\eta_{\rm struct}
=
\min\left(
1,
\frac{\mathrm{Gap}}
\max(\chi^2_{\rm norm},\varepsilon_\chi)c_{\rm mix}}
\right),
\qquad
N_{\rm eff}^{\rm struct}=N\eta_{\rm struct}.
}
```

Pour QMC :

```math
\eta_{\rm struct}^{\rm QMC}
=
\frac{\mathrm{Gap}}
\max(\chi^2_{\rm norm},\varepsilon_\chi)c_{\rm mix}},
```

avec cap séparé `eta_qmc_max` calibré.

Statut :

```math
\boxed{
N_{\rm eff}^{\rm struct}\text{ est un proxy calibrable à comparer à }N_{\rm eff}^{\rm func}.
}
```

La validation empirique consiste à mesurer la corrélation entre :

```math
N_{\rm eff}^{\rm struct}
\quad\text{et}\quad
N_{\rm eff}^{\rm func}(f).
```

---

## 12. Variance diagnostique

Approximation :

```math
\boxed{
\widehat{\mathrm{Var}}_{\rm diag}(\hat I_N(f))
=
\frac{\sigma_f^2}{N}
\cdot
\max(\chi^2_{\rm norm},\varepsilon_\chi)
\cdot
\frac1{\max(\mathrm{Gap},\varepsilon_{\rm gap})}
\cdot
\kappa_f.
}
```

Les constantes :

- `epsilon_chi` évite les divisions ou logs dégénérés.
- `epsilon_gap` évite l'explosion numérique lorsque le gap projeté est nul.
- `kappa_f` dépend de l'intégrande et doit être calibré.

Statut :

```math
\boxed{
\text{Approximation diagnostique à calibrer, non borne universelle.}
}
```

---

## 13. VaR et CVaR

Pour un quantile :

```math
q_p=F_X^{-1}(p),
```

l'estimateur de quantile vérifie asymptotiquement :

```math
\mathrm{Var}(\hat q_p)
\approx
\frac{p(1-p)}
{N f_X(q_p)^2}.
```

En remplaçant `N` par `N_eff` :

```math
\boxed{
\mathrm{Var}_{\rm diag}(\hat q_p)
\approx
\frac{p(1-p)}
{N_{\rm eff}f_X(q_p)^2}.
}
```

Pour une erreur cible `epsilon` :

```math
\boxed{
N_{\rm target}^{\rm VaR}
=
\frac{p(1-p)}
{\varepsilon^2 f_X(q_p)^2}
\cdot
\frac{N}{N_{\rm eff}}.
}
```

CVaR :

```math
\mathrm{CVaR}_p
=
\mathbb E[X\mid X>q_p].
```

Approximation prudente :

```math
\boxed{
\mathrm{Var}_{\rm diag}(\widehat{\mathrm{CVaR}}_p)
\approx
\frac{
\mathrm{Var}(X\mid X>q_p)
}{
(1-p)N_{\rm eff}
}
\cdot
c_{\rm tail}.
}
```

Cette formule est une approximation diagnostique, pas une identité universelle. Selon la convention d'estimation de la CVaR et selon que l'incertitude sur le quantile `q_p` est incluse ou non, une pénalité supplémentaire liée à `(1-p)` peut apparaître. Le facteur `c_tail` absorbe cette correction ainsi que l'incertitude liée à la densité de queue et aux dépendances résiduelles ; il doit être calibré empiriquement.

---

## 14. Drift local

Moyenne partielle :

```math
\bar u_t
=
\frac1t\sum_{i=1}^{t}u_i.
```

Drift maximal :

```math
\boxed{
\Delta_U(t)
=
\sup_{1\leq r\leq t}
\left|
\bar u_r-\frac12
\right|.
}
```

Score normalisé :

```math
\boxed{
R_U(t)
=
\sqrt t\,\Delta_U(t).
}
```

Un `R_U(t)` élevé peut signaler warm-up, dérive précoce, seed atypique ou bug de conversion uniforme.

---

## 15. Score d'audit global

Sous-scores :

```math
S_{\rm trans}
=
\mathrm{Gap}
\cdot
\exp(-|\log(\max(\chi^2_{\rm norm},\varepsilon_\chi))|).
```

```math
S_{\rm ent}=Q_5(\tilde H_s).
```

```math
S_{\rm MC}=\eta_{\rm MC}.
```

```math
S_Z
=
\exp(-c_Z KS_{\rm avg}).
```

```math
S_{\rm tail}
=
\exp\left(
-c_{\rm tail}
\max\left(
0,
\frac{Q_{\rm tail}}{0.02}-1
\right)
\right).
```

Agrégation :

```math
\boxed{
S_{\rm audit}
=
\left(
S_{\rm trans}^{w_1}
S_{\rm ent}^{w_2}
S_{\rm MC}^{w_3}
S_Z^{w_4}
S_{\rm tail}^{w_5}
\right)^{
1/(w_1+\cdots+w_5)
}.
}
```

Statut :

```math
\boxed{
S_{\rm audit}\text{ est un score produit calibrable, non une norme officielle.}
}
```

---

## 16. Règle de décision

Décision :

```math
\mathrm{decision}
=
D(S_{\rm audit},Q_{\rm tail},N_{\rm eff}/N,\epsilon_T).
```

Exemple opérationnel :

- `continue` si `S_audit >= theta_ok`.
- `reseed` si `S_audit < theta_ok` mais anomalie localisée sur quelques seeds.
- `switch` si `S_audit < theta_bad`, ou `Q_tail` très supérieur à `0.02`, ou `N_eff/N` trop faible.

Les seuils `theta_ok`, `theta_bad`, `tail_multiplier`, `eta_min` sont des paramètres de politique de risque.

---

## 17. Temps de décroissance diagnostique

Modèle projeté :

```math
B_t=B_0(1-\mathrm{Gap})^t.
```

On veut :

```math
B_t\leq\varepsilon_{\rm tol}.
```

Donc :

```math
\boxed{
t_{\rm mix}^{\rm diag}
=
\left\lceil
\frac{
\log(\varepsilon_{\rm tol}/B_0)
}{
\log(1-\mathrm{Gap})
}
\right\rceil.
}
```

Forme numérique stable pour petits gaps :

```math
t_{\rm mix}^{\rm diag}
\approx
\left\lceil
\frac{
\log(B_0/\varepsilon_{\rm tol})
}{
\mathrm{Gap}
}
\right\rceil.
```

Statut :

```math
\boxed{
t_{\rm mix}^{\rm diag}\text{ est un temps de décroissance dans la projection finie.}
}
```

---

## 18. Benchmark relatif

Pour comparer deux moteurs `A` et `B` :

```math
\boxed{
G_{A/B}
=
\left(
\frac{\mathrm{Gap}_A}{\mathrm{Gap}_B}
\right)^\alpha
\left(
\frac{\Phi_{\chi,A}}{\Phi_{\chi,B}}
\right)^\beta
\left(
\frac{N_{\rm eff,A}/N}{N_{\rm eff,B}/N}
\right)^\gamma
\left(
\frac{t_B}{t_A}
\right)^\delta.
}
```

Profils de poids :

- `speed_only`
- `stability_only`
- `rare_event_sensitive`
- `balanced`

Si :

```math
G_{A/B}>1,
```

alors `A` est meilleur que `B` selon le profil choisi.

---

## 19. Reproductibilité backend

Pour chaque backend `b`, on calcule :

```math
H_b(s,N)
=
SHA256(x^{(b)}_{s,0}\Vert\cdots\Vert x^{(b)}_{s,N-1}).
```

Reproductibilité bit-exacte :

```math
\boxed{
H_{\rm CPU}=H_{\rm CUDA}=H_{\rm Metal}.
}
```

Si la reproductibilité bit-exacte n'est pas requise ou impossible, on mesure :

```math
D_{\rm backend}
=
\max_{b_1,b_2}
\|\mu^{(k)}_{b_1}-\mu^{(k)}_{b_2}\|_{\rm TV},
```

ou :

```math
\Delta I_{\rm backend}
=
\max_{b_1,b_2,f}
|I_{b_1}(f)-I_{b_2}(f)|.
```

---

## 20. Diagnostic multi-lane GPU

Pour un générateur parallèle avec lanes `ell=1,...,L` :

```math
u_{\ell,t}.
```

Corrélation inter-lane :

```math
C_{\ell,m}
=
\mathrm{Corr}(u_{\ell,t},u_{m,t}).
```

Collision de sous-flux :

```math
\mathrm{Collisions}
=
\#\{(\ell,m,t,r):x_{\ell,t}=x_{m,r}\}.
```

Distance entre lanes :

```math
D_{\rm lane}
=
\max_{\ell,m}
\|\mu_\ell-\mu_m\|_{\rm TV}.
```

Hash par lane :

```math
H_\ell(s,N)
=
SHA256(x_{\ell,0}\Vert\cdots\Vert x_{\ell,N-1}).
```

Ces diagnostics sont essentiels pour CUDA, Metal et tout générateur massivement parallèle.

---

## 21. Architecture TACM v1.1

Les formules TACM se regroupent en sept dimensions :

| Dimension | Role |
|---|---|
| `S_dist` | Uniformité brute, chi-carre, KS, AD |
| `S_trans` | Projection markovienne, lambda-gap, stabilité transitionnelle |
| `S_func` | Variance fonctionnelle inter-seed |
| `S_Z` | Calibration statistique `Z_s=F_0(V_s)` |
| `S_backend` | Reproductibilité CPU/GPU |
| `S_lane` | Stabilité multi-lane GPU |
| `S_perf` | Performance temporelle |

Score final :

```math
\boxed{
S_{\rm TACM}
=
\left(
S_{\rm dist}^{w_d}
S_{\rm trans}^{w_t}
S_{\rm func}^{w_f}
S_Z^{w_z}
S_{\rm backend}^{w_b}
S_{\rm lane}^{w_l}
S_{\rm perf}^{w_p}
\right)^{
1/\sum w
}.
}
```

---

## 22. Statut des formules

| Formule | Statut |
|---|---|
| `mu^(1)_{s,b,N}` | définition marginale |
| `mu^(k)_{s,b,N}` | définition bloc / dépendance temporelle |
| `chi2_norm` | diagnostic classique sous référence IID |
| `Gap=1-|lambda_2|` | diagnostic spectral fini projeté |
| `epsilon_T` | diagnostic seed/backend |
| `V_s(f)` | définition empirique |
| `rho_f` | dispersion brute |
| `Z_s=F_0(V_s)` | calibration statistique sous modèle nul |
| `N_eff_func=sigma_f^2/V_s` | définition fonctionnelle |
| `N_eff_struct` | proxy diagnostique borné |
| `Var_diag` | approximation calibrable |
| VaR/CVaR avec `N_eff` | approximation finance |
| `S_audit` | score produit calibrable |
| `t_mix_diag` | modèle de décroissance projeté |
| `G_A/B` | benchmark composite |
| Hashes backend/lane | preuve de replay |

---

## 23. Conclusion

La contribution TACM n'est pas une addition d'indicateurs. C'est une chaîne :

```math
\boxed{
\text{mesures empiriques de blocs}
\rightarrow
\text{couverture}
\rightarrow
\text{mélange projeté}
\rightarrow
\text{stabilité fonctionnelle}
\rightarrow
\text{coût Monte Carlo}
\rightarrow
\text{impact VaR/CVaR}
\rightarrow
\text{décision opérationnelle}.
}
```

Cette structure peut servir :

- à une v1.1 scientifique du papier HAL ;
- à une spécification d'API d'audit PRNG ;
- à un produit industriel finance, HPC et simulation ;
- à une stratégie de validation CPU/CUDA/Metal reproductible.

Le point de rigueur essentiel est de toujours documenter les hypothèses : IID de référence, taille des bacs, traitement des états non visités, convention de matrice, mode de réplication, politique de seed, backend, lanes et seuils calibrés.
