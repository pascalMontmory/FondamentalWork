# Diagnostic initial: dynamique locale Montmory

Date: 2026-05-23  
Statut: diagnostic preliminaire, non conclusif

## Commande conceptuelle

Le test correspond a:

```bash
python3 Math/Collatz-Montmory/work/scripts/evaluate_local_dynamics.py \
  --seed-limit 10000 \
  --steps 50 \
  --q-values 3,5,7,11,13,17,19,23,29,31 \
  --seed-mode twins
```

## Resultat local reproduit pendant l'audit

```text
seed_count = 205
q, bias, product_bias, C_dyn
3,  1.946628407460545,  1.946628407460545,  2.5701794884965063
5,  1.1678622668579628, 2.2733938646669785, 3.0016156436673698
7,  1.0763462458153992, 2.446958951494064,  3.2307777294421465
11, 1.0426590148254424, 2.5513438096830985, 3.3685995245001283
13, 1.0155384548497892, 2.5909877502761485, 3.4209423561185948
17, 1.0424932249322494, 2.701087175545336,  3.566309229137402
19, 1.0316988775424085, 2.7867086071543175, 3.6793572286701894
23, 1.0229555236728838, 2.8506789625552775, 3.763818800633924
29, 1.017879093823618,  2.901646519187817,  3.8311124701055554
31, 1.0117086363561403, 2.9356208431150477, 3.8759695728574957
```

## Interpretation

Ce premier test ne soutient pas la cible:

```math
C_{Montmory}=0.107983974916.
```

Au contraire, sur petite borne et petite profondeur, le produit de biais est superieur a `1`, ce qui donne un coefficient dynamique beaucoup plus grand que `2C_2`, alors que la cible demanderait:

```math
B_M\approx0.08178598968002706.
```

Ce resultat n'est pas une refutation asymptotique. Il montre surtout que la dynamique empirique candidate doit etre testee avec controles, profondeurs, bornes plus grandes, et separation entrainement/hors echantillon.

## Consequence pour le programme

La dynamique locale candidate B est falsifiable. Les premiers diagnostics imposent de ne pas presenter `C_Montmory` comme validee par cette voie.

Prochaines mesures:

1. comparer `seed-mode twins` et `seed-mode odd-control`;
2. faire varier `steps`;
3. faire varier `q-max`;
4. verifier si le produit est domine par `q=3`;
5. mesurer des fenetres de graines disjointes.