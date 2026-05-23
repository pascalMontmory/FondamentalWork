# Sensor technical noise budget

This report extends the phase-space CAD proxy with first-order technical
noise envelopes for a three-pulse cold-atom gravimeter.

The model is useful for ranking assumptions, not for certifying an
instrument. The PSDs and coefficients are explicit inputs that must be
replaced by measured laser, seismometer, magnetometer and thermal data for
a real design.

## Model status

| block | status | comment |
|---|---|---|
| quantum projection noise | standard quantum limit | `1/(C sqrt(N_at))` |
| photon shot noise | detection proxy | Poisson photon count with detection efficiency and excess imaging noise |
| laser phase noise | envelope PSD | replace by measured Raman relative phase PSD |
| seismic vibration | envelope PSD + isolation transfer | constant `-40 dB` is kept only as an optimistic bound |
| thermal drift | proxy | BBR plus mechanical thermal phase; not a calibrated Allan model |
| Johnson-Nyquist magnetic noise | proxy | magnetic ASD times explicit `dnu/dB` sensitivity |
| duty cycle | explicit | `T_cycle = T_prep + 2 T_i + T_detection + T_dead` |

## Equations

```text
sigma_phi_laser^2 = integral |H_phi(f)|^2 S_phi(f) df
|H_phi(f)|^2 ~= 16 sin^4(pi f T_i)
sigma_phi_vib^2 = k_eff^2 integral |H_a(f)|^2 S_a(f) df
|H_a(f)|^2 ~= [4 sin^2(pi f T_i)/(2 pi f)^2]^2
sigma_phi_JN^2 = (2 pi)^2 integral |H_nu(f)|^2 (dnu/dB)^2 S_B(f) df
sigma_phi_QPN = 1/(C sqrt(N_at))
sigma_phi_photon = F_excess/(C sqrt(N_ph_per_atom N_at eta_det))
sigma_phi_total^2 = phi_QPN^2 + phi_photon^2 + (phi_laser/C)^2 + (phi_vib/C)^2 + (phi_thermal/C)^2 + (phi_JN/C)^2
T_cycle = T_prep + 2 T_i + T_detection + T_dead
delta a_sqrtHz = sigma_phi_total sqrt(T_cycle)/(k_eff T_i^2)
```

## Nominal contribution budget

Nominal case: `sr88_nominal_typical_lab_active`, closest point to `T_i = 100 ms`.

| contribution | variance fraction [%] | phase term [rad] |
|---|---:|---:|
| qpn | 0.92 | 1.86e-03 |
| photon | 3.69 | 3.73e-03 |
| laser | 45.57 | 7.86e-03 |
| vibration | 49.44 | 8.18e-03 |
| thermal | 0.38 | 7.13e-04 |
| johnson | 0.00 | 3.97e-08 |

Result at this point:

```text
T_i = 0.102 s
T_cycle = 1.253 s
dominant_noise = vibration
delta a = 11.52 microGal/sqrtHz
```

## Benchmark sanity check

| model case | published reference | T_i [s] | model [microGal/sqrtHz] | reference [microGal/sqrtHz] | ratio |
|---|---|---:|---:|---:|---:|
| nim_like_active_105ms | NIM transportable atomic gravimeter lab benchmark | 0.106 | 19.72 | 20.50 | 0.96 |
| muquans_like_quiet_site | Muquans/Exail AQG quiet-site datasheet | 0.102 | 26.44 | 50.00 | 0.53 |

The benchmark cases are not fitted instruments. They are sanity checks:
the model should land in the same order of magnitude only after choosing
reasonable atom number, contrast, cycle time and isolation envelopes.

Public anchors used here:

- Muquans/Exail AQG: `50 microGal/sqrtHz` sensitivity at a quiet place;
- NIM transportable atomic gravimeter: `20.5 microGal/sqrtHz` in the
  laboratory and `10.8 microGal/sqrtHz` in a seismic station, with a
  `105 ms` interrogation time and `1 s` measurement cycle reported.

## Sample scan values

