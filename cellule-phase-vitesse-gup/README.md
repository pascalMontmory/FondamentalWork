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

## Lecture rapide

La branche actuelle ajoute une piste applicative autour des capteurs quantiques
a atomes froids. La contribution doit etre lue en deux niveaux separes :

1. Le cadre GUP fournit le langage position-vitesse et la mesure de cellule de
   phase.
2. L'application industrielle exploite surtout la limite robuste `beta -> 0`,
   c'est-a-dire les grandeurs standard `lambda_th`, `eta`, `sigma_v`, expansion
   du nuage, nombre d'atomes detectes, contraste et temps de cycle.

La conclusion courte est conservatrice : les gaz chauds industriels restent
profondement classiques, alors que le meme langage de phase-space devient utile
pour prefiltrer des sources atomiques froides destinees a la gravimetrie, aux
gyroscopes, aux accelerometres et aux gradiometres.

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
- `PUBLICATION_MESURE_G_ATOMIQUE.md` : publication autonome proposant une
  mesure differentielle de la constante gravitationnelle `G` par interferometrie
  atomique et masses sources modulees.
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
- `scripts/compare_atom_phase_space_budget.py` : comparaison Rb/Sr/Yb/Cs/Li
  avec contrainte `N_phase_cap = eta_max V_eff / lambda_th^3`.
- `scripts/simulate_sensor_noise_budget.py` : budget technique QPN, shot
  photonique, laser, vibration sismique, Johnson-Nyquist, thermique et duty
  cycle pour un gravimetre atomique.

## Pipeline reproductible

Executer les controles de base :

```bash
python3 -m py_compile scripts/*.py
python3 scripts/test_industrial_phase_space_gases.py
python3 scripts/test_quantum_gas_thresholds.py
python3 scripts/test_phase_space_sensor_cad.py
python3 scripts/test_atom_phase_space_budget.py
python3 scripts/test_sensor_noise_budget.py
```

Regenerer les rapports numeriques :

```bash
python3 scripts/simulate_industrial_phase_space_gases.py
python3 scripts/simulate_quantum_gas_thresholds.py
python3 scripts/score_industrial_applications.py
python3 scripts/simulate_cold_atom_sensor_phase_space.py
python3 scripts/simulate_atom_interferometer_design.py
python3 scripts/phase_space_sensor_cad.py
python3 scripts/compare_atom_phase_space_budget.py
python3 scripts/simulate_sensor_noise_budget.py
```

Compiler les publications LaTeX :

```bash
latexmk -pdf publication_industrial_phase_space_gases.tex
latexmk -pdf paper_quantum_sensor_phase_space.tex
latexmk -pdf phase_space_cad_quantum_sensors.tex
```

## Sorties generees

Les scripts ecrivent notamment :

- `reports/industrial_phase_space_report.md`
- `reports/industrial_phase_space_summary.json`
- `reports/phase_space_sensor_cad_report.md`
- `reports/phase_space_sensor_cad_summary.json`
- `reports/atom_phase_space_budget_report.md`
- `reports/atom_phase_space_budget_summary.json`
- `reports/sensor_noise_budget_report.md`
- `reports/sensor_noise_budget_summary.json`
- `reports/data/*.csv`
- `reports/figures/*.png`

Les CSV, PNG et PDF sont des sorties locales reproductibles. La PR privilegie
les sources, les scripts, les rapports Markdown et les tests plutot que les
binaires generes.

## Resultat capteur nominal

Le budget technique le plus recent ajoute explicitement :

- Quantum Projection Noise : `sigma_phi_QPN = 1/(C sqrt(N_at))` ;
- shot photonique de detection avec photons par atome, efficacite et facteur
  d'exces d'imagerie ;
- vibration sismique avec isolation dependante de la frequence ;
- Johnson-Nyquist magnetique separe du bruit thermique ;
- cycle complet `T_cycle = T_prep + 2 T_i + T_detection + T_dead`.

Cas nominal Sr88 autour de `T_i = 0.102 s` :

- `T_cycle = 1.253 s` ;
- bruit dominant : vibration ;
- sensibilite estimee : `11.52 microGal/sqrtHz`.

Sanity checks de benchmark :

- cas NIM-like : `19.72 microGal/sqrtHz` contre `20.5 microGal/sqrtHz` publie ;
- cas Muquans/Exail-like : `26.44 microGal/sqrtHz` contre `50 microGal/sqrtHz`
  datasheet, meme ordre de grandeur mais sans ajustement force.

## Piste mesure de G

La publication `PUBLICATION_MESURE_G_ATOMIQUE.md` applique ce budget a la mesure
de la constante gravitationnelle de Newton. La strategie proposee est une mesure
differentielle : deux nuages atomiques, des masses sources modulees entre des
configurations `A/B/C/D`, puis un fit global de `G` sur le champ geometrique
calcule.

Le texte fixe aussi une cible de precision realiste : battre les mesures
atomiques publiees autour de `150 ppm` est plausible comme premier palier ;
devenir competitif avec les meilleures mesures modernes demande plutot
`10-50 ppm`, ou la geometrie des masses et les systematiques dominent.

## Portee scientifique

Le dossier ne revendique pas une detection industrielle directe des corrections
GUP. Pour les atomes froids usuels, le facteur
`epsilon_GUP = beta0 (m v / p_Pl)^2` reste negligeable meme avec un `beta0`
phenomenologique tres large.

La valeur applicative est donc le cadre de conception :

```text
temperature -> vitesse -> expansion -> atomes detectes -> bruit de phase -> sensibilite
```

Un score positif signifie seulement que le budget de phase-space ne tue pas deja
l'architecture. La performance reelle reste decidee par la vibration residuelle,
le bruit de phase laser, les aberrations de front d'onde, la detection, le
contraste, le temps de cycle et les donnees PSD mesurees sur instrument.

## Conclusion courte

Les gaz de chambre d'un moteur chimique sont beaucoup trop classiques pour que
`h^3` donne un levier direct de poussee. Le critere devient utile pour cryogenie
profonde, hydrogene liquide, helium, faisceaux froids et controle de validite
des equations d'etat. La piste industrielle la plus solide reste le CAD de
sources atomiques pour capteurs quantiques.

## Envoi email style Securaw

Un script local reprend le principe SMTP/MIME de Securaw Attesta sans afficher
les secrets :

```bash
php tools/send_pdf_attesta_style.php \
  --to destinataire@example.com \
  --pdf paper_quantum_sensor_phase_space.pdf \
  --dry-run
```

Retirer `--dry-run` pour envoyer effectivement, apres confirmation du
destinataire.
