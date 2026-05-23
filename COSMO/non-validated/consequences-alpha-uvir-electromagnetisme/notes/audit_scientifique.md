# Audit scientifique

## Formules verifiees

Toutes les relations suivantes sont correctes si l'on pose
`L=alpha^{-1}` :

```text
e = q_P / sqrt(L)
k_e e^2 = hbar c / L
v_e = c / L
a0 = lambda_bar_e L
r_e = lambda_bar_e / L
a0 r_e = lambda_bar_e^2
E_R = m_e c^2/(2 L^2)
sigma_T = (8 pi/3) lambda_bar_e^2/L^2
R_K = Z0 L/2
G0 = 4/(Z0 L)
Phi0 = h sqrt(L)/(2 q_P)
F_e/F_G = (m_P/m_e)^2/L
m_star = m_P/sqrt(L)
chi_e = beta0 (m_e/m_P)^2/L^2
```

## Corrections et caveats necessaires

1. `v_e=alpha c` est la vitesse de Bohr/echelle caracteristique de l'etat
   fondamental hydrogene. Le traitement spectroscopique moderne utilise
   l'equation de Dirac, la masse reduite, la structure fine, le Lamb shift et
   les corrections QED.
2. `E_1=-m_e c^2 alpha^2/2` est la limite proton infiniment massif. Pour
   l'hydrogene reel, remplacer `m_e` par la masse reduite au premier ordre.
3. Les reecritures avec `L` ne prouvent pas la conjecture alpha--Lambda. Elles
   montrent seulement que si `alpha` est holographique, alors toute la
   physique atomique basse energie herite de ce logarithme.
4. La contrainte la plus forte est dynamique : si `L` varie dans le temps,
   alors `alpha` varie. Les horloges atomiques et les spectres astrophysiques
   imposent donc que l'echelle IR pertinente soit quasi constante.

## Resultat numerique cle

Avec CODATA 2022 :

```text
chi_e/beta0 = 9.328622322062e-50
```

Donc un `beta0` d'ordre unite est invisible en physique atomique. En revanche,
un `beta0 ~ 10^60` universel donnerait `chi_e ~ 10^11`, ce qui est exclu. Cette
observation renforce la conclusion precedente : le grand `beta0` ajuste a
l'energie noire ne peut pas etre un parametre GUP universel local.
