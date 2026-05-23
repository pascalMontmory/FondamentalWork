# Large Prime-Pattern Terminal Scan -- 2026-05-23

> Status: large finite diagnostic.
>
> Limits: `N = 300000, 1000000, 3000000`.
>
> Bounds: `B = 27, 89, 127`.
>
> Terminal filter: `A = {14,23,61,89}`.

This scan follows the requested next step after the first `N=100000`
diagnostic. It reports:

- distance curves `D_B(pattern, prime non-pattern control)`;
- terminal filter masses `nu_{B,P_H,N}(A)`;
- sample sizes for `twin`, `cousin`, and `sexy` starts.

Generated files:

- `prime_pattern_terminal_curves.csv`
- `distance_to_non_pattern_control.svg`
- `terminal_filter_mass.svg`

## Commands

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile Math/MathClass/scripts/generate_prime_pattern_curves.py
```

```bash
PYTHONDONTWRITEBYTECODE=1 python3 Math/MathClass/scripts/generate_prime_pattern_curves.py --limits 300000,1000000,3000000 --bounds 27,89,127 --terminal-set 14,23,61,89
```

## Distance To Prime Non-Pattern Control

The control is:

- `twin` vs `prime_non_twin`;
- `cousin` vs `prime_non_cousin`;
- `sexy` vs `prime_non_sexy`.

### Twin

| B | N=300000 | N=1000000 | N=3000000 |
|---|---:|---:|---:|
| 27 | 0.018210 | 0.008255 | 0.007623 |
| 89 | 0.035677 | 0.020304 | 0.011198 |
| 127 | 0.048005 | 0.024763 | 0.013497 |

### Cousin

| B | N=300000 | N=1000000 | N=3000000 |
|---|---:|---:|---:|
| 27 | 0.020378 | 0.013784 | 0.008000 |
| 89 | 0.041290 | 0.023271 | 0.014849 |
| 127 | 0.048311 | 0.028772 | 0.017028 |

### Sexy

| B | N=300000 | N=1000000 | N=3000000 |
|---|---:|---:|---:|
| 27 | 0.012129 | 0.007212 | 0.003711 |
| 89 | 0.029951 | 0.016682 | 0.011323 |
| 127 | 0.035715 | 0.018669 | 0.013353 |

## Terminal Filter Mass `A={14,23,61,89}`

### Twin

| B | N=300000 | N=1000000 | N=3000000 |
|---|---:|---:|---:|
| 27 | 0.610554 | 0.619048 | 0.617093 |
| 89 | 0.224783 | 0.226466 | 0.235142 |
| 127 | 0.018704 | 0.016893 | 0.018632 |

### Cousin

| B | N=300000 | N=1000000 | N=3000000 |
|---|---:|---:|---:|
| 27 | 0.633950 | 0.625491 | 0.623499 |
| 89 | 0.235966 | 0.238335 | 0.236819 |
| 127 | 0.016134 | 0.017559 | 0.018102 |

### Sexy

| B | N=300000 | N=1000000 | N=3000000 |
|---|---:|---:|---:|
| 27 | 0.623188 | 0.625778 | 0.623932 |
| 89 | 0.241046 | 0.235323 | 0.237710 |
| 127 | 0.019157 | 0.019285 | 0.019274 |

## Sample Sizes At `N=3000000`

| Pattern | Sample size |
|---|---:|
| twin | 20932 |
| cousin | 20826 |
| sexy | 41559 |

## Verdict

```math
\boxed{
\text{Les identites finies MathClass sont validees.}
}
```

```math
\boxed{
\text{Les distances motif vs controle non-motif diminuent avec }N.
}
```

```math
\boxed{
\text{Aucun biais terminal specifique aux jumeaux n'est valide jusqu'a }3\cdot10^6.
}
```

```math
\boxed{
\text{Le filtre }A=\{14,23,61,89\}\text{ n'isole pas les jumeaux.}
}
```

Interpretation:

- The decreasing distances support terminal neutrality or convergence toward a
  shared motif law, rather than a stable twin-specific resonance.
- The filter mass is close across `twin`, `cousin`, and `sexy`.
- At this stage, `A={14,23,61,89}` is best interpreted as a common terminal
  motif filter, or as a general structural effect, not as a twin-specific
  Montmory filter.

## Next Diagnostic Step

The next useful scan is not a new claim. It is a robustness check:

```text
N = 10000000
```

with the same curves and with additional controls modulo `30030` if runtime
allows.
