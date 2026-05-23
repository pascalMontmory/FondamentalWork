# Terminal Signature Tests -- 2026-05-23

> Status: reproducible diagnostic report.
>
> Scope: MathClass terminal signatures for Collatz terminal entry.
>
> This report validates finite identities and records experimental convergence
> diagnostics. It does not prove Collatz, Hardy-Littlewood, or terminal limits
> for prime patterns.

## Commands

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile Math/MathClass/scripts/*.py
```

```bash
PYTHONDONTWRITEBYTECODE=1 python3 Math/MathClass/scripts/check_mathclass_identities.py --limit 10000 --bounds 27,89,127
```

```bash
PYTHONDONTWRITEBYTECODE=1 python3 Math/MathClass/scripts/scan_terminal_signature_convergence.py --limits 10000,30000,100000 --bounds 27,89,127
```

```bash
PYTHONDONTWRITEBYTECODE=1 python3 Math/MathClass/scripts/scan_prime_pattern_terminal_signatures.py --limits 10000,30000,100000 --bounds 27,89,127 --terminal-set 14,23,61,89
```

## Exact Finite Identities

All exact finite tests returned `ok`.

Validated families and classes:

- `all = odd + even`;
- `odd = mod1_4 + mod3_4`;
- `prime = twin + prime_non_twin`;
- terminal fibers for `all`;
- pseudometric symmetry and triangle inequality for `odd`, `odd_prime`, `admissible_210`;
- projection for `all`, `odd`, `even`, `mod1_4`, `mod3_4`, `admissible_210`, `prime`, `odd_prime`, `twin`, `cousin`, `sexy`, `prime_non_twin`;
- TV contraction under projection for pairs among `odd`, `prime`, `twin`, `cousin`, `sexy`, `admissible_210`.

Largest observed errors were floating-point roundoff, around `1e-17` to `1e-16`.

Sample exact-test excerpts:

```text
mixture,odd=mod1_4+mod3_4,27,0,ok
pure_terminal,all_fibers,89:89,0,ok
projection,twin,127->89,6.9388939039072284e-18,ok
tv_contraction,sexy|admissible_210,127->89,0,ok
```

Conclusion:

```math
\boxed{
\text{The finite MathClass identities are implemented correctly.}
}
```

## Experimental Convergence Scan

Limits:

```text
N = 10000, 30000, 100000
```

Bounds:

```text
B = 27, 89, 127
```

### Stable or Improving Signals

For `odd`, stability improved clearly:

```text
odd, B=27: 0.0187333333 -> 0.0046466667
odd, B=89: 0.0226000000 -> 0.0098133333
odd, B=127: 0.0254666667 -> 0.0131533333
```

For `prime`, stability also improved:

```text
prime, B=27: 0.0271499873 -> 0.0145449598
prime, B=89: 0.0363167469 -> 0.0214988479
prime, B=127: 0.0450830658 -> 0.0276222417
```

Distances `prime` vs `admissible_210` at `N=100000`:

```text
B=27: 0.0060567309
B=89: 0.0139293992
B=127: 0.0188571980
```

These are smaller than `prime` vs `odd`, suggesting that a visible part of the
prime signal is explained by local modular constraints.

### Prime Patterns

At `N=100000`, distances to `admissible_210` were:

```text
twin,  B=27: 0.0224359552
twin,  B=89: 0.0483929495
twin,  B=127: 0.0757148880

cousin, B=27: 0.0294466684
cousin, B=89: 0.0658660367
cousin, B=127: 0.0694891062

sexy,   B=27: 0.0185407294
sexy,   B=89: 0.0416821388
sexy,   B=127: 0.0526988582
```

These are diagnostic only. They do not yet establish stable asymptotic bias.

Stability for `twin` did not improve at this range:

```text
twin, B=27: 0.0260092965 -> 0.0395148423
twin, B=89: 0.0622969656 -> 0.0703104225
twin, B=127: 0.0823836632 -> 0.0853137115
```

Interpretation: the twin-prime sample is still too small at `N=100000` for a
stable terminal law verdict.

## Terminal Filter Mass Diagnostic

Terminal set:

```text
A = {14,23,61,89}
```

At `N=100000`:

```text
twin:
  B=27:  0.6102941176
  B=89:  0.2385620915
  B=127: 0.0179738562

cousin:
  B=27:  0.6324013158
  B=89:  0.2236842105
  B=127: 0.0180921053

sexy:
  B=27:  0.6301593788
  B=89:  0.2415202289
  B=127: 0.0179812015
```

Interpretation:

- The masses are similar across `twin`, `cousin`, and `sexy`.
- This does not currently isolate a twin-specific Montmory signal.
- The chosen set `A` should be treated as a diagnostic filter, not a validated
  arithmetic resonance.

## Verdict Table

| Test | Verdict |
|---|---|
| Union decomposition | OK |
| Pure terminal classes | OK |
| Pseudometric symmetry/triangle | OK |
| Projection between bounds | OK |
| TV contraction | OK |
| Convergence for `odd` | compatible, improving |
| Convergence for `prime` | compatible, improving |
| Convergence for `twin` | inconclusive at `N=100000` |
| Convergence for `cousin` | mixed but improving at larger bounds |
| Convergence for `sexy` | mixed |
| Prime vs modulo controls | much of signal appears modular |
| Twin/cousin/sexy vs controls | diagnostic, not stable enough |
| Terminal filter `A={14,23,61,89}` | no twin-specific signal isolated |

## Conclusion

The exact finite MathClass framework works.

The experimental scans show that:

1. basic classes such as `odd`, `admissible_210`, and `prime` show improving
   stability as `N` grows;
2. prime patterns remain sample-limited at `N=100000`;
3. no robust twin-specific terminal resonance is validated by these tests;
4. controls modulo `30`, `210`, and `2310` are essential before interpreting
   any prime-pattern signal.

The next useful run is a larger scan:

```text
N = 300000, 1000000, 3000000
```

especially for `twin`, `cousin`, and `sexy`.
