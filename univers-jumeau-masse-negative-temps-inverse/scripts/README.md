# Scripts

## Pipeline theorique

```bash
python3 scripts/run_all_twin_tests.py
```

Ce pipeline lance les tests `test_*.py` et produit:

- `reports/twin_verdict_matrix.md`
- `reports/results_json/*.json`

## Tests observationnels

Les scripts `obs_*.py` sont separes du pipeline theorique. Ils servent a tester
les problemes cosmologiques ouverts avec donnees publiques ou mesures
compressees.

Principaux scripts:

- `obs_test_h0_s8_tensions.py`
- `obs_test_cosmic_birefringence_mobius.py`
- `obs_fit_cmb_birefringence_spectra.py`
- `obs_birefringence_theory_discriminants.py`
- `obs_test_desi_w0wa_edge.py`
- `obs_test_cmb_lowell_edge.py`
- `obs_test_bbn_lithium_edge.py`
- `obs_test_edges21cm_twin_cooling.py`

## Donnees jouet

```bash
python3 scripts/obs_make_birefringence_toy_data.py
python3 scripts/obs_fit_cmb_birefringence_spectra.py \
  --observed reports/toy_birefringence/toy_observed_eb_tb.csv \
  --theory reports/toy_birefringence/toy_theory_te_ee_bb.csv
```

Ce test verifie que l'ajusteur retrouve un angle `beta` injecte dans `EB/TB`.
