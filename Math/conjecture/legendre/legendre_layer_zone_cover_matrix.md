# Layer-Zone Cover Matrix

This note refines the capacity dichotomy by separating the A0 and A1 layers.

The previous three-zone decomposition assigned a block to low, middle, or
high depending on whether at least one label was in that zone.  For a proof,
one needs the full \(3\times3\) layer matrix.

## 1. Label zones

Keep
\[
  A=3m,\qquad T_m=\lfloor\sqrt{6m}\rfloor,
\]
\[
  B_m=6Q^\ast_m+4,\qquad C_m=2T_m.
\]

For each layer \(i\in\{0,1\}\), split labels into:
\[
  L_i:\ p_i\le B_m,
\]
\[
  M_i:\ B_m<p_i\le C_m,
\]
\[
  H_i:\ C_m<p_i\le A.
\]

Every failed coprime block belongs to one of the nine cells
\[
  (L_0,L_1),\ (L_0,M_1),\ (L_0,H_1),
\]
\[
  (M_0,L_1),\ (M_0,M_1),\ (M_0,H_1),
\]
\[
  (H_0,L_1),\ (H_0,M_1),\ (H_0,H_1).
\]

## 2. Structural meaning of each cell

The cells have different proof status:

- \((L_0,L_1)\): entirely inside the low-label cofactor box.  This is the
  only cell with possible repeated ordered pairs.
- Any cell involving \(M_i\): endpoint correction, because
  \[
    0\le C_m-B_m\le4.
  \]
- \((H_0,H_1)\): high-high adjacency.  This is controlled by the shift
  intersections of least-root images.
- \((H_0,L_1)\) and \((L_0,H_1)\): mixed cells.  One coordinate is a
  least-root image, while the other is covered by the low cofactor box.
- \((H_0,M_1)\) and \((M_0,H_1)\): high least-root plus finite endpoint
  correction.

Thus only two infinite mechanisms remain:

1. low cofactor coverage;
2. high least-root images.

The middle labels are finite endpoint corrections.

## 3. Exact matrix cover condition

A counterexample to the A-channel gives a cover
\[
  \mathcal Q_{\rm cop}(m)
  =
  \bigcup_{X,Y\in\{L,M,H\}}\mathcal Q_{XY}(m),
\]
where \(\mathcal Q_{XY}\) is the set of blocks for which A0 uses a label in
zone \(X\) and A1 uses a label in zone \(Y\).

The matrix is exact.  The cells can be attacked independently:

- prove \(\mathcal Q_{LL}\) is not large enough using centered cofactor
  descent inside the low box;
- absorb all \(M\)-cells by a finite endpoint argument;
- prove that \(H\)-cells are sparse or non-covering using least-root image
  correlations.

## 4. Why this matters

The raw Mobius identity has no clean sign.  The layer-zone matrix preserves
which part of the obstruction is responsible for each failed block.

In particular, a future proof does not need to prove that high least-root
events are rare in isolation.  It only needs to prove that their images
cannot exactly complement the low-box cofactor cover across all complete
coprime blocks.

This is the precise finite/infinite split now available.
