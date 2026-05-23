# Mesurer G par interferometrie atomique differentielle

## Resume

La constante gravitationnelle de Newton `G` est mesurable en laboratoire, mais
elle reste l'une des constantes fondamentales les moins bien determinees. La
difficulte ne vient pas de l'equation de Newton elle-meme, mais du fait que les
forces gravitationnelles entre masses de laboratoire sont tres faibles et que
les erreurs de geometrie, de densite, de position et d'environnement dominent
rapidement le signal.

Cette publication propose une extension directe du cadre `Phase-Space CAD for
Cold-Atom Quantum Sensors` vers une mesure plus fiable de `G`. L'idee n'est pas
de deriver `G` depuis le modele GUP ou depuis le scenario d'univers jumeau. Dans
l'etat actuel du travail, `G` reste une constante d'entree. La contribution est
metrologique : utiliser un interferometre atomique differentiel, des masses
sources modulees et un budget de bruit complet pour extraire `G` avec une chaine
d'incertitude explicite.

Le principe central est :

```text
source mass state A -> phase atomique phi_A
source mass state B -> phase atomique phi_B
Delta phi = phi_A - phi_B
G = parameter fitted from Delta phi and the measured source geometry
```

Cette architecture transforme une mesure absolue fragile en mesure modulee et
differentielle. Elle ne supprime pas les erreurs systematiques, mais elle les
rend calculables, separables et testables.

## 1. Position du probleme

La loi newtonienne pour deux masses ponctuelles est

```text
F = G m1 m2 / r^2.
```

Pour une masse test atomique, l'information utile est l'acceleration produite par
une masse source controlee :

```text
a_source ~= G M / r^2.
```

Une mesure naive donnerait alors

```text
G ~= a_source r^2 / M.
```

Cette formule est seulement une intuition. Dans une experience reelle, la masse
source est etendue, l'echantillon atomique a une distribution spatiale, les
masses ont une densite non parfaitement uniforme, et le champ gravitationnel
local de la Terre n'est pas constant. Le probleme correct est donc geometrique :

```text
a_source(x) = G integral rho(x') (x' - x) / |x' - x|^3 d^3x'.
```

L'interferometre atomique ne mesure pas directement `G`; il mesure une phase. La
valeur de `G` est ensuite ajustee comme parametre de proportionnalite entre le
champ calcule des masses sources et la phase observee.

## 2. Pourquoi les atomes froids sont utiles

Un interferometre atomique a impulsions lumineuses mesure une acceleration par
la relation de premiere approximation

```text
Delta phi = k_eff a T_i^2.
```

Ici :

- `k_eff` est le vecteur d'onde effectif des impulsions optiques ;
- `a` est l'acceleration projetee sur l'axe sensible ;
- `T_i` est le temps d'interrogation ;
- `Delta phi` est la phase differentielle mesuree.

Pour mesurer `G`, on cherche la petite acceleration additionnelle produite par
des masses sources. On module les masses entre deux configurations `A` et `B` :

```text
Delta a_source = a_source,A - a_source,B
Delta phi_AB = k_eff Delta a_source T_i^2.
```

Cette modulation est importante parce qu'elle rejette une grande partie des
termes communs : gravite terrestre moyenne, offsets instrumentaux, derive lente,
et une partie des bruits environnementaux si la cadence de modulation est bien
choisie.

## 3. Architecture proposee

L'architecture la plus robuste n'est pas un gravimetre simple, mais un
gradiometre atomique differentiel :

```text
upper atom cloud
lower atom cloud
source masses moved between state A and state B
simultaneous phase readout
fit of G from the differential phase pattern
```

La mesure utile est une difference de differences :

```text
Delta Phi_G = (phi_upper,A - phi_lower,A) - (phi_upper,B - phi_lower,B).
```

Cette observable reduit :

- l'acceleration commune de la plateforme ;
- les vibrations communes ;
- les derives lentes de l'environnement ;
- une partie des biais laser communs ;
- les variations lentes de `g` terrestre.

