# Full A-Block Repair Probe Notes

This note documents the exploratory tool
\[
  \texttt{tools/full\_ablock\_repair\_probe.py}.
\]

The tool combines two exact objects:

1. the least-root low/middle/high A-block cover matrix;
2. the nonprimitive \(t=3u\) repair channel.

It is not a proof.  It is designed to find full coprime A-block covers and
then check whether they are repaired by the nonprimitive channel.

## 1. Definition of a full A-block cover

For a fixed \(m\), a full A-block cover means:

- every coprime complete A-block has an A0 certificate in the current
  low/middle/high model;
- every coprime complete A-block has an A1 certificate in the same model.

Equivalently, the probe reports
\[
  \texttt{covered}=\texttt{cop}.
\]

This does not mean Legendre fails.  It only means the coprime A-block gate
has no open layer.

## 2. Nonprimitive repair search

For every full cover, the tool searches the exact \(t=3u\) channel:

- if \(m\equiv u\pmod2\), test
  \[
    9(m^2+u^2)-1,\qquad 9(m^2+u^2)+1;
  \]
- if \(m\not\equiv u\pmod2\), test
  \[
    9(m^2+u^2)+2.
  \]

The admissibility inequalities are the exact ones from
`legendre_multiple_of_three_refined_channels.md`.

## 3. First scans

Command:
\[
\texttt{python3 Math/conjecture/legendre/tools/full\_ablock\_repair\_probe.py --start 1 --end 10000}
\]

Output:
\[
\begin{array}{c|c}
\text{quantity} & \text{value}\\
\hline
\text{full covers} & 1\\
\text{first full cover} & m=391\\
\text{without nonprimitive repair} & 0\\
\text{repair }u\text{ counts} & \{1:1\}\\
\text{repair }r\text{ counts} & \{-1:1\}.
\end{array}
\]

The full cover is exactly the one recorded in
\[
  \texttt{legendre\_m391\_full\_Ablock\_cover.md}.
\]
It is repaired by
\[
  u=1,\qquad t=3,\qquad r=-1.
\]

Second scan:
\[
\texttt{python3 Math/conjecture/legendre/tools/full\_ablock\_repair\_probe.py --start 10001 --end 20000}
\]

Output:
\[
  \text{full covers}=0.
\]

Thus, in the range
\[
  1\le m\le20000,
\]
the only full A-block cover found is
\[
  m=391,
\]
and it is repaired by \(u=1,r=-1\).

## 4. Proof-search consequence

The data suggest a sharper candidate theorem:

> Full coprime A-block covers are exceptional, and every such cover is
> accompanied by a nonprimitive repair.

This is only a conjectural guide.  The proof target should be stated exactly
as:

> If the coprime A-block gate has a full low/middle/high cover at \(m\), then
> the nonprimitive \(t=3u\) channel has a prime witness.

The first calibration case is
\[
  m=391,\qquad u=1,\qquad r=-1.
\]
