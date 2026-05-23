# PRNG

This directory is the starting point for the mathematical work around your PRNG
pseudo-random number generator.

The goal is to separate the mathematical structure of the generator from any
specific implementation repository. This makes the PRNG easier to review,
compare, test and reuse.

## Status

`PRNG` is currently a mathematical and algorithmic workstream. It should not yet
be described as cryptographically secure unless a formal threat model, security
claims and statistical test results are written here.

Use this directory to define:

```text
state space
transition function
output function
seed/key material
period assumptions
mixing or diffusion properties
statistical tests
security claims and non-claims
implementation links
```

## Proposed documents

| File | Purpose |
|---|---|
| `definitions.md` | State, transition, output and seeding definitions |
| `notation.md` | Symbols, bit/word conventions, endian rules and parameters |
| `period.md` | Period claims, assumptions and proof sketches |
| `diffusion.md` | Avalanche, mixing and bias analysis |
| `statistical-tests.md` | TestU01, PractRand, Dieharder or custom test summaries |
| `security-model.md` | Threat model, intended use and explicit non-claims |
| `links-to-repos.md` | Repositories or products that use the PRNG |
| `open-questions.md` | Unresolved mathematical or security questions |

## Review discipline

Every PRNG claim should be classified explicitly:

| Claim type | Required evidence |
|---|---|
| statistical quality | reproducible test output and seed set |
| period | proof, algebraic argument or bounded empirical claim |
| unpredictability | threat model and attack analysis |
| cryptographic security | formal security argument and external review |
| implementation correctness | reference vectors and cross-language tests |

## First task

Create `definitions.md` with the canonical generator interface:

```text
seed -> state_0
state_n -> state_{n+1}
state_n -> output_n
```

Then add at least one reference vector:

```text
seed = ...
first outputs = ...
```

This lets other repositories test that they are using exactly the same PRNG.

## Relationship to VDF and COSMO

If the PRNG uses VDF-like delay, iteration, verifiable computation or algebraic
state evolution, document the mathematical link in both:

- `Math/PRNG/links-to-repos.md`
- `Math/VDF/links-to-repos.md`

If the PRNG is used in simulations under `COSMO/`, document that as an
implementation dependency, not as a cosmological claim.