Elle augmente aussi la sensibilite a la geometrie locale des masses sources, ce
qui est precisement le signal recherche pour `G`.

## 4. Lien avec le budget de bruit deja construit

Le travail capteurs atomiques ajoute deja les termes qui doivent entrer dans une
mesure de `G` :

```text
sigma_phi_QPN = 1/(C sqrt(N_at))
sigma_phi_photon = F_excess/(C sqrt(N_ph_per_atom N_at eta_det))
sigma_phi_laser^2 = integral |H_phi(f)|^2 S_phi(f) df
sigma_phi_vib^2 = k_eff^2 integral |H_a(f)|^2 S_a(f) df
sigma_phi_JN^2 = (2 pi)^2 integral |H_nu(f)|^2 (dnu/dB)^2 S_B(f) df
T_cycle = T_prep + 2 T_i + T_detection + T_dead
```

Pour `G`, ce budget doit etre transforme en incertitude relative :

```text
sigma_G / G ~= sqrt(
  (sigma_DeltaPhi / DeltaPhi_G)^2
  + geometry_terms^2
  + mass_terms^2
  + atom_cloud_terms^2
  + environmental_terms^2
).
```

Le point important est que la sensibilite atomique n'est qu'une partie du
probleme. Une experience `G` peut etre limitee par le capteur, mais elle est
souvent limitee par la geometrie et les systematiques des masses sources.

## 5. Ordres de grandeur

Prenons un ordre de grandeur simple. Une masse source effective de `200 kg` a
`0.2 m` donne une acceleration ponctuelle approximative

```text
a_source ~ G M / r^2
         ~ 6.67e-11 * 200 / 0.04
         ~ 3.3e-7 m/s2
         ~ 33 microGal.
```

Avec `k_eff ~= 1.6e7 m^-1` et `T_i = 0.15 s`, la phase source serait de l'ordre

```text
Delta phi ~ k_eff a_source T_i^2
          ~ 1.6e7 * 3.3e-7 * 0.0225
          ~ 0.12 rad.
```

C'est un signal mesurable. Mais une mesure de `G` a `10 ppm` demanderait de
controler la partie utile du signal autour de

```text
10 ppm of 33 microGal ~= 3.3e-10 m/s2.
```

Une mesure a `1 ppm` demanderait encore un ordre de grandeur de mieux. Cela
montre pourquoi le protocole doit etre differentiel, module et geometriquement
sur-contraint.

## 6. Peut-on faire mieux que l'existant ?

La reponse courte est : potentiellement oui contre les mesures atomiques
existantes, mais pas automatiquement contre tout l'etat de l'art mondial.

Les ordres de grandeur publics sont les suivants :

- les mesures de `G` par interferometrie atomique publiees ont atteint environ
  `150 ppm` d'incertitude relative dans l'experience de Rosi et al. ;
- les meilleures mesures modernes par balance ou pendule de torsion atteignent
  plutot la zone `10-30 ppm`, avec une dispersion persistante entre experiences ;
- la valeur recommandee CODATA 2022 garde une incertitude relative d'environ
  `22 ppm`, ce qui reflete la difficulte et la dispersion des mesures.

Notre protocole peut donc viser trois paliers :

```text
< 150 ppm  : battre clairement la reference atomique publiee
< 50 ppm   : devenir competitif dans la famille des mesures modernes de G
< 10 ppm   : attaquer l'etat de l'art global, tres difficile
```

Le capteur atomique seul peut probablement atteindre le premier palier si le
signal source est assez grand et si la modulation A/B est propre. Le deuxieme
palier demande deja une excellente metrologie des masses et des distances. Le
troisieme palier ne depend presque plus du bruit atomique seul : il depend de la
geometrie 3D, de la densite interne des masses, des positions des nuages, des
systematiques thermiques, magnetiques, electrostatiques et de la repetition des
inversions de signe.

