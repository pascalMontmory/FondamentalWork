# Audit mathematique : formulation position-vitesse

## Formules confirmees

- La reecriture non relativiste `p = mv` donne bien :

```tex
\dd^3p = m^3 \dd^3v,
\qquad
\dd N =
\frac{m^3\dd^3x\dd^3v}{h^3(1+\beta m^2v^2)^3}.
```

- Le seuil de correction est impulsionnel, mais s'ecrit en vitesse :

```tex
v_{\mathrm{GUP}} = \frac{1}{m\sqrt{\beta}}.
```

- La longueur minimale ne depend pas de la masse :

```tex
\Delta x_{\min} = \hbar\sqrt{\beta}.
```

- La densite differentielle non relativiste en vitesse est :

```tex
\frac{\dd n}{\dd v}
=
\frac{4\pi g m^3}{h^3}
\frac{v^2}{(1+\beta m^2v^2)^3}.
```

- Son maximum est situe en :

```tex
v_{\mathrm{pic}} = \frac{v_{\mathrm{GUP}}}{\sqrt{2}}.
```

- Le nombre total maximal de modes est independant de la masse :

```tex
n_{\max} = \frac{g\pi^2}{4h^3\beta^{3/2}}.
```

- Le jacobien relativiste pour le module de l'impulsion est correct :

```tex
p = \gamma mv,
\qquad
p^2\dd p = m^3\gamma^5v^2\dd v.
```

- La fonction de partition classique basse temperature est correcte :

```tex
Z_1 = Z_{1,0}[1-9\theta_T+90\theta_T^2+\cdots],
\qquad
\theta_T = \beta m k_BT.
```

- Les corrections derivees sont coherentes :

```tex
\frac{U}{N}
=
\frac32 k_BT
-9\beta m k_B^2T^2
+99\beta^2m^2k_B^3T^3+\cdots,
```

```tex
\frac{C_V}{N}
=
\frac32 k_B
-18\beta m k_B^2T
+297\beta^2m^2k_B^3T^2+\cdots.
```

## Corrections et prudences

- La formulation `p=mv` est strictement non relativiste. La version relativiste doit etre ecrite avec `p=\gamma mv`, et les particules sans masse n'ont pas de variable vitesse utile de ce type.
- Le facteur `v_GUP` n'est pas un nouveau seuil fondamental independant : c'est seulement le seuil impulsionnel `p_GUP` exprime en vitesse.
- Pour des objets composes, appliquer `m = M_total` sans regle de composition produit un effet macroscopique artificiel. Il faut une loi de composition du parametre GUP ou une formulation en constituants.
- La longueur d'onde minimale issue de `k(p)` depend des conventions numeriques. Avec `lambda = 2pi/k`, on obtient `lambda_min = 4 hbar sqrt(beta)`, alors que l'incertitude minimale donne `Delta x_min = hbar sqrt(beta)`. Ces deux quantites ne doivent pas etre identifiees au facteur exact pres.

## Ajout utile non present dans le texte initial

Pour le gaz classique massif non relativiste, la limite haute temperature est finie :

```tex
\lim_{T\to\infty}\frac{U}{N} =
\frac{3}{2m\beta}
=
\frac32 \frac{p_{\mathrm{GUP}}^2}{m}.
```

Donc, contrairement aux photons pour lesquels `u(T) ~ n_max k_B T`, un gaz classique massif dans le regime non relativiste du modele a une energie moyenne qui sature. Cette limite doit toutefois etre utilisee avec prudence, car le regime non relativiste finit par echouer si l'energie approche `mc^2`.
