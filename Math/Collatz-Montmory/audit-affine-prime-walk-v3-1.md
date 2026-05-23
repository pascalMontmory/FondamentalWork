# Audit mathematique du manuscrit V3.1: marche affine, flattening et facteurs HL

Date: 2026-05-23

Objet audite: version V3.1 du manuscrit `Facteurs locaux dynamiques pour les motifs de nombres premiers via une marche affine et un theoreme de flattening`.

## Verdict court

La V3.1 n'est pas mathematiquement publiable en l'etat. Elle ne peut pas etre presentee comme prete pour `Compositio Mathematica`, `Duke Mathematical Journal`, `Annals`, ou `Inventiones`.

Les corrections annoncees ameliorent la presentation, mais les preuves centrales restent invalides. Plusieurs erreurs sont structurelles: formule affine fausse, injectivite fausse, mauvaise utilisation de Littlewood-Offord, confusion entre marche affine et convolution additive, et produit local mal defini.

## Resume des points bloquants

| Bloc | Probleme | Consequence |
| --- | --- | --- |
| Formule de `b(epsilon)` | Incompatible avec l'ordre de composition `f_{epsilon_L} o ... o f_{epsilon_1}`. | Les lemmes qui utilisent `B_L` ne portent pas sur la marche definie. |
| Lemme no-wrap | L'injectivite annoncee est fausse. | Le flattening fonde sur absence de collisions s'effondre. |
| Littlewood-Offord | Le lemme cite est faux comme enonce pour tout `theta`. | La proposition d'aplatissement n'est pas demontree. |
| Sous-famille LO | Fixer la queue ne rend pas les coefficients independants comme affirme. | L'argument de reduction a une somme lineaire est incorrect. |
| Utilisation d'une sous-famille | Une borne sur une sous-famille ne borne pas la moyenne totale. | Le passage au Fourier global est invalide. |
| `mu^{(*m)}` | Notation de convolution additive pour une marche affine. | La formule `hat(mu^{*m}) = hat(mu)^m` n'est pas applicable. |
| Produit `K_H^{mix}` | Produit indexe par `q <= Q`, alors que HL est un produit sur les premiers. | Ambiguite ou erreur de definition. |
| Resultats numeriques | Non reproductibles. | Ils ne peuvent pas soutenir une soumission. |

## 1. Formule de `b(epsilon)` incorrecte

La V3.1 definit:

```text
F_epsilon = f_{epsilon_L} o ... o f_{epsilon_1}
f_0(x)=x/2
f_1(x)=(3x+1)/2
```

puis annonce:

```text
b(epsilon) = sum_{j=1}^L epsilon_j 2^{-j} 3^{k_{>j}(epsilon)}
```

Cette formule est fausse pour l'ordre de composition indique.

Exemple `L=2`, `epsilon=(1,0)`:

```text
F_epsilon(x) = f_0(f_1(x)) = (3x+1)/4
```

Donc le terme constant est:

```text
b = 1/4
```

La formule V3.1 donne:

```text
b = 1/2
```

La formule compatible est:

```text
b(epsilon) = sum_{j=1}^L epsilon_j 3^{k_{>j}(epsilon)} / 2^{L-j+1}
```

ou:

```text
b(epsilon) = 2^{-L} B_L(epsilon)
B_L(epsilon) = sum_{j=1}^L epsilon_j 2^{j-1} 3^{k_{>j}(epsilon)}
```

La V3.1 utilise a la place:

```text
B_L(epsilon) = sum epsilon_j 2^{L-j} 3^{k_{>j}(epsilon)}
```

qui correspond a une autre indexation et ne suit pas de la composition telle qu'ecrite.

## 2. Lemme no-wrap: l'injectivite est fausse

La V3.1 affirme:

```text
Si q > 6^L/5, alors epsilon -> b(epsilon) mod q est injective.
```

La borne `B_L < 6^L/5` ne prouve pas que les valeurs `B_L(epsilon)` sont distinctes. Elle prouve seulement que deux valeurs deja distinctes ne se confondent pas modulo `q`.

