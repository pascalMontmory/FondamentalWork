# Endpoint Gates in the Real Five-Root Casas-Alvero Frontier

This note records the part of the current five-root analysis that is stable
enough to be separated from the ongoing exceptional-fiber computations.

It does not claim a full proof of the five-root frontier.  Its scope is:

1. closure of the massive endpoint gate, equivalently endpoint multiplicity
   \(d-4\);
2. closure of the next endpoint gate, endpoint multiplicity \(d-5\);
3. generic closure of the endpoint multiplicity \(d-6\) gate.

The remaining \(d-6\) work is finite over the parameter line and should be
handled separately.

## 1. Normalization and Endpoint Gates

Work in the real five-root frontier after centering.  The roots may be
normalized so that an endpoint is \(-1\).  An endpoint gate occurs when a top
derivative order is covered automatically by the endpoint because its
multiplicity is high enough.

For an endpoint of multiplicity \(m\), derivative order \(d-r\) is
automatically covered only when
\[
  d-r < m.
\]
Thus the massive endpoint gate is \(m=d-4\), the next endpoint gate is
\(m=d-5\), and the following one is \(m=d-6\).

The moment notation is
\[
  P_k=\sum_i m_i r_i^k,
\]
with \(P_1=0\).  The normalized top derivatives are encoded by the
polynomials \(Q_j\), and a Casas-Alvero cover condition asks that each
relevant \(Q_j\) vanish at one of the roots.

## 2. Endpoint Multiplicity \(d-4\)

The massive endpoint branch is closed.

After reducing the last possible \(Q_4\)-cover to a quadratic endpoint
relation \(F_a\), the two relevant cover conditions reduce modulo \(F_a\) to
linear remainders.  A common root must satisfy a resultant condition in the
endpoint parameter \(n\):
\[
  \operatorname{Res}_a(E_3,C_{34})=0.
\]
The exact resultant factors as
\[
\begin{aligned}
  2^{30}n^{10}(n+1)^8(n+2)^{12}(n+3)^{16}
  (n+4)^6(n+5)^2P_{13}(n)^2P_{46}(n).
\end{aligned}
\]
The prefactor is nonzero for all admissible \(n\ge2\).  The factor \(P_{13}\)
has no root modulo \(13\), and \(P_{46}\) has no root modulo \(17\).  Hence no
integer \(n\ge2\) can satisfy the last massive endpoint condition.

Therefore endpoint multiplicity \(d-4\) is impossible in the real five-root
frontier.

## 3. Endpoint Multiplicity \(d-5\)

After the \(d-4\) closure, the next endpoint gate has endpoint multiplicity
\[
  n=d-5.
\]
The four remaining roots have total multiplicity \(5\).  With roots
\[
  -1,\quad 0,\quad a,\quad Y,\quad z
\]
and multiplicities
\[
  n,\quad m_0,\quad m_a,\quad m_y,\quad m_z,
\]
the centroid equation and \(Q_2(a)=0\) eliminate \(z\) and give the weighted
quadratic
\[
\begin{aligned}
  F_m(Y)=&
  m_y(m_y+m_z)Y^2
  +2m_y(m_a a-n)Y+n^2-2m_a n a+m_z n\\
  &+m_a(m_a+m_z)a^2-m_z(n+5)(n+4)a^2.
\end{aligned}
\]

Up to exchanging \(Y,z\), there are three weight types:
\[
  (2,1,1,1),\quad(1,2,1,1),\quad(1,1,2,1).
\]

For the two symmetric types \((2,1,1,1)\) and \((1,2,1,1)\), all cover triples
for \(Q_3,Q_4,Q_5\) have generic gcd \(1\) over \(\mathbb Q(n)[a]\).  The
integer exceptional factors have only inadmissible roots:
\[
  \{-6,-3,-2,-1\}
  \quad\text{or}\quad
  \{-6,-4,-2,-1\}.
\]
Since \(n=d-5\ge1\), no exceptional specialization survives.

