# Cellule position-vitesse deformee par GUP

Ce dossier contient une note de verification et de developpement autour de la
reformulation en variables position-vitesse d'une mesure de phase GUP :

```tex
\dd N =
\frac{m^3 \dd^3x \dd^3v}{h^3(1+\beta m^2v^2)^3}.
```

Le point central est que la longueur minimale reste universelle,
`\Delta x_min = \hbar sqrt(beta)`, tandis que le seuil cinematique en vitesse
depend de la masse :

```tex
v_GUP = 1/(m sqrt(beta)).
```

## Contenu

- `main.tex` : version verifiee et corrigee du manuscrit.
- `PUBLICATION_INDUSTRIELLE.md` : publication courte en Markdown sur les
  applications industrielles de la cellule de phase.
- `publication_industrial_phase_space_gases.tex` : version LaTeX avec figures.
- `PAPER_QUANTUM_SENSOR_PHASE_SPACE.md` : papier complet sur l'application la
  plus forte, les capteurs quantiques a atomes froids.
- `paper_quantum_sensor_phase_space.tex` : version LaTeX du papier capteurs.
- `PHASE_SPACE_CAD_QUANTUM_SENSORS.md` : extension applicative sous forme de
  cadre CAD pour capteurs quantiques, navigation inertielle, gravimetrie et
  gyroscopes atomiques.
- `phase_space_cad_quantum_sensors.tex` : version LaTeX/PDF du cadre CAD.
- `notes/formula_audit.md` : verification des formules et points de prudence.
- `notes/cross_conclusions.md` : conclusions tirees du croisement avec la
  note sur la cellule de phase deformee.
- `notes/industrial_phase_space_gases.md` : exploration gaz industriels,
  moteurs, cryogenie, hydrogene liquide, helium et faisceaux froids.
- `notes/industrial_application_search.md` : recherche d'applications
  industrielles plus fortes, avec conclusion en faveur des capteurs atomiques
  et faisceaux haute brillance.
- `scripts/test_velocity_thresholds.py` : test numerique des seuils
  masse-vitesse avec donnees publiques CODATA/NIST.
- `scripts/simulate_industrial_phase_space_gases.py` : simulations et figures
  sur le critere `eta = n lambda_th^3`.

## Simulation industrielle

```bash
python3 scripts/test_industrial_phase_space_gases.py
python3 scripts/simulate_industrial_phase_space_gases.py
python3 scripts/test_quantum_gas_thresholds.py
python3 scripts/simulate_quantum_gas_thresholds.py
python3 scripts/score_industrial_applications.py
python3 scripts/simulate_cold_atom_sensor_phase_space.py
python3 scripts/simulate_atom_interferometer_design.py
python3 scripts/phase_space_sensor_cad.py
python3 scripts/test_phase_space_sensor_cad.py
```

Sorties:

- `reports/industrial_phase_space_report.md`
- `reports/industrial_phase_space_summary.json`
- `reports/phase_space_sensor_cad_report.md`
- `reports/phase_space_sensor_cad_summary.json`
- `reports/data/*.csv`
- `reports/figures/*.png`

Conclusion courte: les gaz de chambre d'un moteur chimique sont beaucoup trop
classiques pour que `h^3` donne un levier direct de poussee. Le critere devient
utile pour cryogenie profonde, hydrogene liquide, helium, faisceaux froids et
controle de validite des equations d'etat.

Compiler la publication industrielle:

```bash
latexmk -pdf publication_industrial_phase_space_gases.tex
latexmk -pdf paper_quantum_sensor_phase_space.tex
latexmk -pdf phase_space_cad_quantum_sensors.tex
```

## Envoi email style Securaw

Un script local reprend le principe SMTP/MIME de Securaw Attesta sans afficher
les secrets:

```bash
php tools/send_pdf_attesta_style.php \
  --to destinataire@example.com \
  --pdf paper_quantum_sensor_phase_space.pdf \
  --dry-run
```

Retirer `--dry-run` pour envoyer effectivement, apres confirmation du
destinataire.
