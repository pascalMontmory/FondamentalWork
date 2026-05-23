# Resonance Hypotheses Status

> Status: non-validated analysis.
>
> This file records the current hypothesis state after testing passage-window laws. It should not be cited as a verified mathematical result.

## 1. Definitions under test

For a center `B` and multiplicative width `eta`, define

\[
I_{B,\eta}=\{m\in\mathbb N:e^{-\eta}B\le m\le e^{\eta}B\}.
\]

For a trajectory starting at `n`, define first passage into the window:

\[
\tau_{B,\eta}(n)=\inf\{t\ge0:T^t(n)\in I_{B,\eta}\}.
\]

The first passage value, centered passage time, and residence count are

\[
P_{B,\eta}(n)=T^{\tau_{B,\eta}(n)}(n),
\]

\[
U_{B,\eta}(n)=\tau_{B,\eta}(n)-\frac{\log_2 n-\log_2 B}{d},
\qquad
 d=1-\frac{\log_2 3}{2},
\]

\[
R_{B,\eta}(n)=\#\{t:T^t(n)\in I_{B,\eta}\}.
\]

The full law being tested is

\[
\mathcal R_{B,\eta}^P
=\operatorname{Law}_P(P_{B,\eta},U_{B,\eta},R_{B,\eta}).
\]

## 2. Hypotheses

### H0: no arithmetic resonance

For a control population `C`,

\[
\mathcal R_{B,\eta}^{\rm twin}-\mathcal R_{B,\eta}^{C}\to 0
\]

in the finite diagnostic distances below, and

\[
\Omega_{B,\eta}^{\rm twin/C}(x)=
\frac{H_{B,\eta}^{\rm twin}(x)}{H_{B,\eta}^{C}(x)}\to1.
\]

Interpretation: the center may be a common Collatz passage zone, but it is not arithmetically special for twin primes.

### H1: weak resonance center

A center `B` is a weak resonance center for population `P` if

\[
\mathcal R_{B,\eta}^P
\]

stabilizes as `x` grows. This is a Collatz-dynamical statement only. It does not imply an arithmetic effect.

### H2: arithmetic resonance center

A center `B` is an arithmetic resonance center for twin primes if both hold:

\[
\mathcal R_{B,\eta}^{\rm twin}
\]

stabilizes, and for at least one control `C`,

\[
\liminf_x D_{B,\eta}^{\rm twin/C}(x)>0
\]

with stable sign/magnitude in the hit-rate ratio.

Here the diagnostic distance is

\[
D_{B,\eta}^{\rm twin/C}(x)=
\operatorname{TV}(P_{B,\eta}^{\rm twin},P_{B,\eta}^{C})
+
\operatorname{KS}(U_{B,\eta}^{\rm twin},U_{B,\eta}^{C})
+
\operatorname{KS}(R_{B,\eta}^{\rm twin},R_{B,\eta}^{C}).
\]

## 3. Full-law diagnostic

Script:

```bash
python3 Math/Collatz-Montmory/work/scripts/evaluate_resonance_law_distance.py --limit 3000000 --eta 0.08
python3 Math/Collatz-Montmory/work/scripts/evaluate_resonance_law_distance.py --limit 10000000 --centers 41,85,89,127,255 --eta 0.08
```

The first command tests all centers used in the passage-rate diagnostic. The second command extends selected centers to `10^7`.

## 4. Result at 3e6

At `x=3*10^6`, `eta=0.08`, the full-law distances for `B=89` are:

| center | control | twin hit | control hit | TV(P) | KS(U) | KS(R) | D |
|---:|---|---:|---:|---:|---:|---:|---:|
| 89 | prime-non-twin | 0.634626409 | 0.636915914 | 0.007336095 | 0.012287238 | 0.004495196 | 0.024118530 |
| 89 | odd-sample | 0.634626409 | 0.636240000 | 0.007267147 | 0.011622937 | 0.005783470 | 0.024673554 |

These distances are small and do not show strong separation.

## 5. Result at 1e7 for selected centers

At `x=10^7`, `eta=0.08`:

| center | control | twin hit | control hit | TV(P) | KS(U) | KS(R) | D |
|---:|---|---:|---:|---:|---:|---:|---:|
| 41 | prime-non-twin | 0.787012547 | 0.784279340 | 0.002260050 | 0.004266267 | 0.001693607 | 0.008219925 |
| 41 | odd-sample | 0.787012547 | 0.784080000 | 0.002866569 | 0.003560550 | 0.001493940 | 0.007921059 |
| 85 | prime-non-twin | 0.674143778 | 0.672277650 | 0.005068185 | 0.003097463 | 0.003610816 | 0.011776464 |
| 85 | odd-sample | 0.674143778 | 0.671824000 | 0.006999457 | 0.006324472 | 0.004224265 | 0.017548194 |
| 89 | prime-non-twin | 0.639081044 | 0.636783807 | 0.004433077 | 0.003249336 | 0.002763868 | 0.010446281 |
| 89 | odd-sample | 0.639081044 | 0.636328000 | 0.006323355 | 0.005724556 | 0.003466792 | 0.015514704 |
| 127 | prime-non-twin | 0.755832486 | 0.756927863 | 0.006749220 | 0.005382816 | 0.001637709 | 0.013769745 |
| 127 | odd-sample | 0.755832486 | 0.754988000 | 0.007553065 | 0.006774995 | 0.002490342 | 0.016818402 |
| 255 | prime-non-twin | 0.776619193 | 0.777491009 | 0.008726651 | 0.007335419 | 0.001910719 | 0.017972789 |
| 255 | odd-sample | 0.776619193 | 0.776104000 | 0.009398033 | 0.006770685 | 0.002599706 | 0.018768424 |

For `B=89`, the distance to prime non-twin controls drops from about `0.0241` at `3e6` to about `0.0104` at `1e7`.

## 6. Updated hypothesis status

### Rejected provisionally: H2 for `B=89` under this window test

Current finite data do **not** support a twin-prime-specific arithmetic resonance centered at `89` for `eta=0.08`.

The hit rates are close to controls, and the full-law distance decreases when the range is extended to `10^7`.

### Still open: H1 for `B=89`

`B=89` may still define a stable Collatz passage law

\[
\mathcal R_{89,0.08}^{P}
\]

for broad populations. That would be a Collatz-dynamical phenomenon, not a twin-prime arithmetic resonance.

### Still open: Lambda_B terminal-bound framework

This result does not invalidate the separate terminal-bound Lambda_B framework based on

\[
(E_B(n),\tau_B(n)-\log_2(n)/d).
\]

It only says that the different interpretation of `B` as an oscillation/passage center around `89` has no visible twin-prime-specific signal in the tested range.

## 7. Current working conclusion

The project should separate three notions:

1. **terminal bound**: enter `<=B`;
2. **passage center**: enter a window around `B`;
3. **arithmetic resonance**: passage law differs for an arithmetic population such as twin primes.

The data currently support only cautious work on (1) and maybe (2). They do not support claiming (3) for `B=89`.
