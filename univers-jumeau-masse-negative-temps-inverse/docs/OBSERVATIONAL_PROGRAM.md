# Programme observationnel

## Objectif

Tester les canaux observables du modele sans lui attribuer des effets qu'il ne
possede pas.

```text
mode zero strict -> acceleration homogene seulement
low-ell          -> signature globale faible possible
EB/TB CMB        -> meilleure piste Moebius/CPT
k > 0 local      -> fortement contraint
```

## Priorite 1: birefringence CMB

Observable:

```text
beta
C_l^EB
C_l^TB
```

Programmes:

```bash
python3 scripts/obs_test_cosmic_birefringence_mobius.py
python3 scripts/obs_fit_cmb_birefringence_spectra.py \
  --observed observed_eb_tb.csv \
  --theory theory_te_ee_bb.csv
python3 scripts/obs_birefringence_theory_discriminants.py
```

Profil favorable Moebius:

```text
isotrope
achromatique
stable entre instruments
non correle a la poussiere
pas de deformation TT/TE/EE
eventuel lien parite low-ell
```

## Priorite 2: DESI / bord dynamique

Observable:

```text
w0, wa
rho_edge(z)
```

Programme:

```bash
python3 scripts/obs_test_desi_w0wa_edge.py --chain desi_chain.csv
```

Interpretation:

```text
si w0=-1 et wa=0 -> zero-mode degenere Lambda-CDM
si wa != 0 robuste -> bord elastique/dynamique necessaire
```

## Priorite 3: CMB low-ell

Programme:

```bash
python3 scripts/obs_test_cmb_lowell_edge.py \
  --observed-cl planck_tt.csv \
  --theory-cl lcdm_tt.csv
```

Le modele ne doit viser qu'une signature globale faible, pas la carte CMB
complete.

## Garde-fous negatifs

### H0

Le zero-mode pur ne resout pas la tension H0.

```bash
python3 scripts/obs_test_h0_s8_tensions.py
```

### S8

Le zero-mode pur ne modifie pas assez la croissance locale.

### Lithium primordial

Le bord tardif est negligeable a BBN.

```bash
python3 scripts/obs_test_bbn_lithium_edge.py
```

### EDGES 21 cm

Le zero-mode ne refroidit pas localement le gaz.

```bash
python3 scripts/obs_test_edges21cm_twin_cooling.py
```

## Donnees publiques

- Planck Legacy Archive: spectres CMB et cartes.
- ACT/SPT/Simons/LiteBIRD: polarisation CMB et futurs tests de beta.
- DESI DR2: BAO, chaines `w0-wa`.
- Pantheon+/SH0ES: supernovae et H0.
- DES/KiDS/HSC: weak lensing et S8.
- EDGES: spectre 21 cm public.
- SPARC: courbes de rotation, surtout comme null-test local.
