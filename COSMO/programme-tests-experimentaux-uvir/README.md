# Programme de tests experimentaux GUP--UV/IR

Ce dossier transforme les implications experimentales du cadre GUP--UV/IR en
matrice de tests.

Les six axes sont :

1. exclure ou borner un `beta0 ~ 10^60` universel avec FIRAS, BBN, CMB,
   fermions denses et physique atomique ;
2. tester la branche holographique `rho_grav(L)=3c^4/(8 pi G L^2)` ;
3. determiner si `L` doit etre `H^{-1}`, horizon futur, horizon apparent ou
   `R_Lambda` ;
4. chercher une energie noire dynamique `w(a)` proche de `-1` ;
5. tester la relation `alpha--Lambda` ;
6. calculer si le mode de bord Maxwell donne vraiment `g_edge=1/2`.

Conclusion courte :

- `beta0 ~ 10^60` est exclu comme parametre local universel ;
- `L=c/H(t)` est fortement defavorise par les limites sur la variation de
  `alpha` ;
- les branches viables sont une projection holographique/IR, une echelle
  asymptotique `R_Lambda`, ou une dynamique d'horizon non locale ;
- le verrou theorique reste le calcul de bord Maxwell.

Reproduire le tableau :

```bash
python3 scripts/test_matrix_uvir.py
```
