# Atom comparison: phase-space budget

This report adds an explicit sensitivity figure of merit with a
phase-space atom-number cap:

```text
N_phase_cap = eta_max V_eff / lambda_th^3
N_detected = min(N_technical survival, N_phase_cap)
FOM = sqrt(N_detected) T_i^2
delta a ~= 1 / (k_eff FOM)
```

The GUP correction is also quantified through
`epsilon_GUP = beta0 (m sigma_v / p_Pl)^2`.

| atom | access | best T [K] | best Ti [s] | recoil T [K] | sigma_v [m/s] | N budget | FOM max | delta a [m/s2] | beta p2 beta0=1 | beta p2 beta0=1e26 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Sr88 | good | 1.00e-08 | 1 | 2.29e-07 | 9.73e-04 | 1.00e+07 | 3.16e+03 | 1.73e-11 | 4.73e-58 | 4.73e-32 |
| Yb174 | good | 1.00e-08 | 1 | 1.78e-07 | 6.91e-04 | 1.00e+07 | 3.16e+03 | 1.40e-11 | 9.37e-58 | 9.37e-32 |
| Cs133 | excellent | 1.00e-07 | 1 | 9.92e-08 | 2.50e-03 | 1.00e+07 | 3.16e+03 | 2.14e-11 | 7.16e-57 | 7.16e-31 |
| Rb87 | excellent | 1.00e-07 | 1 | 1.81e-07 | 3.09e-03 | 9.99e+06 | 3.16e+03 | 1.96e-11 | 4.68e-57 | 4.68e-31 |
| Li7 | specialized | 3.00e-07 | 1 | 3.03e-06 | 1.89e-02 | 1.07e+06 | 1.03e+03 | 5.16e-11 | 1.13e-57 | 1.13e-31 |
| Li6 | specialized | 3.00e-07 | 1 | 3.54e-06 | 2.04e-02 | 8.74e+05 | 9.35e+02 | 5.71e-11 | 9.72e-58 | 9.72e-32 |

Interpretation:

- `FOM = sqrt(N_detected) T_i^2` is a first-order proxy. A real
  instrument must also include contrast, laser phase noise, vibration
  rejection, wavefront aberrations, detection noise, duty cycle and Allan
  deviation;
- heavier atoms have smaller velocity dispersion at fixed temperature;
- Sr/Yb benefit from narrow-line cooling but require more complex optics;
- Li has larger recoil and larger velocity spread, so it is less natural
  for compact inertial sensors despite specialized advantages;
- even the deliberately loose `beta0=1e26` GUP column is far below
  direct relevance for cold-atom sensor design.

Data: `reports/data/atom_phase_space_budget.csv`

Figure: `reports/figures/atom_phase_space_budget.png`

Focused figure: `reports/figures/atom_phase_space_budget_focus.png`