For the asymmetric type \((1,1,2,1)\), the weighted quadratic is
\[
  F(Y)=6Y^2+4(a-n)Y+n^2-2na+n-(n+3)(n+6)a^2,
\]
and \(z=n-a-2Y\).  Each cover condition reduces modulo \(F\) to a linear
equation in \(Y\).  Pairwise compatibility and elimination in \(a\) produce
univariate necessary factors in \(n\).  The exact computation shows only
linear inadmissible roots
\[
  \{-6,-4,-3,-2,-1,0\}
\]
and five nonlinear factors of degrees
\[
  5,\quad7,\quad7,\quad20,\quad22.
\]
These nonlinear factors have no integer roots by modular root tests:
degree \(5\) modulo \(7\), the degree \(7\) factors modulo \(5\), degree \(20\)
modulo \(11\), and degree \(22\) modulo \(7\).

Thus endpoint multiplicity \(d-5\) is impossible.

## 4. Endpoint Multiplicity \(d-6\): Generic Closure

For endpoint multiplicity
\[
  n=d-6,
\]
the remaining four roots have total multiplicity \(6\).  The same reduction
gives the weighted quadratic
\[
\begin{aligned}
  F_m(Y)=&
  m_y(m_y+m_z)Y^2+2m_y(m_a a-n)Y+n^2-2m_a n a+m_z n\\
  &+m_a(m_a+m_z)a^2-m_z(n+6)(n+5)a^2.
\end{aligned}
\]

There are seven weight types:
\[
\begin{gathered}
  (1,1,2,2),\quad(1,1,3,1),\quad(1,2,2,1),\\
  (1,3,1,1),\quad(2,1,2,1),\quad(2,2,1,1),\quad(3,1,1,1).
\end{gathered}
\]

For the four types
\[
  (1,1,2,2),\quad(1,3,1,1),\quad(2,2,1,1),\quad(3,1,1,1),
\]
all \(4^4\) cover quadruples have gcd \(1\) over \(\mathbb Q(n)[a]\).  Hence
these four types are generically impossible.

For the remaining three types
\[
  (1,1,3,1),\quad(1,2,2,1),\quad(2,1,2,1),
\]
the equation-level products
\[
  R_k=\prod_{X\in\{0,a,Y,z\}}H_k(X),\qquad k=3,4,5,6,
\]
reduce modulo \(F_m\) to equations linear in \(Y\).  The generic gcd over
\(\mathbb Q(n)[a]\) is certified to be \(1\) by modular specialization:
\[
\begin{array}{c|c|c}
  \text{type} & p & n\pmod p \\
  \hline
  (1,1,3,1) & 11 & 4 \\
  (1,2,2,1) & 11 & 1 \\
  (2,1,2,1) & 11 & 1.
\end{array}
\]
If a positive-degree common factor existed generically over \(\mathbb Q(n)\),
it would survive all but finitely many good specializations.  These good
specializations have gcd \(1\), so the generic common factor cannot exist.

Therefore all seven endpoint-\(d-6\) types are generically impossible.

## 5. What Remains Outside This Note

The \(d-6\) generic closure does not yet remove every integer specialization.
The remaining obstruction is finite over the \(n\)-line.  Algebraically, one
must eliminate from the saturated ideal
\[
  \langle E_3,E_{34},E_{35},E_{36}\rangle:
  \langle a(n+1)(n+2)(n+3)(n+4)(n+5)(n+6)\rangle^\infty
\]
down to \(\mathbb Z[n]\), or give an equivalent local geometric certificate
for every exceptional fiber.

The current SymPy-based scripts have already localized this problem, but they
are not the right tool for the exact saturated elimination.  The next phase
should use Sage/Singular/Magma or a separate geometric argument.

## Computational Certificates

The following scripts support the claims in this note:

- `Math/conjecture/tools/massive_endpoint_q4_certificates.py`
- `Math/conjecture/tools/endpoint_d5_reduction.py`
- `Math/conjecture/tools/endpoint_d5_symmetric_gcds.py`
- `Math/conjecture/tools/endpoint_d5_symmetric_resultants.py`
- `Math/conjecture/tools/endpoint_d5_asymmetric_resultants.py`
- `Math/conjecture/tools/endpoint_d6_reduction.py`
- `Math/conjecture/tools/endpoint_d6_type_generic_probe.py`
- `Math/conjecture/tools/endpoint_d6_equation_modular_probe.py`

