# Legendre Literature Pack

This folder stores references for the Legendre project.

It intentionally stores metadata, links, and proof-use notes rather than
third-party PDFs.  Many journal articles are copyrighted, and arXiv papers
may have different licenses.  If a PDF is needed later, use the link in
`arxiv_manifest.tsv` or the DOI in `references.bib` and check the license
before committing a local copy.

## Current Proof Status

Legendre's conjecture asks for a prime in
\[
  (n^2,(n+1)^2)
\]
for every positive integer \(n\).  With \(x=n^2\), this is a short interval
of length about
\[
  2\sqrt{x}.
\]

Known unconditional prime-in-short-interval technology remains above this
square-root threshold.  The literature below is organized around the main
ways one might still try to make progress.

## A. Direct Short-Interval Prime Technology

These papers indicate what a direct analytic proof would need to improve.

- Guth and Maynard, *New large value estimates for Dirichlet polynomials*,
  arXiv:2405.20552.
  Relevance: modern large-value estimates; gives asymptotics for primes in
  intervals of length \(x^{17/30+o(1)}\), still above \(x^{1/2}\).

- Li, *The number of primes in short intervals and numerical calculations
  for Harman's sieve*, arXiv:2308.04458.
  Relevance: refinements around the \(x^{0.52}\) barrier; useful for
  checking exactly where Harman-sieve technology still misses Legendre.

- Baker, Harman, and Pintz, *The difference between consecutive primes, II*,
  Proc. London Math. Soc. 83 (2001).
  Relevance: classical unconditional exponent \(21/40=0.525\).

- Ingham, *On the difference between consecutive primes*, Quarterly Journal
  of Mathematics 8 (1937).
  Relevance: historical method giving a prime between sufficiently large
  consecutive cubes, not squares.

## B. Computation and Verification

- Sorenson and Webster, *An algorithm and computation to verify Legendre's
  Conjecture up to \(3.33\cdot 10^{13}\)*, arXiv:2401.13753.
  Relevance: strongest located computational verification of
  Oppermann/Legendre in this folder.

## C. Almost-Prime Between Squares

These are important because pure sieve technology can reach almost-primes in
the Legendre interval, but not primes without a new parity-breaking step.

- Campbell, *On the Existence of Integers with At Most 3 Prime Factors
  Between Every Pair of Consecutive Squares*, arXiv:2603.10356.
  Relevance: explicit \(P_3\) analogue of Legendre for every interval between
  consecutive squares.

- Dudek and Johnston, earlier \(P_4\) result referenced by Campbell.
  Relevance: predecessor to the \(P_3\) theorem; locate exact citation before
  using in a formal note.

## D. Large Gaps and Probabilistic Models

These sources explain why Cramer-style heuristics are not proofs, and why
large-gap constructions do not currently threaten Legendre but shape the
right model.

- Ford, Green, Konyagin, and Tao, *Large gaps between consecutive prime
  numbers*, arXiv:1408.4505.
  Relevance: modern large prime gap construction.

- Banks, Ford, and Tao, *Large prime gaps and probabilistic models*,
  arXiv:1908.08613.
  Relevance: rigorous framework for probabilistic gap models and interval
  sieve heuristics.

## E. Maier Matrix and Irregularity

- Maier, *Primes in short intervals*, Michigan Mathematical Journal 32
  (1985).
  Relevance: shows Cramer-style local models fail in very short intervals.
  A possible Legendre route would need a "matrix inversion" rather than a
  direct random model.

## F. Related Consecutive-Power Results

- Dudek, *An Explicit Result for Primes Between Cubes*, arXiv:1401.4233.
  Relevance: explicit version for cubes; useful calibration for what current
  zero methods can prove.

- Johnston, Thomas, Sorenson, and Webster, *Primes and almost primes between
  cubes*, arXiv:2601.15564.
  Relevance: recent computation plus sieve pattern analogous to square
  intervals.

- Cully-Hugill, *Primes between consecutive powers*, arXiv:2107.14468.
  Relevance: strongest located explicit consecutive-power theorem in this
  pack; far from squares, but useful for explicit-formula calibration.

## G. Claim Watchlist

- Mahilmaran, *Existence of primes between two consecutive squares*,
  arXiv:1908.08995.
  Relevance: claims a proof of Legendre in math.GM.  Treat only as a
  line-by-line verification target, not as a result, unless a rigorous
  independent check succeeds.

## Recommended Reading Order

1. Campbell 2026, to understand the best available almost-prime theorem
   between consecutive squares.
2. Guth-Maynard 2024 and Baker-Harman-Pintz 2001, to understand why direct
   prime-gap technology does not yet reach \(x^{1/2}\).
3. Maier 1985 and Banks-Ford-Tao 2019, to calibrate probabilistic and matrix
   routes.
4. Sorenson-Webster 2024, to understand the computational frontier.
5. The quotient-certificate notes in the parent folder, especially the
   strategy reset and the six quotient skeletons.

## Local Policy

- Keep bibliographic metadata in Git.
- Keep arXiv IDs and DOI links in Git.
- Do not commit copyrighted journal PDFs without explicit license clearance.
- If a preprint PDF is added later, store its license and source URL next to
  it.
