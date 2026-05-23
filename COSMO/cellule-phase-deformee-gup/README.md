# Cellule de phase deformee et GUP

Ce dossier contient une note mathematique de travail autour d'une cellule elementaire de phase dependante de l'impulsion :

```tex
\heff^3(p)=h^3(1+\beta p^2)^\gamma
```

Le cas principal etudie est `gamma = 3`, avec des consequences candidates sur la densite d'etats, les saturations UV, le rayonnement noir, l'energie du vide et des scenarios cosmologiques effectifs.

## Contenu

- `main.tex` : manuscrit LaTeX principal.
- `figures/` : figures utilisees par le manuscrit.
- `scripts/generate_density_saturation.py` : generation de la figure de saturation des modes.
- `notes/formula_audit.md` : audit des formules et conclusions.
- `Makefile` : commandes utiles pour compiler et regenerer la figure.

## Compilation

```bash
make figures
make pdf
```

Dependances usuelles :

- une distribution LaTeX avec `pdflatex`;
- Python 3 avec `numpy` et `matplotlib` pour regenerer la figure.
