# PRNG Verified Results

No PRNG quality, security, period, distribution, independence, seed-impact, or parameter-robustness result is currently verified in this directory.

## Verified Definitional Statements

The only verified content currently allowed here is definitional:

- the generator tuple notation `G = (S, P, T, O)`;
- the distinction between seed model, perturbation rule, parameter control, observable, and output horizon;
- the requirement that every empirical statement declare its reproducible protocol.

## Promotion Requirements

A result can be added to this file only if it includes at least one of:

- a complete proof with explicit hypotheses;
- an exact finite enumeration with command, range, code version, and expected output;
- a reproducible empirical check clearly labelled as computational evidence, not proof.

Statements about cryptographic security require a separate threat model. Statistical evidence alone must not be promoted to a security theorem.
