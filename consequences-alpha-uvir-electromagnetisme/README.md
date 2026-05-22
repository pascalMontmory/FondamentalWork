# Consequences electromagnetiques de la conjecture UV/IR sur alpha

Ce dossier formalise les consequences algebriques de

```text
alpha^{-1} = L = ln(R_Lambda/(10 pi ell_P)).
```

Verdict court :

- les formules du texte sont correctes comme reecritures algebriques une fois
  `alpha=1/L` pose ;
- elles ne constituent pas des predictions independantes, car beaucoup de
  grandeurs atomiques contiennent deja `alpha` par definition ;
- les points physiquement exploitables sont :
  - la contrainte de non-variation temporelle de `alpha`, qui exclut un choix
    naif `L=c/H(t)` ;
  - la correction GUP atomique
    `chi_e = beta0 (m_e/m_P)^2 / L^2`, utile pour montrer qu'un `beta0`
    universel enorme serait incompatible avec la physique de precision ;
  - le verrou theorique `g_edge^{U(1)}=1/2`, qui reste le calcul central.

Reproduire le test numerique :

```bash
python3 scripts/test_em_consequences.py
```

Compiler la note :

```bash
latexmk -pdf -interaction=nonstopmode main.tex
```
