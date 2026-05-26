# PRNG Structural Diagnostics v1.2 — Cahier de révision HAL

Superseded for publication by `Math/PRNG/publication/hal/hal-05633702v1/`.

Statut : document de préparation interne pour une révision HAL.

Objet : définir les ajouts nécessaires à la version HAL v1.0 afin de produire une version v1.2 plus robuste, plus calibrée statistiquement et plus défendable scientifiquement.

Positionnement : la v1.2 ne remplace pas la v1.0. Elle la renforce. La v1.0 introduit le cadre structurel ; la v1.2 clarifie le statut des ratios bruts et ajoute une calibration statistique des variances seed-conditionnées.

Bundle reproductible associé : [`prng-ztest`](./prng-ztest/README.md).

---

## 1. Résumé exécutif

La version HAL v1.0 introduit un cadre de diagnostic structurel des PRNG pour les workloads Monte Carlo :

- sensibilité à la seed ;
- dispersion de variance fonctionnelle ;
- score `GSQI` ;
- instabilité de transition `epsilon_T` ;
- diagnostics cross-backend ;
- limites de reproductibilité ;
- logs BigCrush importés.

La version v1.2 ajoute une couche statistiquement calibrée :

```math
Z_s(f)=F_0(V_s(f)).
```

Sous le modèle nul, les valeurs `Z_s(f)` doivent être uniformes :

```math
Z_s(f)\sim U[0,1].
```

Cette couche répond directement à une critique méthodologique importante : une variance empirique varie naturellement. Le fait qu'elle varie selon la seed ne suffit pas, à lui seul, à conclure à une instabilité du PRNG. Il faut comparer cette variation à sa loi attendue.

La v1.2 reformule donc les ratios bruts :

```math
\rho_f=
\frac{\max_s V_s(f)}
{\min_{s,V_s(f)>0}V_s(f)}
```

comme des alertes exploratoires, et non comme des preuves d'anomalie.

Diagnostic v1.2 :

```math
\boxed{
\rho_f\text{ grand} \Rightarrow \text{alerte brute}
}
```

puis :

```math
\boxed{
Z_s(f)\not\sim U[0,1] \Rightarrow \text{anomalie statistiquement calibrée}
}
```

---

## 2. Message scientifique central

La phrase centrale de la v1.2 doit être :

```math
\boxed{
\text{Un ratio inter-seed élevé n'est pas, à lui seul, une preuve d'instabilité PRNG.}
}
```

La contribution méthodologique est :

```math
\boxed{
\text{une calibration statistique des variances seed-conditionnées par leur loi nulle.}
}
```

Formulation anglaise recommandée :

> A large inter-seed variance ratio is not, by itself, evidence of PRNG instability. Version 1.2 adds a null-calibrated probability-integral-transform diagnostic for seed-conditioned Monte Carlo variances.

---

## 3. Changement de statut par rapport à v1.0

### v1.0

La v1.0 introduit la variance seed-conditionnée :

```math
V_s(f)
```

et le ratio de dispersion :

```math
\rho_f=
\frac{\max_s V_s(f)}
{\min_{s,V_s(f)>0}V_s(f)}.
```

Ces quantités décrivent la dispersion inter-seed.

### Limite de v1.0

Avec un faible nombre de réplications, par exemple :

```math
R=8,
```

les estimateurs de variance sont eux-mêmes très variables. Un grand ratio `rho_f` peut donc apparaître même sous un modèle idéal.

### v1.2

La v1.2 ajoute :

```math
Z_s(f)=F_0(V_s(f)).
```

Sous l'hypothèse nulle :

```math
Z_s(f)\sim U[0,1].
```

Conséquence :

- si les `Z_s` sont compatibles avec une loi uniforme, les ratios bruts doivent être relativisés ;
- si les `Z_s` ne sont pas compatibles avec une loi uniforme, il existe un signal seed-conditionné calibré.

---

## 4. Motivation de la calibration

Texte recommandé pour la version anglaise :

