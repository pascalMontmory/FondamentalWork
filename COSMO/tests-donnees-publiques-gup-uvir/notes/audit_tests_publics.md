# Audit des tests publics

## Resultat global

Les tests confirment une conclusion nette :

```math
\beta_0^{(\Lambda)}\sim10^{60}
```

ne peut pas etre un parametre universel applique aux photons, au plasma
primordial et aux fermions denses. Cette valeur doit etre interpretee soit
comme un parametre effectif du secteur gravitationnel/vide, soit abandonnee au
profit d'une projection UV/IR holographique.

## 1. FIRAS / CMB

Pour les photons, la deformation utilisee dans les notes donne

```math
u(E,T)\propto
\frac{E^3}{(e^{E/k_BT}-1)(1+\beta E^2/c^2)^3}.
```

Avec

```math
\beta E^2/c^2 = \beta_0(E/E_P)^2,
```

le parametre pertinent au CMB est

```math
\theta_{\rm CMB}=\beta_0(k_BT_0/E_P)^2.
```

Le script compare le spectre GUP au meilleur corps noir ajuste en temperature
sur la bande FIRAS 2--20 cm^-1. Le critere public utilise est la precision
FIRAS d'environ `50 ppm` sur les deviations de forme du corps noir.

Resultat numerique du script :

```text
theta_CMB(beta0_DE) = 8.745620e-04
RMS distortion / peak = 2.806066e-03
FIRAS public limit used = 5.000000e-05
beta0 bound from FIRAS shape ~= 3.716510e+58
exclusion factor = 6.358730e+01
```

Conclusion : `beta0_DE ~ 10^60` produit une distorsion trop grande. Il est donc
exclu comme parametre photon universel.

## 2. Energie noire holographique

La relation

```math
\rho_X(L)=\eta\frac{3c^4}{8\pi G L^2}
```

n'est testable cosmologiquement qu'apres un choix dynamique de `L`. Pour
l'horizon des evenements futur dans le modele HDE plat non interactif :

```math
w_{\rm HDE}
=
-\frac13-\frac{2}{3c_{\rm hde}}\sqrt{\Omega_{\rm DE}}.
```

Avec `Omega_DE=0.685`, `c_hde=1` donne `w0=-0.885`, en tension avec la
contrainte publique Planck+BAO+SNe approximative `w=-1.03+-0.03`. Un parametre
`c_hde ~ 0.79` reproduit mieux cette valeur.

Conclusion : la piste holographique est testable, mais le choix de longueur IR
et son parametre dynamique sont decisifs.

## 3. SPARC / acceleration cosmologique

Les notes donnent deux accelerations possibles :

```math
a_{\rm dS}=c^2\sqrt{\Lambda/3},
\qquad
a_\Lambda=c^2\sqrt{\Lambda}.
```

Le script compare `a_dS/(2pi)` et `a_Lambda/(2pi)` a l'echelle empirique
SPARC/MOND `a0 ~ 1.2e-10 m/s^2`.

Conclusion : l'accord est seulement d'ordre de grandeur. C'est une piste de
coincidence UV/IR interessante, mais pas une preuve du GUP.

## 4. BBN / Neff

La correction de rayonnement des notes est

```math
\frac{\Delta u}{u}
\simeq
-\frac{40\pi^2}{7}\beta_0\left(\frac{k_BT}{E_P}\right)^2.
```

A `T ~ 1 MeV`, le `beta0_DE` donnerait une correction gigantesque. Une borne
conservatrice `|Delta rho/rho| < 0.1` impose environ

```math
\beta_0 \lesssim 10^{41}.
```

Resultat numerique du script :

```text
|delta rho/rho| at T~1 MeV for beta0_DE = 8.941578e+17
beta0 bound for <10% radiation correction ~= 2.642965e+41
exclusion factor = 8.941578e+18
```

Conclusion : `beta0_DE ~ 10^60` est exclu dans le secteur radiation du jeune
univers.

## 5. Etoiles a neutrons

Dans la matiere dense, un ordre de grandeur typique est

```math
p_F c \sim 300 MeV.
```

La correction GUP est controlee par

```math
\chi = \beta_0(p_Fc/E_P)^2.
```

Exiger `chi < 0.1` donne une borne d'ordre

```math
\beta_0 \lesssim 10^{38}.
```

Resultat numerique du script :

```text
chi=beta p_F^2 at beta0_DE = 1.426905e+21
beta0 bound for chi<0.1 ~= 1.656192e+38
exclusion factor = 1.426905e+22
```

Conclusion : `beta0_DE ~ 10^60` est exclu pour les fermions denses, sinon la
physique des etoiles a neutrons serait radicalement modifiee.

## Conclusion scientifique

Les donnees publiques imposent une lecture stricte :

```math
\boxed{
\text{le } \beta_0\text{ ajuste a }\rho_{\rm DE}
\text{ ne peut pas etre universel.}
}
```

La conclusion positive des travaux reste :

```math
\boxed{
\text{GUP regularise l'UV, mais l'energie noire doit venir d'une projection IR/holographique.}
}
```

Ce resultat est publiable comme contrainte/no-go conditionnelle : toute theorie
qui identifie directement le vide GUP a l'energie noire doit expliquer pourquoi
la deformation ne s'applique pas universellement aux photons, au plasma
primordial et a la matiere dense.
