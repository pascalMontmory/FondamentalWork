# Audit des formules

## Donnees

Constantes CODATA/NIST 2022 :

```tex
c,\quad h,\quad \hbar=h/(2\pi),\quad G.
```

Parametres Planck 2018 utilises :

```tex
H_0 = 67.4\ \mathrm{km\,s^{-1}\,Mpc^{-1}},
\qquad
\Omega_m = 0.315,
\qquad
\Omega_\Lambda = 1-\Omega_m = 0.685.
```

## Verification analytique

La densite d'energie noire est

```tex
\rho_\Lambda
=
\Omega_\Lambda \frac{3H_0^2}{8\pi G}c^2.
```

La regularisation GUP du vide dans le modele `gamma=3` donne

```tex
\rho_{\mathrm{vac}}
=
\frac{g\rho_P}{16\pi^2\beta_0^2},
\qquad
\rho_P=\frac{c^7}{\hbar G^2}.
```

En imposant `rho_vac = rho_Lambda`, on obtient

```tex
\beta_0^2
=
\frac{g\rho_P}{16\pi^2\rho_\Lambda}
=
\frac{g c^5}{6\pi\hbar G\Omega_\Lambda H_0^2}.
```

Comme

```tex
t_P=\sqrt{\frac{\hbar G}{c^5}},
```

alors

```tex
\boxed{
\beta_0^{(\Lambda)}
=
\left(\frac{g}{6\pi\Omega_\Lambda}\right)^{1/2}
\frac{1}{H_0t_P}
}
```

Cette formule a ete verifiee numeriquement et reproduit la valeur directe
obtenue avec `rho_P/rho_Lambda`.

## Nouvelle echelle de longueur

La longueur minimale effective correspondant a cette identification est

```tex
\ell_\Lambda
=
\sqrt{\beta_0^{(\Lambda)}}\,\ell_P
=
\left(\frac{g}{6\pi\Omega_\Lambda}\right)^{1/4}
\sqrt{\ell_P\frac{c}{H_0}}.
```

Donc l'identification directe de l'energie noire selectionne l'echelle
geometrique

```tex
\sqrt{\ell_P R_H},
\qquad
R_H=\frac{c}{H_0}.
```

Pour `g=1`, `ell_Lambda = 2.48e-5 m`.

## Nouvelle echelle d'energie

L'impulsion/energie GUP associee est

```tex
E_{\mathrm{GUP}}
=
\frac{\hbar c}{\ell_\Lambda}
=
\left(\frac{6\pi\Omega_\Lambda}{g}\right)^{1/4}
\sqrt{E_P\,\hbar H_0}.
```

Pour `g=1`, `E_GUP = 7.94 meV`.

## Masse critique

La reformulation position-vitesse donne

```tex
v_{\mathrm{GUP}}
=
c\frac{m_P}{m\sqrt{\beta_0}}.
```

Sous l'identification a l'energie noire :

```tex
\frac{v_{\mathrm{GUP}}}{c}
=
\frac{m_*}{m},
\qquad
m_*c^2=E_{\mathrm{GUP}}.
```

Pour `g=1`, `m_* c^2 = 7.94 meV`. Toute particule de masse plus grande que
cette echelle aurait un seuil GUP subluminal si le meme `beta0` etait applique
universellement.

## Densite maximale de modes ajustee a l'energie noire

Le premier manuscrit donne, pour `gamma=3`,

```tex
n_{\max}
=
\frac{g}{32\pi\beta_0^{3/2}\ell_P^3}.
```

En inserant la valeur `beta0_Lambda`, on trouve une nouvelle forme fermee :

```tex
\boxed{
n_{\max}^{(\Lambda)}
=
\frac{g^{1/4}(6\pi\Omega_\Lambda)^{3/4}}{32\pi}
\frac{1}{(\ell_P R_H)^{3/2}},
\qquad
R_H=\frac{c}{H_0}.
}
```

La distance moyenne entre modes est donc de l'ordre de la meme echelle
UV/IR mixte :

```tex
\boxed{
\left(n_{\max}^{(\Lambda)}\right)^{-1/3}
=
\left[
\frac{32\pi}{g^{1/4}(6\pi\Omega_\Lambda)^{3/4}}
\right]^{1/3}
\sqrt{\ell_P R_H}.
}
```

Pour `g=1`, le script donne :

```text
nmax = 6.49e11 m^-3
nmax^(-1/3) = 1.16e-4 m
```

## Statut physique

Le resultat positif est mathematique : la mesure GUP regularise bien
l'integrale UV et transforme la divergence du vide en quantite finie.

Le resultat negatif est aussi important : si cette valeur finie est identifiee
directement a l'energie noire observee, le parametre `beta0` n'est plus
planckien mais cosmologique, `beta0 ~ 1/(H0 tP)`. Le meme parametre ne peut pas
etre applique sans modification a la cinematique ordinaire, car il rend les
corrections GUP accessibles a des vitesses non relativistes pour les particules
massives.

Conclusion exploitable : l'identification `rho_vac = rho_Lambda` impose soit
un secteur de vide effectif distinct, soit une annulation/renormalisation
gravitationnelle, soit un `beta0` dependant du secteur, soit une formulation
covariante ou holographique plus contrainte.