> The initial framework introduced inter-seed variance dispersion ratios as practical diagnostics. However, empirical variances are themselves random quantities. Therefore, large max/min ratios may occur even under a null model, especially when the number of replicates is small. To distinguish ordinary sampling fluctuation from genuine seed-conditioned instability, we introduce a calibrated probability-integral-transform diagnostic.

Version française :

> La version initiale introduisait des ratios de dispersion inter-seed comme diagnostics pratiques. Cependant, une variance empirique est elle-même une variable aléatoire. Des ratios max/min élevés peuvent donc apparaître naturellement, surtout lorsque le nombre de réplications est faible. Pour distinguer les fluctuations ordinaires d'une instabilité réellement conditionnée par la seed, nous ajoutons un diagnostic calibré par transformation intégrale de probabilité.

---

## 5. Diagnostic calibré `Z_s`

Pour une seed `s`, un intégrande `f`, une taille d'échantillon `N` et `R` réplications :

```math
I_{s,r}(f)
=
\frac1N\sum_{t=1}^{N}f(u_{s,r,t}).
```

Moyenne sur les réplications :

```math
\bar I_s(f)
=
\frac1R\sum_{r=1}^{R}I_{s,r}(f).
```

Variance seed-conditionnée :

```math
V_s(f)
=
\frac1{R-1}
\sum_{r=1}^{R}
\left(
I_{s,r}(f)-\bar I_s(f)
\right)^2.
```

Sous l'hypothèse nulle d'un PRNG idéal et d'un estimateur Monte Carlo approximativement gaussien :

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

Sous l'hypothèse nulle :

```math
\boxed{
Z_s(f)\sim U[0,1].
}
```

---

## 6. Variances théoriques des intégrandes

Pour `f_1(u)=u` :

```math
\sigma_{f_1}^2=\frac1{12}.
```

Pour `f_2(u)=sin(2 pi u)` :

```math
\sigma_{f_2}^2=\frac12.
```

Pour `f_3(u)=u^2` :

```math
\mathbb E[u^2]=\frac13,
\qquad
\mathbb E[u^4]=\frac15,
```

donc :

```math
\sigma_{f_3}^2
=
\frac15-\frac19
=
\frac4{45}.
```

Pour `f_4(u)=1_{u>0.99}` :

```math
p=0.01,
\qquad
\sigma_{f_4}^2=p(1-p)=0.0099.
```

Pour les indicateurs d'événements rares et les petits `N`, l'approximation normale peut être imparfaite. Une calibration binomiale exacte ou une calibration bootstrap peut être utilisée comme contrôle de robustesse.

---

## 7. Indicateurs à rapporter en v1.2

### Ratio brut

```math
\rho_f
=
\frac{\max_s V_s(f)}
{\min_{s,V_s(f)>0}V_s(f)}.
```

Statut :

```math
\boxed{\text{alerte brute}}
```

### Ratio robuste

```math
\rho_f^{95/5}
=
\frac{Q_{95}(V_s(f))}
{Q_5(V_s(f))}.
```

Statut :

```math
\boxed{\text{dispersion robuste}}
```

### Test KS des `Z_s`

On teste :

```math
\{Z_s(f):s\in\mathcal B\}
```

contre :

```math
U[0,1].
```

On rapporte :

```math
KS_f,
\qquad
p_{\rm KS}.
```

### Taux de seeds extrêmes

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

### Nombre effectif de tirages

```math
N_{\rm eff,s}(f)
=
\frac{\sigma_f^2}{V_s(f)}.
```

Ratio :

```math
\eta_s(f)
=
\frac{N_{\rm eff,s}(f)}{N}.
```

Il faut rapporter :

```math
Q_5(\eta_s(f)),
\quad
Q_{50}(\eta_s(f)),
\quad
Q_{95}(\eta_s(f)).
```

Point d'interprétation important : ici `V_s(f)` désigne la variance des estimateurs Monte Carlo répétés `I_{s,r}(f)` pour une seed fixée, pas la variance brute des valeurs ponctuelles `f(u_t)`.

---

## 8. Figures à produire

