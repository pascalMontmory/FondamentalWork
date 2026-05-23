# Audit du cadre maitre

## Correct

- La mesure GUP choisie donne bien les integrales :

```text
int p^2 dp/(1+beta p^2)^3 = pi/(16 beta^(3/2))
int p^3 dp/(1+beta p^2)^3 = 1/(4 beta^2)
```

- La densite maximale de modes est :

```text
nmax = g pi^2/(4 h^3 beta^(3/2))
     = g/(32 pi beta0^(3/2) ell_P^3)
```

- La densite de vide regularisee est :

```text
rho_reg = g rho_P/(16 pi^2 beta0^2)
```

- L'identite UV/IR est :

```text
rho_DE/rho_P = (3 Omega_Lambda/8pi) (ell_P/L_H)^2
```

- Le parametre direct `rho_reg=rho_DE` vaut :

```text
beta0_DE(g=1) = 2.363228e60
sqrt(beta0_DE) ell_P = 2.484636e-5 m
```

## A corriger dans le statut

- `rho_grav=min[rho_reg,rho_BH]` est une prescription effective, pas une
  equation dynamique derivee.
- La soustraction du vide plat est une condition de renormalisation, pas une
  preuve que la constante cosmologique est resolue.
- Le calcul par bits d'horizon donne seulement l'echelle `c^4/(G L^2)` sauf si
  l'energie par bit et les facteurs numeriques sont fixes.
- La relation alpha--Lambda est une conjecture numeriquement forte, mais non
  derivee tant que `g_edge^{U(1)}=1/2` n'est pas prouve.
- L'extension aux autres interactions doit tenir compte du running des
  couplages, du confinement QCD et du melange electroweak.

## Verdict

Le cadre est defendable comme theorie effective conditionnelle. Son apport est
une architecture unifiee et falsifiable, pas encore une theorie fondamentale.
