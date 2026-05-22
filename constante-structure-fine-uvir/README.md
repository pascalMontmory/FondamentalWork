# Conjecture UV/IR pour la constante de structure fine

Ce dossier teste et formalise la relation candidate

```text
alpha^{-1} = ln(R_Lambda / (10 pi ell_P))
```

avec `R_Lambda = sqrt(3/Lambda)` et `Lambda = 3 Omega_Lambda H0^2/c^2`.

Verdict court :

- l'algebre interne de la note est correcte ;
- avec CODATA 2022 et Planck 2018, la relation donne
  `alpha^{-1}=137.036063743`, tres proche de `137.035999177` ;
- l'ecart relatif est `4.7e-7`, mais l'ecart absolu reste tres superieur a
  l'incertitude experimentale de `alpha` ;
- le resultat doit donc etre presente comme une conjecture UV/IR
  conditionnelle, pas comme une derivation confirmee ;
- le verrou theorique est la derivation independante de
  `g_eff^{U(1)}=5/2`, surtout la contribution `+1/2` du mode de bord Maxwell
  dans une capacite holographique renormalisee.

Reproduire le test :

```bash
python3 scripts/test_alpha_uvir.py
```

Compiler la note :

```bash
latexmk -pdf -interaction=nonstopmode main.tex
```
