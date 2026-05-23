# Theorie holographique UV/IR a cellule de phase deformee

Ce dossier contient la version "cadre maitre" des travaux GUP--UV/IR.

L'architecture est :

```text
cellule GUP -> densite UV finie -> no-go beta0 universel
             -> projection holographique IR -> energie noire effective

horizon de Sitter + seuil U(1) -> conjecture alpha--Lambda
```

Verdict court :

- les integrales GUP et les identites Planck--Hubble sont correctes ;
- l'identification directe `rho_reg=rho_DE` force `beta0~10^60`, exclu comme
  parametre local universel ;
- la projection `rho_grav(L)=min[rho_reg,3c^4/(8pi G L^2)]` est une hypothese
  effective utile, mais pas encore une dynamique covariante ;
- la relation `alpha^{-1}=ln(R_Lambda/(10 pi ell_P))` est numeriquement forte,
  mais reste conditionnelle au calcul du seuil de bord `U(1)`.

Reproduire les verifications :

```bash
python3 scripts/check_master_equations.py
```

Compiler :

```bash
latexmk -pdf -interaction=nonstopmode main.tex
```
