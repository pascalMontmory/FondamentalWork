# Least-Root Zone Probe Notes

This note documents the exploratory probe
\[
  \texttt{tools/least\_root\_zone\_probe.py}.
\]

The probe measures the exact objects defined in the current boundary of the
Legendre attack.  It is not a proof and it is not used as evidence of
truth.  Its role is to identify which cells of the final cover matrix carry
the obstruction.

## 1. What the probe computes

For a given \(m\), put
\[
  A=3m,\qquad T_m=\lfloor\sqrt{6m}\rfloor,
\]
\[
  Q_m^\ast=\left\lfloor\frac{\sqrt{6m}-2}{3}\right\rfloor,
\]
\[
  B_m=6Q_m^\ast+4,\qquad C_m=2T_m.
\]

For every complete coprime A-block, the tool computes which layer zones are
available:

- \(L\): a low label \(p\le B_m\);
- \(M\): a middle label \(B_m<p\le C_m\);
- \(H\): a high label \(C_m<p\le A\), encoded by a least-root event.

It reports:

- number of complete coprime blocks;
- blocks covered in both A0 and A1 by the current certificate sets;
- A0-open and A1-open blocks;
- low-low, mixed high/low-or-middle, and high-high counts;
- sizes of the high least-root coordinate images;
- priority and full zone matrices when `--verbose` is used.

## 2. Commands

Single values:
\[
\texttt{python3 Math/conjecture/legendre/tools/least\_root\_zone\_probe.py --m 100000 --verbose}
\]

Range:
\[
\texttt{python3 Math/conjecture/legendre/tools/least\_root\_zone\_probe.py --start 1 --end 200}
\]

Range summary:
\[
\texttt{python3 Math/conjecture/legendre/tools/least\_root\_zone\_probe.py --start 1 --end 10000 --summary-only}
\]

Multiple values:
\[
\texttt{python3 Math/conjecture/legendre/tools/least\_root\_zone\_probe.py --m 100 --m 1000 --m 10000 --verbose}
\]

Detailed block certificates:
\[
\texttt{python3 Math/conjecture/legendre/tools/least\_root\_zone\_probe.py --m 391 --show-blocks}
\]

## 3. First profiles

For
\[
  m=1000,
\]
the tool reports:
\[
\begin{array}{c|c}
\text{quantity} & \text{value}\\
\hline
\text{complete coprime blocks} & 26\\
\text{covered in both layers} & 15\\
\text{A0-open} & 10\\
\text{A1-open} & 3\\
\text{low-low} & 9\\
\text{mixed} & 12\\
\text{high-high} & 1
\end{array}
\]

For
\[
  m=10000,
\]
it reports:
\[
\begin{array}{c|c}
\text{quantity} & \text{value}\\
\hline
\text{complete coprime blocks} & 81\\
\text{covered in both layers} & 60\\
\text{A0-open} & 14\\
\text{A1-open} & 8\\
\text{low-low} & 42\\
\text{mixed} & 43\\
\text{high-high} & 11
\end{array}
\]

For
\[
  m=100000,
\]
it reports:
\[
\begin{array}{c|c}
\text{quantity} & \text{value}\\
\hline
\text{complete coprime blocks} & 256\\
\text{covered in both layers} & 180\\
\text{A0-open} & 46\\
\text{A1-open} & 33\\
\text{low-low} & 119\\
\text{mixed} & 135\\
\text{high-high} & 49
\end{array}
\]

## 4. Interpretation

The initial profiles suggest that the high-high cell is real but does not
dominate.  The mixed cells and the low-low cofactor box carry a large part
of the remaining cover.

The useful mathematical lesson is therefore:

> the next proof attempt should not focus only on high-high least-root
> correlations.  It should also attack the mixed neighbor cells and the
> low-low centered cofactor box.

This is only guidance for proof search.  The exact closure target remains
the non-cover theorem in `legendre_current_boundary_of_attack.md`.

## 5. First full A-block cover

Scanning
\[
  1\le m\le10000
\]
with
\[
\texttt{--summary-only}
\]
finds exactly one full cover in the current model:
\[
  m=391.
\]

The summary line is
\[
\texttt{full\_cover: m=391 cop=13 covered=13 ratio=1.0000 defect=0}
\]
with
\[
  \texttt{lowlow}=9,\qquad
  \texttt{mixed}=9,\qquad
  \texttt{hihi}=2.
\]

This is now recorded separately in
\[
  \texttt{legendre\_m391\_full\_Ablock\_cover.md}.
\]

It disproves the naive closure lemma that an open coprime A-block layer must
always exist.  The full Legendre interval is nevertheless repaired by the
nonprimitive \(t=3u\) channel.
