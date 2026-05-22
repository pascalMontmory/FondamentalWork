# Audit scientifique de la conjecture alpha--Lambda

## Elements verifies

La relation entropique

```text
alpha^{-1} = 1/2 ln(S_Lambda / S0)
S_Lambda/kB = pi R_Lambda^2/ell_P^2
S0/kB = 100 pi^3
```

implique bien

```text
alpha^{-1} = ln(R_Lambda/(10 pi ell_P)).
```

La relation inverse est aussi correcte :

```text
Lambda = 3/(100 pi^2 ell_P^2) exp(-2/alpha).
```

La reduction du facteur `10 pi` est algebriquement correcte :

```text
S0/kB = 4 pi (2 pi g_eff)^2
S0/kB = 100 pi^3
=> g_eff = 5/2.
```

Le flot

```text
d alpha^{-1} / d ln L = 1
```

decoule directement de la loi d'aire `S(L) proportional L^2`.

## Test numerique

Avec les valeurs centrales CODATA 2022 et Planck 2018 :

```text
alpha_inv_CODATA_2022          = 137.035999177
alpha_inv_pred_10pi            = 137.036063742708
delta                          = 6.456570762e-05
relative_delta                 = 4.711587321e-07
Lambda_from_alpha / Lambda_obs = 1.000129139753
C_fit/(10*pi)                  = 1.000064567792
g_eff_fit                      = 2.500161419480
```

La proximite numerique est forte. Elle n'est cependant pas une preuve, car le
facteur `10 pi` est equivalent a choisir un seuil `S0` tres precis. La formule
devient predictive seulement si `g_eff=5/2` est derive sans utiliser la valeur
observee de `alpha`.

## Points fragiles

1. Le choix de `R_Lambda` depend du modele cosmologique. Ici on prend
   `Lambda = 3 Omega_Lambda H0^2/c^2`, ce qui est un choix LambdaCDM actuel.
2. La constante `alpha` utilisee est la valeur basse energie CODATA. En theorie
   quantique des champs, `alpha` court avec l'echelle de renormalisation.
3. Les modes de bord Maxwell sont bien connus dans les calculs d'entropie, et
   des determinants a demi-puissance apparaissent naturellement. En revanche,
   l'application
   `C_ren[(det K)^q]=|q|` est une definition supplementaire, pas un resultat
   etabli.
4. L'identification `2 polarisations + 1/2 mode de bord = 5/2` est plausible
   comme comptage effectif, mais elle doit etre demontree depuis une fonction
   de partition de bord normalisee.

## Conclusion

Le texte doit etre presente comme un theoreme conditionnel :

```text
si la capacite holographique U(1) vaut g_eff=5/2,
alors alpha^{-1}=ln(R_Lambda/(10 pi ell_P)).
```

Ce qui est nouveau et exploitable n'est pas encore une prediction etablie de
`alpha`; c'est la reduction du probleme numerique au calcul microphysique d'un
mode de bord Maxwell.
