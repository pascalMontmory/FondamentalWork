# Dark-Energy GUP Scale Identity

> Status: conditional algebraic identity, audit level A3.
>
> Verified here: dimensions, algebraic derivation, and numerical equality
> between the closed form and the direct density inversion.
>
> Not verified here: that dark energy is physically produced by a GUP-regulated
> vacuum, that `beta_0` is universal, or that the GUP model is fundamental.

## 1. Assumptions

Use CODATA/NIST constants

```math
c,\qquad \hbar,\qquad G
```

and cosmological parameters

```math
H_0,\qquad \Omega_\Lambda.
```

Define the Planck time and Planck energy density by

```math
t_P=\sqrt{\frac{\hbar G}{c^5}},
\qquad
\rho_P=\frac{c^7}{\hbar G^2}.
```

The observed dark-energy density in flat LCDM notation is

```math
\rho_\Lambda
=
\Omega_\Lambda \frac{3H_0^2}{8\pi G}c^2.
```

The GUP-regulated vacuum density used in the `gamma=3` phase-cell model is

```math
\rho_{\rm vac}
=
\frac{g\rho_P}{16\pi^2\beta_0^2},
```

where `g` is an effective degeneracy factor.

## 2. Derivation

Assume the conditional identification

```math
\rho_{\rm vac}=\rho_\Lambda.
```

Then

```math
\beta_0^2
=
\frac{g\rho_P}{16\pi^2\rho_\Lambda}.
```

Substituting the definitions of `rho_P` and `rho_Lambda`,

```math
\beta_0^2
=
\frac{g}{16\pi^2}
\frac{c^7}{\hbar G^2}
\frac{8\pi G}{3\Omega_\Lambda H_0^2c^2}.
```

Therefore

```math
\beta_0^2
=
\frac{g c^5}{6\pi\hbar G\Omega_\Lambda H_0^2}.
```

Since

```math
\frac{1}{t_P^2}
=
\frac{c^5}{\hbar G},
```

we obtain the closed form

```math
\boxed{
\beta_0^{(\Lambda)}
=
\left(\frac{g}{6\pi\Omega_\Lambda}\right)^{1/2}
\frac{1}{H_0t_P}.
}
```

## 3. Dimensional Check

`H_0` has dimension `T^-1` and `t_P` has dimension `T`, so

```math
H_0t_P
```

is dimensionless. The prefactor

```math
\left(\frac{g}{6\pi\Omega_\Lambda}\right)^{1/2}
```

is also dimensionless. Thus `beta_0^(Lambda)` is dimensionless, as required.

## 4. Associated Length Scale

With

```math
\ell_P=\sqrt{\frac{\hbar G}{c^3}},
```

the effective GUP length associated with this conditional identification is

```math
\ell_\Lambda
=
\sqrt{\beta_0^{(\Lambda)}}\,\ell_P.
```

Using the closed form above,

```math
\boxed{
\ell_\Lambda
=
\left(\frac{g}{6\pi\Omega_\Lambda}\right)^{1/4}
\sqrt{\ell_P\frac{c}{H_0}}.
}
```

Thus the selected length is the geometric mean of the Planck length and the
Hubble radius, up to the factor `(g/(6 pi Omega_Lambda))^(1/4)`.

## 5. Numerical Check

With

```math
H_0=67.4\ {\rm km\,s^{-1}\,Mpc^{-1}},
\qquad
\Omega_\Lambda=0.685,
\qquad
g=1,
```

the reproducible check gives

```text
beta_0^(Lambda) = 2.363227961266532e+60
ell_Lambda      = 2.484635557428229e-05 m
relative error between closed form and direct density inversion ~ 1.5e-16
```

The direct inversion is

```math
\beta_0^{\rm direct}
=
\left(\frac{g\rho_P}{16\pi^2\rho_\Lambda}\right)^{1/2}.
```

The test verifies

```math
\beta_0^{\rm direct}
=
\left(\frac{g}{6\pi\Omega_\Lambda}\right)^{1/2}
\frac{1}{H_0t_P}
```

up to floating-point precision.

## 6. Interpretation Boundary

This formula proves only the algebraic consequence of the conditional
identification `rho_vac = rho_Lambda` inside the selected GUP regulator model.

It does **not** prove:

- that the physical vacuum energy equals the observed dark-energy density;
- that `beta_0` is universal;
- that `beta_0 ~ 10^60` is compatible with local precision physics;
- that the cosmological constant problem is solved.

In fact, the COSMO notes indicate that a universal local `beta_0` of this size
is strongly constrained or excluded in several sectors. The safe use of this
identity is as a scale relation and no-go diagnostic.

