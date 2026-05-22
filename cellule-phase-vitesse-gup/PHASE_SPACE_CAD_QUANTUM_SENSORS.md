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

The current simulator is not a complete instrument model. It does not include:

- laser phase noise;
- wavefront aberrations;
- vibration rejection;
- magnetic systematics;
- cold collisions;
- dead time and Allan deviation;
- full detection noise;
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
reports/phase_space_sensor_cad_summary.json
reports/phase_space_sensor_cad_report.md
reports/figures/phase_space_sensor_cad.png
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
