# Sensor technical noise budget

This report extends the phase-space CAD proxy with first-order technical
noise envelopes for a three-pulse cold-atom gravimeter.

The model is useful for ranking assumptions, not for certifying an
instrument. The PSDs and coefficients are explicit inputs that must be
replaced by measured laser, seismometer and thermal data for a real design.

## Equations

```text
sigma_phi_laser^2 = integral |H_phi(f)|^2 S_phi(f) df
|H_phi(f)|^2 ~= 16 sin^4(pi f T_i)
sigma_phi_vib^2 = k_eff^2 integral |H_a(f)|^2 S_a(f) df
|H_a(f)|^2 ~= [4 sin^2(pi f T_i)/(2 pi f)^2]^2
sigma_phi_total^2 = 1/N + (phi_laser/C)^2 + (phi_vib/C)^2 + (phi_thermal/C)^2
delta a_sqrtHz = sigma_phi_total sqrt(T_cycle)/(k_eff T_i^2)
```

The vibration model uses acceleration PSD envelopes in `(m/s2)^2/Hz`.
The isolation factor multiplies acceleration amplitude spectral density,
so `0.01` corresponds to about `-40 dB` amplitude isolation.

## Sample values

| case | Ti [s] | laser [rad] | vib [rad] | thermal [rad] | total [rad] | delta a [microGal/sqrtHz] |
|---|---:|---:|---:|---:|---:|---:|
| typical_lab_no_isolation | 0.050 | 7.87e-03 | 3.03e-02 | 5.03e-04 | 5.69e-02 | 1.71e+02 |
| typical_lab_no_isolation | 0.102 | 7.86e-03 | 8.19e-02 | 1.02e-03 | 1.50e-01 | 1.10e+02 |
| typical_lab_no_isolation | 0.245 | 7.95e-03 | 2.58e-01 | 2.45e-03 | 4.70e-01 | 5.96e+01 |
| typical_lab_no_isolation | 0.495 | 7.98e-03 | 5.35e-01 | 4.95e-03 | 9.73e-01 | 3.02e+01 |
| typical_lab_no_isolation | 1.000 | 8.00e-03 | 9.21e-01 | 1.00e-02 | 1.67e+00 | 1.27e+01 |
| typical_lab_40db_isolation | 0.050 | 7.87e-03 | 3.03e-04 | 5.03e-04 | 1.44e-02 | 4.31e+01 |
| typical_lab_40db_isolation | 0.102 | 7.86e-03 | 8.19e-04 | 1.02e-03 | 1.45e-02 | 1.07e+01 |
| typical_lab_40db_isolation | 0.245 | 7.95e-03 | 2.58e-03 | 2.45e-03 | 1.59e-02 | 2.01e+00 |
| typical_lab_40db_isolation | 0.495 | 7.98e-03 | 5.35e-03 | 4.95e-03 | 1.97e-02 | 6.11e-01 |
| typical_lab_40db_isolation | 1.000 | 8.00e-03 | 9.21e-03 | 1.00e-02 | 2.87e-02 | 2.18e-01 |
| quiet_site_40db_isolation | 0.050 | 7.87e-03 | 6.66e-05 | 2.52e-04 | 1.21e-02 | 3.65e+01 |
| quiet_site_40db_isolation | 0.102 | 7.86e-03 | 1.31e-04 | 5.09e-04 | 1.22e-02 | 8.94e+00 |
| quiet_site_40db_isolation | 0.245 | 7.95e-03 | 2.86e-04 | 1.22e-03 | 1.24e-02 | 1.57e+00 |
| quiet_site_40db_isolation | 0.495 | 7.98e-03 | 4.35e-04 | 2.47e-03 | 1.29e-02 | 4.01e-01 |
| quiet_site_40db_isolation | 1.000 | 8.00e-03 | 4.97e-04 | 5.00e-03 | 1.46e-02 | 1.11e-01 |
| urban_40db_isolation | 0.050 | 7.87e-03 | 5.32e-02 | 1.01e-03 | 1.08e-01 | 3.23e+02 |
| urban_40db_isolation | 0.102 | 7.86e-03 | 7.84e-02 | 2.03e-03 | 1.58e-01 | 1.16e+02 |
| urban_40db_isolation | 0.245 | 7.95e-03 | 1.25e-01 | 4.90e-03 | 2.50e-01 | 3.17e+01 |
| urban_40db_isolation | 0.495 | 7.98e-03 | 1.79e-01 | 9.90e-03 | 3.59e-01 | 1.11e+01 |
| urban_40db_isolation | 1.000 | 8.00e-03 | 2.56e-01 | 2.00e-02 | 5.14e-01 | 3.91e+00 |

## Interpretation

- Without isolation, vibration dominates quickly as `T_i` grows.
- With `-40 dB` vibration isolation, the same source budget can move into
  the `10-50 microGal/sqrtHz` transportable range for realistic
  interrogation times, depending on contrast and cycle time.
- The laser phase model is intentionally an envelope. A real Raman system
  must replace it by the measured relative phase-noise PSD.
- The thermal term combines BBR sensitivity and a mechanical thermal
  phase proxy. It is usually not the dominant per-shot term here, but it
  matters for drift, systematics and Allan deviation.

Data: `reports/data/sensor_noise_budget.csv`

Figure: `reports/figures/sensor_noise_budget.png`
