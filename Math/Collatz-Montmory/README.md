# Collatz-Montmory

This directory is the verified-facing entry point for the Collatz-Montmory work.

Only material that is definitional, proven, or explicitly presented as a conditional verified-formulas note should remain visible at this level. Drafts, conjectures, diagnostics, protocols, and scripts are kept under `work/` until they are promoted.

## Visible Files

| File | Status |
| --- | --- |
| `definitions.md` | Definitions and required conventions. |
| `verified-lemmas.md` | Proven elementary statements only. |
| `conditional-normalization.md` | Conditional Hardy-Littlewood normalization note: validated normalization and conditional implications only; no validation of `C_Montmory` itself. |

## Work Area

Exploratory material is kept in `work/`:

- conjectures;
- computational protocols;
- diagnostics;
- candidate filters;
- scripts;
- salvage notes and research drafts.

Material in `work/` is not advertised as verified.

## Promotion Rule

A statement can move from `work/` to the visible root only if it has one of the following:

- a complete written proof with explicit hypotheses;
- a bounded reproducible computational verification with command, range, code version, and expected output;
- a clearly labelled conditional theorem whose assumptions are stated and whose proof is algebraic or already included.

Nothing is promoted because it is plausible, elegant, numerically suggestive, or useful for a protocol.