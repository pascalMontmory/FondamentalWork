# Ramified Fibers of the \(u=1\) Cluster

This note separates the exceptional color gates from the
\(u=1\)-cluster obstruction.

The previous colored-distance gate showed that the only ways for a forced
label to escape its quadratic-residue color class are ramified small-prime
gates.  Here those gates are written as exact quotient equations.

Throughout,
\[
  A=3m,\qquad p_c=A-r_c,\qquad
  e_c=\frac{r_c^2+c}{A-r_c}.
\]

## 1. Odd ramified gate \(5\mid A\)

In the odd no-\(u=1\)-repair cluster
\[
  \{2,4,8,10\},
\]
the only ramified escape is
\[
  p_{10}=5,\qquad 5\mid A.
\]

Then the distance and quotient are no longer variables:
\[
  r_{10}=A-5,
\]
and
\[
  e_{10}
  =
  \frac{(A-5)^2+10}{5}
  =
  \frac{A^2}{5}-2A+7.
\]

The other offsets cannot use the label \(5\), because when \(5\mid A\),
\[
  A^2+2,\quad A^2+4,\quad A^2+8
\]
are congruent to
\[
  2,\quad4,\quad3\pmod5.
\]
Thus their labels are primes at least \(7\), and their distances satisfy
\[
  r_2,r_4,r_8\le A-7.
\]

Since the quotient function
\[
  F_c(r)=\frac{r^2+c}{A-r}
\]
is increasing in both \(r\) and \(c\), we get
\[
  e_2,e_4,e_8<e_{10}.
\]

Therefore, in the odd ramified gate, \(e_{10}\) is the top quotient rank.
The no-\(u=1\)-repair obstruction reduces to the three remaining offsets
\[
  \{2,4,8\}
\]
plus the deterministic terminal label
\[
  p_{10}=5.
\]

For the remaining three quotients, equality is still finite.  If two of
\[
  e_2,e_4,e_8
\]
were equal, then the maximum offset difference is \(6\), so
\[
  r\le 4.
\]
Since the maximum offset among \(\{2,4,8\}\) is \(8\),
\[
  A\le4+16+8=28.
\]

Hence in the odd ramified gate:
\[
\boxed{
  A>28
  \quad\Longrightarrow\quad
  e_2,e_4,e_8\ \text{are distinct and }e_{10}\text{ is the top rank}.
}
\]

Since \(A=3m\), this holds for every odd ramified branch with
\[
  m\ge15.
\]

## 2. Even ramified gate \(p_5=5,\ 5\mid A\)

In the even no-\(u=1\)-repair cluster
\[
  \{1,5,11\},
\]
one ramified gate is
\[
  p_5=5,\qquad 5\mid A.
\]

Then
\[
  r_5=A-5,
\]
and
\[
  e_5
  =
  \frac{(A-5)^2+5}{5}
  =
  \frac{A^2}{5}-2A+6.
\]

The labels for \(c=1\) and \(c=11\) cannot also be \(5\), because if
\(5\mid A\), then
\[
  A^2+1\equiv1\pmod5,\qquad
  A^2+11\equiv1\pmod5.
\]
Thus their labels are at least \(7\), and
\[
  r_1,r_{11}\le A-7.
\]

For \(p\ge7\) and \(c\le11\),
\[
  \frac{(A-p)^2+c}{p}
  =
  \frac{A^2}{p}-2A+p+\frac cp
  \le
  \frac{A^2}{7}-2A+7+\frac{11}{7}.
\]
Therefore
\[
  e_5-e_c
  \ge
  \frac{2A^2}{35}+6-7-\frac{11}{7}
  =
  \frac{2A^2}{35}-\frac{18}{7}.
\]
This is positive for \(A\ge7\).

Hence:
\[
\boxed{
  p_5=5,\ 5\mid A
  \quad\Longrightarrow\quad
  e_5\text{ is the top quotient rank}.
}
\]

