# Phase-Space CAD for Cold-Atom Quantum Sensors

## Abstract

This note develops a practical application of the phase-space cell relation

```text
D^3 v^3 ~ h^3 / m^3
```

and of the thermal phase-space density

```text
eta = n lambda_th^3.
```

The result is not a propulsion mechanism and not a new equation of state. The
useful industrial application is a first-order computer-aided design framework
for cold-atom quantum sensors: gravimeters, gyroscopes, accelerometers,
gravity gradiometers and inertial navigation units.

This phase-space CAD framework is primarily motivated, but not driven, by GUP
considerations. The GUP deformation gives a useful theoretical language for
phase-space counting, while the applied sensor budget uses the experimentally
robust `beta -> 0` limit.

The central claim is conservative: before detailed optical, electronic and
vibration models are introduced, a candidate atom-sensor architecture must
already pass a phase-space budget. Temperature, density, atomic mass,
interrogation time, cloud expansion and detected atom number are coupled. A
design that fails this budget cannot reach the target sensitivity without a
larger package, a colder source, a denser source, better detection, or a
different atom.

## Core formulas

The de Broglie thermal wavelength is

```text
lambda_th = h / sqrt(2 pi m k_B T).
```

The phase-space density is

```text
eta = n lambda_th^3.
```

The one-dimensional thermal velocity dispersion is

```text
sigma_v = sqrt(k_B T / m).
```

For a Gaussian cloud released into free expansion, a first-order radius proxy is

```text
R(t) = sqrt(R0^2 + sigma_v^2 t^2).
```

For a light-pulse atom interferometer, the shot-noise acceleration floor is

```text
delta a ~= 1 / (k_eff T_i^2 sqrt(N_detected)).
```

For a gyroscope using a transverse atomic velocity `v`, a Sagnac-like proxy is

```text
delta Omega ~= 1 / (2 k_eff v T_i^2 sqrt(N_detected)).
```

These equations are standard dimensional and interferometric estimates. The
added value is to treat them as one coupled design budget instead of isolated
figures of merit.

## Explicit phase-space budget

For a gravimeter-like sensor, a simple sensitivity figure of merit is

```text
FOM = sqrt(N_detected) T_i^2
FOM_Hz = sqrt(N_detected / T_cycle) T_i^2, if the total cycle time is known
delta a ~= 1 / (k_eff FOM).
```

The detected atom number cannot be chosen independently of the source
phase-space density. A conservative cap is

```text
N_phase_cap = eta_max V_eff / lambda_th^3
N_detected = min(N_technical survival, N_phase_cap).
```

The script `scripts/compare_atom_phase_space_budget.py` implements this budget
with `eta_max = 0.3`, a `12 mm` aperture radius and a technical atom cap of
`1e7`. It scans Rb87, Cs133, Sr88, Yb174, Li6 and Li7.

Best practical-floor points:

| atom | access | best T [K] | best Ti [s] | recoil T [K] | sigma_v [m/s] | N budget | FOM max | delta a [m/s2] |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Sr88 | good | 1.0e-8 | 1 | 2.29e-7 | 9.73e-4 | 1.0e7 | 3.16e3 | 1.73e-11 |
| Yb174 | good | 1.0e-8 | 1 | 1.78e-7 | 6.91e-4 | 1.0e7 | 3.16e3 | 1.40e-11 |
| Cs133 | excellent | 1.0e-7 | 1 | 9.92e-8 | 2.50e-3 | 1.0e7 | 3.16e3 | 2.14e-11 |
| Rb87 | excellent | 1.0e-7 | 1 | 1.81e-7 | 3.09e-3 | 9.99e6 | 3.16e3 | 1.96e-11 |
| Li7 | specialized | 3.0e-7 | 1 | 3.03e-6 | 1.89e-2 | 1.07e6 | 1.03e3 | 5.16e-11 |
| Li6 | specialized | 3.0e-7 | 1 | 3.54e-6 | 2.04e-2 | 8.74e5 | 9.35e2 | 5.71e-11 |

This makes the atom-choice trade-off explicit: Sr/Yb can reach lower practical
temperatures through narrow-line cooling, Rb/Cs remain mature and accessible,
while Li expands faster and has a larger recoil temperature.

