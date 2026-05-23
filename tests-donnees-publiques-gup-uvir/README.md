# Tests avec donnees publiques du cadre GUP--UV/IR

Ce dossier rassemble des tests observationnels simples des notes GUP--UV/IR.
Les tests utilisent des constantes CODATA/NIST 2022, les parametres Planck
2018, et des contraintes publiques issues de FIRAS, Planck+BAO+SNe, SPARC,
BBN/CMB et etoiles a neutrons.

## Question testee

Le test principal est volontairement strict : peut-on appliquer partout le meme
parametre local

```text
beta0_Lambda ~= 2.36e60
```

obtenu en identifiant directement la densite de vide GUP regularisee a l'energie
noire observee ?

## Resultat court

Non. Ce `beta0` est exclu comme parametre universel pour les photons, la
radiation primordiale et les fermions denses.

La piste viable est donc une separation de secteurs : GUP comme regulateur UV
local, puis projection gravitationnelle/holographique IR. Les relations
`rho_DE ~ rho_P (ell_P/L_H)^2` et `a_dS/(2pi) ~ 10^-10 m/s^2` sont compatibles
comme ordres d'echelle, mais ne constituent pas seules une preuve dynamique.

## Bornes numeriques visibles

| Probe | Critere utilise | Borne approx. sur `beta0` | Verdict pour `beta0_Lambda` |
|---|---|---:|---|
| FIRAS/CMB | distorsion de forme du corps noir, env. `50 ppm` | `3.72e58` | exclu comme parametre photon universel |
| BBN/radiation | correction radiation `< 10%` vers `T ~ 1 MeV` | `2.64e41` | exclu dans le secteur radiation primordial |
| Fermions denses | `chi = beta0 (p_F c/E_P)^2 < 0.1` | `1.66e38` | exclu pour fermions denses |
| HDE simple | `w0` avec `Omega_DE=0.685`, `c_hde=1` | `w0 = -0.885` | tension avec `w = -1.03 +- 0.03` |

## Interpretation

Ces tests ne refutent pas toute idee GUP ou UV/IR. Ils refutent une hypothese
plus specifique : un meme `beta0 ~ 10^60` local et universel dans tous les
secteurs physiques.

C'est ce qui force la distinction professionnelle suivante :

```text
resultat robuste: no-go du beta0 universel ajuste a Lambda
piste ouverte: projection IR/holographique ou secteur gravitationnel effectif
```

## Script principal

```bash
python3 scripts/run_public_data_tests.py
```

Il produit un rapport numerique reproductible dans le terminal.

## Statut scientifique

- `observationally constrained` pour les bornes publiques visibles ci-dessus ;
- `rejected as primary mechanism` pour le `beta0_Lambda` universel ;
- `candidate conjecture` pour les modeles de projection IR qui evitent ce
  parametre universel local.
