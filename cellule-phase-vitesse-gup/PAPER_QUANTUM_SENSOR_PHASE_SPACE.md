# Phase-space engineering for cold-atom quantum sensors

## Abstract

This paper develops a practical engineering interpretation of the
position--velocity phase-space formulation

```text
dN = m^3 d3x d3v / [h^3(1 + beta m^2 v^2)^3].
```

The GUP deformation itself is not presented as an industrial technology. The
useful part is the phase-space language. In the non-deformed limit it gives the
standard thermal de Broglie and phase-space-density criteria used to describe
cold atomic sources:

```text
lambda_th = h / sqrt(2 pi m k_B T)
eta = n lambda_th^3
sigma_v = sqrt(k_B T / m)
```

The strongest industrial application is not rocket propulsion or ordinary
cryogenic engineering. It is the design and evaluation of cold-atom sources for
quantum inertial sensors: gravimeters, gyroscopes, accelerometers and gravity
gradiometers. The same language is also relevant to high-brightness electron,
ion, atomic and molecular beams.

## 1. What is new and what is not

The following are not new:

- the phase-space cell `h^3`;
- the thermal de Broglie wavelength;
- the degeneracy parameter `eta = n lambda_th^3`;
- atom interferometry;
- industrial quantum sensors.

The useful contribution here is narrower:

- translating the existing position--velocity GUP formalism into an engineering
  phase-space diagnostic;
- showing quantitatively why chemical rocket gases are irrelevant for this
  idea;
- identifying cold-atom inertial sensors as the strongest industrial target;
- providing reproducible scripts for design-level estimates.

## 2. Phase-space source quality

For a massive non-relativistic particle, the non-deformed phase-space count is:

```text
dN = m^3 d3x d3v / h^3.
```

For a source of atoms with spatial volume `Vx` and velocity-space volume `Vv`,
the dimensionless phase-space occupation scales like:

```text
f_6D ~ N h^3 / (m^3 Vx Vv).
```

For a thermal cloud this reduces to the familiar degeneracy parameter:

```text
eta = n lambda_th^3.
```

This is exactly the quantity that matters when producing a cold atomic ensemble:
high enough density, low enough velocity spread, and enough coherence for
interferometry.

## 3. Cold-atom interferometer design equations

An atom interferometer measures acceleration through a phase:

```text
Delta phi = k_eff a T_i^2
```

where:

- `k_eff` is the effective optical wave vector;
- `a` is acceleration;
- `T_i` is the interferometer interrogation time.

The shot-noise acceleration floor scales as:

```text
delta a ~ 1 / (k_eff T_i^2 sqrt(N_detected)).
```

The problem is that atoms expand during interrogation. If the initial cloud
radius is `R0`, then:

```text
sigma_v = sqrt(k_B T / m)
R(T_i) = sqrt(R0^2 + sigma_v^2 T_i^2).
```

So reducing temperature improves the instrument twice:

1. it reduces cloud expansion;
2. it permits longer interrogation time;
3. it preserves detected atom number;
4. it increases matter-wave phase-space quality.

## 4. Numerical example: Rb87 source

For rubidium-87 at density `n=1e18 m^-3`, the source quality changes rapidly
with temperature.

| T [K] | eta | sigma_v [m/s] | radius after 1 s |
|---:|---:|---:|---:|
| 1e-8 | 6.57 | 9.78e-4 | 1.4 mm |
| 1e-7 | 0.208 | 3.09e-3 | 3.25 mm |
| 1e-6 | 0.00657 | 9.78e-3 | 9.83 mm |
| 1e-5 | 2.08e-4 | 3.09e-2 | 3.1 cm |

This is a concrete engineering result. If the chamber or laser aperture is of
order centimeters, a `10 microkelvin` cloud expands too much for a long
interrogation. A `10 nanokelvin` to `100 nanokelvin` source is much more
compatible with compact, high-sensitivity instruments.

## 5. Market relevance

There is a real market for quantum sensors, but it is a deep-tech B2B market,
not a consumer market. Public market estimates put the global quantum sensor
market in the hundreds of millions of dollars, with projections above one
billion dollars around 2030. The most relevant segments are:

- GPS-denied navigation;
- inertial measurement;
- gravity mapping;
- underground/subsurface detection;
- defense and aerospace;
- geophysics and resource exploration;
- timing and atomic clocks.

The value of the present work is not to replace sensor physics. It is to provide
a transparent front-end design layer:

```text
temperature -> velocity spread -> cloud expansion -> atom survival -> sensitivity
```

The extended CAD note adds an explicit atom-number cap:

```text
N_phase_cap = eta_max V_eff / lambda_th^3
N_detected = min(N_technical survival, N_phase_cap)
FOM = sqrt(N_detected) T_i^2
FOM_Hz = sqrt(N_detected / T_cycle) T_i^2
delta a ~= 1 / (k_eff FOM)
```

This turns the phase-space argument into a concrete screening tool: a proposed
sensor source must have enough atoms, enough usable volume, low enough velocity
spread and a realistic cooling pathway at the same time.

This FOM is deliberately incomplete. It is useful for first-order screening but
does not include contrast loss, laser phase noise, vibration rejection, wavefront
aberrations, detection noise, duty cycle or Allan deviation. Once the total
cycle time is known, the useful per-root-Hz proxy is
`FOM_Hz = sqrt(N_detected / T_cycle) T_i^2`, so dead time and slow preparation
directly reduce the apparent source advantage.

## 6. Product concept

A realistic product is not a new physical device by itself. It is a design and
simulation tool:

```text
PhaseSpace Designer for Quantum Sensors
```

Inputs:

- atom: Rb87, Cs133, Sr88, Yb174, Li6, Li7;
- density;
- temperature;
- initial cloud radius;
- aperture or chamber radius;
- interrogation time;
- effective wave vector;
- initial atom number.

Outputs:

- `lambda_th`;
- `eta`;
- `sigma_v`;
- cloud expansion;
- detected atom fraction proxy;
- shot-noise acceleration floor;
- phase-space atom-number cap;
- recoil temperature;
- GUP correction estimate `beta0 (m sigma_v / p_Pl)^2`;
- design warnings.

Industrial users:

- quantum sensor startups;
- aerospace and defense labs;
- navigation companies;
- geophysics and underground mapping groups;
- academic labs commercializing cold-atom instruments.

## 7. Limits

This paper does not claim that GUP corrections are measurable in these systems.
With `beta0=1`, the GUP thermal parameter is absurdly small in ordinary
laboratory conditions:

```text
theta_T = beta m k_B T << 1.
```

For the deformed phase-space measure,

```text
dN_GUP = dN_0 / (1 + beta m^2 v^2)^3,
epsilon_GUP = beta p^2 = beta0 (m v / p_Pl)^2.
```

For Rb87 at `T = 1 microkelvin`,

```text
sigma_v = 9.78e-3 m/s
epsilon_GUP(beta0=1)    = 4.68e-56
epsilon_GUP(beta0=1e26) = 4.68e-30
```

Thus `(1 + epsilon_GUP)^-3 ~= 1` to overwhelming accuracy. The GUP term is a
theoretical motivation for the position-velocity notation, not the industrial
effect exploited by the CAD framework.

The useful industrial layer is the non-GUP phase-space formulation. The GUP
terms remain a speculative theoretical extension.

The current simulations are also not complete instrument models. They omit:

- laser phase noise;
- vibration noise;
- wavefront aberrations;
- atom-atom interactions;
- magnetic systematics;
- detection noise;
- full geometry of the vacuum chamber and optics.

They are meant as first-pass design filters.

## 8. Conclusion

The strongest industrial use of the position--velocity phase-space formulation
is not propulsion. It is quantum-source engineering.

The practical statement is:

```text
Use phase-space formulas to choose temperature, density, cloud size and
interrogation time for cold-atom inertial sensors.
```

This is scientifically standard but industrially meaningful. The novelty is in
the clean integration with the existing GUP position--velocity framework and in
the reproducible design pipeline.

The natural deployment path is open source: transparent assumptions, benchmark
scenarios, atom databases, cycle-time models, package constraints and vibration
budgets that can be inspected, challenged and extended by the quantum-sensor
community.