La strategie realiste n'est donc pas de promettre d'emblee la meilleure valeur
de `G`. Elle est de construire une mesure atomique independante, reproductible,
avec des systematiques differentes des balances de torsion. Meme si elle n'est
pas immediatement plus precise que les meilleures mesures, elle peut etre tres
utile parce qu'elle teste `G` avec une physique instrumentale differente.

## 7. Masse source et geometrie

La masse source ne doit pas etre modelisee comme un point. Il faut decrire les
volumes reels : cylindres, anneaux, parallelepipedes, spheres ou assemblages
symetriques. Le champ doit etre calcule par integration numerique ou formule
analytique controlee.

Pour une densite discretisee :

```text
a_source(x_i) = G sum_j rho_j DeltaV_j (x_j - x_i) / |x_j - x_i|^3.
```

La phase observee doit ensuite etre moyennee sur la distribution atomique :

```text
<Delta phi> = integral n_atom(x, v) k_eff a_source[x(t)] T_i^2 d^3x d^3v.
```

Dans le modele de premiere passe, on peut separer :

```text
atom cloud center
cloud radius
velocity spread
interrogation trajectory
source mass mesh
source mass position
source mass density map
```

Une publication serieuse sur `G` doit donc publier non seulement la sensibilite
du capteur, mais aussi le modele CAO/metrologique des masses.

## 8. Protocole experimental propose

### Etape 1 - calibration sans masses modulees

Mesurer le bruit de phase differentiel sans mouvement des masses sources :

```text
Phi_0(t) = phi_upper(t) - phi_lower(t).
```

But : caracteriser vibration residuelle, bruit laser, detection, bruit
magnetique et derive thermique.

### Etape 2 - modulation A/B lente

Deplacer les masses sources entre deux configurations stables :

```text
A: masses near upper/lower geometry
B: masses swapped or moved to cancellation geometry
```

Mesurer :

```text
Delta Phi_AB = mean(Phi_A) - mean(Phi_B).
```

But : extraire le signal gravitationnel module.

### Etape 3 - inversion de signe geometrique

Utiliser une seconde paire de positions qui inverse le signe attendu :

```text
C/D such that Delta Phi_CD ~= -Delta Phi_AB.
```

But : tester les offsets qui ne changent pas de signe avec la geometrie.

### Etape 4 - scan de distance

Repeter pour plusieurs distances source-atome :

```text
r1, r2, r3, ...
```

But : verifier que le signal suit le champ calcule, pas seulement une derive
lineaire ou thermique.

### Etape 5 - fit global

Ajuster `G` sur toutes les configurations :

```text
Phi_measured,k = G K_geometry,k + b0 + b1 t + nuisance_terms + noise.
```

`K_geometry,k` est calcule par le modele de masse source avec `G=1`. Le fit
estime `G`, les offsets et les parametres nuisibles contraints.

## 9. Budget d'incertitude

Un budget minimal doit inclure :

| Terme | Effet sur G | Controle requis |
|---|---:|---|
| masse totale | proportionnel | pesee et tracabilite SI |
| densite interne | biais geometrique | cartographie, usinage, symetrie |
| position masses | fort, souvent dominant | interferometrie, metrologie 3D |
| position nuages atomiques | fort | imagerie, calibration trajectoire |
| taille du nuage | moyenne spatiale du champ | temperature, expansion, modele source |
| vibration | bruit de phase | gradiometrie, isolation, seismometre |
| laser | bruit et biais phase | reference phase, symetrie impulsions |
| magnetique | biais atomique | blindage, choix atomique, mesure B |
| thermique | dilatation et phase | capteurs temperature, modele expansion |
| electrostatique | force parasite sur masses | mise a la masse, blindage |
| Coriolis | biais trajectoire | controle rotation, inversion k_eff |

La mesure devient credible seulement si chaque terme a une experience de
renversement ou une contrainte independante.

## 10. Role du cadre GUP, UV/IR et univers jumeau

Le cadre GUP position-vitesse aide a organiser les grandeurs de source atomique :

