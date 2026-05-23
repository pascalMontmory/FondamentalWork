# Programme Lambda_B: loi mobile d'entree et fluctuation Collatz

Date: 2026-05-23  
Statut: programme mathematique conditionnel + diagnostic reproductible

## 1. Objectif

Le niveau publiable du programme Collatz-Montmory depend d'un objet precis:

```math
\Lambda_B^{\mathcal P}.
```

Cet objet doit etre la loi limite jointe de:

```math
\left(E_B(n),\ \tau_B(n)-\frac{\log_2 n}{d}\right),
\qquad
 d=1-\frac12\log_2 3.
```

La formulation cible est:

```math
\boxed{
\left(E_B(n),\ \tau_B(n)-\frac{\log_2 n}{d}\right)
\Longrightarrow
\Lambda_B^{\mathcal P}
}
```

pour `n` tire dans une population arithmetique `\mathcal P`.

Cette note fait deux choses:

1. formuler proprement l'hypothese `Lambda_B`;
2. donner un diagnostic reproductible fort par fenetres disjointes.

## 2. Definitions

Transformation acceleree:

```math
T(n)=
\begin{cases}
n/2, & n\equiv0\pmod2,\\
(3n+1)/2, & n\equiv1\pmod2.
\end{cases}
```

Temps d'entree:

```math
\tau_B(n)=\min\{t\ge0:T^t(n)\le B\}.
```

Point d'entree:

```math
E_B(n)=T^{\tau_B(n)}(n).
```

Fluctuation centree:

```math
u_B(n)=\tau_B(n)-\frac{\log_2 n}{d}.
```

Score normalise associe:

```math
Z_B(n)=\left(\frac{\log_2 n}{\tau_B(n)}-d\right)\log_2 n.
```

## 3. Relation entre Z_B et la fluctuation

Posons:

```math
L=\log_2 n,
\qquad
\tau_B(n)=\frac{L}{d}+u.
```

Alors:

```math
\frac{L}{\tau_B(n)}
=d\left(1+\frac{du}{L}\right)^{-1}.
```

Donc:

```math
Z_B(n)
=
-d^2u+O\left(\frac{u^2}{L}\right).
```

Ainsi, si:

```math
u_B(n)=u
```

admet une loi limite avec `u^2/L -> 0` en probabilite, alors `Z_B` admet aussi une loi limite, obtenue essentiellement par la transformation:

```math
u\mapsto -d^2\nu.
```

## 4. Hypothese Lambda_B

### Hypothese Lambda_B(P)

Pour une population `\mathcal P`, il existe une mesure de probabilite:

```math
\Lambda_B^{\mathcal P}
\in
\mathcal P(\{1,\dots,B\}\times\mathbb R)
```

telle que:

```math
\left(E_B(n),\ \tau_B(n)-\frac{\log_2 n}{d}\right)
\Longrightarrow
\Lambda_B^{\mathcal P}
```

lorsque `n` est tire uniformement dans `\mathcal P\cap[1,x]` et `x->infty`.

La mesure d'entree terminale est alors la marginale:

```math
\nu_B^{\mathcal P}(y)
=
\Lambda_B^{\mathcal P}(\{y\}\times\mathbb R).
```

## 5. Version paires jumelles

Pour les jumeaux, la formulation correcte est jointe:

```math
\left(
E_B(p),E_B(p+2),
\tau_B(p)-\frac{\log_2 p}{d},
\tau_B(p+2)-\frac{\log_2(p+2)}{d}
\right)
\Longrightarrow
\Lambda_B^{(2)}.
```

Le score de paire `min` est une fonction mesurable de cette limite jointe, modulo l'approximation entre `Z_B` et la fluctuation centree.

## 6. Theoreme conditionnel: Lambda_B implique une loi du score

### Theoreme

Supposons `Lambda_B(P)` et:

```math
\frac{\left(\tau_B(n)-\log_2 n/d\right)^2}{\log_2 n}
\to0
```

en probabilite sur `\mathcal P`. Alors `Z_B(n)` converge en loi vers:

```math
(-d^2\pi_2)_*\Lambda_B^{\mathcal P},
```

ou:

```math
\pi_2(y,u)=u.
```

### Preuve

L'expansion:

```math
Z_B(n)=-d^2u+O(u^2/L)
```

montre que l'erreur tend vers zero en probabilite. Le resultat suit par le theoreme de continuite des applications mesurables.

## 7. Theoreme conditionnel: Lambda_B et coefficient filtre

Supposons:

1. Hardy-Littlewood jumeaux:

```math
\pi_2(x)\sim2C_2\frac{x}{\log^2x};
```

2. une loi limite jointe `\Lambda_B^{(2)}`;
3. un seuil `\alpha` fixe tel que la queue du score de paire ait une masse:

```math
\rho_{B,\alpha}
=
\Lambda_B^{(2)}(\text{queue }Z_B^{pair}\ge\alpha);
```

4. une decorrelation locale suffisante pour transferer cette masse a la population des jumeaux.

Alors:

