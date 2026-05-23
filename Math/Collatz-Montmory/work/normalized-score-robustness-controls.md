# Robustesse et controles du score Collatz normalise

Date: 2026-05-23  
Statut: note de travail, diagnostic preliminaire

## 1. Objet teste

On reprend le score:

```math
Z_B(p)=\left(\min(\kappa_B(p),\kappa_B(p+2))-d\right)\log_2 p,
\qquad
d=1-\frac12\log_2 3.
```

La question est double:

1. le signal depend-il fortement du seuil `B` ?
2. le signal est-il specifique aux premiers jumeaux ou visible aussi sur des controles ?

La densite cible est:

```math
\rho_M\approx0.08178598968002705.
```

## 2. Sensibilite au seuil B

On calibre le seuil `alpha` sur les paires de jumeaux jusqu'a `10^6`, puis on teste jusqu'a `10^7`.

```text
B    alpha      cum_1e7_ratio  window_(1e6,3e6]  window_(3e6,1e7]
27   3.05905    0.0837404      0.0814072        0.0849190
63   4.17440    0.0826209      0.0810154        0.0833158
89   4.41983    0.0821121      0.0792134        0.0831318
127  4.99195    0.0779904      0.0790566        0.0767977
255  5.85393    0.0735633      0.0727885        0.0720406
511  7.10289    0.0628096      0.0611142        0.0592935
```

Interpretation:

- `B=27,63,89` restent proches de la cible jusqu'a `10^7`;
- `B=127` commence a decrocher;
- `B=255,511` decrochent nettement.

Conclusion: le signal n'est pas uniquement attache a `B=89`, mais il depend de la zone de seuil. Le choix de `B` doit donc etre justifie avant toute publication forte.

## 3. Comparaison des modes normalises

Avec `B=89`, on compare:

```text
min-log-centered
geo-log-centered
harm-log-centered
```

Calibration sur `10^6`:

```text
mode  alpha    window_(1e6,3e6]  window_(3e6,1e7]  cum_1e7
min   4.43073  0.0787432         0.0823434         0.0814963
geo   5.46150  0.0749040         0.0721983         0.0741199
harm  5.21223  0.0742772         0.0731970         0.0746286
```

Le mode `min` est le plus proche de la densite cible. Cela peut avoir un sens: le minimum impose que les deux membres de la paire soient dans la queue compressive. Les modes `geo` et `harm` diluent cette condition.

## 4. Controle: p premier mais p+2 non premier

On garde le meme seuil `alpha=4.430733769771316`, calibre sur les jumeaux jusqu'a `10^6`, et on l'applique aux premiers `p` tels que `p+2` n'est pas premier.

```text
window              count   selected  selected/count
(1e5,1e6]           61961   5311      0.0857152
(1e6,3e6]           125555  10036     0.0799331
(3e6,1e7]           409715  32997     0.0805365
```

Ce controle est tres important: le score normalise selectionne presque la meme proportion chez les premiers non jumeaux que chez les premiers jumeaux.

Interpretation prudente:

- le filtre semble surtout mesurer une queue Collatz sur les nombres premiers `p`;
- il n'est pas fortement specifique a la condition `p+2` premier;
- si cette queue a une densite limite `rho`, alors sous une hypothese d'independance avec l'evenement jumeau, on obtiendrait naturellement un coefficient filtre `2C_2 rho`.

Cela rend la piste mathematiquement plus propre, mais moins specifique aux jumeaux.

## 5. Controle: paires impaires ordinaires

Avec le meme seuil et un echantillon deterministe d'impairs (`odd_stride=20`):

```text
window              sample   selected  selected/sample
(1e5,1e6]           22500    2232      0.0992000
(1e6,3e6]           50000    4628      0.0925600
(3e6,1e7]           175000   16591     0.0948057
```

Le ratio est plus haut que chez les premiers. Cela suggere que la primalite de `p` modifie legerement la distribution du score Collatz, ou que l'echantillon impair contient des biais residue-classe absents chez les premiers.

## 6. Interpretation scientifique

Le candidat `min-log-centered` devient plus interessant pour une raison precise:

```math
N_M(x) \approx \rho \pi_2(x)
```

pourrait decouler de deux hypotheses separees:

1. la queue Collatz normalisee a une densite limite `rho` sur les premiers;
2. cette queue est asymptotiquement independante de la condition `p+2` premier.

Alors, sous Hardy-Littlewood jumeaux:

```math
N_M(x)\sim 2C_2\rho\frac{x}{\log^2 x}.
```

La valeur candidate correspondrait a:

```math
rho=\frac{0.107983974916}{2C_2}
\approx0.08178598968002705.
```

## 7. Verrou restant

Le point faible n'est plus seulement numerique. Il faut maintenant expliquer pourquoi le seuil de queue devrait etre proche de:

```text
alpha ~= 4.4
```

Sans justification de ce seuil, la constante reste calibree. Avec une loi limite de `Z_B(p)` sur les premiers, le seuil pourrait devenir une quantile theorique ou conventionnellement fixe.

## 8. Commandes reproductibles

Jumeaux:

```bash
python3 Math/Collatz-Montmory/work/scripts/evaluate_montmory_filter.py \
  --limit 10000000 \
  --calibrate-x 1000000 \
  --x-values 1000000,3000000,10000000 \
  --mode min-log-centered \
  --population twins
```

Premiers non jumeaux avec le seuil jumeau calibre:

```bash
python3 Math/Collatz-Montmory/work/scripts/evaluate_montmory_filter.py \
  --limit 10000000 \
  --alpha 4.430733769771316 \
  --x-values 1000000,3000000,10000000 \
  --mode min-log-centered \
  --population prime-non-twin
```

Controle impair echantillonne:

```bash
python3 Math/Collatz-Montmory/work/scripts/evaluate_montmory_filter.py \
  --limit 10000000 \
  --alpha 4.430733769771316 \
  --x-values 1000000,3000000,10000000 \
  --mode min-log-centered \
  --population odd-sample \
  --odd-stride 20
```

## 9. Conclusion

Le score normalise `min-log-centered` reste la meilleure piste actuelle. Le resultat le plus utile est le controle `prime-non-twin`: il suggere que la densite cible pourrait venir d'une queue Collatz stable sur les premiers, puis se transmettre aux jumeaux par decorrelation.

Ce n'est toujours pas une validation de `C_Montmory`, mais c'est une formulation mathematique plus defendable que le filtre brut.