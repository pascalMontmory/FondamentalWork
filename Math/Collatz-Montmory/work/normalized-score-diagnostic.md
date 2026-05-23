# Diagnostic du score Collatz normalise

Date: 2026-05-23  
Statut: note de travail, signal positif preliminaire

## 1. Motivation

Le seuil brut:

```math
S_B(p)=\min(\kappa_B(p),\kappa_B(p+2))
```

derive fortement avec `X`. Une explication plausible est que `\kappa_B(n)` se rapproche lentement de la derive moyenne du modele aleatoire Collatz accelere.

Pour une etape acceleree aleatoire:

```math
n\mapsto n/2
\quad\text{ou}\quad
n\mapsto (3n+1)/2,
```

la derive descendante moyenne en logarithme base 2 est:

```math
d=1-\frac12\log_2 3
\approx0.20751874963942196.
```

On teste donc le score centre:

```math
Z_B(p)=\left(S_B(p)-d\right)\log_2 p.
```

Ce score n'est pas prouve asymptotiquement naturel. Il est teste parce qu'il corrige la derive principale observee du seuil brut.

## 2. Resultat principal du test

Avec la densite cible:

```math
\rho_M\approx0.08178598968002705,
```

on calibre un seuil `alpha` sur une borne `X_train`, puis on teste hors echantillon.

### Calibration sur `10^6`

```text
alpha = 4.430733769771316
x        selected/twins      coefficient_estimate
1000000  0.0818527141282    0.1275000458
3000000  0.0799560313516    0.1240423880
10000000 0.0814963033304    0.1248565194
```

Contrairement au score brut, la proportion selectionnee reste proche de la cible jusqu'a `10^7`.

### Calibration sur `3*10^6`

```text
alpha = 4.397778941227406
x        selected/twins      coefficient_estimate
3000000  0.0818199197094    0.1269339917
10000000 0.0832768093332    0.1275843459
```

Le seuil calibre a `3*10^6` reste aussi proche de la cible a `10^7`.

## 3. Test par fenetres disjointes

Les bornes cumulatives peuvent masquer une derive. On teste donc les fenetres disjointes apres calibration.

Avec `alpha=4.430733769771316` calibre sur `10^6`:

```text
window              twin_count  selected  selected/twins
(1000000,3000000]   12763       1005      0.0787432422
(3000000,10000000]  38048       3133      0.0823433558
```

Avec `alpha=4.397778941227406` calibre sur `3*10^6`:

```text
window              twin_count  selected  selected/twins
(3000000,10000000]  38048       3199      0.0840780067
```

Ces fenetres restent proches de la cible `0.08178598968`. C'est un signal plus fort que le simple test cumulatif.

## 4. Comparaison avec le score brut

Le score brut calibre sur `10^6` donnait:

```text
x        selected/twins
1000000  0.0818527141
3000000  0.0642802523
10000000 0.0506172421
```

Le score centre-log calibre sur `10^6` donne:

```text
x        selected/twins
1000000  0.0818527141
3000000  0.0799560314
10000000 0.0814963033
```

C'est le premier diagnostic qui ne s'effondre pas immediatement hors echantillon.

## 5. Quantiles du score normalise

Le seuil superieur qui garde `rho_M` des paires evolue comme suit:

```text
X        count   mean      median    upper_rho_threshold
100000   1216    1.54146   1.00836   4.80192
300000   2986    1.37667   0.92522   4.53644
1000000  8161    1.27472   0.87513   4.43073
3000000  20924   1.19669   0.78092   4.39778
10000000 58972   1.13996   0.70425   4.42604
```

La moyenne et la mediane continuent de baisser, mais le quantile superieur cible devient beaucoup plus stable a partir de `10^6`.

## 6. Interpretation prudente

Ce resultat ne valide pas `C_Montmory`. Il indique seulement qu'une version normalisee du filtre Collatz est plus plausible que le seuil brut.

La piste devient:

```math
M_\alpha(p,p+2)=1
\quad\Longleftrightarrow\quad
\left(\min(\kappa_B(p),\kappa_B(p+2))-d\right)\log_2 p\ge\alpha.
```

Pour la valeur candidate, les tests preliminaires suggerent un seuil autour de:

```text
alpha ~= 4.4
```

Mais ce seuil reste calibre numeriquement. Il ne doit pas etre presente comme une constante demontree.

## 7. Prochains tests obligatoires

Avant toute promotion de cette piste, il faut:

1. pousser le test a `10^8` si le temps de calcul le permet;
2. comparer `min-log-centered`, `geo-log-centered`, `harm-log-centered`;
3. verifier la sensibilite au seuil `B=89`;
4. chercher une justification probabiliste du facteur `log_2 p`;
5. comparer aux entiers impairs de controle pour voir si le signal est propre aux jumeaux.

## 8. Commande reproductible

Depuis la racine du depot:

```bash
python3 Math/Collatz-Montmory/work/scripts/evaluate_montmory_filter.py \
  --limit 10000000 \
  --calibrate-x 1000000 \
  --x-values 1000000,3000000,10000000 \
  --mode min-log-centered
```

Sortie attendue principale:

```text
mode=min-log-centered
alpha=4.430733769771316
1000000,...,0.08185271412817056,...
3000000,...,0.07995603135155802,...
10000000,...,0.08149630333039408,...
```

## 9. Conclusion de travail

La piste `min-log-centered` est actuellement la plus prometteuse des filtres directs testes. Elle ne prouve rien, mais elle transforme l'echec du seuil brut en une hypothese plus precise: `C_Montmory` pourrait correspondre a une queue de grande deviation Collatz apres recentrage par la derive aleatoire moyenne.

Le prochain verrou est de montrer que cette queue a une limite non arbitraire et que le seuil proche de `4.4` n'est pas une calibration de plus.