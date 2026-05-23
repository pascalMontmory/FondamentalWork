# Audit mathematique du manuscrit V3.8: marche affine et motifs de premiers

Date: 2026-05-23

Objet audite: manuscrit intitule `Facteurs locaux dynamiques pour les motifs de nombres premiers via une marche affine`, version V3.8 fournie dans la conversation.

## Verdict court

Le manuscrit n'est pas pret pour une soumission a `Compositio Mathematica`, `Duke Mathematical Journal`, `IMRN`, ni une revue comparable.

Les corrections typographiques listees dans la V3.8 sont utiles, mais elles ne resolvent pas les problemes mathematiques centraux. Plusieurs enonces structurants sont faux, non prouves, ou incompatibles avec les definitions donnees.

Statut recommande: document exploratoire / preprint interne, pas article soumis.

## Points bloquants

| Bloc | Statut | Probleme |
| --- | --- | --- |
| Formule de `b(epsilon)` | fausse | Elle ne correspond pas a la composition annoncee des applications affines. |
| Lemme no-wrap / injectivite | faux comme ecrit | Meme avec la formule corrigee, `epsilon -> b(epsilon)` n'est pas injective. |
| Fourier avec `B_L/(q 2^L)` | invalide | Confusion entre l'inverse modulaire de `2^L` modulo `q` et la division reelle par `2^L`. |
| Lemme des frequences exceptionnelles | non demontre | L'argument major/minor arcs est seulement affirme. |
| Proposition de mixing | non prouvee et asymptotiquement incoherente | Les bornes affichees ne donnent pas `q^{-Omega(log log q)}` avec `m ~ log q/log log q`. |
| Mixing depuis loi initiale arbitraire | non justifie | L'operateur est affine, pas une convolution additive simple. |
| Resultats numeriques | non reproductibles | Scripts `sur demande`, pas de donnees ni protocole complet. |
| Verdict revue | injustifie | Les resultats centraux ne sont pas etablis. |

## 1. Erreur dans la formule de `b(epsilon)`

Le manuscrit definit:

```text
phi_epsilon = f_{epsilon_L} o ... o f_{epsilon_1}
```

avec:

```text
f_0(x) = x/2
f_1(x) = (3x+1)/2
```

Il annonce ensuite:

```text
b(epsilon) = sum_{j=1}^L epsilon_j 2^{-j} 3^{k_{>j}(epsilon)}
```

Cette formule est incompatible avec la composition.

Exemple avec `L=2`, `epsilon=(1,0)`:

```text
f_0(f_1(x)) = (3x+1)/4
```

Donc:

```text
b = 1/4
```

Mais la formule du manuscrit donne:

```text
b = 1/2
```

La formule compatible avec l'ordre de composition annonce est:

```text
b(epsilon) = sum_{j=1}^L epsilon_j 3^{k_{>j}(epsilon)} / 2^{L-j+1}
```

ou encore:

```text
b(epsilon) = 2^{-L} B_L(epsilon)
B_L(epsilon) = sum_{j=1}^L epsilon_j 2^{j-1} 3^{k_{>j}(epsilon)}
```

Cette correction change les objets utilises dans les lemmes de no-wrap et de Fourier.

## 2. L'injectivite de `epsilon -> b(epsilon)` est fausse

Le manuscrit affirme que si `q > 6^L/5`, alors l'application `epsilon -> b(epsilon) mod q` est injective.

Cette implication est incorrecte. Le fait que les valeurs soient petites devant `q` evite seulement les collisions modulaires entre entiers distincts. Il ne prouve pas que les entiers `B_L(epsilon)` sont distincts.

Avec la formule corrigee de `B_L`, il existe deja une collision exacte pour `L=5`:

```text
epsilon  = (1,1,1,0,0)
epsilon' = (1,0,0,0,1)
B_L(epsilon) = 19
B_L(epsilon') = 19
```

Donc:

```text
b(epsilon) = b(epsilon') = 19/32
```

La conclusion d'injectivite est fausse independamment de `q`.

## 3. Confusion entre inverse modulaire et division reelle

Dans `F_q`, l'expression:

```text
b(epsilon) = 2^{-L} B_L(epsilon) mod q
```

utilise l'inverse modulaire de `2^L` modulo `q`.

Mais le manuscrit emploie des phases de type:

```text
e_q( xi B_L(epsilon) / (q 2^L) )
```

Cela traite `2^{-L}` comme une division reelle par `2^L`, ce qui n'est pas la meme operation que l'inverse modulaire modulo `q`.

La phase correcte devrait etre ecrite en termes modulaires:

```text
e_q( xi * inv_q(2^L) * B_L(epsilon) )
```

Cette difference invalide les arguments de separation diophantienne tels qu'ils sont ecrits.

## 4. Le lemme des frequences exceptionnelles n'est pas prouve

Le Lemme `lem:exc` affirme l'existence d'un ensemble exceptionnel `E` de taille:

```text
|E| << q 2^{-theta L}
```

et une borne:

```text
|hat(mu)(xi)| << L^{-1/2}
```

hors de `E`.

Le texte donne seulement une indication:

```text
separation diophantienne des phases, argument major/minor arcs
```

Ce n'est pas une preuve. Une preuve devrait au minimum fournir:

1. la definition exacte des phases modulo `q`;
2. une majoration quantitative de l'ensemble exceptionnel;
3. une inegalite de Littlewood-Offord ou sum-product applicable a cette famille precise;
4. le suivi des constantes en fonction de `c`;
5. la gestion des collisions exactes de `B_L`.