### Figure 1 — Histogrammes `Z_s`

Un histogramme par intégrande :

- `identity` ;
- `sin` ;
- `quadratic` ;
- `rare_099`.

Chaque figure peut afficher plusieurs PRNG. Objectif :

```math
\boxed{
\text{voir si les }Z_s\text{ ressemblent à une uniforme.}
}
```

### Figure 2 — Ratio brut vs calibration

Table ou figure montrant `rho_f` et `p_KS(Z_s)`. Objectif :

```math
\boxed{
\text{montrer qu'un ratio brut élevé peut être compatible avec la loi nulle.}
}
```

### Figure 3 — Taux de seeds extrêmes

Barplot de `Q_tail(f)` avec ligne de référence :

```math
0.02.
```

### Figure 4 — Efficacité `N_eff/N`

Distribution ou quantiles de :

```math
\eta_s(f)=\frac{N_{\rm eff,s}(f)}{N}.
```

---

## 9. Tables à inclure

### Table 1 — Résumé par PRNG et intégrande

| PRNG | Backend | Integrand | `rho_max/min` | `rho_95/5` | KS stat | KS p-value | Extreme rate | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|

### Table 2 — Quantiles `N_eff/N`

| PRNG | Backend | Integrand | `Q5` | `Q50` | `Q95` |
|---|---|---:|---:|---:|---:|

### Table 3 — Interprétation

| Situation | Interprétation |
|---|---|
| `rho_f` élevé, `Z_s ~ U[0,1]` | ratio brut impressionnant mais compatible avec le bruit |
| `rho_f` élevé, `Z_s` non uniforme | anomalie seed-conditionnée plausible |
| `Q_tail >> 0.02` | excès de seeds extrêmes |
| `N_eff/N << 1` | perte d'efficacité Monte Carlo |

---

## 10. Protocole expérimental recommandé

Configuration minimale pour valider le pipeline :

```math
100\ \text{seeds},
\quad
R=8\ \text{réplications},
\quad
N=50\,000.
```

Configuration cible :

```math
100\ \text{seeds},
\quad
R\geq8,
\quad
N=10^6.
```

Configuration robuste :

```math
100\ \text{seeds},
\quad
R\geq16,
\quad
N\geq10^6.
```

Plus `R` est grand, plus le diagnostic `V_s(f)` est stable.

---

## 11. Format de données à publier

Le fichier central doit utiliser une ligne par réplication Monte Carlo :

```csv
generator,backend,seed,integrand,replicate,N,estimate
Philox,cpu,0,rare_099,0,1000000,0.00997
Philox,cpu,0,rare_099,1,1000000,0.01004
```

À partir de ce fichier, on peut reproduire :

- `V_s` ;
- `T_s` ;
- `Z_s` ;
- `N_eff` ;
- les histogrammes ;
- les tests KS ;
- les ratios bruts.

---

## 12. Bundle reproductible v1.2

Le bundle de référence est publié dans :

```text
Math/PRNG/WIP/prng-ztest/
```

Structure cible :

```text
prng-ztest/
  README.md
  requirements.txt
  scripts/
    generate_public_prng_estimates.py
    compute_z_scores.py
    plot_z_histograms.py
  data/
    public_prng_estimates.csv
  results/
    z_scores_table.csv
    z_summary.csv
  figures/
    hist_Zs_identity.png
    hist_Zs_sin.png
    hist_Zs_quadratic.png
    hist_Zs_rare_099.png
```

La version WIP actuelle inclut déjà le README, les scripts et un résumé `z_summary.csv` généré sur VPS. Les fichiers complets `data`, `z_scores_table` et `figures` peuvent être ajoutés au bundle lorsque le run cible `N=10^6` sera figé.

---

## 13. Interprétation scientifique attendue

La v1.2 doit établir clairement :

```math
\boxed{
\text{les ratios max/min sont utiles comme alertes, mais insuffisants comme preuves.}
}
```

```math
\boxed{
\text{le diagnostic }Z_s=F_0(V_s)\text{ distingue fluctuations normales et anomalies.}
}
```

