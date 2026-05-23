# Cellule position-vitesse deformee par GUP

Ce dossier contient une note de verification et de developpement autour de la reformulation en variables position-vitesse d'une mesure de phase GUP :

```math
\dd N =
\frac{m^3 \dd^3x \dd^3v}{h^3(1+\beta m^2v^2)^3}.
```

Le point central est que la longueur minimale reste universelle, `\Delta x_min = \hbar sqrt(beta)`, tandis que le seuil cinematique en vitesse depend de la masse :

```math
v_GUP = 1/(m sqrt(beta)).
```

## Contenu

- `main.tex` : version verifiee et corrigee du manuscrit.
- `notes/formula_audit.md` : verification des formules et points de prudence.
- `notes/cross_conclusions.md` : conclusions tirees du croisement avec la note sur la cellule de phase deformee.
- `scripts/test_velocity_thresholds.py` : test numerique des seuils masse-vitesse avec donnees publiques CODATA/NIST.
