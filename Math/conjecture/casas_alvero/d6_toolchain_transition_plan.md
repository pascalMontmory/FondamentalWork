# Endpoint \(d-6\) Toolchain Transition Plan

The SymPy scripts have reached their useful limit.  They are good for
deriving formulas, finite-field diagnostics, and small gcd tests, but the
remaining endpoint-\(d-6\) task is a saturated elimination problem.  That
should be moved to a system with native Groebner bases, saturation, and
modular reconstruction.

## Current Algebraic Target

For each remaining endpoint-\(d-6\) type, keep the equation-level system
\[
  F_m=0,\qquad R_3=R_4=R_5=R_6=0,
\]
where
\[
  R_k=\prod_{X\in\{0,a,Y,z\}}H_k(X).
\]
After reducing modulo \(F_m\), form the compact eliminants
\[
  E_3,\quad E_{34},\quad E_{35},\quad E_{36}
\]
in \(\mathbb Z[n,a]\).  The exact object to project is
\[
  I=
  \langle E_3,E_{34},E_{35},E_{36}\rangle:
  \langle a(n+1)(n+2)(n+3)(n+4)(n+5)(n+6)\rangle^\infty.
\]
The desired certificate is
\[
  I\cap\mathbb Z[n].
\]

## Why SymPy Should Stop Here

The remaining operations are not just large polynomial gcds.  They require:

- exact saturation by a product of factors;
- elimination order control;
- modular computations with rational reconstruction;
- factor-aware treatment of leading coefficient and denominator losses;
- repeatable certificates that can be checked independently.

SymPy can prototype these operations but is not strong enough for the final
elimination workload.

## Sage/Singular Route

Use Sage as the orchestration layer and Singular as the elimination engine.

Recommended first implementation:

1. Generate \(F_m,R_3,R_4,R_5,R_6\) from the existing Python formulas, but
   export them as exact integer polynomials.
2. Build a Singular ring with variables ordered for elimination, for example
   \[
     (Y,a,n,s)
   \]
   with a block order eliminating \(Y,a,s\) before \(n\).
3. Encode saturation by adding an auxiliary variable:
   \[
     1-s\,a(n+1)(n+2)(n+3)(n+4)(n+5)(n+6)=0.
   \]
4. Compute the elimination ideal and extract the univariate part in \(n\).
5. Factor the result over \(\mathbb Z\), then test integer roots \(n\ge1\).

This route gives the closest match to the current mathematical formulation.

## Magma Route

Use Magma if Singular elimination remains too slow or if modular
reconstruction is easier there.

Recommended Magma target:

- define the ideal over \(\mathbb Q[n,a,Y,s]\);
- saturate by the product factor using the auxiliary equation;
- eliminate \(Y,a,s\);
- factor the resulting univariate polynomial;
- cross-check selected modular fibers against the SymPy finite-field scripts.

Magma is likely better for one-shot exact computations, while Sage/Singular
is better for keeping the workflow in the repository.

## Local Geometric Route

The local geometric checker has shown that some regular \(a\)-gcd fibers are
projection artifacts: they do not lift to any \(Y\) satisfying the full
system.  This suggests an alternate path.

For each CRT class and type:

1. extract the common \(a\)-factor over the local field;
2. test all \(a\)-roots, not only linear gcds;
3. solve the full \((a,Y)\)-system;
4. kill degeneracies
   \[
     a=0,\quad Y=0,\quad Y=a,\quad z=0,\quad z=a,\quad z=Y
   \]
   and hidden denominator failures;
5. record any genuine nondegenerate local points separately.

This is not a replacement for exact elimination unless it is converted into
a finite certificate for every exceptional class, but it is useful for
detecting projection artifacts before running expensive exact algebra.

## Immediate Engineering Tasks

1. Extend `endpoint_d6_regular_t_geometry_check.py` so it tests every root of
   a nonlinear gcd in \(a\), not only degree-one gcds.
2. Add an export script that writes the compact \(d-6\) eliminants to a
   Sage-readable format.
3. Implement one Sage/Singular prototype for the smallest remaining type and
   one CRT class.
4. Compare the eliminated \(n\)-factor against the existing modular residue
   data.
5. Only after that, scale to the remaining classes.

## Success Criterion

The next phase succeeds when every remaining \(d-6\) exceptional class is
accounted for by one of:

- a univariate exact factor in \(n\) with no admissible integer root;
- a local geometric contradiction after lifting to \((a,Y,z)\);
- an explicitly isolated nondegenerate local point that requires a new
  theoretical argument.

