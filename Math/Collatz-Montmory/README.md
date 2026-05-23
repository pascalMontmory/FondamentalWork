# Collatz-Montmory

This directory is the verified-facing entry point for the Collatz-Montmory work.

Only material that is definitional, proven, or explicitly presented as a conditional verified-formulas note should remain visible at this level. Drafts, conjectures, diagnostics, protocols, and scripts are kept under `work/` until they are promoted.

## Current Verified Position

The following is mathematically verified at this level:

- the accelerated Collatz map is well-defined on positive integers;
- stopping-time and terminal-entry objects can be defined whenever the relevant stopping times exist;
- changing a bound `B_2` to a smaller bound `B_1` adds an exact terminal correction;
- the terminal correction law is a push-forward of the entrance measure;
- the exact effect on `K_B(n)=log_2(n)/tau_B(n)` follows algebraically.

The following is not verified at this level:

- global Collatz convergence;
- existence of limiting entrance laws `nu_B`;
- existence of a limiting law for the normalized score `Z_B`;
- stability of a class of bounds containing `89`;
- decorrelation with `p+2` prime;
- the value `C_Montmory = 0.107983974916`.

## Visible Files

| File | Status |
| --- | --- |
| `definitions.md` | Exact definitions currently allowed in verified-facing notes. |
| `verified-lemmas.md` | Proven elementary statements and bound-correction identities. |
| `bound-correction-identities.md` | Reader-facing summary of the verified identities and explicit non-verified claims. |
| `conditional-normalization.md` | Conditional Hardy-Littlewood normalization note: validated normalization and conditional implications only; no validation of `C_Montmory` itself. |

## Work Area

Exploratory material is kept in `work/`:

- conjectures;
- computational protocols;
- diagnostics;
- candidate filters;
- scripts;
- salvage notes and research drafts;
- conditional asymptotic programs that are not yet proven.

Material in `work/` is not advertised as verified.

## Promotion Rule

A statement can move from `work/` to the visible root only if it has one of the following:

- a complete written proof with explicit hypotheses;
- a bounded reproducible computational verification with command, range, code version, and expected output;
- a clearly labelled conditional theorem whose assumptions are stated and whose proof is algebraic or already included.

Nothing is promoted because it is plausible, elegant, numerically suggestive, or useful for a protocol.