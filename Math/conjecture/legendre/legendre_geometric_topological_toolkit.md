# Geometric and Topological Toolkit for Legendre

This note records geometric and topological approaches that could genuinely
change the Legendre attack.

The rule is the same as elsewhere: a geometric analogy is useless unless it
becomes an exact object such as a variety, a projection, a nerve complex, a
homology obstruction, a tropical cone, or a descent map.

## 1. Incidence varieties

The centered certificate equations are
\[
  (A-r_c)e_c=r_c^2+c.
\]

For a finite offset set \(\mathcal C\), define the incidence variety
\[
  V_{\mathcal C}
  \subset
  \mathbb A^{1+2|\mathcal C|}
\]
with coordinates
\[
  A,\quad (r_c,e_c)_{c\in\mathcal C},
\]
cut out by
\[
  (A-r_c)e_c-r_c^2-c=0
  \qquad(c\in\mathcal C),
\]
together with:

- pair compatibility equations;
- label-distinctness saturations;
- quotient-rank case equations or inequalities converted to cases;
- color equations over residue fields;
- ramification gates split off separately.

The key projection is
\[
  \pi:V_{\mathcal C}\to\mathbb A^1_A.
\]

Closure target:

> Show that the projection image contains no admissible integer \(A\) in a
> given residue fiber.

For shared-\(5\),
\[
  \mathcal C=\{5,17,25,49,65\}.
\]

This is the cleanest geometric formulation currently available.

## 2. Elimination and exceptional fibers

The practical algebraic-geometric attack is:

1. choose a rank permutation \(\pi\);
2. choose a ramification pattern
   \[
     \rho\subseteq\{7\mid A,\ 13\mid A,\ 17\mid A\};
   \]
3. build the saturated ideal
   \[
     I_{\pi,\rho};
   \]
4. eliminate all variables except \(A\):
   \[
     I_{\pi,\rho}\cap\mathbb Z[A].
   \]

If the eliminant contains a polynomial \(F(A)\), then admissible centers
must satisfy
\[
  F(A)=0.
\]

If in addition the residue conditions imply
\[
  F(A)\not\equiv0
\]
over a suitable modulus, that branch is killed.

This is the geometric version of the modular certificate idea.

## 3. Curves and genus

Pairwise compatibility equations often reduce a two-offset subsystem to a
curve.  For two offsets \(c,d\), one has
\[
  e_c e_d(r_c-r_d)
  +e_d(r_c^2+c)
  -e_c(r_d^2+d)
  =
  0.
\]

After fixing quotient ranks or small quotient values, the subsystem can
become:

- a conic;
- a Pell-type curve;
- an elliptic curve;
- a higher-genus curve.

This already happened once in the project: a residual \(m\equiv3\pmod4\)
endpoint reduced to a rank-\(3\) elliptic curve and was killed by a
\(3\)-adic Mordell-Weil coset argument.

Closure target:

> Force the shared-\(5\) compressed certificate into finitely many curves,
> then close their integral points by local obstruction, Mordell-Weil
> descent, or genus \(>1\) finiteness plus explicit elimination.

This is not hypothetical; it is the same kind of mechanism that already
closed one branch.

## 4. Tropical geometry

The quotient-rank inequalities are already tropical in spirit.

Write the centered equation as
\[
  r_c^2+e_cr_c+c=e_cA.
\]

For large \(A\), the leading balances are between
\[
  r_c^2,\quad e_cr_c,\quad e_cA.
\]

Different quotient ranks define different tropical cones.  A rank
permutation \(\pi\) is possible only if its cone contains integer points
compatible with:

- offset order;
- color classes;
- pair equations;
- label distinctness.

Closure target:

> Tropicalize the shared-\(5\) incidence variety and prove that every
> admissible cone either has no integer lift or lies in a ramified gate.

This may explain why rank barriers alone do not close the problem: the
contradiction must occur after lifting from the tropical cone back to exact
arithmetic.

## 5. Nerve complexes of covers

A full composite certificate is a cover of the required offset/block set by
prime-label events.

For a fixed \(A\), define sets
\[
  S_p=\{c\in\mathcal C:p\mid A^2+c\}.
\]

A full cover is
\[
  \mathcal C\subseteq\bigcup_p S_p.
\]

The nerve complex \(\mathcal N_A\) has a vertex for each label \(p\), and a
simplex for each compatible family of labels with nonempty joint coverage.

Topological idea:

> Show that the nerve required by a full cover has impossible homology or
> impossible dimension after the compatibility constraints are imposed.

For the shared-\(5\) fiber, the variable labels are already pairwise
distinct.  The nerve is therefore very sparse, which makes a topological
non-cover certificate plausible.

Practical form:

> Build the finite compatibility complex for \(\mathcal C=\{5,17,25,49,65\}\)
> modulo a chosen product of small primes, then prove it is collapsible below
> the dimension needed to support a full certificate.

This is an exact finite combinatorial topology problem, not a heuristic.

## 6. Discrete Morse compression

If a compatibility complex exists, discrete Morse theory can sometimes
collapse it while preserving homotopy type.

Legendre translation:

- cells are partial certificates;
- a matching removes certificates that contain a locally replaceable label;
- critical cells are irreducible obstruction certificates.

Closure target:

> Construct an acyclic matching on the certificate complex such that no full
> certificate cell is critical.

This would be a topological version of descent: every bad certificate is
paired with a simpler one until none remain.

## 7. Arithmetic topology

Arithmetic topology treats primes as analogues of knots and residue
conditions as linking data.

For Legendre, the only immediately useful translation is through
compatibility graphs:

- a label \(p\) links offsets \(c,d\) if it can divide both;
- label-distinctness says most links are forbidden;
- ramified gates are special knots tied to \(A\).

This language is less directly actionable than incidence geometry, but it
suggests looking for linking obstructions in the graph of repeated labels.

Verdict:

> Keep as intuition only unless it becomes an explicit graph homology or
> linking-number invariant.

## 8. Recommended geometric pivot

The most concrete geometric route is:

> Shared-\(5\) incidence elimination.

Build, for each rank permutation and ramification pattern, the ideal
\[
  I_{\pi,\rho}
  =
  \left\langle
    (A-r_c)e_c-r_c^2-c,\ 
    \text{pair equations},\
    \text{rank cases},\
    \text{color cases}
  \right\rangle
\]
for
\[
  c\in\{5,17,25,49,65\}.
\]

Then eliminate:
\[
  I_{\pi,\rho}\cap\mathbb Z[A].
\]

If elimination is too large over \(\mathbb Z\), do it modulo primes and seek
a Nullstellensatz certificate:
\[
  1\in I_{\pi,\rho}\otimes\mathbb F_\ell.
\]

This is the geometric/topological counterpart of the Hamiltonian/SOS route:
both try to prove that the compressed certificate variety is empty.

## 9. What not to do

Do not introduce geometry as vocabulary only.

Acceptable next outputs:

- an explicit shared-\(5\) incidence ideal;
- a modular Groebner/Nullstellensatz certificate for one rank permutation;
- a nerve complex with a proven homology obstruction;
- a discrete Morse matching that contracts all full certificates;
- a descent map extracted from a geometric projection.

Anything else is likely another version of the already explored fiber
enumeration.
