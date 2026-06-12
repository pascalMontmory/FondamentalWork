# Capacity Dichotomy After High-Label Reduction

This note combines the high-label one-shot theorem with the high-label
least-root gate.

It gives a precise branch decomposition for any remaining counterexample.

## 1. Notation

Let
\[
  A=3m,\qquad T_m=\lfloor\sqrt{6m}\rfloor,
\]
and
\[
  Q^\ast_m=
  \left\lfloor\frac{\sqrt{6m}-2}{3}\right\rfloor.
\]

Let
\[
  B_m=6Q^\ast_m+4,
  \qquad
  C_m=2T_m.
\]

The interval of complete blocks lies in
\[
  0\le q\le Q^\ast_m.
\]

## 2. Three label zones

Every certificate prime \(p\le A\) lies in one of three zones:

1. **low labels**
   \[
     p\le B_m;
   \]
2. **middle labels**
   \[
     B_m<p\le C_m;
   \]
3. **least-root high labels**
   \[
     C_m<p\le A.
   \]

The middle zone has bounded width:
\[
  0\le C_m-B_m\le4.
\]
Indeed \(B_m=6\lfloor(\sqrt{6m}-2)/3\rfloor+4\) and
\(C_m=2\lfloor\sqrt{6m}\rfloor\).  Writing
\[
  \lfloor\sqrt{6m}\rfloor=3a+\rho,\qquad \rho\in\{0,1,2\},
\]
one gets
\[
  C_m-B_m=
  \begin{cases}
  2,&\rho=0,\\
  4,&\rho=1,\\
  0,&\rho=2.
  \end{cases}
\]

Thus middle labels are a finite endpoint correction, not an asymptotic
source of repeated coverage.

## 3. Exact dichotomy for a failed block

If a coprime complete block fails, it has an ordered certificate pair
\[
  (p_0,p_1).
\]

Either:

- both labels are low:
  \[
    p_0,p_1\le B_m;
  \]
- at least one label is middle:
  \[
    B_m<p_i\le C_m;
  \]
- or at least one label is high:
  \[
    p_i>C_m.
  \]

In the high case, that label is forced by the least-root gate:
\[
  t=\|Ai_p\|_p
  \]
in A0, or
\[
  t=\|s_p\|_p,\qquad s_p^2\equiv-A^2-1\pmod p
  \]
in A1.

In the low case, all repeated ordered-pair behavior is confined to the box
\[
  p_0,p_1\le B_m=O(\sqrt m).
\]

## 4. Counterexample decomposition

Let
\[
  \mathcal Q_{\rm cop}(m)
\]
be the coprime complete block set.  A counterexample gives a partition
\[
  \mathcal Q_{\rm cop}(m)
  =
  \mathcal Q_{\rm low}
  \cup
  \mathcal Q_{\rm mid}
  \cup
  \mathcal Q_{\rm high},
\]
where:

- \(\mathcal Q_{\rm low}\) is covered by ordered pairs in the low box
  \(p_0,p_1\le B_m\);
- \(\mathcal Q_{\rm mid}\) uses at least one of the finitely many endpoint
  labels \(B_m<p\le C_m\);
- \(\mathcal Q_{\rm high}\) is covered through least-root images of primes
  \(p>C_m\).

This is exact.  There is no heuristic density assumption.

## 5. New closure target

The original cover problem has now become the following three-part
non-cover problem:

1. low box: rule out full coverage by the finite low-label cofactor system;
2. middle endpoint: handle the bounded correction \(B_m<p\le C_m\);
3. high least-root: prove that least-root images cannot supply all remaining
   blocks in both layers.

This is a significant reduction because the high labels are no longer
arbitrary one-shot certificates.  They are encoded by least square roots,
while all repetition is confined to \(O(\sqrt m)\)-sized label boxes.
