# Innovations Methodologiques

## Contribution Principale

Nous proposons d'elever la sensibilite a la seed et la stabilite fonctionnelle au rang de proprietes de premier ordre dans l'evaluation des PRNG pour les simulations Monte Carlo.

Alors que les batteries classiques, comme TestU01 BigCrush ou PractRand, evaluent principalement la qualite statistique d'un flux, le cadre propose mesure systematiquement:

- la dispersion de la variance Monte Carlo selon la seed;
- la robustesse des estimateurs sur des integrandes representatives;
- la reproductibilite bit-exact entre architectures;
- la difference entre succes statistique global et stabilite fonctionnelle pratique.

Un PRNG peut passer BigCrush avec de bons p-values tout en presentant une dispersion inter-seed superieure a un facteur `20` sur certaines integrandes. Ce phenomene est precisement l'objet du diagnostic structurel.

## Difference avec les Batteries Classiques

Les batteries statistiques classiques testent des proprietes de distribution sur un ou plusieurs flux. Elles repondent principalement a la question:

```text
Le flux observe ressemble-t-il a un flux uniforme independant selon une famille de tests?
```

Le diagnostic structurel repond a une autre question:

```text
La performance Monte Carlo reste-t-elle stable quand on change la seed,
la fonction estimee, ou le backend d'execution?
```

Ces deux questions sont complementaires. Le succes a BigCrush est necessaire pour une revendication serieuse, mais il n'est pas suffisant pour etablir la stabilite fonctionnelle.

## Notion de Stabilite Fonctionnelle

Pour une integrande `f`, une seed `s`, un nombre d'echantillons `N` et `R` repetitions, on mesure:

```text
I_{s,r}(f) = (1/N) sum_{t=1}^N f(u_{s,r,t})
```

Puis la variance empirique associee a la seed:

```text
V_s(f) = (1/(R-1)) sum_{r=1}^R (I_{s,r}(f) - bar I_s(f))^2
```

La dispersion inter-seed est:

```text
rho_f(B) = max_{s in B} V_s(f) / min_{s in B, V_s(f)>0} V_s(f)
```

Une valeur elevee de `rho_f(B)` indique qu'une partie de la performance Monte Carlo depend fortement du choix de la seed.

## Integrandes de Diagnostic

Le protocole utilise des integrandes simples mais informatives:

```text
f_1(u) = u
f_2(u) = sin(2 pi u)
f_3(u) = u^2
f_4(u) = 1{u > 0.99}
```

La derniere integrande teste un evenement rare. Elle est importante parce que les defauts pratiques des PRNG apparaissent souvent plus nettement dans les queues de distribution que dans les moyennes simples.

## Auto-Decouverte des Seeds Structurelles

Au lieu de choisir quelques seeds arbitraires, le protocole explore un ensemble fini `B`, typiquement 100 seeds, puis extrait des seeds representatives:

```text
s_best   = argmin_{s in B} S(s)
s_worst  = argmax_{s in B} S(s)
s_median = argmin_{s in B} |S(s) - median_B S|
s_std    = argmin_{s in B} |S(s) - (mean_B S + std_B S)|
```

Le score proprietaire complet n'est pas publie, mais un score ouvert peut etre construit a partir des variances normalisees:

```text
S_open(s) = (1/4) sum_{f in F} |Z_s(f)|
```

avec:

```text
Z_s(f) = (log V_s(f) - median_{b in B} log V_b(f)) / MAD_{b in B}(log V_b(f))
```

Ce score ouvert suffit a reproduire l'esprit du diagnostic sans divulguer les metriques proprietaires.

## Resultats Numeriques Reportes

Les resultats ci-dessous sont des observations reportees dans la note technique. Les logs et tables brutes doivent encore etre importes pour transformer ces resultats en evidence reproductible complete.

| PRNG | Backend | rho quadratic | rho rare event |
| --- | --- | ---: | ---: |
| Montmory_CTACM | CPU | `~10` | `~3.4` |
| Montmory_CTACM | GPU lane 1 | `~10` | `~3.4` |
| MT19937 | CPU | `~10` | `~14` |
| MT19937-64 | CPU | `~1.9` | `~25` |
| PCG32 | CPU | `~15` | `~3.2` |
| xoshiro256** | CPU | `~5.9` | `~10.5` |
| Philox4x32-10 | CPU | `~4.6` | `~11` |
| MRG32k3a | CPU | `~7.7` | `~3.9` |

Le resultat marquant est que plusieurs generateurs connus peuvent montrer une forte amplification de variance sur l'evenement rare, tout en restant compatibles avec les batteries statistiques classiques.

## Lecture des Resultats

Les valeurs `rho_f` ne doivent pas etre interpretees comme des preuves de superiorite generale d'un generateur. Elles mesurent une propriete conditionnelle:

```text
rho_f(B, N, R, backend, seed_selection)
```

pour:

- une famille d'integrandes donnee;
- un ensemble de seeds donne;
- un nombre d'echantillons `N`;
- un nombre de repetitions `R`;
- un backend d'execution;
- une regle de selection des seeds representatives.

L'apport methodologique est de rendre cette dependance explicite. Le resultat scientifique important n'est donc pas seulement la valeur numerique d'un tableau, mais le fait qu'un test de stabilite inter-seed revele des differences que BigCrush ne mesure pas.

## Reproductibilite Cross-Architecture

La condition cible est:

```text
stream_x86(seed) = stream_Metal(seed) = stream_CUDA(seed)
```

ou, de facon verifiable:

```text
SHA256(stream_x86(seed,n))
  = SHA256(stream_Metal(seed,n))
  = SHA256(stream_CUDA(seed,n))
```

Cette exigence est centrale pour les simulations GPU, car un PRNG utilisable en calcul scientifique doit permettre de distinguer les effets numeriques reels des artefacts de backend.

## Positionnement

La nouveaute n'est pas de remplacer BigCrush, PractRand ou les preuves mathematiques classiques. La nouveaute est de completer ces outils par une couche de diagnostic structurel:

- inter-seed;
- inter-fonctionnelle;
- inter-backend;
- orientee Monte Carlo.

Le cadre propose donc une evaluation plus proche de l'usage reel des PRNG dans les simulations.