Avec la formule corrigee de `B_L`, on a une collision exacte pour `L=5`:

```text
B_L(1,1,1,0,0) = 19
B_L(1,0,0,0,1) = 19
```

Donc l'injectivite est fausse.

La version V3.1 ne peut pas utiliser ce lemme comme fondement d'un aplatissement Fourier.

## 3. La remarque sur Erdos-Murty est hors sujet

La V3.1 ecrit que pour `L=floor(c log q)`, `c < 1/log 6`, la condition:

```text
q > 6^L/5
```

est satisfaite pour une densite 1 de premiers par un resultat d'ordre multiplicatif.

Mais cette condition est simplement analytique:

```text
6^L <= 6^{c log q} = q^{c log 6}
```

Si `c < 1/log 6`, alors `6^L/5 < q` pour tout `q` assez grand, pas seulement pour une densite 1. L'appel a Erdos-Murty n'est donc pas pertinent ici.

Et meme lorsque `q > 6^L/5`, cela ne donne pas l'injectivite, comme explique ci-dessus.

## 4. Le lemme Littlewood-Offord est faux comme enonce

La V3.1 enonce:

```text
Pour des entiers non nuls distincts v_j,
| 2^{-L} sum_e exp(2 pi i theta sum e_j v_j) | <= C L^{-1/2}
```

pour tout `theta`.

C'est faux. Si `theta` est un entier, alors tous les termes valent 1 et la moyenne vaut 1.

Des versions correctes de Littlewood-Offord bornent des concentrations ponctuelles ou des moyennes sous hypotheses arithmetiques/non-concentration. Elles ne donnent pas cette borne uniforme en `theta` sans conditions supplementaires.

Dans le manuscrit, `theta = xi/(q 2^L)` est en plus issu d'une confusion entre division reelle et inverse modulaire.

## 5. Le lemme de sous-famille est incorrect

La V3.1 affirme:

```text
Fixons epsilon_{L/2+1}, ..., epsilon_L = 0.
Alors k_{>j}(epsilon)=0 pour j <= L/2.
```

C'est faux. Pour `j <= L/2`, `k_{>j}` inclut aussi les variables:

```text
epsilon_{j+1}, ..., epsilon_{L/2}
```

qui restent libres. Donc `k_{>j}` n'est pas nul en general, et les coefficients ne deviennent pas simplement `2^{L-j}`.

Pour rendre `k_{>j}=0` pour tous les `j <= L/2`, il faudrait aussi fixer les variables libres apres `j`, ce qui detruit la sous-famille de taille `2^{L/2}`.

## 6. Une sous-famille ne controle pas la moyenne totale

Meme si une sous-famille `E` de taille `2^{L/2}` avait une bonne annulation, cela ne suffirait pas a borner:

```text
2^{-L} sum_{epsilon in {0,1}^L} phase(epsilon)
```

La contribution du complement peut etre de taille presque 1. Une borne sur une tranche ne donne pas une borne sur l'ensemble sans decomposition conditionnelle et controle uniforme sur toutes les fibres.

La preuve de la Proposition `flatten` ne fournit pas ce controle.

## 7. Confusion entre marche affine et convolution

La V3.1 note:

```text
mu_{q;L}^{(*m)}
```

et utilise implicitement:

```text
widehat{mu^{(*m)}}(xi) = widehat{mu}(xi)^m
```

Mais la dynamique est affine:

```text
x -> a_epsilon x + b_epsilon
```

La transformee de Fourier evolue comme:

```text
widehat{T nu}(xi)
  = E_epsilon e_q(xi b_epsilon) widehat{nu}(a_epsilon xi)
```

Les frequences sont permutees par multiplication par `a_epsilon`. Ce n'est pas une convolution additive. Il faut analyser un operateur sur les frequences ou une marche sur `AGL_1(F_q)`. Cette analyse n'est pas fournie.

Donc le corollaire:

```text
||mu_{q;L}^{(*m)} - u_q||_TV << sqrt(q) alpha(q)^m
```

ne suit pas des definitions donnees.

## 8. Le resultat uniforme est trivialement vrai mais ne donne pas le flattening

