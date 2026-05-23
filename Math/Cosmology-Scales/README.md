# Cosmology Scales

This directory contains reusable mathematical identities involving Planck,
Hubble, and cosmological scales.

The material here is not a claim that a physical model is established. A formula
may be listed here when it is an algebraic consequence of explicitly stated
assumptions and can be checked independently of the surrounding COSMO narrative.

## Contents

- `dark-energy-gup-scale.md`: conditional derivation of
  `beta_0^(Lambda)` from the identity `rho_vac = rho_Lambda`.
- `scripts/test_beta0_lambda_identity.py`: numerical check that the closed form
  for `beta_0^(Lambda)` equals the direct density inversion.

## Status Rule

Formulas in this directory should state:

- assumptions;
- dimensional status;
- derivation;
- numerical check if constants are involved;
- what the formula does not prove physically.

