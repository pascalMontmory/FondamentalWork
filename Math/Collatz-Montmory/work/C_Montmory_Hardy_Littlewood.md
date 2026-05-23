# C_Montmory comme coefficient asymptotique Hardy-Littlewood filtre

Date: 2026-05-23

Statut: formalisation conditionnelle. Ce document ne prouve pas la conjecture des nombres premiers jumeaux et ne prouve pas l'existence inconditionnelle de la constante. Il fixe le sens mathematiquement coherent de `C_Montmory = 0.107983974916` si on l'interprete comme coefficient asymptotique direct.

## 1. Convention retenue

On retient la convention:

```math
N_M(x) \sim C_{\mathrm{Montmory}} \frac{x}{\log^2 x}
```

avec:

```math
C_{\mathrm{Montmory}} = 0.107983974916.
```

Ici `N_M(x)` doit compter un sous-ensemble precis de paires de premiers jumeaux satisfaisant un critere Montmory:

```math
N_M(x)
=
\#\{p \le x : p,p+2 \text{ premiers et } \mathcal M(p,p+2)=1\}.
```

Le critere `\mathcal M` reste a definir exactement. Sans cette definition, la constante ne peut pas etre verifiee.

## 2. Rappel Hardy-Littlewood

La conjecture de Hardy-Littlewood pour les premiers jumeaux predit:

```math
\pi_2(x) \sim 2 C_2 \frac{x}{\log^2 x},
```

ou:

```math
C_2 = \prod_{p>2}\left(1 - \frac{1}{(p-1)^2}\right)
    \approx 0.66016181584686957392781211001455577843.
```

Donc:

```math
2C_2 \approx 1.32032363169373914785562422002911155687.
```

## 3. Densite relative Montmory

Si `C_Montmory` est le coefficient direct, alors le sous-ensemble Montmory aurait une densite relative asymptotique:

```math
\rho_M
:=
\lim_{x\to\infty}\frac{N_M(x)}{\pi_2(x)}
=
\frac{C_{\mathrm{Montmory}}}{2C_2}.
```

Numeriquement:

```math
\rho_M
\approx
0.08178598968002706089023195723731714404.
```

Interpretation: le filtre Montmory retiendrait environ `8.1786%` de la masse Hardy-Littlewood attendue des premiers jumeaux.

## 4. Theoreme conditionnel maximal

### Theoreme

Soit `\mathcal M` un critere booleen sur les paires de premiers jumeaux. Supposons:

1. Hardy-Littlewood jumeaux:

```math
\pi_2(x) \sim 2C_2\frac{x}{\log^2x}.
```

2. Existence d'une densite relative Montmory parmi les jumeaux:

```math
\frac{N_M(x)}{\pi_2(x)} \to \rho_M.
```

Alors:

```math
N_M(x) \sim (2C_2\rho_M)\frac{x}{\log^2x}.
```

En particulier, si:

```math
\rho_M = \frac{0.107983974916}{2C_2},
```

alors:

```math
N_M(x) \sim 0.107983974916\frac{x}{\log^2x}.
```

### Preuve

Par definition:

```math
N_M(x)
=
\frac{N_M(x)}{\pi_2(x)}\,\pi_2(x).
```

En utilisant les deux hypotheses:

```math
\frac{N_M(x)}{\pi_2(x)}\to\rho_M,
\qquad
\pi_2(x)\sim 2C_2\frac{x}{\log^2x}.
```

Donc:

```math
N_M(x)\sim \rho_M\,2C_2\frac{x}{\log^2x}.
```

C'est exactement le coefficient annonce.

## 5. Reciproque logique

Si l'on prouve directement:

```math
N_M(x) \sim C_{\mathrm{Montmory}}\frac{x}{\log^2x}
```

avec `C_Montmory > 0`, alors on prouve automatiquement:

```math
N_M(x)\to\infty.
```

