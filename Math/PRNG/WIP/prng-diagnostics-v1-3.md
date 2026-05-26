# TACM / PRNG Diagnostics v1.3

> **Publication status**: superseded for publication by
> [`Math/PRNG/publication/hal/hal-05633702v1/`](../publication/hal/hal-05633702v1/).
>
> **Status**: working note retained for traceability.
>
> **Objective**: describe the v1.3 interpretation layer for calibrated
> seed-conditioned PRNG diagnostics.

The submitted consolidated manuscript is the authoritative version. This WIP
note keeps the v1.3 logic in a GitHub-readable Markdown form.

## 1. Central Message

TACM does not replace TestU01 or BigCrush. It adds a Monte Carlo
workload-facing layer that measures how seed-conditioned PRNG streams affect
replicated Monte Carlo estimators.

The v1.3 contribution is interpretive:

- raw inter-seed variance ratios are exploratory alerts;
- null-calibrated scores decide whether the alert is compatible with the null;
- ECDF and tail-rate diagnostics separate mild calibration drift from tail
  anomaly.

## 2. Seed-Conditioned Monte Carlo Estimates

For seed \(s\), replicate \(r\), sample size \(N\), and integrand \(f\), define:

$$
I_{s,r}(f)
=
\frac{1}{N}
\sum_{t=1}^{N}
f(u_{s,r,t}).
$$

The replicated mean is:

$$
\bar I_s(f)
=
\frac{1}{R}
\sum_{r=1}^{R}
I_{s,r}(f).
$$

The seed-conditioned variance is:

$$
V_s(f)
=
\frac{1}{R-1}
\sum_{r=1}^{R}
\left(
I_{s,r}(f)-\bar I_s(f)
\right)^2.
$$

Here \(V_s(f)\) is the empirical variance of replicated Monte Carlo estimates
\(I_{s,r}(f)\). It is not the within-run sample variance of the raw values
\(f(u_t)\).

## 3. Null-Calibrated Diagnostic

Under the null model, the replicated estimator is approximated by:

$$
I_{s,r}(f)
\approx
\mathcal N
\left(
\mu_f,
\frac{\sigma_f^2}{N}
\right).
$$

Therefore:

$$
T_s(f)
=
\frac{(R-1)V_s(f)}
{\sigma_f^2/N}
\sim
\chi^2_{R-1}.
$$

The calibrated diagnostic is:

$$
Z_s(f)
=
F_{\chi^2_{R-1}}
\left(
T_s(f)
\right).
$$

Under the null model:

$$
Z_s(f)\sim U[0,1].
$$

The raw ratio:

$$
\rho_f
=
\frac{\max_s V_s(f)}
{\min_{s:V_s(f)>0} V_s(f)}
$$

is therefore only an alert. The calibrated evidence is the distribution of
\(Z_s(f)\).

## 4. Tail Rate

The tail-rate diagnostic is:

$$
Q_{\mathrm{tail}}(f)
=
\frac{1}{|\mathcal B|}
\left|
\left\{
s\in\mathcal B:
Z_s(f)<0.01
\ \mathrm{or}\
Z_s(f)>0.99
\right\}
\right|.
$$

Under uniformity:

$$
\mathbb E[Q_{\mathrm{tail}}(f)]\approx 0.02.
$$

Interpretation:

- \(Q_{\mathrm{tail}}(f)\approx 0.02\): no massive population of extreme seeds;
- \(Q_{\mathrm{tail}}(f)\gg 0.02\): possible tail anomaly.

## 5. ECDF Interpretation

For each generator and integrand, plot the empirical CDF:

$$
\widehat F_Z(z)
$$

against the uniform diagonal:

$$
F(z)=z.
$$

The v1.3 interpretation is:

| ECDF shape | v1.3 verdict | Meaning |
|---|---|---|
| close to the diagonal | `compatible` | compatible with the null model |
| smooth global shift | `calibration_drift` | mild global calibration deformation, without excess extreme seeds |
| deformation at extremes | `tail_anomaly` | abnormal population of extreme seeds |

This table deliberately keeps the verdict labels outside display math so that
GitHub renders the underscores correctly.

## 6. Three-Class Verdict

### Compatible

Use `compatible` when:

$$
p_{\mathrm{KS}}\geq 0.05
$$

and:

$$
Q_{\mathrm{tail}}(f)\approx 0.02.
$$

### Calibration Drift

Use `calibration_drift` when:

$$
p_{\mathrm{KS}}<0.05
$$

but:

$$
Q_{\mathrm{tail}}(f)\approx 0.02.
$$

This means the ECDF has a detectable global deformation, but no clear excess
of extreme seeds.

### Tail Anomaly

Use `tail_anomaly` when:

$$
Q_{\mathrm{tail}}(f)\gg 0.02.
$$

This is the most important class for tail-sensitive Monte Carlo workloads.

## 7. Exact Rare-Event Calibration

For the rare-event integrand:

$$
f(u)=\mathbf 1_{\{u>0.99\}},
$$

the count per replicate is:

$$
K_{s,r}
=
\sum_{t=1}^{N}
\mathbf 1_{\{u_{s,r,t}>0.99\}}.
$$

Under the null:

$$
K_{s,r}
\sim
\mathrm{Binomial}(N,p),
\qquad
p=0.01.
$$

An exact binomial PIT score can therefore be computed as:

$$
Z^{\mathrm{bin}}_{s,r}
=
F_{\mathrm{Binomial}(N,p)}
\left(
K_{s,r}
\right).
$$

Because the binomial law is discrete, the reproducibility bundle also provides
a randomized PIT variant.

## 8. Multiple Testing

With four generators and four integrands, the baseline performs:

$$
m=16
$$

tests. A strict Bonferroni threshold is:

$$
p_{\mathrm{Bonf}}
=
\frac{0.05}{16}
=
0.003125.
$$

Therefore, an isolated \(p_{\mathrm{KS}}<0.05\) is interpreted as exploratory
unless it survives multiple-testing correction and is supported by tail-rate
evidence.

## 9. Reproducibility Bundle

The companion bundle is:

```text
Math/PRNG/WIP/prng-ztest/
```

It contains:

- public CPU-only generation scripts;
- \(Z_s\) computation;
- ECDF and histogram plotting;
- exact binomial rare-event calibration;
- summary CSV files and versioned figures.

The authoritative HAL-submitted manuscript is:

```text
Math/PRNG/publication/hal/hal-05633702v1/
```

## 10. Current Baseline Conclusion

The current CPU-only baseline does not support strong claims of
seed-pathological behaviour for the tested public PRNGs and simple diagnostic
workloads.

Several generator/integrand pairs show mild `calibration_drift`, but the
observed tail rates do not indicate a clear `tail_anomaly`.

TACM v1.3 therefore separates raw dispersion alerts from calibrated evidence:

- `compatible`: no calibrated anomaly detected;
- `calibration_drift`: mild global ECDF deformation;
- `tail_anomaly`: excess extreme seeds.
