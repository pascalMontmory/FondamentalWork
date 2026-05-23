# Conclusions croisees des deux notes

Les deux notes decrivent la meme mesure GUP sous deux angles :

```math
\frac{\dd^3p}{(1+\beta p^2)^3}
\qquad\Longleftrightarrow\qquad
\frac{m^3\dd^3v}{(1+\beta m^2v^2)^3}.
```

## 1. Separation nette entre trois regimes thermiques

La mesure donne trois comportements differents :

```math
n_{\max}<\infty
```

pour le nombre de modes, mais pas une energie thermique universellement bornee.

- Bosons sans masse :

```math
u(T)\sim n_{\max}k_BT
```

a haute temperature.

- Gaz classique massif non relativiste :

```math
\frac{U}{N}\to \frac{3}{2m\beta}.
```

- Fermions degeneres ultrarelativistes :

```math
\rho_{\max}=\frac{g\pi c}{h^3\beta^2}.
```

Conclusion : la deformation GUP ne produit pas une seule notion de saturation, mais une famille de saturations dependant de la statistique, de la masse et de la relation de dispersion.

## 2. Nouvelle formule utile : pic relativiste en vitesse

Pour la densite de modes relativiste en vitesse,

```math
\frac{\dd n}{\dd v}
\propto
\frac{\gamma^5v^2}{(1+\beta\gamma^2m^2v^2)^3},
```

posons

```math
t=\frac{p}{mc}=\gamma\frac{v}{c},
\qquad
A=\beta m^2c^2.
```

Le maximum est donne par `z=t^2`, ou

```math
A z^2-(5-4A)z-2=0.
```

Donc

```math
z_{\mathrm{pic}}
=
\frac{(5-4A)+\sqrt{(5-4A)^2+8A}}{2A}.
```

La vitesse du pic est alors

```math
v_{\mathrm{pic,rel}}
=
c\sqrt{\frac{z_{\mathrm{pic}}}{1+z_{\mathrm{pic}}}}.
```

Limites :

- si `A >> 1`, on retrouve le pic non relativiste `v_pic = 1/(m sqrt(2 beta))` ;
- si `A << 1`, le pic se rapproche de `c`, avec une impulsion de l'ordre de quelques `p_GUP`.

## 3. No-go phenomenologique entre energie noire et seuil vitesse

Le premier test a montre que reproduire l'energie noire par

```math
\rho_{\mathrm{vac}}=\frac{g\rho_P}{16\pi^2\beta_0^2}
```

exige typiquement :

```math
\beta_0\sim 10^{60}.
```

La seconde note traduit cette valeur en seuil vitesse :

```math
v_{\mathrm{GUP}}=
c\frac{m_P}{m\sqrt{\beta_0}}.
```

Pour `g=1`, on obtient environ :

```text
electron : v_GUP ~ 4.7 m/s
proton   : v_GUP ~ 2.5e-3 m/s
```

Ce resultat est physiquement intenable pour une deformation universelle appliquee aux particules ordinaires. Il fournit donc une conclusion forte : la regularisation du vide ne peut pas expliquer directement l'energie noire avec le meme `beta_0` universel qui controle la cinematique des particules.

## 4. Direction publiable

La direction la plus propre n'est pas de promettre une resolution de la constante cosmologique. Elle est plutot de formuler un theoreme de structure :

> Une mesure de phase GUP peut rendre fini le nombre de modes et regulariser certaines integrales UV, mais ses consequences thermodynamiques dependent de la statistique et de la relation de dispersion. Toute identification directe a l'energie noire impose des seuils masse-vitesse incompatibles avec une deformation universelle simple.