Comme chaque objet compte par `N_M(x)` est une paire de premiers jumeaux, cela implique l'existence d'une infinite de premiers jumeaux.

Donc une preuve inconditionnelle de `C_Montmory > 0` sous cette definition serait au moins aussi forte qu'une preuve d'une infinite de premiers jumeaux.

Conclusion: il ne faut pas presenter cette constante comme demontree tant que le probleme des jumeaux n'est pas contourne par une hypothese clairement conditionnelle ou par un critere qui ne compte pas necessairement des jumeaux premiers.

## 6. Ce qui peut etre prouve maintenant

Sans nouvelle preuve profonde sur les premiers jumeaux, on peut prouver seulement les enonces conditionnels suivants:

1. Si Hardy-Littlewood est vraie et si le filtre Montmory a une densite relative `rho_M`, alors `C_Montmory = 2C_2 rho_M`.
2. Si `C_Montmory = 0.107983974916` est retenu comme coefficient direct, alors `rho_M = 0.081785989680027...`.
3. Si des calculs numeriques donnent `N_M(x)/(x/log^2x) -> 0.107983974916` sur une plage, cela constitue une evidence experimentale, pas une preuve asymptotique.

## 7. Programme de preuve rigoureux

Pour transformer cette constante en resultat publiable, il faudrait:

1. Definir le filtre `\mathcal M(p,p+2)` sans ambiguite.
2. Produire un algorithme exact pour calculer `N_M(x)`.
3. Calculer `N_M(x)` et `N_M(x)/\pi_2(x)` sur des plages croissantes.
4. Identifier un modele probabiliste expliquant la limite `rho_M`.
5. Prouver, au moins conditionnellement a Hardy-Littlewood generalise, que le filtre Montmory est asymptotiquement decorrele des contraintes de primalite sauf par un facteur `rho_M`.
6. Montrer que les erreurs sont suffisamment petites:

```math
N_M(x) = C_{\mathrm{Montmory}}\frac{x}{\log^2x} + o\left(\frac{x}{\log^2x}\right).
```

## 8. Impacts mathematiques si la constante est etablie

Si `C_Montmory` est prouvee comme coefficient positif pour un sous-ensemble de premiers jumeaux:

1. Cela impliquerait une infinite de premiers jumeaux.
2. Cela donnerait une sous-classe structuree de jumeaux avec densite asymptotique positive relative aux jumeaux HL.
3. Cela fournirait une nouvelle statistique arithmetique reliant primalite et dynamique Montmory/Collatz.
4. Cela pourrait etre compare aux constantes de singular series de Hardy-Littlewood.
5. Cela donnerait un invariant numerique testable pour les modeles de compression arithmetique.

## 9. Impacts informatiques possibles

Les impacts informatiques sont conditionnels et ne doivent pas etre surevalues:

1. Generation de jeux de tests arithmetiques structures.
2. Filtrage heuristique de paires candidates dans des recherches de jumeaux.
3. Mesure de biais ou de complexite dynamique pour des suites issues d'entiers premiers.
4. Eventuelle integration dans TimeChain2 comme constante de protocole, mais seulement comme constante empirique tant qu'aucune preuve asymptotique n'existe.

## 10. Formulation recommandee

Formulation correcte:

```text
Nous definissons C_Montmory^HL comme le coefficient asymptotique conjectural d'un sous-ensemble Montmory de paires de premiers jumeaux. Sous Hardy-Littlewood et sous l'hypothese d'une densite relative Montmory rho_M parmi les jumeaux, on a C_Montmory^HL = 2 C_2 rho_M. La valeur numerique 0.107983974916 correspond a rho_M ~= 0.08178598968.
```

Formulation a eviter:

```text
C_Montmory est une constante mathematique demontree et immuable issue de Hardy-Littlewood.
```

La valeur peut etre immuable dans un protocole logiciel, mais pas encore comme constante mathematique prouvee.