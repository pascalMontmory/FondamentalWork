# PRNG Conjectures and Open Questions

This file records unverified research directions. Nothing here is a verified result.

## Micro-Uncertainty Conjectures

### Seed Perturbation Amplification

For a useful generator and a suitable output observable, small structured seed perturbations should rapidly become difficult to distinguish from independent seed draws.

Required future work:

- define the generator family;
- define the perturbation operator;
- choose observables with known failure modes;
- compare against exact enumeration where the state space is small enough;
- report negative cases rather than only passing tests.

### Parameter-Control Stability

There may be parameter regions where seed-impact observables remain stable across a control grid.

This is not yet a theorem. A candidate stability region must be tied to a finite grid, horizon, seed model, observable list, and acceptance rule.

### Structured-Seed Risk

Structured seeds may create detectable bias even when uniform seeds look acceptable under the same generator.

This should be tested separately from ordinary randomness batteries because timestamp-like, counter-like, hash-prefix, and domain-encoded seeds can stress different parts of the transition rule.

## Open Questions

- Which seed perturbation operators best model the intended micro-uncertainty work: bit flips, additive offsets, hash-domain changes, timestamp jitter, or application-specific encoding changes?
- Which parameter families are intended to be controlled?
- Is the goal statistical adequacy, cryptographic unpredictability, reproducible simulation, or protocol fairness?
- Which claims can be exactly enumerated on reduced state spaces?
- Which empirical checks should be treated as regression tests rather than evidence of randomness?

## Non-Claims

- Passing a randomness battery does not prove security.
- Seed sensitivity alone does not prove unpredictability.
- Parameter robustness for one observable does not imply robustness for another.
- A result observed in an external API is not part of this repository until its inputs, command, code version, and expected output are documented here.
