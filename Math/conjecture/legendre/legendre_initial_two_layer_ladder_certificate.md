# Initial Two-Layer Ladder Certificate

This note combines the A0 and A1 spacing envelopes into one global
label-order certificate.

The key extra point is that, in the clean strong gate, every one of the
eight initial prime labels is odd.  Thus all eight center-distances lie in
one parity class, even before using the stronger A0 congruence modulo \(4\).

## 1. Global distance ladder

Let the eight prime labels be sorted increasingly:
\[
  P_1<P_2<\cdots<P_8,
\]
and write
\[
  P_j=A-D_j.
\]

Then
\[
  D_1>D_2>\cdots>D_8.
\]

All labels \(P_j\) are odd primes, so
\[
  D_j\equiv A-1\pmod2
  \qquad(1\le j\le8).
\]

Therefore the global distances satisfy the parity ladder
\[
\boxed{
  D_i\ge D_j+2(j-i)
  \qquad(1\le i<j\le8).
}
\]

Combining this with the global order-statistic barrier
\[
  D_j\ge B_{9-j}(A)
\]
already gives
\[
\boxed{
  D_i\ge
  \max_{i\le j\le8}
  \left(B_{9-j}(A)+2(j-i)\right).
}
\]

This is the global parity envelope.  The A0 layer adds a sharper local edge.

## 2. Layer word

Let
\[
  L=(L_1,\dots,L_8)\in\{0,1\}^8
\]
record the layer of the label \(P_j\), with
\[
  L_j=0 \quad\text{for A0},\qquad L_j=1 \quad\text{for A1}.
\]

Every clean strong-gate certificate has exactly four A0 labels and four A1
labels, so \(L\) has four zeros and four ones.

Let
\[
  a_1<a_2<a_3<a_4
\]
be the A0 positions in the label order.  Since A0 labels satisfy
\[
  P_{a_u}\equiv1\pmod4,
\]
their center-distances satisfy
\[
  D_{a_u}\equiv A-1\pmod4.
\]

Hence consecutive A0 distances in label order obey
\[
\boxed{
  D_{a_u}\ge D_{a_{u+1}}+4
  \qquad(1\le u<4).
}
\]

The A1 consecutive spacing is only \(2\), and is already included in the
global parity ladder.

## 3. Word-dependent lower envelope

Attach a directed weighted graph to \(L\) on vertices \(1,\dots,8\):

- for every \(1\le i<8\), add the global parity edge
  \[
    i\to i+1
  \]
  with weight \(2\);
- for consecutive A0 positions \(a_u<a_{u+1}\), add the A0 edge
  \[
    a_u\to a_{u+1}
  \]
  with weight \(4\).

Let \(W_L(i,j)\) be the maximum path weight from \(i\) to \(j\), with
\[
  W_L(i,i)=0.
\]

Then every clean strong-gate certificate with layer word \(L\) satisfies
\[
\boxed{
  D_i\ge D_j+W_L(i,j)
  \qquad(i\le j).
}
\]

Using \(D_j\ge B_{9-j}(A)\), define
\[
\boxed{
  H_i^L(A):=
  \max_{i\le j\le8}
  \left(B_{9-j}(A)+W_L(i,j)\right).
}
\]

Thus the label-order distances must satisfy the word-dependent ladder
\[
\boxed{
  D_i\ge H_i^L(A)
  \qquad(1\le i\le8).
}
\]

This refines the separate A0 and A1 envelopes because it remembers the
actual interleaving of the two layers in the global prime-label order.

## 4. Offset-to-label matching

The offset order is fixed by the parity of \(m\).

For even \(m\):
\[
\begin{array}{c|cccccccc}
  i      & 1&2&3&4&5&6&7&8\\
  \hline
  c_i    & 1&5&17&25&49&65&101&121\\
  \ell_i & 0&1&1&0&0&1&1&0
\end{array}
\]

For odd \(m\):
\[
\begin{array}{c|cccccccc}
  i      & 1&2&3&4&5&6&7&8\\
  \hline
  c_i    & 2&4&16&26&50&64&100&122\\
  \ell_i & 1&0&0&1&1&0&0&1
\end{array}
\]

A certificate must choose a bijection
\[
  \pi:\{1,\dots,8\}\to\{1,\dots,8\}
\]
from offset positions to label positions such that
\[
\boxed{
  L_{\pi(i)}=\ell_i
  \qquad(1\le i\le8).
}
\]

The center-distance attached to offset \(c_i\) is then
\[
  r_i=D_{\pi(i)}.
\]

Since label position \(\pi(i)\) has the \(\pi(i)\)-th smallest prime label,
its distance rank among increasing distances is
\[
\boxed{
  s_i=9-\pi(i).
}
\]

## 5. Quotient-rank compatibility

For \(m\ge4881\), the eight quotient parameters are distinct.  Let
\[
  q_i=\operatorname{rank}(e_i)
\]
be the quotient rank attached to offset \(c_i\).  Then \(q\) is a permutation
of \(\{1,\dots,8\}\), and the order constraint gives
\[
\boxed{
  \operatorname{Inv}(q)\subseteq\operatorname{Inv}(s).
}
\]

Equivalently, for each offset position \(i\),
\[
\boxed{
  \max(1,q_i-i+1)
  \le
  s_i
  \le
  \min(8,8+q_i-i).
}
\]

The quotient-rank barrier also gives
\[
\boxed{
  r_i=D_{\pi(i)}\ge B_{q_i}(A).
}
\]

Thus every offset must satisfy the combined lower bound
\[
\boxed{
  D_{\pi(i)}
  \ge
  \max\{H_{\pi(i)}^L(A),\,B_{q_i}(A)\}.
}
\]

## 6. Divisibility and pair compatibility

The centered divisor equation for each offset is
\[
\boxed{
  A-D_{\pi(i)}\mid D_{\pi(i)}^2+c_i.
}
\]

Equivalently, with
\[
  e_i=\frac{D_{\pi(i)}^2+c_i}{A-D_{\pi(i)}},
\]
one has
\[
  A
  =
  D_{\pi(i)}
  +
  \frac{D_{\pi(i)}^2+c_i}{e_i}.
\]

For every pair \(i\ne j\), the shared center forces
\[
\boxed{
  e_j(D_{\pi(i)}^2+c_i)
  -
  e_i(D_{\pi(j)}^2+c_j)
  =
  e_ie_j(D_{\pi(j)}-D_{\pi(i)}).
}
\]

These are not optional congruences.  They are exact compatibility equations
for all eight offsets sharing the same center \(A=3m\).

## 7. Clean strong-gate certificate

For \(m\ge4881\), a clean strong-gate counterexample must therefore produce:

1. a parity choice for \(m\);
2. a layer word \(L\) with four A0 and four A1 positions;
3. a layer-respecting matching \(\pi\);
4. a quotient-rank permutation \(q\);
5. distances \(D_1>\cdots>D_8\) in one parity class;
6. quotients \(e_1,\dots,e_8\);
7. all divisibility and pair-compatibility equations above.

The next exact closure target is now finite and structural:

> eliminate every two-layer ladder certificate, rather than search over
> \(m\).

This is stronger than the separate A0 and A1 envelopes.  It turns the clean
strong gate into a finite family of layer-word and matching skeletons, each
of which must still satisfy rigid quotient equations.
