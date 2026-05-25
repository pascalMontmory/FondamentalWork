# PRNG Diagnostic Formulas

## Status

This file records public formulas for the PRNG diagnostic framework. It does not disclose the proprietary `Montmory_CTACM` transition rule or extraction map.

The formulas below define the evaluation method: seed sensitivity, functional variance dispersion, Markov diagnostics, spectral proxies, and cross-backend reproducibility. The key convention is that `Phi` is always a declared observable applied to a finite output window, not an implicit claim about the generator as a whole.

## 1. Abstract PRNG Model

A deterministic PRNG is represented as

```text
G = (S, P, T, O)
```

where:

- `S` is the state space;
- `P` is the parameter space;
- `T_p : S -> S` is the transition map for parameters `p in P`;
- `O_p : S -> A` is the output map.

For seed `s_0` and parameter value `p`, the finite state, word, and uniform windows are:

```text
s_{t+1} = T_p(s_t)
x_t = O_p(s_t)
u_t = U(x_t)
```

```text
X_n(p,s) = (x_0, ..., x_{n-1})
U_n(p,s) = (u_0, ..., u_{n-1})
```

The exact `T_p`, `O_p`, and `U` must be specified for any reproducible generator claim.

## 2. Seed Perturbation Model

Let `Seed` be the declared seed domain. A seed perturbation rule is a map:

```text
N_delta : Seed -> P(Seed)
```

where `P(Seed)` is the power set of the seed domain. Thus `N_delta(s)` is a finite set of allowed perturbed seeds around base seed `s`.

Examples:

```text
N_bit,h(s) = { s xor e : HammingWeight(e) <= h }
N_1bit(s) = { s xor 2^j : 0 <= j < w }
N_add,k(s) = { (s + r) mod 2^w : -k <= r <= k }
```

An observable is a function on a finite window:

```text
Phi : A^n -> R^d
```

or, for Monte Carlo uniforms:

```text
Phi : [0,1)^n -> R^d
```

For example, `Phi` may be a bit-frequency statistic, a Markov transition matrix, a TestU01 score, or a Monte Carlo estimate `I_s(f)`.

The paired seed perturbation response is:

```text
Delta_Phi(s, s', p, n) = Phi(G(p, s, n)) - Phi(G(p, s', n))
```

where `s' in N_delta(s)` and `n` is the output horizon.

The absolute seed response is:

```text
D_Phi(s, delta, p, n) =
  median_{s' in N_delta(s)} |Delta_Phi(s, s', p, n)|
```

The worst-case local response is:

```text
W_Phi(s, delta, p, n) =
  max_{s' in N_delta(s)} |Delta_Phi(s, s', p, n)|
```

## 3. Monte Carlo Functional Variance

For an integrand `f : [0,1) -> R`, seed `s`, replicate `r`, and sample size `N`, the Monte Carlo estimator is:

```text
I_{s,r}(f) = (1 / N) sum_{t=1}^N f(u_{s,r,t})
```

Across `R` independent replicates for the same seed:

```text
bar I_s(f) = (1 / R) sum_{r=1}^R I_{s,r}(f)
```

```text
V_s(f) = (1 / (R - 1)) sum_{r=1}^R (I_{s,r}(f) - bar I_s(f))^2
```

The inter-seed dispersion ratio for a seed set `B` is:

```text
rho_f(B) = max_{s in B} V_s(f) / min_{s in B, V_s(f)>0} V_s(f)
```

when the denominator is nonzero.

The reported structural diagnostics use the integrands:

```text
f_1(u) = u
f_2(u) = sin(2 pi u)
f_3(u) = u^2
f_4(u) = 1{u > 0.99}
```

The rare-event functional is intentionally included because it can reveal seed-dependent tail instability that ordinary bit-frequency tests may miss.

## 4. Structural Seed Score

A public, non-proprietary structural score can be defined from normalized functional variances. Fix:

```text
F = {f_1, f_2, f_3, f_4}
```

and compute for every `s in B`:

```text
Z_s(f) = (log V_s(f) - median_{b in B} log V_b(f)) / MAD_{b in B}(log V_b(f))
```

where `MAD` is the median absolute deviation:

```text
MAD(Y) = median_i |Y_i - median_j Y_j|
```

A simple open structural score is:

```text
S_open(s) =
  w_1 |Z_s(f_1)| +
  w_2 |Z_s(f_2)| +
  w_3 |Z_s(f_3)| +
  w_4 |Z_s(f_4)|
```

with nonnegative weights `w_i`.

To remove ambiguity, the default open score uses equal weights:

```text
w_1 = w_2 = w_3 = w_4 = 1/4
```

and therefore:

```text
S_open(s) = (1/4) sum_{f in F} |Z_s(f)|
```

The proprietary production score used to discover representative seeds is not disclosed, but any external reviewer can reproduce a comparable seed-sensitivity profile from `V_s(f_i)`.

## 5. Representative Seeds

For a finite seed set `B`, representative seeds can be selected as:

```text
s_best = argmin_{s in B} S(s)
s_worst = argmax_{s in B} S(s)
s_median = argmin_{s in B} |S(s) - median_{b in B} S(b)|
```