This ramified gate reduces the even cluster to the two remaining variable
offsets
\[
  \{1,11\}
\]
plus the deterministic terminal label \(p_5=5\).

## 3. Even ramified gate \(p_{11}=11,\ 11\mid A\)

The other even ramified gate is
\[
  p_{11}=11,\qquad 11\mid A.
\]

Then
\[
  r_{11}=A-11,
\]
and
\[
  e_{11}
  =
  \frac{(A-11)^2+11}{11}
  =
  \frac{A^2}{11}-2A+12.
\]

Unlike the \(p_5=5\) gate, this does not automatically make \(e_{11}\) the
top quotient.  A label \(p=5\) can occur at \(c=1\) exactly in the
shared-\(5\) gate
\[
  A\equiv\pm2\pmod5,
\]
and it can occur at \(c=5\) exactly in the ramified gate \(5\mid A\).  If
neither of these \(5\)-gates is present, the smallest possible remaining
labels are at least \(7\), and an offset with label \(7\) can have quotient
of order \(A^2/7\), larger than \(A^2/11\).

Thus the exact split is:

- if \(5\mid A\) also holds, the \(p_5=5\) gate gives the top quotient;
- if \(A\equiv\pm2\pmod5\), the shared-\(5\) atom below gives a larger
  \(p=5\) quotient;
- if neither \(5\)-gate holds, the \(p_{11}=11\) gate is deterministic but
  not necessarily top-ranked.

So the \(11\)-ramified branch is a genuine residual fiber, not a solved
rank endpoint.

## 4. Even shared-\(5\) gate \(A\equiv\pm2\pmod5\)

The shared-\(5\) gate is different from the ramified gate \(5\mid A\).  It is
\[
  A^2\equiv -1\pmod5,
\]
or
\[
  A\equiv\pm2\pmod5.
\]

Then
\[
  5\mid A^2+1
  \quad\text{and}\quad
  5\mid A^2+11.
\]
Thus the offsets \(1\) and \(11\) may share the same prime label
\[
  p_1=p_{11}=5.
\]

Their distance is common:
\[
  r_1=r_{11}=A-5.
\]
The quotients are
\[
  e_1
  =
  \frac{(A-5)^2+1}{5}
  =
  \frac{A^2-10A+26}{5},
\]
and
\[
  e_{11}
  =
  \frac{(A-5)^2+11}{5}
  =
  \frac{A^2-10A+36}{5}.
\]
Therefore
\[
\boxed{
  e_{11}=e_1+2.
}
\]

So the shared-\(5\) gate is not a free collision.  It is a rigid two-offset
atom:
\[
\boxed{
  (p_1,p_{11})=(5,5),
  \qquad
  (r_1,r_{11})=(A-5,A-5),
  \qquad
  e_{11}=e_1+2.
}
\]

The only remaining variable offset in the even cluster is then \(c=5\).
Since \(A\equiv\pm2\pmod5\), the value \(A^2+5\) is not divisible by \(5\);
therefore its label is at least \(7\).

## 5. Descent interpretation

The exceptional color gates are now not vague exceptions.  They are finite
fiber types:

1. odd \(5\mid A\): deterministic top atom \(c=10,\ p=5\);
2. even \(5\mid A\): deterministic top atom \(c=5,\ p=5\);
3. even \(11\mid A\): deterministic atom \(c=11,\ p=11\), not always top;
4. even \(A\equiv\pm2\pmod5\): rigid shared atom \(c=1,11,\ p=5\) with
   quotient gap \(2\).

Thus the next exact target is a finite-fiber descent:

> In each ramified or shared fiber, the deterministic atom must either
> force a nonprimitive repair at a higher \(u\), or reduce the full A-block
> cover to a smaller colored-rank cluster on the remaining offsets.

This still does not close Legendre.  It removes the ambiguity from the
exceptional color gates and leaves a finite list of algebraic fibers.