This FOM is only a first-order proxy. An engineering-grade model must multiply
the ideal atom-shot-noise term by contrast and duty-cycle factors, then add
laser phase noise, vibration residuals, wavefront aberrations, detection noise
and Allan-deviation behavior.

When the total cycle time is known, the per-root-Hz proxy should be written as

```text
FOM_Hz = sqrt(N_detected / T_cycle) T_i^2.
```

This makes duty cycle explicit: long cooling, preparation, detection or dead
times reduce the usable sensitivity even if the single-shot atom budget looks
excellent.

## Technical noise budget extension

The script `scripts/simulate_sensor_noise_budget.py` adds a first-order
technical-noise envelope for a three-pulse gravimeter. It is deliberately kept
separate from the atom-source budget because these terms are instrument and site
dependent:

```text
sigma_phi_laser^2 = integral |H_phi(f)|^2 S_phi(f) df
|H_phi(f)|^2 ~= 16 sin^4(pi f T_i)
sigma_phi_vib^2 = k_eff^2 integral |H_a(f)|^2 S_a(f) df
|H_a(f)|^2 ~= [4 sin^2(pi f T_i)/(2 pi f)^2]^2
sigma_phi_total^2 = 1/N + (phi_laser/C)^2 + (phi_vib/C)^2 + (phi_thermal/C)^2
delta a_sqrtHz = sigma_phi_total sqrt(T_cycle)/(k_eff T_i^2)
```

The vibration model uses approximate acceleration ASD envelopes for quiet,
typical-lab and urban sites. The laser model uses a simple Raman relative
phase-noise PSD envelope. The thermal model combines a BBR sensitivity proxy
with an empirical mechanical thermal phase term. These are not universal
constants; they are placeholders to be replaced by measured PSDs and calibrated
instrument data.

The first generated benchmark gives the expected qualitative result: vibration
dominates in a non-isolated lab, while a `-40 dB` amplitude isolation factor can
move the model into the `10-50 microGal/sqrt(Hz)` transportable range for
moderate to long interrogation times.

## Example use case

Consider a portable gravimeter targeting an aggressive

```text
delta a_target = 10 microGal/sqrt(Hz) = 1e-7 m/s2/sqrt(Hz).
```

The conversion matters: `1 microGal = 1e-8 m/s2`, so a target of
`1e-8 m/s2/sqrt(Hz)` would be `1 microGal/sqrt(Hz)`, a much more aggressive
stretch target rather than a standard portable field specification. Public
transportable atom gravimeters are commonly reported around
`10-65 microGal/sqrt(Hz)`, depending on vibration environment and architecture.

The phase-space budget says a `10 microGal/sqrt(Hz)` target is not necessarily
atom-shot-noise limited at the source level. The best Rb87/Sr/Yb points in the
table sit near `1e-11 m/s2` before contrast loss, vibration noise, laser phase
noise, wavefront aberrations, dead time and detection noise are included. The
practical conclusion is precise: the cold-atom source can be good enough in
first order; the hard work moves to vibration rejection, optical phase
stability, contrast preservation, cycle time and field packaging.

For a compact gyroscope aimed at inertial navigation, the same table is only a
source prefilter. A full gyroscope model must add the enclosed interferometer
area, transverse velocity, rotation geometry, platform motion, duty cycle and
long-term bias stability.

Public context for the benchmark range:

- NIM transportable atomic gravimeter: `20.5 microGal/sqrt(Hz)` in the
  laboratory and `10.8 microGal/sqrt(Hz)` in a seismic station;
- mobile atom-interferometer gravity survey: `37 microGal/sqrt(Hz)`;
- commercial absolute quantum gravimeter datasheet: `50 microGal/sqrt(Hz)` in
  a quiet place.

## GUP correction scale

For the deformed measure

```text
dN_GUP = dN_0 / (1 + beta m^2 v^2)^3
```

the relevant small parameter is

```text
epsilon_GUP = beta p^2 = beta0 (m v / p_Pl)^2.
```

For Rb87 at `T = 1 microkelvin`,

```text
sigma_v = 9.78e-3 m/s
epsilon_GUP(beta0=1)    = 4.68e-56
epsilon_GUP(beta0=1e26) = 4.68e-30
(1 + epsilon_GUP)^-3 ~= 1 - 3 epsilon_GUP.
```

