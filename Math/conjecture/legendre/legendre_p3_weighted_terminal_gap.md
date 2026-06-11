# P3 Weighted Terminal Gap

This note corrects the first terminal-descent target.

The factor geometry of a composite \(P_3\) survivor is exact, but by itself
it does not eliminate the near-diagonal channels.  The next valid route must
use either the weighted structure of the \(P_3\) theorem or the existing
prime-free certificate language.

## 1. Why terminal geometry alone is too weak

The previous terminal equation was
\[
  N=(n-a)(n+a+k),
  \qquad
  1\le nk-a(a+k)\le2n.
\]

For \(k=1\), this gives
\[
  N=n^2+n-a(a+1).
\]

Taking
\[
  a=0
\]
produces the always-admissible terminal value
\[
\boxed{
  N=n(n+1)\in(n^2,(n+1)^2).
}
\]

Thus the channel T1 is not geometrically contradictory.  If \(n(n+1)\) has
at most three prime factors, it is a legitimate composite \(P_3\) in the
Legendre interval.  This observation does not assert that it is the
Campbell survivor; it shows that terminal factor geometry alone cannot prove
the near-diagonal terminal lemma.

More generally:

- T1 contains near-diagonal products around \(n(n+1)\);
- T2 contains near-upper-endpoint products around \(n(n+2)\);
- neither channel forces a smaller prime-free interval by formal geometry
  alone.

So the statement

> no \(P_3\) survivor can lie in T1 or T2

is too strong unless it is tied to an additional mechanism.

## 2. Corrected closure principle

Campbell's theorem is not merely the assertion that a mysterious \(P_3\)
exists.  It is proved by a weighted sieve.  To convert it into a prime
theorem, the prime-free assumption must be inserted into the same weighted
framework.

The corrected principle is:

> If \(I_n\) is prime-free, then every positive contribution in the
> between-squares \(P_3\) lower bound must come from terminal composites.
> Therefore the \(P_3\) lower bound must be dominated by the total weighted
> contribution of T1, T2, and Tfar terminal composites.

Thus a proof of Legendre can be obtained from a strict weighted inequality:
\[
\boxed{
  W_{\mathrm{T1}}(n)+W_{\mathrm{T2}}(n)+W_{\mathrm{Tfar}}(n)
  <
  W_{P_3}(n),
}
\]
where \(W_{P_3}(n)\) is the explicit lower-bound weight from the
between-squares \(P_3\) theorem, and \(W_{\mathrm{T*}}(n)\) are the same
weights restricted to terminal composite channels.

This is not a simulation target.  It is an analytic inequality target.

## 3. Terminal channels as weighted sums

For a prime-free interval, the terminal composite set is
\[
  \mathcal T(n)
  =
  \left\{
    (a,k):
    k\ge1,
    1\le nk-a(a+k)\le2n,
    \Omega(n-a)+\Omega(n+a+k)\le3
  \right\}.
\]

The three channel sums are:
\[
  W_{\mathrm{T1}}(n)
  =
  \sum_{\substack{a\ge0\\0\le a(a+1)\le n-1\\
  \Omega(n-a)+\Omega(n+a+1)\le3}}
  \omega_n\bigl((n-a)(n+a+1)\bigr),
\]
\[
  W_{\mathrm{T2}}(n)
  =
  \sum_{\substack{a\ge0\\0\le a(a+2)\le2n-1\\
  \Omega(n-a)+\Omega(n+a+2)\le3}}
  \omega_n\bigl((n-a)(n+a+2)\bigr),
\]
and
\[
  W_{\mathrm{Tfar}}(n)
  =
  \sum_{\substack{k\ge3,\ a\ge0\\
  n(k-2)\le a(a+k)\le nk-1\\
  \Omega(n-a)+\Omega(n+a+k)\le3}}
  \omega_n\bigl((n-a)(n+a+k)\bigr).
\]

Here \(\omega_n\) denotes the exact sieve weight used in the \(P_3\)
existence proof.  The immediate task is not to guess \(\omega_n\), but to
extract it from the paper and rewrite these three sums in its notation.

## 4. Where the certificate language enters

The weighted terminal inequality alone still faces the parity barrier.
The advantage of our previous work is that a prime-free \(I_n\) is not an
arbitrary interval with only composite values.  It carries explicit
small-prime certificates for many structured candidates:
\[
  n^2+t^2+\epsilon.
\]

Therefore the terminal sums above should be further split by certificate
type:
\[
  W_{\mathrm{T*}}(n)
  =
  W_{\mathrm{T*}}^{\mathrm{cert}}(n)
  +
  W_{\mathrm{T*}}^{\mathrm{uncert}}(n).
\]

The desired exact plan is:

1. show that terminal composites counted by the \(P_3\) weight must either
   lie in one of the existing quotient-certificate skeletons or in a small
   exceptional family;
2. eliminate the skeleton part by the Pell-synchronized quotient equations;
3. bound the exceptional family strictly below the \(P_3\) lower bound.

This is the first formulation that genuinely combines the analytic
almost-prime theorem with the algebraic certificate route.

## 5. New exact next task

The next concrete task is no longer the false geometry-only T1/T2 lemma.
It is:

> Extract Campbell's \(P_3\) weight and rewrite its lower bound as a sum over
> terminal factor pairs \((a,k)\).  Then determine whether the T1 and T2
> near-diagonal channels can saturate the lower bound without producing an
> actual prime.

If T1 and T2 can saturate the weight, the \(P_3\)-upgrade route is blocked.
If they cannot, the remaining Tfar channel has a genuine factor-drop
structure and becomes a plausible descent target.

This is the correct proof-first continuation: not more computation, but an
exact translation of a modern \(P_3\) theorem into the terminal-factor
language.
