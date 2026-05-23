# Synthese des travaux confirmes GUP--UV/IR

Ce dossier contient une synthese LaTeX des resultats confirmes des notes
precedentes.

Le mot "confirme" signifie ici :

- formule derivee et verifiee mathematiquement dans le cadre du modele ;
- identite dimensionnelle exacte ;
- contrainte numerique reproduite avec constantes publiques ;
- exclusion observationnelle conditionnelle.

Il ne signifie pas que le GUP ou la theorie UV/IR complete sont etablis
experimentalement.

## Conclusions robustes

1. La cellule de phase GUP rend finies certaines integrales UV dans le cadre
   choisi.
2. L'identification directe de cette densite regularisee a l'energie noire
   observee impose `beta0_Lambda(g=1) = 2.363228e60`.
3. Cette valeur correspond a une echelle mixte UV/IR, pas a une correction
   planckienne locale naturelle.
4. Si ce meme `beta0` est applique universellement aux photons, a la radiation
   primordiale ou aux fermions denses, il est exclu par les tests publics
   resumes ci-dessous.
5. La conclusion solide est donc negative : un `beta0 ~ 10^60` local et
   universel n'est pas viable.
6. La piste encore ouverte est une separation de secteurs : regularisation UV
   locale d'un cote, projection gravitationnelle/holographique IR de l'autre.
7. Les relations Planck-Hubble-energie noire sont des identites dimensionnelles
   utiles, mais elles ne constituent pas seules une dynamique.
8. La conjecture `alpha--Lambda` est numeriquement proche, mais reste
   speculative tant que l'incertitude, le choix du facteur et la non-variation
   temporelle ne sont pas traites comme tests centraux.
9. Les scenarios jumeaux ou zero-mode doivent rester separes des resultats
   robustes tant qu'ils ne donnent pas une signature distincte de Lambda-CDM.
10. L'application la plus mature hors cosmologie est le CAD de capteurs
    atomiques, car elle produit des budgets de bruit et des benchmarks
    directement falsifiables.

## Chiffres principaux

| Quantite | Valeur | Interpretation |
|---|---:|---|
| `rho_DE` | `5.253229e-10 J/m^3` | densite d'energie noire utilisee |
| `beta0_Lambda(g=1)` | `2.363228e60` | valeur imposee par `rho_reg = rho_DE` |
| FIRAS/CMB | `beta0 <= 3.72e58` | exclut `beta0_Lambda` comme parametre photon universel |
| BBN/radiation | `beta0 <= 2.64e41` | exclut `beta0_Lambda` dans le secteur radiation primordial |
| Fermions denses | `beta0 <= 1.66e38` | exclut `beta0_Lambda` pour les fermions denses |

## Document principal

Compiler :

```bash
latexmk -pdf -interaction=nonstopmode main.tex
```

## Documents transverses

Depuis la racine du depot :

- `docs/CLAIMS_MATRIX.md` classe les claims robustes, conjecturaux et
  speculatifs.
- `docs/NUMERICAL_RESULTS_INDEX.md` liste les valeurs numeriques principales.
- `docs/SCIENTIFIC_CONSOLIDATION_PLAN.md` decrit les prochaines consolidations
  scientifiques.