```math
\#\{p\le x:p,p+2\text{ premiers},Z_B^{pair}(p)\ge\alpha\}
\sim
2C_2\rho_{B,\alpha}\frac{x}{\log^2x}.
```

La valeur candidate `C_Montmory` correspondrait a:

```math
\rho_{B,\alpha}
=
\frac{0.107983974916}{2C_2}.
```

## 8. Protocole de test fort

Un test numerique de `Lambda_B` ne doit pas seulement verifier un ratio final. Il doit comparer des lois empiriques sur fenetres disjointes.

Pour chaque fenetre `I=(a,b]`, on mesure:

```math
\widehat\Lambda_{B,I}^{\mathcal P}
=
\mathcal L_I\left(E_B(n),\tau_B(n)-\frac{\log_2 n}{d}\right).
```

Diagnostics minimaux:

1. distance TV entre les marginales de `E_B`;
2. distance KS entre les fluctuations centrees `u`;
3. distance KS entre les scores `Z=-d^2u`;
4. quantiles de `u` et de `Z`;
5. comparaison `twins` vs `prime-non-twin`.

## 9. Diagnostic B=89 jusqu'a 10^7

Commande conceptuelle:

```bash
python3 Math/Collatz-Montmory/work/scripts/evaluate_lambda_limit.py \
  --bound 89 \
  --limit 10000000 \
  --population twins
```

et:

```bash
python3 Math/Collatz-Montmory/work/scripts/evaluate_lambda_limit.py \
  --bound 89 \
  --limit 10000000 \
  --population prime-non-twin
```

Fenestres:

```text
(1e5,1e6]
(1e6,3e6]
(3e6,1e7]
```

### Jumeaux

```text
window          n      TV_E_vs_prev  KS_u_vs_prev  KS_Z_vs_prev
(1e5,1e6]       6945   -             -             -
(1e6,3e6]       12763  0.0284141     0.0408103     0.0408103
(3e6,1e7]       38048  0.0209214     0.0218025     0.0218025
```

Top entrees terminales dans la derniere fenetre:

```text
61:0.220721
59:0.078900
86:0.067940
65:0.067678
82:0.057138
77:0.054615
73:0.044575
76:0.038819
```

Quantiles de `Z` dans la derniere fenetre:

```text
q10  = -1.005919
q25  =  0.177043
q50  =  1.291474
q75  =  2.132200
q90  =  2.662452
q918 =  2.767303
```

### Premiers non jumeaux

```text
window          n       TV_E_vs_prev  KS_u_vs_prev  KS_Z_vs_prev
(1e5,1e6]       61961   -             -             -
(1e6,3e6]       125555  0.0077063     0.0367727     0.0367727
(3e6,1e7]       409715  0.0060429     0.0234266     0.0234266
```

Top entrees terminales dans la derniere fenetre:

```text
61:0.216716
59:0.076236
65:0.069168
86:0.068548
82:0.056598
77:0.052954
73:0.045263
76:0.040472
```

Quantiles de `Z` dans la derniere fenetre:

```text
q10  = -1.054062
q25  =  0.167545
q50  =  1.293086
q75  =  2.132926
q90  =  2.662647
q918 =  2.772252
```

## 10. Interpretation

Ces resultats ne prouvent pas `Lambda_B`, mais ils sont compatibles avec une stabilisation faible:

- les distances entre fenetres diminuent;
- les lois des jumeaux et des premiers non jumeaux sont proches;
- les entrees terminales dominantes sont les memes;
- les quantiles de `Z` dans la derniere fenetre sont presque identiques entre jumeaux et premiers non jumeaux.

Cela soutient une hypothese plus precise:

```text
La loi Lambda_B existe d'abord sur les premiers, puis la condition p+2 premier
est approximativement decorrelee de cette loi mobile.
```

## 11. Criteres avant publication

Pour rendre ce programme publiable, il faut au moins:

1. pousser les diagnostics a `10^8` ou plus;
2. tester plusieurs bornes `B` dans la bande stable;
3. montrer que les distances entre fenetres decroissent avec `x`;
4. comparer aux populations controles;
5. formuler une hypothese de decorrelation precise entre `Lambda_B` sur les premiers et la condition `p+2` premier;
6. isoler une raison non calibree pour le seuil de queue `alpha`.

## 12. Statut

Verifie:

- les definitions;
- l'expansion algebrique reliant `Z_B` a la fluctuation centree;
- le protocole de test;
- les valeurs diagnostiques ci-dessus pour les bornes indiquees.

Non verifie:

- existence de `Lambda_B`;
- convergence asymptotique;
- decorrelation avec les jumeaux;
- valeur `C_Montmory`.

## 13. Conclusion

Le programme publiable doit etre centre sur:

```math
\boxed{
\left(E_B(n),\tau_B(n)-\frac{\log_2 n}{d}\right)
\Longrightarrow
\Lambda_B^{\mathcal P}
}
```

Les premiers diagnostics jusqu'a `10^7` sont encourageants, surtout parce que les lois jumeaux et premiers non jumeaux sont proches. La prochaine etape forte est de montrer la stabilisation sur des plages plus grandes et de formaliser la decorrelation avec la condition jumelle.