# Verdict des tests

## 1. `beta0 ~ 10^60` universel

Verdict : exclu.

Les tests FIRAS, BBN et fermions denses donnent des bornes beaucoup plus basses
que `beta0_DE`. La physique atomique ajoute un argument direct :

```text
chi_e/beta0 = (m_e/m_P)^2 alpha^2 ~= 9.33e-50
```

Donc `beta0_DE ~ 2.36e60` donnerait `chi_e ~ 2.2e11`, incompatible avec les
spectres atomiques.

## 2. Branche holographique

La formule

```text
rho_BH(L) = 3 c^4/(8 pi G L^2)
```

est une borne gravitationnelle et une identite pour `L=c/H0` :

```text
rho_BH(L_H)=rho_c.
```

Elle est correcte, mais elle n'est pas encore une dynamique. Il faut expliquer
pourquoi la partie gravitationnellement active vaut `Omega_Lambda rho_c` et
pourquoi son tenseur effectif donne `w ~= -1`.

## 3. Choix de la longueur IR

Si on prend `L=c/H(t)` dans la relation alpha--L, alors alpha varie :

```text
dot alpha / alpha = - alpha d ln L/dt.
```

En LCDM aujourd'hui :

```text
dot alpha/alpha ~= -2.37e-13 / an.
```

C'est environ `2e5` fois plus grand qu'une limite atomique typique
`~1e-18/an`. Donc `L=c/H(t)` est fortement defavorise.

La piste viable est plutot une echelle quasi constante : `R_Lambda`, horizon de
de Sitter asymptotique, ou horizon futur avec variation tres faible.

## 4. Energie noire dynamique

Les modeles holographiques standards predisent souvent

```text
w = -1/3 - 2 sqrt(Omega_DE)/(3 c_hde).
```

Pour `c_hde=1`, on obtient `w ~= -0.885`, ce qui est testable et deja tendu
face aux contraintes proches de `w=-1`.

## 5. Relation alpha--Lambda

Avec CODATA 2022 et Planck 2018 :

```text
alpha_inv_pred = 137.036063742708
alpha_inv_obs  = 137.035999177
Lambda(alpha)/Lambda_obs = 1.000129139753
```

La coherence numerique est forte. Elle devient predictive seulement si le
facteur `10 pi` est derive independamment.

## 6. Mode de bord Maxwell

Ce n'est pas un test de donnees publiques. C'est un calcul theorique :

```text
Z_edge proportional [det'(-Delta_S2)]^{+-1/2}
```

Le but est de justifier rigoureusement que la capacite holographique
renormalisee du mode de bord vaut

```text
g_edge^{U(1)} = 1/2.
```
