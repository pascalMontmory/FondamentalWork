# TACM / PRNG Diagnostics v1.3

> **Status**: publishable revision draft.
>
> **Objective**: provide a compact, robust and interpretable v1.3 centered on calibrated interpretation of \(Z_s\) diagnostics.
>
> **Central message**:
>
> $$
> \boxed{
> \text{TACM does not replace TestU01; it adds a Monte Carlo workload-facing layer}
> }
> $$
>
> $$
> \boxed{
> \text{that quantifies and classifies seed sensitivity in a calibrated and interpretable way.}
> }
> $$

---

## 0. Positioning of Versions

### v1.0 — Initial framework

Version 1.0 introduced:

- seed sensitivity;
- functional variance;
- inter-seed ratios;
- GSQI;
- transition instability \(\epsilon(T)\);
- BigCrush / cross-backend evidence;
- limitations and non-claims.

### v1.1 — Formula development

Version 1.1 developed the formulae around the empirical measure:

$$
\mu_{s,b,N}
=
\frac1N
\sum_{t=1}^{N}
\delta_{u_{s,b,t}}.
$$

It clarified \(\chi^2\), projected \(\lambda\)-gap, \(N_{\rm eff}\), audit scores, VaR/CVaR approximations, backend reproducibility and multi-lane diagnostics.

### v1.2 — Null calibration

Version 1.2 introduced:

$$
T_s(f)
=
\frac{(R-1)V_s(f)}
{\sigma_f^2/N},
$$

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

It corrected the interpretation of raw ratios:

$$
\boxed{
\rho_f\text{ high} \Rightarrow \text{raw alert, not proof of anomaly.}
}
$$

### v1.3 — Robust interpretation

Version 1.3 focuses on interpreting \(Z_s\) and distinguishing:

$$
\boxed{\text{normal null-compatible noise}}
$$

$$
\boxed{\text{mild calibration drift}}
$$

$$
\boxed{\text{tail anomaly}}
$$

$$
\boxed{\text{detectable injected defect}}
$$

---

## 1. Diagnostic Reminder

For a seed \(s\), replicate \(r\), sample size \(N\), and integrand \(f\):

$$
I_{s,r}(f)
=
\frac1N
\sum_{t=1}^{N}
f(u_{s,r,t}).
$$

The replicated mean is:

$$
\bar I_s(f)
=
\frac1R
\sum_{r=1}^{R}
I_{s,r}(f).
$$

The seed-conditioned variance is:

$$
V_s(f)
=
\frac1{R-1}
\sum_{r=1}^{R}
\left(
I_{s,r}(f)-\bar I_s(f)
\right)^2.
$$

Here \(V_s(f)\) is the variance of replicated Monte Carlo estimates \(I_{s,r}(f)\), not the within-run variance of raw values \(f(u_t)\).

Under the null:

$$
I_{s,r}(f)
\approx
\mathcal N
\left(
\mu_f,\frac{\sigma_f^2}{N}
\right),
$$

so:

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
\boxed{
Z_s(f)
=
F_{\chi^2_{R-1}}
\left(
T_s(f)
\right).
}
$$

Under the null:

$$
\boxed{
Z_s(f)\sim U[0,1].
}
$$

Interpretation:

$$
\boxed{
\rho_f\text{ is an alert; }Z_s\text{ is the calibration.}
}
$$

---

## 2. Interpreting \(Z_s\)

### 2.1 KS test

For each generator and integrand, test:

$$
\{Z_s(f):s\in\mathcal B\}
$$

against:

$$
U[0,1].
$$

Report:

$$
p_{\rm KS}.
$$

With many seeds, for example \(S=1000\), KS can detect small smooth deformations. Therefore:

$$
\boxed{
p_{\rm KS}<0.05\text{ is not automatically a PRNG failure.}
}
$$

### 2.2 Tail rate

Define:

$$
Q_{\rm tail}(f)
=
\frac1{|\mathcal B|}
\#\{s:Z_s(f)<0.01\ \text{or}\ Z_s(f)>0.99\}.
$$

Under uniformity:

$$
\mathbb E[Q_{\rm tail}(f)]\approx0.02.
$$

Interpretation:

$$
Q_{\rm tail}\approx0.02
\Rightarrow
\text{no massive population of extreme seeds.}
$$