```text
lambda_th
eta = n lambda_th^3
sigma_v
cloud expansion
N_detected
```

Il ne donne pas actuellement une prediction de `G`. La relation UV/IR et les
travaux holographiques utilisent `G` dans les echelles de Planck, la densite
critique et les bornes de trou noir. Ils peuvent contraindre la coherence du
cadre, mais ils ne remplacent pas une determination metrologique de `G`.

Le scenario jumeau peut jouer un role conceptuel pour tester un `G_effectif`
cosmologique ou une fuite de mode local, mais dans sa version zero-mode homogene
il reste degenere avec une constante cosmologique. Il ne change donc pas la
strategie locale de mesure de `G`.

La separation correcte est :

```text
G theory status: input constant in the present framework
G metrology status: measurable parameter improved by atom interferometry CAD
```

## 11. Extension logicielle proposee

Le dossier peut etre etendu avec un script dedie :

```text
scripts/simulate_newton_G_atom_interferometer.py
```

Fonctions minimales :

```text
load_source_mass_geometry()
mesh_gravity_field(G=1)
propagate_atom_cloud()
compute_phase_for_configuration(A, B, C, D)
add_sensor_noise_budget()
propagate_geometry_uncertainties()
fit_G_from_synthetic_data()
write_G_budget_report()
```

Sorties :

```text
reports/newton_G_atom_interferometer_report.md
reports/newton_G_atom_interferometer_summary.json
reports/data/newton_G_configurations.csv
reports/data/newton_G_uncertainty_budget.csv
reports/figures/newton_G_signal_vs_distance.png
```

Tests :

```text
test point-mass limit against G M/r^2
test symmetry cancellation A/B
test sign inversion C/D
test phase scaling with k_eff and T_i^2
test uncertainty propagation for mass and distance
```

## 12. Critere de succes

Une premiere version ne doit pas promettre une meilleure valeur mondiale de `G`.
Elle doit viser trois resultats controlables :

1. montrer que le signal source module depasse le bruit atomique et vibrationnel
   sur un temps d'integration realiste ;
2. identifier le terme systematique dominant dans la geometrie source-atome ;
3. produire un budget d'incertitude complet, falsifiable et reproductible.

Une experience devient competitive seulement si

```text
sigma_G/G < 100 ppm
```

puis interessante metrologiquement si elle descend vers

```text
sigma_G/G < 10 ppm.
```

Le niveau `1 ppm` demande une maitrise geometrique et systematique beaucoup plus
severe que le seul bruit de phase atomique.

## 13. Conclusion

Oui, le travail actuel peut aider a trouver une maniere plus fiable de mesurer
`G`, mais par une voie precise : transformer le CAD de capteurs atomiques en CAD
metrologique pour masses sources modulees.

La valeur ajoutee est la combinaison de quatre elements :

- source atomique optimisee par phase-space ;
- budget de bruit complet en phase et en `microGal/sqrtHz` ;
- mesure differentielle et modulee du champ de masses connues ;
- inversion geometrique de `G` avec propagation des incertitudes.

Le modele jumeau et le cadre UV/IR gardent une valeur theorique, mais la mesure
fiable de `G` doit rester une experience locale, differentielle, traceable et
sur-contrainee. C'est exactement le type de probleme ou le pipeline capteurs
atomiques peut devenir utile.

## References indicatives

- CODATA 2022 / NIST, recommended value of the Newtonian constant of gravitation.
- J. B. Fixler et al., atom-interferometer measurement of the Newtonian constant
  of gravity, Science 315, 74-77, 2007.
- G. Rosi et al., precision measurement of the Newtonian gravitational constant
  using cold atoms, Nature 510, 518-521, 2014.
- Q. Li et al., measurements of the gravitational constant using two independent
  methods, Nature 560, 582-588, 2018.
- Reviews and comparisons of precision measurements of `G`, including the
  persistent dispersion between independent laboratory determinations.