En l'etat, le lemme est une hypothese forte, pas un resultat.

## 5. La proposition de mixing ne suit pas des bornes affichees

La proposition affirme:

```text
sum_{xi != 0} |hat(mu)(xi)|^{2m}
  << q 2^{-theta L} + q (C/sqrt(L))^{2m}
```

puis conclut, pour:

```text
L = c log q
m ~ log q / log log q
```

que:

```text
||mu^{[m]} - u_q||_TV <= q^{-Omega(log log q)}
```

Cette conclusion ne suit pas.

Premier terme:

```text
q 2^{-theta L} = q exp(-theta c log(2) log q)
               = q^{1 - theta c log(2)}
```

Or `c < 1/log 6`, donc `c log 2 < log 2/log 6 ~= 0.3869`. Comme `theta < 1`, l'exposant `1 - theta c log 2` reste positif. Apres racine carree, ce terme ne donne pas une decroissance en `q`.

Deuxieme terme:

```text
q (C/sqrt(L))^{2m}
```

avec `m ~ A log q / log log q` donne au mieux une puissance `q^{1-A+o(1)}` si `A` est choisi grand. Cela peut donner `q^{-kappa}` pour une constante `kappa`, mais pas `q^{-Omega(log log q)}`.

Conclusion: la borne annoncee `q^{-Omega(log log q)}` est asymptotiquement incompatible avec les estimations affichees.

## 6. L'operateur affine n'est pas une convolution additive simple

Pour une transformation affine aleatoire:

```text
x -> a_epsilon x + b_epsilon
```

la transformee de Fourier evolue selon:

```text
widehat{T nu}(xi)
  = E_epsilon e_q(xi b_epsilon) widehat{nu}(a_epsilon xi)
```

Ce n'est pas simplement:

```text
widehat{T nu}(xi) = widehat{mu}(xi) widehat{nu}(xi)
```

Donc les puissances `|hat(mu)(xi)|^{2m}` ne decrivent pas automatiquement l'iteration de `T_L` depuis une loi initiale arbitraire.

Il faut analyser une marche sur le groupe affine ou un operateur sur les frequences. Cette analyse n'est pas fournie.

## 7. Le resultat exact avec depart uniforme est correct mais peu nouveau

L'enonce:

```text
T_L u_q = u_q
```

est correct lorsque `(q,6)=1`, car chaque application affine est bijective.

Le corollaire:

```text
Sigma_{q,H}^{dyn} = 1 - nu_H(q)/q
```

est egalement correct si `X_0` est uniforme.

Mais ce resultat vient seulement de l'invariance de la mesure uniforme par bijection. Il ne prouve pas un phenomene de mixing, ni Hardy-Littlewood, ni une correction dynamique non triviale.

## 8. Probleme avec les resultats numeriques

Le manuscrit annonce des gains de stabilite de 20--30%, mais les scripts sont seulement `disponibles sur demande`.

Pour un article mathematique moderne, surtout avec une composante experimentale, il faut fournir:

- code versionne;
- donnees brutes ou procedure de generation;
- definition exacte de l'estimateur `K_H^{mix}` utilise numeriquement;
- graine et environnement;
- barres d'erreur justifiees;
- comparaison a une baseline clairement definie.

En l'etat, ces tableaux ne sont pas auditables.

## 9. Corrections typographiques utiles mais insuffisantes

Les corrections suivantes sont bonnes:

- remplacer `nu_H(p)/p` mal fractionne par `nu_H(p)/p` correctement parenthese;
- preciser le nombre d'iterations dans l'abstract;
- mettre le lemme de queue dans un environnement `lemma`;
- remplacer `SL_2(F_q)` par `AGL_1(F_q)` dans les perspectives;
- preciser la dependance des constantes;
- ajouter `par sommation partielle` pour la queue du produit HL.

Mais ces corrections ne touchent pas les failles centrales: formule de `b`, injectivite, Fourier modulaire, lemme exceptionnel, et mixing.

## 10. Recommandation de statut

Ne pas ecrire:

```text
V3.8 prete pour Compositio Mathematica / Duke Mathematical Journal
```

Ecrire plutot:

```text
V3.8 est une note exploratoire. Le modele uniforme reproduit exactement les facteurs locaux de Hardy-Littlewood par invariance de la mesure uniforme. Les extensions non uniformes et deterministes dependent de lemmes de mixing affine qui ne sont pas demontres dans la version actuelle.
```

## 11. Corrections minimales avant une V3.9

1. Corriger la formule de `b(epsilon)` ou changer explicitement l'ordre d'indexation.
2. Supprimer ou reformuler le lemme d'injectivite des decalages.
3. Recrire les phases Fourier avec l'inverse modulaire de `2^L`.
4. Remplacer la proposition de mixing par une conjecture, sauf preuve complete.
5. Supprimer la borne `q^{-Omega(log log q)}` tant que le calcul d'exposants n'est pas repare.
6. Remplacer `resultat principal` par `resultat exact uniforme + programme conditionnel`.
7. Fournir un script reproductible pour les experiences numeriques.
8. Retirer les affirmations de pret-a-soumettre a des revues majeures.

## 12. Verification rapide utilisee

Controle de la formule de `b`:

```python
from fractions import Fraction

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
```

Sortie:

```text
(3/4, 1/4)
```

Collision avec la formule corrigee de `B_L`:

```text
B_L(1,1,1,0,0) = 19
B_L(1,0,0,0,1) = 19
```

Ces deux verifications suffisent a invalider les lemmes structurants dans leur forme actuelle.