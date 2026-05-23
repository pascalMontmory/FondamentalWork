# Contrainte energie noire et regulateur GUP

Ce dossier transforme le test numerique `rho_vac = rho_Lambda` en note
analytique. Il montre que la regularisation UV par la mesure GUP est
mathematiquement finie, mais qu'une identification directe a l'energie noire
impose une valeur enorme de `beta0`.

## Resultat central

```tex
\beta_0^{(\Lambda)}
=
\left(\frac{g}{6\pi\Omega_\Lambda}\right)^{1/2}
\frac{1}{H_0t_P}.
```

Pour `g=1` avec les entrees Planck 2018 utilisees dans le dossier :

```text
beta0_Lambda = 2.363228e60
```

La longueur minimale effective devient alors :

```tex
\ell_\Lambda
=
\sqrt{\beta_0^{(\Lambda)}}\,\ell_P
=
\left(\frac{g}{6\pi\Omega_\Lambda}\right)^{1/4}
\sqrt{\ell_P\frac{c}{H_0}}.
```

Cette longueur est le produit geometrique de l'echelle de Planck et de l'echelle
de Hubble, a un facteur numerique pres.

## Interpretation

Le resultat n'est pas une prediction reussie de l'energie noire par un GUP local
universel. C'est un no-go conditionnel : pour forcer
`rho_vac = rho_Lambda`, le regulateur GUP doit prendre une valeur cosmologique
`beta0 ~ 10^60`.

Cette valeur est beaucoup trop grande pour rester un parametre local universel
applique indistinctement aux photons, a la radiation primordiale et aux fermions
denses. Elle pousse donc vers une separation :

```text
GUP local comme regulateur UV
+ projection gravitationnelle/holographique IR
```

## Chiffres a retenir

| Quantite | Valeur | Statut |
|---|---:|---|
| `rho_DE` utilisee dans la synthese | `5.253229e-10 J/m^3` | entree cosmologique reproduite |
| `beta0_Lambda(g=1)` | `2.363228e60` | valeur imposee par le matching direct |
| echelle energetique mixte | `E_P / sqrt(beta0_Lambda) = 7.94 meV` | consequence du matching, pas preuve dynamique |

## Commande

```bash
latexmk -pdf -interaction=nonstopmode main.tex
```

## Statut scientifique

- `verified algebra` pour la derivation analytique ;
- `rejected as primary mechanism` pour l'identification directe locale et
  universelle `rho_reg = rho_DE` ;
- `candidate conjecture` pour la suite UV/IR holographique qui pourrait remplacer
  ce matching direct.