| case | Ti [s] | cycle [s] | QPN [rad] | photon [rad] | laser [rad] | vib [rad] | thermal [rad] | JN [rad] | dominant | delta a [microGal/sqrtHz] |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| typical_lab_no_isolation | 0.050 | 1.201 | 1.82e-03 | 6.10e-03 | 7.87e-03 | 3.03e-02 | 5.03e-04 | 2.88e-07 | vibration | 1.54e+02 |
| typical_lab_no_isolation | 0.102 | 1.303 | 1.82e-03 | 6.10e-03 | 7.86e-03 | 8.19e-02 | 1.02e-03 | 3.97e-07 | vibration | 1.03e+02 |
| typical_lab_no_isolation | 0.245 | 1.590 | 1.82e-03 | 6.10e-03 | 7.95e-03 | 2.58e-01 | 2.45e-03 | 6.72e-07 | vibration | 6.13e+01 |
| typical_lab_no_isolation | 0.495 | 2.090 | 1.82e-03 | 6.10e-03 | 7.98e-03 | 5.35e-01 | 4.95e-03 | 1.10e-06 | vibration | 3.56e+01 |
| typical_lab_no_isolation | 1.000 | 3.100 | 1.82e-03 | 6.10e-03 | 8.00e-03 | 9.21e-01 | 1.00e-02 | 1.79e-06 | vibration | 1.83e+01 |
| typical_lab_constant_40db | 0.050 | 1.201 | 1.82e-03 | 6.10e-03 | 7.87e-03 | 3.03e-04 | 5.03e-04 | 2.88e-07 | laser | 4.21e+01 |
| typical_lab_constant_40db | 0.102 | 1.303 | 1.82e-03 | 6.10e-03 | 7.86e-03 | 8.19e-04 | 1.02e-03 | 3.97e-07 | laser | 1.08e+01 |
| typical_lab_constant_40db | 0.245 | 1.590 | 1.82e-03 | 6.10e-03 | 7.95e-03 | 2.58e-03 | 2.45e-03 | 6.72e-07 | laser | 2.23e+00 |
| typical_lab_constant_40db | 0.495 | 2.090 | 1.82e-03 | 6.10e-03 | 7.98e-03 | 5.35e-03 | 4.95e-03 | 1.10e-06 | laser | 7.57e-01 |
| typical_lab_constant_40db | 1.000 | 3.100 | 1.82e-03 | 6.10e-03 | 8.00e-03 | 9.21e-03 | 1.00e-02 | 1.79e-06 | thermal | 3.21e-01 |
| typical_lab_active_portable | 0.050 | 1.201 | 1.82e-03 | 6.10e-03 | 7.87e-03 | 1.95e-03 | 5.03e-04 | 2.88e-07 | laser | 4.32e+01 |
| typical_lab_active_portable | 0.102 | 1.303 | 1.82e-03 | 6.10e-03 | 7.86e-03 | 7.23e-03 | 1.02e-03 | 3.97e-07 | laser | 1.41e+01 |
| typical_lab_active_portable | 0.245 | 1.590 | 1.82e-03 | 6.10e-03 | 7.95e-03 | 3.67e-02 | 2.45e-03 | 6.72e-07 | vibration | 8.96e+00 |
| typical_lab_active_portable | 0.495 | 2.090 | 1.82e-03 | 6.10e-03 | 7.98e-03 | 1.28e-01 | 4.95e-03 | 1.10e-06 | vibration | 8.54e+00 |
| typical_lab_active_portable | 1.000 | 3.100 | 1.82e-03 | 6.10e-03 | 8.00e-03 | 4.14e-01 | 1.00e-02 | 1.79e-06 | vibration | 8.23e+00 |
| sr88_nominal_typical_lab_active | 0.050 | 1.151 | 1.86e-03 | 3.73e-03 | 7.87e-03 | 2.21e-03 | 3.53e-04 | 2.88e-08 | laser | 3.31e+01 |
| sr88_nominal_typical_lab_active | 0.102 | 1.253 | 1.86e-03 | 3.73e-03 | 7.86e-03 | 8.18e-03 | 7.13e-04 | 3.97e-08 | vibration | 1.15e+01 |
| sr88_nominal_typical_lab_active | 0.245 | 1.540 | 1.86e-03 | 3.73e-03 | 7.95e-03 | 4.15e-02 | 1.72e-03 | 6.72e-08 | vibration | 8.01e+00 |
| sr88_nominal_typical_lab_active | 0.495 | 2.040 | 1.86e-03 | 3.73e-03 | 7.98e-03 | 1.45e-01 | 3.47e-03 | 1.10e-07 | vibration | 7.72e+00 |
| sr88_nominal_typical_lab_active | 1.000 | 3.050 | 1.86e-03 | 3.73e-03 | 8.00e-03 | 4.68e-01 | 7.01e-03 | 1.79e-07 | vibration | 7.48e+00 |
| nim_like_active_105ms | 0.050 | 0.891 | 5.74e-03 | 2.96e-02 | 7.87e-03 | 9.14e-04 | 5.03e-04 | 2.88e-07 | photon | 8.08e+01 |
| nim_like_active_105ms | 0.102 | 0.993 | 5.74e-03 | 2.96e-02 | 7.86e-03 | 3.01e-03 | 1.02e-03 | 3.97e-07 | photon | 2.13e+01 |
| nim_like_active_105ms | 0.245 | 1.280 | 5.74e-03 | 2.96e-02 | 7.95e-03 | 1.39e-02 | 2.45e-03 | 6.72e-07 | vibration | 5.50e+00 |
| nim_like_active_105ms | 0.495 | 1.780 | 5.74e-03 | 2.96e-02 | 7.98e-03 | 4.53e-02 | 4.95e-03 | 1.10e-06 | vibration | 3.63e+00 |
| nim_like_active_105ms | 1.000 | 2.790 | 5.74e-03 | 2.96e-02 | 8.00e-03 | 1.39e-01 | 1.00e-02 | 1.79e-06 | vibration | 3.24e+00 |
| muquans_like_quiet_site | 0.050 | 0.501 | 9.04e-03 | 5.11e-02 | 7.87e-03 | 3.72e-04 | 6.04e-04 | 2.88e-07 | photon | 9.81e+01 |
| muquans_like_quiet_site | 0.102 | 0.603 | 9.04e-03 | 5.11e-02 | 7.86e-03 | 8.13e-04 | 1.22e-03 | 3.97e-07 | photon | 2.64e+01 |
| muquans_like_quiet_site | 0.245 | 0.890 | 9.04e-03 | 5.11e-02 | 7.95e-03 | 2.31e-03 | 2.94e-03 | 6.72e-07 | photon | 5.63e+00 |
| muquans_like_quiet_site | 0.495 | 1.390 | 9.04e-03 | 5.11e-02 | 7.98e-03 | 4.95e-03 | 5.94e-03 | 1.10e-06 | photon | 1.82e+00 |
| muquans_like_quiet_site | 1.000 | 2.400 | 9.04e-03 | 5.11e-02 | 8.00e-03 | 9.65e-03 | 1.20e-02 | 1.79e-06 | photon | 6.90e-01 |

## Interpretation

- The constant `-40 dB` isolation case is an optimistic lower-bound
  envelope, not a portable-system claim.
- The `portable_active`, `cs_avi_like` and `feedforward_compensation`
  cases use frequency-dependent isolation transfer functions, including
  weak or no rejection at the lowest frequencies.
- The photon-shot term is separated from QPN because imaging background,
  camera readout and optical collection can make it much larger than the
  ideal Poisson limit; this is represented by `photon_excess_noise_factor`.
- The Johnson-Nyquist term is normally small in these nominal cases, but
  it is now explicit and can dominate if shielding is poor or if the
  chosen transition has a large `dnu/dB` sensitivity.
- The duty cycle matters directly through `sqrt(T_cycle)`. Long source
  preparation can erase part of the gain from increasing `T_i`.

Data: `reports/data/sensor_noise_budget.csv`

Figures:

- `reports/figures/sensor_noise_budget.png`
- `reports/figures/sensor_noise_dominance.png`
