# Audit des conclusions cosmologiques

## Resultat negatif verifie

La mesure GUP `gamma=3` donne une densite de vide regularisee :

```math
\rho_{\rm reg}
=
\frac{g\rho_P}{16\pi^2\beta_0^2}.
```

Pour `beta0=1` et `g=1`, cette densite est finie mais reste planckienne a un
facteur `1/(16 pi^2)` pres. Elle est environ `10^121` fois plus grande que
l'energie noire observee.

Conclusion : le GUP seul est un regulateur UV, pas une solution complete de la
constante cosmologique.

## Relation UV/IR correcte

La densite d'energie noire actuelle s'ecrit exactement

```math
\rho_{\rm DE}
=
\Omega_\Lambda\rho_c
=
\frac{3\Omega_\Lambda}{8\pi}\rho_P
\left(\frac{\ell_P}{L_H}\right)^2.
```

Cette relation montre que le petit facteur vient du rapport d'aires
`\ell_P^2/L_H^2`.

## Densite d'horizon

La borne de non-effondrement donne

```math
\rho_{\rm BH}(L)
=
\frac{3c^4}{8\pi G L^2}
=
\frac{3}{8\pi}\rho_P\left(\frac{\ell_P}{L}\right)^2.
```

Pour `L=L_H`, `rho_BH(L_H)=rho_c`. Donc

```math
\rho_{\rm DE}=\Omega_\Lambda\rho_{\rm BH}(L_H).
```

## Transition primordiale

L'egalite entre branche GUP et branche horizon donne

```math
\boxed{
L_*=\beta_0\sqrt{\frac{6\pi}{g}}\ell_P.
}
```

Pour `beta0=1`, `g=1`, cette transition est a `4.34 ell_P`. Cela soutient
l'interpretation suivante : la branche GUP est pertinente dans le regime
planckien, tandis que la branche horizon controle les grandes echelles.

## Equation d'etat

Une densite `rho ~ L^{-2}` ne garantit pas `w=-1`. Dans le modele standard
d'energie noire holographique plat et non interactif, avec horizon des
evenements futur et parametre dimensionnel note ici `c_hde`, on obtient

```math
\boxed{
w_{\rm HDE}
=
-\frac13-\frac{2}{3c_{\rm hde}}\sqrt{\Omega_{\rm DE}}.
}
```

Pour `Omega_DE=0.685` :

```text
c_hde=0.8 -> w0=-1.023
c_hde=1.0 -> w0=-0.885
c_hde=1.2 -> w0=-0.793
```

Cette formule indique clairement que la dynamique de `L` est decisive. Si
`L=c/H`, le terme `L^{-2}` ressemble plutot a une renormalisation de `G`.

## Conclusion exploitable

La meilleure formulation de publication est un theoreme conditionnel :

```math
\text{GUP UV fini}+\text{borne IR d'horizon}
\Rightarrow
\rho_{\rm grav}\sim\rho_P(\ell_P/L)^2.
```

La partie nouvelle a developper n'est donc pas seulement la regularisation de
l'integrale UV, deja connue dans la litterature GUP, mais la regle covariante
qui selectionne la partie gravitationnellement active du vide regularise.
