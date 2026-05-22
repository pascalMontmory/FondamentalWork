# Audit des formules

## Identites verifiees

La densite critique d'energie est

```tex
\rho_c=\frac{3c^2H_0^2}{8\pi G}.
```

Avec `L_H=c/H0`, `rho_P=c^7/(\hbar G^2)` et
`\ell_P^2=\hbar G/c^3`, on a exactement

```tex
\rho_P\ell_P^2=\frac{c^4}{G}.
```

Donc

```tex
\boxed{
\rho_{\rm DE}
=
\Omega_\Lambda\rho_c
=
\frac{3\Omega_\Lambda}{8\pi}\rho_P
\left(\frac{\ell_P}{L_H}\right)^2.
}
```

Cette equation n'est pas une nouvelle loi dynamique : c'est une identite
dimensionnelle exacte une fois `H0` et `Omega_Lambda` fixes.

## Borne trou noir

Pour une sphere de rayon `L`,

```tex
E=\rho\frac{4\pi}{3}L^3,
\qquad
E_{\rm BH}=\frac{c^4L}{2G}.
```

La condition `E <= E_BH` donne

```tex
\boxed{
\rho\leq \rho_{\rm BH}(L)=\frac{3c^4}{8\pi G L^2}.
}
```

Pour `L=L_H`, `rho_BH(L_H)=rho_c`. Cette egalite est exacte avec la
definition choisie de `L_H`.

## Echelle d'energie noire

La definition

```tex
E_{\rm DE}=[\rho_{\rm DE}(\hbar c)^3]^{1/4}
```

donne

```tex
\boxed{
E_{\rm DE}
=
\left(\frac{3\Omega_\Lambda}{8\pi}\right)^{1/4}
\sqrt{E_PE_H},
\qquad
E_H=\hbar H_0.
}
```

Le script numerique donne `E_DE = 2.241 meV`.

## Regulateur GUP

Le regulateur GUP `gamma=3` donne

```tex
\rho_{\rm reg}
=
\frac{g\rho_P}{16\pi^2\beta_0^2}.
```

Le facteur numerique `16 pi^2` est important. Il explique pourquoi l'echelle
d'energie GUP ajustee a `rho_DE` differe de `E_DE` :

```tex
\boxed{
\frac{E_{\rm GUP}^{(\Lambda)}}{E_{\rm DE}}
=
\left(\frac{16\pi^2}{g}\right)^{1/4}
=
\frac{2\sqrt{\pi}}{g^{1/4}}.
}
```

Pour `g=1`, ce rapport vaut `3.5449`, ce qui verifie
`7.94 meV / 2.24 meV`.

## Projection gravitationnelle candidate

La forme

```tex
\rho_{\rm grav}(L)=
\min\left[
\frac{g\rho_P}{16\pi^2\beta_0^2},
\frac{3c^4}{8\pi G L^2}
\right]
```

est une equation candidate, pas une consequence automatique du GUP. Elle
combine deux contraintes : regularisation UV et non-effondrement gravitationnel.

Le croisement des deux branches est

```tex
\boxed{
L_\times
=
\beta_0\sqrt{\frac{6\pi}{g}}\ell_P.
}
```

Pour `beta0=1` et `g=1`, `L_cross = 4.34 ell_P`. Donc a toute echelle
macroscopique, la branche gravitationnelle domine.

## Acceleration cosmologique

Avec

```tex
\Lambda=\frac{3\Omega_\Lambda H_0^2}{c^2},
```

il faut distinguer

```tex
a_\Lambda=c^2\sqrt{\Lambda}=cH_0\sqrt{3\Omega_\Lambda}
```

et l'echelle de Sitter usuelle

```tex
\boxed{
a_{\rm dS}=c^2\sqrt{\frac{\Lambda}{3}}=cH_0\sqrt{\Omega_\Lambda}.
}
```

Si on compare a une acceleration de type MOND, la convention la plus frequente
est plutot

```tex
a_{\rm dS}/(2\pi)
```

que `c^2 sqrt(Lambda)/(2pi)`. Les deux different d'un facteur `sqrt(3)`.

## Point dynamique ouvert

Une densite `rho ~ L^{-2}` ne suffit pas a definir une energie noire
acceleratrice. Si `L=c/H`, le terme est proportionnel a `H^2` et peut se
comporter comme une renormalisation de `G`. Pour obtenir `w` proche de `-1`, il
faut une longueur IR non locale ou dynamique, par exemple l'horizon des
evenements futur dans les modeles d'energie noire holographique.