$$
Q_{\rm tail}\gg0.02
\Rightarrow
\text{possible tail anomaly.}
$$

### 2.3 ECDF

Plot:

$$
\widehat F_Z(z)
$$

against:

$$
F(z)=z.
$$

Reading:

$$
\boxed{
\text{ECDF close to diagonal}\Rightarrow \texttt{compatible}.
}
$$

$$
\boxed{
\text{smooth global shift}\Rightarrow \texttt{calibration\_drift}.
}
$$

$$
\boxed{
\text{deformation at extremes}\Rightarrow \texttt{tail\_anomaly}.
}
$$

---

## 3. Three-Class Verdict

Version 1.3 replaces:

```text
compatible / suspicious
```

with:

```text
compatible
calibration_drift
tail_anomaly
```

### Compatible

Criteria:

$$
p_{\rm KS}\geq0.05
$$

and:

$$
Q_{\rm tail}\approx0.02.
$$

Interpretation:

$$
\boxed{
\text{the }Z_s\text{ values are compatible with }U[0,1].
}
$$

### Calibration drift

Criteria:

$$
p_{\rm KS}<0.05
$$

but:

$$
Q_{\rm tail}\approx0.02.
$$

Interpretation:

$$
\boxed{
\text{small global calibration deformation without excess extreme seeds.}
}
$$

### Tail anomaly

Criterion:

$$
Q_{\rm tail}\gg0.02.
$$

Interpretation:

$$
\boxed{
\text{abnormal population of extreme seeds.}
}
$$

This is the most important class for tail-sensitive Monte Carlo workloads.

---

## 4. Exact Rare-Event Calibration

For:

$$
f(u)=\mathbf 1_{\{u>0.99\}},
$$

the rare-event count is:

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

Define:

$$
\boxed{
Z^{\rm bin}_{s,r}
=
F_{\mathrm{Binomial}(N,p)}
\left(
K_{s,r}
\right).
}
$$

Because the binomial law is discrete, a randomized PIT can be used:

$$
Z^{\rm bin,rand}_{s,r}
=
F_{\mathrm{Binomial}(N,p)}(K_{s,r}-1)
+
U_{s,r}\,\mathbb P(K=K_{s,r}).
$$

This protects the rare-event diagnostic from relying only on the Gaussian / \(\chi^2\) approximation.

| generator | \(p_{\rm KS}^{\chi^2}\) | \(p_{\rm KS}^{\rm binomial}\) | \(Q_{\rm tail}\) | verdict |
|---|---:|---:|---:|---|
| MT19937 | TBD | TBD | TBD | TBD |
| PCG64 | TBD | TBD | TBD | TBD |
| Philox | TBD | TBD | TBD | TBD |
| SFC64 | TBD | TBD | TBD | TBD |

---

## 5. Experimental Validation

### 5.1 Public PRNG baseline

Recommended configuration:

$$
S=1000,
\qquad
N=50\,000,
\qquad
R=8.
$$

Generators:

- MT19937;
- PCG64;
- Philox;
- SFC64.

Integrands:

$$
u,
\qquad
\sin(2\pi u),
\qquad
u^2,
\qquad
\mathbf 1_{\{u>0.99\}}.
$$

Report:

- \(p_{\rm KS}\);
- \(Q_{\rm tail}\);
- \(\rho_{95/5}\);
- three-class verdict.

### 5.2 Power test — marginal bias

Controlled perturbation:

$$
u'_t=(u_t+\varepsilon)\bmod1,
$$

or:

$$
u'_t=\min(1,u_t+\varepsilon).
$$

Expected diagnostics:

- \(\chi^2\);
- ECDF \(Z_s\);
- \(Q_{\rm tail}\) if the effect touches a tail;
- drift \(\Delta_U\), if available.

### 5.3 Power test — temporal correlation

Controlled perturbation:

$$
u'_t=(1-\alpha)u_t+\alpha u_{t-1}\pmod1.
$$

Expected diagnostics:

- projected \(\lambda\)-gap;
- \(\epsilon(T)\);
- \(\chi^2_{2D}\);
- ECDF \(Z_s\), if the workload is affected.

### 5.4 Power test — rare-event deletion

If:

$$
u_t>0.99,
$$

replace with probability \(\alpha\) by:

$$
u'_t=0.98.
$$

Expected diagnostic:

$$
\boxed{
Z^{\rm bin}\text{ should detect the anomaly.}
}
$$

---

## 6. Multiple Testing

With several generators and integrands, several tests are performed. A single:

$$
p<0.05
$$

is not enough to conclude.

For \(m\) tests, Bonferroni gives:

$$
p_{\rm Bonf}=\frac{0.05}{m}.
$$

For example:

$$
m=16
\Rightarrow
p_{\rm Bonf}=0.003125.
$$

Therefore:

$$
\boxed{
p_{\rm KS}<0.05\text{ is exploratory if multiple-testing correction does not confirm it.}
}
$$

---

## 7. Synthesis Tables

### Table A — Calibration summary

| generator | integrand | \(S\) | \(N\) | \(R\) | \(p_{\rm KS}\) | \(Q_{\rm tail}\) | verdict |
|---|---|---:|---:|---:|---:|---:|---|
| MT19937 | identity | 1000 | 50000 | 8 | TBD | TBD | TBD |
| MT19937 | sin | 1000 | 50000 | 8 | TBD | TBD | TBD |
| MT19937 | quadratic | 1000 | 50000 | 8 | TBD | TBD | TBD |
| MT19937 | rare_099 | 1000 | 50000 | 8 | TBD | TBD | TBD |
| PCG64 | identity | 1000 | 50000 | 8 | TBD | TBD | TBD |
| Philox | rare_099 | 1000 | 50000 | 8 | TBD | TBD | TBD |
| SFC64 | rare_099 | 1000 | 50000 | 8 | TBD | TBD | TBD |

### Table B — ECDF interpretation

| ECDF shape | interpretation |
|---|---|
| close to diagonal | `compatible` |
| smooth global drift | `calibration_drift` |
| deformation at extremes | `tail_anomaly` |

### Table C — Power tests

| defect | intensity | expected diagnostic | detected? |
|---|---:|---|---|
| marginal bias | \(\varepsilon\) | \(\chi^2\), ECDF | yes/no |
| temporal correlation | \(\alpha\) | \(\lambda\)-gap, \(\chi^2_{2D}\) | yes/no |
| rare-event deletion | \(\alpha\) | binomial \(Z\) | yes/no |

---

## 8. Minimal v1.3 Bundle

Scripts to add under:

```text
Math/PRNG/WIP/prng-ztest/scripts/
```

Core:

```text
plot_z_ecdf.py
compute_binomial_rare_event_z.py
inject_prng_defects.py
```

Useful:

```text
adjust_pvalues.py
scan_snr_grid.py
```

Optional:

```text
bootstrap_z_scores.py
```

Minimal versioned artifacts:

```text
results/z_summary.csv
figures/ecdf_Zs_identity.svg
figures/ecdf_Zs_sin.svg
figures/ecdf_Zs_quadratic.svg
figures/ecdf_Zs_rare_099.svg
figures/hist_Zs_identity.svg
figures/hist_Zs_sin.svg
figures/hist_Zs_quadratic.svg
figures/hist_Zs_rare_099.svg
```

Generated locally, not necessarily versioned:

```text
data/public_prng_estimates.csv
results/z_scores_table.csv
```

---

## 9. Limitations

Version 1.3 remains cautious:

- \(Z_s\) depends on the chosen null model;
- the \(\chi^2\) calibration assumes approximately Gaussian Monte Carlo estimates;
- rare-event indicators may require exact binomial or bootstrap calibration;
- a non-rejected test does not prove absence of defect;
- public PRNG baselines are not exhaustive;
- simple workloads do not cover all industrial payoffs;
- injected power tests cover only controlled defect families.

---

## 10. Conclusion

Expected conclusion:

$$
\boxed{
\text{the tested public PRNGs do not show strong seed pathologies in these simple workloads.}
}
$$

But:

$$
\boxed{
\text{TACM detects, classifies and interprets raw alerts, calibration drift and tail anomalies.}
}
$$

Final message:

> TACM does not replace TestU01. It adds a Monte Carlo workload-facing layer that quantifies and classifies seed sensitivity in a statistically calibrated and interpretable way.
