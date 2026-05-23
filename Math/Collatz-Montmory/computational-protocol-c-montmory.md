# Protocole numerique pour tester le filtre C_Montmory

Date: 2026-05-23

Ce protocole accompagne `montmory-filter-lock.md` et `scripts/evaluate_montmory_filter.py`.

## 1. Objectif

Tester si une definition fixee du filtre Montmory produit une densite relative proche de:

```math
\rho_M = \frac{0.107983974916}{2C_2}
       \approx 0.08178598968002706.
```

Le test ne prouve pas l'asymptotique. Il sert a detecter rapidement si le filtre est plausible ou s'il derive.

## 2. Definition testee par defaut

```text
T(n) = n/2        si n est pair
T(n) = (3n+1)/2  si n est impair
B = 89
tau_B(n) = premier t tel que T^t(n) <= B
kappa_B(n) = log2(n) / tau_B(n)
score(p,p+2) = min(kappa_B(p), kappa_B(p+2))
M_alpha(p,p+2) = 1 si score(p,p+2) >= alpha
```

## 3. Commande de base

Depuis la racine du depot:

```bash
python3 Math/Collatz-Montmory/scripts/evaluate_montmory_filter.py \
  --limit 1000000 \
  --x-values 10000,100000,1000000 \
  --mode min
```

Par defaut, le script calibre `alpha` sur toutes les paires jusqu'a `limit` pour viser `rho_M`.

## 4. Test hors echantillon recommande

Calibrer sur une plage basse, tester sur une plage haute:

```bash
python3 Math/Collatz-Montmory/scripts/evaluate_montmory_filter.py \
  --limit 10000000 \
  --calibrate-x 1000000 \
  --x-values 1000000,3000000,10000000 \
  --mode min
```

Interpretation:

- si le ratio selectionne reste proche de `rho_M`, le filtre merite investigation;
- si le ratio derive fortement, le seuil est probablement un artefact de calibration;
- si le coefficient estime ne se stabilise pas vers `0.107983974916`, la constante n'est pas soutenue par ce filtre.

## 5. Modes de score

Le script accepte:

```text
--mode min
--mode geo
--mode harm
```

Le mode `min` est le candidat canonique. Les modes `geo` et `harm` sont exploratoires.

## 6. Donnees a reporter

Chaque experience doit reporter:

```text
limit
calibrate-x
mode
B
alpha obtenu
x
twin_count
selected_count
selected_ratio
coefficient_estimate = selected_count / (x/log(x)^2)
```

## 7. Criteres de rejet

Rejeter une definition de filtre si:

1. le seuil calibre varie fortement quand `calibrate-x` augmente;
2. le ratio hors echantillon derive au lieu de se stabiliser;
3. le coefficient estime ne montre aucune tendance vers `0.107983974916`;
4. le filtre selectionne surtout des artefacts de petite taille;
5. le filtre depend d'un parametre choisi apres observation du jeu de test.

## 8. Criteres de plausibilite

Un filtre devient plausible si:

1. le meme `alpha` fonctionne sur plusieurs ordres de grandeur;
2. `selected_ratio` approche `rho_M`;
3. `coefficient_estimate` approche `C_Montmory`;
4. les modes voisins (`min`, `harm`, `geo`) donnent une structure comprehensible;
5. une heuristique probabiliste explique le seuil.

## 9. Limite scientifique

Meme un tres bon tableau numerique ne prouve pas:

```math
N_M(x) \sim C_Montmory x/log^2x.
```

Il fournit seulement une evidence. Une preuve demanderait une version filtree de Hardy-Littlewood ou une demonstration de decorrelation entre le filtre Collatz-Montmory et les contraintes de primalite.