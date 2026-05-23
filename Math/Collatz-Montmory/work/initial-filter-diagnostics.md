# Diagnostic initial du filtre Montmory canonique

Date: 2026-05-23

Ce fichier consigne un premier test rapide du filtre defini dans `montmory-filter-lock.md`.

## Definition testee

```text
T(n) = n/2        si n est pair
T(n) = (3n+1)/2  si n est impair
B = 89
tau_B(n) = premier t tel que T^t(n) <= 89
kappa_B(n) = log2(n) / tau_B(n)
score(p,p+2) = min(kappa_B(p), kappa_B(p+2))
M_alpha = score >= alpha
```

Densite relative cible:

```text
rho_target = 0.08178598968002705
```

## Test A: calibration sur toute la plage jusqu'a 1e6

Nombre de paires de jumeaux `p,p+2` avec `p <= 1e6`:

```text
8169
```

Seuil calibre sur toute la plage:

```text
alpha = 0.45708224493698213
```

Resultats:

```text
x,twin_count,selected_count,selected_ratio,coefficient_estimate
10000,205,71,0.3463414634146341,0.6022956253503462
30000,467,114,0.24411134903640258,0.40384311884573915
100000,1224,211,0.17238562091503268,0.2796751253277355
300000,2994,357,0.11923847695390781,0.1892705525686197
1000000,8169,669,0.08189496878442894,0.12769091409276173
```

Interpretation: comme le seuil est calibre sur `1e6`, le dernier ratio est proche de la cible par construction. Les ratios aux bornes plus petites sont beaucoup plus eleves, ce qui montre une forte derive de taille finie.

## Test B: calibration sur 1e5, test hors echantillon jusqu'a 1e6

Seuil calibre sur `p <= 100000`:

```text
alpha = 0.563084948632043
```

Resultats hors echantillon:

```text
x,twin_count,selected_count,selected_ratio,coefficient_estimate
100000,1224,101,0.08251633986928104,0.13387292728957956
300000,2994,145,0.04843019372077488,0.07687459418053182
1000000,8169,238,0.02913453299057412,0.04542666301057891
```

Interpretation: le ratio selectionne chute fortement apres la zone de calibration. Ce comportement ne soutient pas encore l'existence d'une densite relative stable pour ce seuil.

## Conclusion du diagnostic

Le filtre canonique `score=min(kappa_B(p),kappa_B(p+2)) >= alpha`, calibre naivement, n'est pas valide par ce premier test jusqu'a `1e6`.

Ce n'est pas une refutation asymptotique, mais c'est un signal negatif important:

1. le seuil `alpha` n'est pas stable a petite echelle;
2. le test hors echantillon derive fortement;
3. la constante `0.107983974916` n'est pas encore soutenue par ce filtre simple.

## Actions recommandees

1. Executer le meme protocole jusqu'a `1e7`, puis `1e8` si possible.
2. Comparer les scores `min`, `harm`, `geo`.
3. Etudier la distribution complete de `kappa_B` au lieu d'un simple seuil.
4. Tester des filtres moins sensibles aux trajectoires longues exceptionnelles.
5. Ne pas figer `C_Montmory` comme resultat tant qu'un filtre hors echantillon ne stabilise pas `rho_target`.
