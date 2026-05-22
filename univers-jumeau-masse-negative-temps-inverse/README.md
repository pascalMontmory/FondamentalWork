# Univers jumeau, masse negative et fleche du temps inverse

Ce dossier est separe des deux papiers precedents:

- `../paper1-no-go-universal-gup-vacuum-dark-energy/`
- `../paper2-alpha-lambda-uvir-conjecture/`

Il teste une configuration speculative differente: deux secteurs conjugues, une branche ordinaire de signe gravitationnel positif, une branche jumelle de signe effectif negatif, et une orientation temporelle opposee.

## Message central

Le scenario jumeau change l'hypothese cosmologique de depart. Il ne doit donc pas etre melange au no-go robuste du papier 1.

Les tests locaux donnent le statut suivant:

- une annulation exacte entre deux secteurs donne `rho_eff = 0`, pas `rho_DE > 0`;
- obtenir l'energie noire observee demande une petite asymetrie residuelle ou un terme de bord/horizon supplementaire;
- les contraintes FIRAS, BBN, atomiques et fermioniques restent applicables a notre secteur si le parametre GUP local y est universel;
- la sensibilite a une puissance generale `gamma` a ete ajoutee: `gamma=3` est le choix isotrope minimal en 3D, mais le no-go local universel survit pour `gamma>2`; pour `gamma<=2`, l'energie de vide massless n'est plus finie;
- la fleche du temps inverse peut etre formulee comme une conjugaison CPT globale, mais elle ne derive pas encore le verrou `g_edge^{U(1)} = 1/2`;
- la relation alpha--Lambda du papier 2 doit utiliser le rayon de de Sitter residuel observe. Si l'annulation est parfaite, `R_Lambda` devient infini et la relation echoue;
- le facteur `1/2` peut etre garde comme comptage d'un bord partage entre deux feuillets; la version Moebius le rend topologique;
- l'image pression/membrane est gardee seulement dans sa version homogene: elle peut representer l'energie noire;
- l'image d'une bosse future du feuillet est compatible si elle signifie une courbure ou tension globale de bord, pas une accumulation locale de masse;
- la carte CMB complete reste expliquee par la physique standard des perturbations primordiales et des oscillations acoustiques; le modele peut seulement motiver une signature globale faible aux grands angles;
- dans la limite parfaitement homogene avec `w=-1`, ce canal est degenere avec Lambda-CDM.

## Pipeline

Executer:

```bash
python3 scripts/run_all_twin_tests.py
```

Sorties:

- `reports/twin_verdict_matrix.md`
- `reports/results_json/*.json`

## Publication

- `PUBLICATION.md` resume la version publiable en Markdown.
- `publication.tex` est une prepublication LaTeX autonome dans la copie locale.
- `main.tex` est la note longue avec tous les tests integres dans la copie locale.

## Statut

Ce dossier est une analyse de configuration, pas une preuve. Il sert a isoler proprement ce que le scenario jumeau peut modifier et ce qu'il ne modifie pas.