```math
\boxed{
\text{une instabilité seed-conditionnée doit être définie par écart à la loi nulle.}
}
```

Si certains résultats relativisent la v1.0, il ne faut pas écrire que la v1.0 était fausse. Formulation recommandée :

> Version 1.0 introduced structural dispersion ratios as practical indicators. Version 1.2 refines their interpretation by treating them as exploratory alerts and adding a null-calibrated probability-integral-transform diagnostic.

En français :

> La version 1.0 introduisait les ratios de dispersion structurelle comme indicateurs pratiques. La version 1.2 précise leur interprétation en les considérant comme des alertes exploratoires, puis ajoute un diagnostic calibré par transformation intégrale de probabilité.

---

## 14. Non-claims à ajouter

La v1.2 doit préciser :

```math
\boxed{
\text{le test }Z_s\text{ n'est pas une preuve mathématique de qualité PRNG.}
}
```

```math
\boxed{
\text{il dépend du modèle nul choisi.}
}
```

```math
\boxed{
\text{l'approximation }\chi^2\text{ suppose des estimateurs approximativement gaussiens.}
}
```

```math
\boxed{
\text{pour les rare-events et petits }N,\text{ une calibration binomiale ou bootstrap peut être préférable.}
}
```

```math
\boxed{
\text{un test non rejeté n'établit pas l'absence de défaut ; il indique seulement l'absence d'anomalie détectée dans ce protocole.}
}
```

---

## 15. Point particulier : rare events

Pour :

```math
f(u)=\mathbf 1_{\{u>0.99\}},
```

l'estimateur est binomial :

```math
K\sim \mathrm{Binomial}(N,0.01),
\qquad
I_N=K/N.
```

La variance théorique est :

```math
\frac{0.01\cdot0.99}{N}.
```

Pour petits `N` ou pour des seuils plus extrêmes :

```math
p\ll1,
```

l'approximation normale peut être imparfaite. La v1.2 doit donc conserver la phrase de prudence suivante :

> For rare-event indicators, exact binomial or bootstrap calibration may be used as a robustness check.

---

## 16. Structure recommandée du papier v1.2

1. Introduction : rappeler la v1.0 et expliquer pourquoi une calibration est nécessaire.
2. Seed-conditioned variance : redéfinir `V_s(f)`.
3. Limitation of raw dispersion ratios : expliquer pourquoi `rho_f` peut être trompeur.
4. Null-calibrated diagnostic : développer `T_s(f)` et `Z_s(f)`.
5. Experimental protocol : décrire seeds, `N`, `R`, PRNG publics et intégrandes.
6. Results : histogrammes, KS, extreme rate, `N_eff`.
7. Discussion : interpréter les cas où ratio brut élevé mais `Z_s` uniforme.
8. Limitations : rare events, petits `R`, modèle nul, dépendance au protocole.
9. Conclusion : expliquer que la v1.2 transforme les ratios bruts en diagnostics calibrés.

---

## 17. Changelog recommandé

```text
Version 1.2 changes:
- adds null-calibrated variance diagnostic Z_s = F_0(V_s);
- clarifies that raw inter-seed ratios are exploratory alerts;
- adds KS and tail-rate tests on Z_s;
- adds N_eff interpretation from replicated estimator variance;
- adds reproducible CPU-only reference pipeline;
- adds rare-event calibration caveat;
- preserves the v1.0 framework and non-claims.
```

---

## 18. Verdict

La v1.2 est publiable comme révision HAL parce qu'elle apporte une amélioration méthodologique réelle :

```math
\boxed{
\text{elle transforme un diagnostic brut en test calibré sous loi nulle.}
}
```

Elle ne détruit pas la v1.0. Elle la rend plus solide :

```math
\boxed{
\text{v1.0 = cadre structurel}
}
```

```math
\boxed{
\text{v1.2 = cadre structurel + calibration statistique}
}
```

Contribution principale :

```math
\boxed{
\text{distinguish raw seed variance dispersion from statistically calibrated seed instability.}
}
```
