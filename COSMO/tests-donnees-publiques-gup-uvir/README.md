# Tests avec donnees publiques du cadre GUP--UV/IR

Ce dossier rassemble des tests observationnels simples des notes GUP--UV/IR.
Les tests utilisent des constantes CODATA/NIST 2022, les parametres Planck
2018, et des contraintes publiques issues de FIRAS, Planck+BAO+SNe, SPARC,
BBN/CMB et etoiles a neutrons.

Conclusion courte :

- un `beta0` ajuste directement a l'energie noire (`~10^60`) est exclu comme
  parametre universel pour les photons, le plasma primordial et les fermions
  denses ;
- la piste viable est une separation de secteurs : GUP comme regulateur UV
  local, puis projection gravitationnelle/holographique IR ;
- les relations `rho_DE ~ rho_P (ell_P/L_H)^2` et
  `a_dS/(2pi) ~ 10^-10 m/s^2` sont compatibles comme ordres d'echelle, mais ne
  constituent pas seules une preuve dynamique.

Script principal :

```bash
python3 scripts/run_public_data_tests.py
```

Il produit un rapport numerique reproductible dans le terminal.
