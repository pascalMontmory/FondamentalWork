# Projected twin-sheet boundary model for dark energy

## Core claim

The robust result is not that the new model is experimentally confirmed. The robust result is that a local universal GUP vacuum explanation of dark energy is excluded, and this conclusion survives a general exponent `gamma`.

The viable positive direction is:

```text
conjugate twin sector
-> global boundary condition
-> zero-mode edge stress
-> Lambda-CDM background limit
```

## Main equations

General GUP measure:

```text
dN_gamma = g d3x d3p / [h^3 (1 + beta p^2)^gamma]
```

Massless vacuum density for `gamma > 2`:

```text
rho_vac(gamma)
  = [2 / ((gamma - 1)(gamma - 2))]
    g rho_P / (16 pi^2 beta0^2)
```

Twin residual accounting:

```text
rho_eff = rho_plus - rho_minus + rho_edge
```

Zero-mode boundary stress:

```text
T_edge_mu_nu = -rho_edge g_mu_nu
delta T_edge(k > 0) ~= 0
```

Hybrid Janus-zero-mode EFT:

```text
T_mix = P0 T_Janus + epsilon_J S_lambda (1 - P0) T_Janus
```

Moebius half-edge:

```text
g_edge_sheet = N_boundary_Moebius / N_boundary_double_cover = 1/2
```

Future-bulge interpretation:

```text
Moebius future/other side
-> global boundary curvature or tension
-> homogeneous negative pressure
-> acceleration
```

CMB boundary signature:

```text
zero-mode       -> acceleration, not the CMB spot map
Moebius low-ell -> possible weak large-angle signature
local dents     -> constrained by CMB/lensing/structure growth
```

## Verification verdicts

Run:

```bash
python3 scripts/run_all_twin_tests.py
```

Key verdicts:

- `gamma sensitivity`: `no_go_robust_to_gamma_variation`
- `zero-mode acceleration`: `viable_as_acceleration_channel`
- `future bulge acceleration`: `viable_if_bulge_means_global_boundary_tension`
- `CMB boundary signature`: `possible_only_as_weak_low_ell_boundary_signature`
- `Lambda-CDM degeneracy`: `degenerate_with_Lambda_CDM_if_exact`
- `hybrid Janus zero-mode EFT`: `viable_as_eft_if_projected_or_screened`
- `Moebius time holonomy`: `compatible_as_global_nontraversable_holonomy`
- `theory upgrade score`: `improves_internal_theory_not_observational_confirmation`

Internal quality score:

```text
unscreened local Janus-like coupling   0.37
pure zero-mode boundary pressure       0.69
hybrid Moebius/projected model         0.84
```

## Final status

The hybrid Moebius/projected version improves the internal theory:

- the half-edge factor gets a topological origin;
- local cross-sheet modes are projected, screened, or explicitly bounded;
- deviations from Lambda-CDM become falsifiable parameters;
- a future-bulge picture is viable only as global boundary tension;
- the CMB role is limited to possible weak low-ell/global signatures.

It does not yet improve experimental confirmation beyond Lambda-CDM. The missing hard result is a spectral derivation of the regularized `U(1)` edge capacity equal to `1/2`.