Si `X_0` est uniforme et chaque application affine est bijective, alors `X_m` reste uniforme. Cela donne exactement:

```text
Sigma_{q,H}^{dyn} = 1 - nu_H(q)/q
```

Mais cela ne prouve pas que des lois non uniformes se melangent, ni que les orbites deterministes se decorrelent.

Le coeur du manuscrit devrait donc etre presente comme:

```text
exactitude uniforme immediate + programme conditionnel pour les lois non uniformes
```

et non comme un theoreme de flattening etabli.

## 9. Probleme dans la definition de `K_H^{mix}`

La V3.1 ecrit:

```text
K_H^{mix}(Q) = prod_{q <= Q} ... prod_{q > Q} ...
```

La constante de Hardy-Littlewood est un produit sur les nombres premiers `p`, pas sur tous les entiers `q`.

Si `q` est cense parcourir les premiers, il faut l'ecrire explicitement:

```text
prod_{p <= Q}
```

Sinon la definition est incorrecte.

## 10. Proposition de discrepance non prouvee

La V3.1 affirme:

```text
Delta_m << (log q)^(-1/2) + exp(-delta R/L)
```

puis:

```text
Delta_m << R^{-alpha}
```

La preuve annexe contient seulement des phrases:

```text
Standard via approximation polynomiale.
```

Ce n'est pas une preuve mathematique. Il manque la definition precise de `Delta_m`, l'inegalite d'Erdos-Turan utilisee, la gestion des orbites affines, et les constantes.

## 11. Resultats numeriques non auditables

La V3.1 dit `experiences numeriques reproductibles`, mais ne fournit pas:

- script;
- donnees brutes;
- methode exacte de calcul de `K_H^{mix}`;
- procedure de generation des echantillons;
- comparaison statistique complete;
- fichier de sortie attendu.

Les figures sont commentees et `a fournir`. Le tableau ne peut pas etre verifie.

## 12. Verdict editorial corrige

La phrase:

```text
La V3.1 est rigoureuse, claire, et publiable dans Compositio ou Duke.
```

est fausse.

Verdict correct:

```text
La V3.1 contient une idee interessante: comparer les facteurs locaux HL a une dynamique affine inspiree de Collatz. Mais seuls les enonces uniformes par invariance de la mesure uniforme sont solides. Les resultats de flattening, mixing, discrepance et transfert determinant restent non prouves ou invalides en l'etat.
```

## 13. Recommandation pour une vraie V3.2

Pour rendre le document mathematiquement sain:

1. Corriger la formule exacte de `b(epsilon)`.
2. Retirer l'injectivite globale de `epsilon -> b(epsilon)`.
3. Remplacer le lemme Littlewood-Offord par un enonce correct avec hypotheses.
4. Ne pas utiliser une sous-famille pour borner la moyenne totale sans decomposition uniforme.
5. Remplacer `mu^{(*m)}` par un operateur de Markov affine `T_L^m`.
6. Analyser l'action sur les frequences `xi -> a_epsilon xi`.
7. Presenter le flattening comme conjectural tant qu'une preuve complete n'est pas disponible.
8. Indexer les produits HL par les premiers `p`.
9. Fournir les scripts numeriques.
10. Retirer toute mention de revue de haut niveau avant correction des preuves.

## 14. Test minimal de verification

```python
from fractions import Fraction

# Composition reelle correspondant a f_0(x)=x/2, f_1(x)=(3x+1)/2.
def compose_b(e):
    a = Fraction(1, 1)
    b = Fraction(0, 1)
    for eps in e:
        if eps == 0:
            a, b = Fraction(1, 2) * a, Fraction(1, 2) * b
        else:
            a, b = Fraction(3, 2) * a, Fraction(3, 2) * b + Fraction(1, 2)
    return a, b

print(compose_b((1, 0)))
# Sortie: (3/4, 1/4), pas b=1/2.
```

Collision de la formule corrigee:

```text
B_L(1,1,1,0,0) = 19
B_L(1,0,0,0,1) = 19
```

Ces deux controles suffisent a invalider la chaine de preuves V3.1 telle qu'ecrite.