# Guide de lecture

Ce dossier contient une piste speculative mais testable autour d'un univers
jumeau, d'un bord Moebius/CPT, et d'un canal cosmologique limite au mode zero.

Le fil directeur est volontairement prudent:

```text
effet local fort     -> rejete ou tres contraint
mode zero global     -> compatible avec acceleration cosmique
phase Moebius/CPT    -> testable par polarisation CMB EB/TB
```

## Lecture rapide

1. `README.md`
   - statut general du dossier;
   - conclusions principales;
   - commandes de verification.

2. `PUBLICATION.md`
   - version courte publiable en Markdown.

3. `publication.tex`
   - prepublication courte.

4. `theory_publication.tex`
   - version theorique plus complete: action effective, limite FRW,
     perturbations, CMB, birefringence.

5. `reports/twin_verdict_matrix.md`
   - matrice de verdicts produite par le pipeline.

## Structure scientifique

### Theorie centrale

- `notes/hermitian_symplectic_layer.md`
- `notes/hybrid_janus_zero_mode_eft.md`
- `notes/mobius_time_holonomy.md`
- `notes/zero_mode_acceleration_channel.md`

Ces notes etablissent le cadre:

```text
H_AB = G_AB + i Omega_AB
projection reelle -> Einstein-Hilbert effectif
bord Moebius -> demi-capacite
mode zero -> pression homogene
```

### Audits et garde-fous

- `notes/equation_audit.md`
- `notes/full_formula_recheck_and_theory_upgrade.md`
- `notes/gamma_free_sensitivity.md`
- `notes/membrane_pressure_audit.md`
- `notes/edge_phase_gravity_audit.md`

Ces notes documentent ce qui fonctionne et ce qui ne fonctionne pas.

### Cosmologie observationnelle

- `notes/lambdacdm_degeneracy_and_falsifiability.md`
- `notes/public_data_observational_programs.md`
- `notes/open_cosmology_problem_test_catalog.md`
- `notes/cmb_boundary_signature.md`

Conclusion importante:

```text
le mode zero exact est compatible mais degenere avec Lambda-CDM;
les differences observables doivent venir de deviations controlees.
```

### Piste la plus specifique: birefringence CMB

- `notes/mobius_cmb_birefringence_program.md`
- `notes/birefringence_theory_discriminants.md`
- `scripts/obs_test_cosmic_birefringence_mobius.py`
- `scripts/obs_fit_cmb_birefringence_spectra.py`
- `scripts/obs_birefringence_theory_discriminants.py`

Signature:

```text
Moebius/CPT -> phase globale -> rotation E/B -> EB et TB non nuls
```

Mais ce n'est pas unique. Il faut discriminer contre axions, SME, gravite
chirale, poussiere galactique et calibration instrumentale.

## Commandes utiles

Pipeline theorique:

```bash
python3 scripts/run_all_twin_tests.py
```

Tests observationnels compacts:

```bash
python3 scripts/obs_test_h0_s8_tensions.py
python3 scripts/obs_test_cosmic_birefringence_mobius.py
python3 scripts/obs_birefringence_theory_discriminants.py
```

Test jouet birefringence:

```bash
python3 scripts/obs_make_birefringence_toy_data.py
python3 scripts/obs_fit_cmb_birefringence_spectra.py \
  --observed reports/toy_birefringence/toy_observed_eb_tb.csv \
  --theory reports/toy_birefringence/toy_theory_te_ee_bb.csv
```

Compilation:

```bash
latexmk -pdf main.tex
latexmk -pdf publication.tex
latexmk -pdf theory_publication.tex
```

## Statut

Ce dossier ne revendique pas une confirmation observationnelle. Il organise une
hypothese falsifiable:

```text
si beta CMB est global, achromatique, stable et non local,
  la piste Moebius/CPT devient interessante;
sinon,
  le modele reste une interpretation de bord de Lambda ou est refute sur ce canal.
```
