# Conclusions cosmologiques GUP--UV/IR

Ce dossier transforme la synthese cosmologique en note autonome. Le resultat
central est negatif et constructif :

```tex
\text{GUP seul}:\quad \infty\rightarrow\rho_{\rm reg}<\infty
\quad\text{mais}\quad
\rho_{\rm reg}\sim\rho_P\quad(\beta_0\sim1).
```

L'energie noire actuelle necessite une liaison UV/IR :

```tex
\rho_{\rm DE}
=
\Omega_\Lambda\rho_{\rm BH}(L_H)
=
\frac{3\Omega_\Lambda}{8\pi}\rho_P
\left(\frac{\ell_P}{L_H}\right)^2.
```

La conclusion exploitable est que le probleme de la constante cosmologique ne
se reduit pas a la regularisation UV. Il faut une dynamique d'horizon capable de
produire une densite `L^{-2}` et une equation d'etat proche de `w=-1`.

Le script `scripts/test_cosmological_conclusions.py` verifie les ordres de
grandeur avec les constantes CODATA/NIST 2022 et les parametres Planck 2018.
