# Test donnees publiques : regulateur UV et energie noire

## Question testee

On teste l'application directe suivante :

```tex
\rho_{\mathrm{vac}} =
\frac{g\rho_P}{16\pi^2\beta_0^2}
```

Cette formule vient du modele `gamma = 3` avec
`\beta = \beta_0 l_P^2/\hbar^2`.

La question est : quelle valeur de `beta_0` faudrait-il pour que l'energie du
vide regularisee soit egale a la densite d'energie noire observee ?

## Donnees utilisees

- Constantes CODATA/NIST 2022 :
  - `c = 299792458 m/s`
  - `h = 6.62607015e-34 J s`
  - `G = 6.67430e-11 m^3 kg^-1 s^-2`
- Parametres cosmologiques Planck 2018, modele LCDM plat :
  - `H0 = 67.4 km/s/Mpc`
  - `Omega_m = 0.315`
  - `Omega_Lambda = 0.685`

On calcule :

```tex
\rho_\Lambda = \Omega_\Lambda \frac{3H_0^2}{8\pi G}c^2.
```

## Resultats numeriques

Le script donne :

```text
rho_DE = 5.253229e-10 J/m^3
rho_P  = 4.632947e+113 J/m^3
```

Inversion de
`\rho_{\mathrm{vac}} = g rho_P/(16 pi^2 beta0^2)` :

```text
g=1       beta0 = 2.36e60   sqrt(beta0) lP = 2.48e-05 m
g=2       beta0 = 3.34e60   sqrt(beta0) lP = 2.95e-05 m
g=100     beta0 = 2.36e61   sqrt(beta0) lP = 7.86e-05 m
g=106.75  beta0 = 2.44e61   sqrt(beta0) lP = 7.99e-05 m
```

Si `beta0 = 1`, alors :

```text
g=1   rho_vac/rho_DE = 5.58e120
g=2   rho_vac/rho_DE = 1.12e121
g=100 rho_vac/rho_DE = 5.58e122
```

## Interpretation

Ce test est fortement contraignant pour l'idee que la regularisation GUP du
vide, seule, expliquerait directement l'energie noire.

Avec `beta0` d'ordre unite, la regularisation remplace l'infini par une valeur
finie mais encore enorme : environ `10^121` fois la densite d'energie noire.

Pour reproduire l'energie noire observee, il faudrait

```tex
\beta_0 \sim 10^{60}
```

ce qui correspond a une longueur minimale effective

```tex
\Delta x_{\min} = \sqrt{\beta_0}l_P \sim 10^{-5}\ \mathrm{m}.
```

Une telle longueur est macroscopique a l'echelle microscopique. Cela rend
l'interpretation "longueur minimale fondamentale universelle" tres difficile.

## Conclusion scientifique

Le modele fournit bien un regulateur UV physique et calculable. En revanche,
il ne resout pas le probleme de la constante cosmologique sans mecanisme
additionnel :

- annulation bosons/fermions ;
- renormalisation gravitationnelle ;
- valeur effective de `beta0` dependante du secteur ;
- dynamique supplementaire annulant presque toute l'energie du vide ;
- formulation covariante differente modifiant le poids spectral.

Ce resultat negatif est publiable comme contrainte de coherence : la mesure
de phase deformee regularise l'UV, mais la regularisation seule ne suffit pas
a expliquer l'energie noire.