So the GUP factor is not an observable industrial correction here. It is many
orders of magnitude below cold-atom sensitivity even with a deliberately loose
phenomenological `beta0 = 1e26`. The industrial framework is therefore the
`beta -> 0` phase-space budget, not detection of the GUP deformation.

## Why this is useful

Cold atoms improve inertial and gravity sensing because they provide stable,
quantum-identical probes. However, the same cooling that improves coherence
also imposes engineering constraints: vacuum package size, laser power, atom
number, detection efficiency, interrogation time and cycle rate.

The phase-space CAD framework answers simple but decisive questions:

- Is the proposed atom source cold enough for the interrogation time?
- Does the cloud still fit in the aperture at detection?
- Is the atom number after expansion high enough for the target shot-noise
  floor?
- Is the phase-space density high enough to justify the source complexity?
- Which atom and package size give the best trade-off?

This is directly relevant to:

- GPS-denied inertial navigation;
- portable gravimetry and underground mapping;
- compact atomic gyroscopes;
- space gravity gradiometry;
- source design for cold-atom clocks and sensors.

## What the model does not claim

The current simulator is not a complete instrument model. The source-only CAD
budget is now complemented by first-order laser, seismic and thermal envelopes,
but it still does not include:

- measured instrument PSDs;
- wavefront aberrations;
- magnetic systematics;
- cold collisions;
- full detection noise;
- Allan deviation beyond the root-Hz proxy;
- feedback and navigation filtering.

Therefore a positive score means only:

```text
the phase-space budget does not already kill the design.
```

It does not prove that the final instrument will meet its mission target.

## Scenarios implemented

The script `scripts/phase_space_sensor_cad.py` evaluates four scenarios:

1. Rb87 GPS-denied inertial accelerometer.
2. Rb87 field gravimeter.
3. Cs133 compact atomic gyroscope.
4. Sr88 source for space gravity gradiometry.

For each scenario it scans atom temperature and interrogation time, then writes:

```text
reports/data/phase_space_sensor_cad.csv
reports/data/atom_phase_space_budget.csv
reports/phase_space_sensor_cad_summary.json
reports/phase_space_sensor_cad_report.md
reports/atom_phase_space_budget_report.md
reports/sensor_noise_budget_report.md
reports/figures/phase_space_sensor_cad.png
reports/figures/atom_phase_space_budget.png
reports/figures/atom_phase_space_budget_focus.png
reports/figures/sensor_noise_budget.png
```

## Scientific interpretation

The useful industrial variable is not only `eta`. The most practical variable
is often `sigma_v`, because it determines how fast the atom cloud expands. A
long interrogation time improves ideal sensitivity as `T_i^2`, but it also lets
the cloud grow. Once the atoms leave the optical aperture, the detected number
falls and the shot-noise benefit is lost.

This creates a real design optimum:

```text
longer T_i helps sensitivity
but colder atoms and larger apertures are required to keep N_detected high.
```

The framework is therefore useful as an early-stage design filter. It can rank
candidate source packages before expensive laboratory optimization.

## Industrial product form

The most credible product is not hardware at first. It is a software tool:

```text
PhaseSpace CAD for Quantum Sensors
```

Minimum viable functions:

- atom database: Rb87, Cs133, Sr88, Yb174, He4;
- temperature-density phase-space calculator;
- ballistic cloud-expansion calculator;
- atom-interferometer shot-noise estimator;
- aperture and package-size constraint;
- scenario ranking;
- CSV/JSON export for engineering teams.

The next industrial version should add:

- laser and vibration noise budgets;
- Allan deviation curves;
- multi-axis IMU geometry;
- gravity-gradient response;
- mission-specific constraints for drone, ship, submarine, aircraft and space
  packages.

## Conclusion

The phase-space cell formulas do not provide a strong application in chemical
rocket propulsion. They do provide a strong application in quantum metrology.

The most defensible practical conclusion is:

```text
phase-space density + velocity dispersion = early design budget for cold-atom sensors
```

This is useful because it connects a compact theoretical formula to a concrete
engineering question: can a proposed quantum sensor architecture reach its
target sensitivity within its volume, temperature, density and atom-number
constraints?

The best next form is an open-source community CAD tool: transparent equations,
public benchmark scenarios, atom databases, package constraints, cycle-time
models, vibration budgets and reproducible reports that labs or companies can
extend without accepting the speculative GUP layer.