A one-standard-deviation representative can be:

```text
s_std = argmin_{s in B} |S(s) - (mean_B S + std_B S)|
```

The default seed and seed `0`, when meaningful, are tracked separately.

## 6. Bit Frequency and Hamming Response

For `n` output words of width `w`, the empirical one-bit frequency is:

```text
F_1 = (1 / (n w)) sum_{t=1}^n popcount(x_t)
```

For paired streams from seeds `s` and `s'`, the normalized Hamming response is:

```text
H(s, s') =
  (1 / (n w)) sum_{t=1}^n popcount(x_t(s) xor x_t(s'))
```

An idealized avalanche-like response is near:

```text
H(s, s') ~= 1 / 2
```

This is evidence about sensitivity, not a cryptographic proof.

## 7. Quantized Markov Diagnostics

For a uniform sequence `u_t in [0,1)` and `q` classes:

```text
c_t = floor(q u_t)
```

with `c_t in {0, ..., q-1}`.

For lag `ell`, empirical transition counts are:

```text
N_{ij}^{(ell)} =
  # { t : c_t = i and c_{t+ell} = j }
```

The row-normalized transition matrix is:

```text
P_{ij}^{(ell)} =
  N_{ij}^{(ell)} / sum_j N_{ij}^{(ell)}
```

for rows with nonzero mass.

The empirical class frequencies are:

```text
pi_i = (1 / n) # { t : c_t = i }
```

Uniform-invariance sup deviation is:

```text
Delta_infty = max_i |pi_i - 1/q|
```

The total-variation deviation from uniform is:

```text
TV(pi, U_q) = (1 / 2) sum_{i=0}^{q-1} |pi_i - 1/q|
```

## 8. Chi-Square Uniformity

For class counts `O_i` and expected count `E = n/q`, the chi-square statistic is:

```text
chi^2 = sum_{i=0}^{q-1} (O_i - E)^2 / E
```

The corresponding p-value is:

```text
p = P(ChiSquare_{q-1} >= chi^2)
```

This test measures marginal class uniformity only. It does not measure seed stability.

## 9. Spectral-Gap Proxy

For a transition matrix `P`, let eigenvalues be ordered by modulus:

```text
1 = |lambda_1| >= |lambda_2| >= ... >= |lambda_q|
```

A spectral-gap proxy is:

```text
gamma = 1 - |lambda_2|
```

A larger `gamma` suggests faster class mixing for the quantized chain, but the result depends on `q`, lag, sample size, and the quantization map.

## 10. Periodogram and Side-Lobe Ratios

For a centered sequence:

```text
y_t = u_t - mean(u)
```

the discrete Fourier amplitude is:

```text
A_k = | sum_{t=0}^{n-1} y_t exp(-2 pi i k t / n) |
```

The peak side-lobe ratio can be reported as:

```text
PSLR = max_{k != k0} A_k / A_{k0}
```

where `k0` is the dominant peak.

An integrated side-lobe ratio can be reported as:

```text
ISLR = (sum_{k != k0} A_k^2) / A_{k0}^2
```

The exact convention for `k0`, centering, normalization, and windowing must be declared.

## 11. Cross-Backend Reproducibility

For backend set:

```text
B = {x86, Metal, CUDA}
```

bit-exact single-lane reproducibility means:

```text
forall b_1, b_2 in B, forall t < n:
  x_t^{(b_1)} = x_t^{(b_2)}
```

A practical repository check can store:

```text
Hash_b(seed, n) = SHA256(x_0 || x_1 || ... || x_{n-1})
```

and require:

```text
Hash_x86(seed, n) = Hash_Metal(seed, n) = Hash_CUDA(seed, n)
```

## 12. Audit Proof

For a canonical JSON payload `J` containing parameters, seed, effective seed, backend, generator version, output hash, and diagnostics, an audit proof can be:

```text
proof = SHA256(canonical_json(J))
```

This proves replay consistency with a declared bundle. It does not prove randomness, security, or low seed sensitivity.

## 13. Affine Reference Generator

For open diagnostics and reduced-state tests, an affine modular generator can be used as a reference model:

```text
y_{t+1} = a y_t + b mod m
u_t = y_t / m
c_t = floor(q u_t)
```

This model matches the public parameter vocabulary used in the CryptoVar-aligned diagnostic scaffold:

```text
(a, b, m, q, lag, diagnostic_n, antithetic)
```

The affine generator is a test scaffold, not the proprietary `Montmory_CTACM` definition.

## 14. Verification Boundary

The following are public formulas:

- seed perturbation response;
- functional variance dispersion;
- representative-seed selection;
- class-frequency and Markov diagnostics;
- chi-square statistic;
- spectral-gap proxy;
- periodogram side-lobe ratios;
- cross-backend stream equality;
- audit hash proof.

The following remain unpublished unless explicitly released:

- `Montmory_CTACM` transition formula;
- `Montmory_CTACM` extraction formula;
- proprietary representative-seed scoring function;
- proprietary constants or implementation-level mixing schedule.
