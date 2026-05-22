# Carte theorique

## Niveau fondamental propose

Le niveau profond n'est pas deux actions Einstein-Hilbert independantes. La
formulation prudente est une couche hermitienne/symplectique:

```text
H_AB = G_AB + i Omega_AB
```

La relativite generale ordinaire apparait comme projection reelle effective:

```text
S_fund[H, nabla, Psi]
  -> S_eff[g_+, psi; Sigma]
```

## Niveau effectif observable

L'action effective utilisee dans la publication est:

```text
S_eff =
  M_Pl^2/2 int sqrt(-g) R
  + S_m
  + S_edge[P0 gamma]
  + epsilon_J S_loc[(1-P0) gamma]
```

Le projecteur `P0` isole le mode homogene du bord.

## Canal acceleration

Le stress tenseur de bord viable est:

```text
T_edge_mu_nu = - rho_edge g_mu_nu
delta T_edge(k > 0) ~= 0
```

Alors:

```text
q0 = 1/2 [Omega_m + Omega_edge (1 + 3w)]
```

Pour `w=-1` et `Omega_edge=0.685`:

```text
q0 = -0.5275
```

## Canal Moebius

L'holonomie globale est:

```text
(chi + 2 pi, tau) ~ (chi, -tau)
psi(chi + 2 pi) = exp(i theta_M) CPT psi(chi)
```

Le facteur demi-bord vient du quotient:

```text
g_edge_sheet = N_boundary(Moebius) / N_boundary(double cover) = 1/2
```

## Perturbations

La condition de compatibilite locale est:

```text
delta rho_edge(k > 0) = 0
```

Une fuite locale serait parametree par:

```text
Phi_cross / Phi_N ~= epsilon_J exp(-r/lambda_s)
```

avec contrainte conservative:

```text
max |Phi_cross/Phi_N| < 1e-5
```

## CMB

Le zero-mode ne remplace pas la physique acoustique du CMB.

La signature specifique possible est une rotation de polarisation:

```text
(Q +/- iU)' = exp(+-2 i beta)(Q +/- iU)
C_l^TB = sin(2 beta) C_l^TE
C_l^EB = 1/2 sin(4 beta)(C_l^EE - C_l^BB)
```

## Verdict theorique

Le modele est:

```text
compatible comme EFT de bord
degenere avec Lambda-CDM dans la limite stricte
testable par deviations controlees, surtout EB/TB CMB
non confirme experimentalement a ce stade
```
