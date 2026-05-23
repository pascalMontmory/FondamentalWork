# Verification des signatures terminales de classes arithmetiques

> Statut : protocole de verification.
>
> Objectif : tester les identites finies demontrees du cadre `MathClass` et
> explorer experimentalement l'existence de lois terminales limites pour
> differentes classes arithmetiques.

Ce protocole separe :

- les identites exactes verifiables a `N` fini ;
- les tests experimentaux de convergence ;
- les biais arithmetiques locaux ;
- les signaux terminaux robustes.

## Niveau A : identites finies

Ces resultats sont exacts a `N` fini. Ils doivent passer a erreur flottante
nulle ou quasi nulle.

Tests couverts par :

```text
Math/MathClass/scripts/check_mathclass_identities.py
```

Le script verifie :

- decomposition des unions disjointes ;
- classes terminales pures ;
- symetrie et inegalite triangulaire de la pseudometrique TV ;
- projection exacte entre bornes ;
- contraction TV sous projection.

Commande :

```bash
PYTHONDONTWRITEBYTECODE=1 python3 Math/MathClass/scripts/check_mathclass_identities.py --limit 10000 --bounds 27,89,127
```

## Niveau B : convergence experimentale

Ces tests ne prouvent pas l'existence d'une limite. Ils mesurent seulement :

```math
\|\nu_{B,\mathcal F,N_i}-\nu_{B,\mathcal F,N_{i+1}}\|_{\rm TV}.
```

Script :

```text
Math/MathClass/scripts/scan_terminal_signature_convergence.py
```

Commande :

```bash
PYTHONDONTWRITEBYTECODE=1 python3 Math/MathClass/scripts/scan_terminal_signature_convergence.py --limits 10000,30000,100000 --bounds 27,89,127
```

## Motifs premiers

Pour :

```math
H=\{0,2\},\quad H=\{0,4\},\quad H=\{0,6\},
```

on compare les classes `twin`, `cousin`, `sexy` a des controles :

- `prime`;
- `prime_non_twin`;
- `odd`;
- `admissible_30`;
- `admissible_210`;
- `admissible_2310`.

Script :

```text
Math/MathClass/scripts/scan_prime_pattern_terminal_signatures.py
```

Commande :

```bash
PYTHONDONTWRITEBYTECODE=1 python3 Math/MathClass/scripts/scan_prime_pattern_terminal_signatures.py --limits 10000,30000,100000 --bounds 27,89,127
```

## Interpretation

Une identite finie qui echoue indique un bug.

Une distance experimentale qui diminue avec `N` est un indice de convergence,
pas une preuve.

Une distance stable positive contre `odd`, mais faible contre `admissible_210`
ou `admissible_2310`, indique probablement un biais modulo plutot qu'une
structure profonde de primalite.

Un signal credible devrait survivre :

1. a l'augmentation de `N` ;
2. aux controles modulo ;
3. aux projections entre bornes ;
4. aux controles contre classes proches.
