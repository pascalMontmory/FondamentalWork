# Exact integral-points closure target for the residual m=3 mod 4 fibers.
#
# Run with:
#   sage Math/conjecture/legendre/tools/m3mod4_residual_integral_points.sage
#
# This is not an interval search.  It asks Sage to determine the integral
# points on the certified rank-3 elliptic curve
#
#   E: y^2 = x^3 - 128*x^2 - 215865*x,
#
# then filters the points coming from the quartic
#
#   W^2 = 1845*s^4 - 128*s^2 - 117
#
# by X = 1845*s^2 and by the separated residual square equations.

E = EllipticCurve(QQ, [0, -128, 0, -215865, 0])

G1 = E(-363, 3696)
G2 = E(-195, 5460)
G3 = E(-117, 4680)
BASIS = [G1, G2, G3]
P0 = 2*G2 + G3 + E(0, 0)

TORSION_EXPECTED = {
    E(0), E(0, 0), E(533, 0), E(-405, 0),
}


def is_square_integer(n):
    n = ZZ(n)
    return n >= 0 and ZZ(n).is_square()


def square_root_integer(n):
    return ZZ(n).sqrt()


def square_x_s(point):
    if point == E(0):
        return None
    x = ZZ(point[0])
    if x % 1845 != 0:
        return None
    s2 = x // 1845
    if not is_square_integer(s2):
        return None
    return square_root_integer(s2)


def passes_common(s):
    z = ZZ(s) ** 2
    return (
        (153*z - 55) % 2 == 0
        and is_square_integer((153*z - 55) // 2)
        and (41*z + 9) % 2 == 0
        and is_square_integer((41*z + 9) // 2)
        and (45*z - 13) % 2 == 0
        and is_square_integer((45*z - 13) // 2)
        and is_square_integer(2673*z - 992)
        and is_square_integer(4617*z - 392)
    )


def passes_r4(s):
    z = ZZ(s) ** 2
    return (
        passes_common(s)
        and is_square_integer(1701*z - 908)
        and is_square_integer(7533*z + 2668)
    )


def passes_r5(s):
    z = ZZ(s) ** 2
    return (
        passes_common(s)
        and is_square_integer(3645*z - 836)
        and is_square_integer(1701*z - 1004)
    )


def integral_points_with_basis():
    try:
        return E.integral_points(mw_base=BASIS, both_signs=True)
    except TypeError:
        # Older Sage versions have a smaller signature.
        return E.integral_points()


print("curve =", E)
print("torsion =", sorted(TORSION_EXPECTED, key=str))
print("basis =", BASIS)
print("residual coset representative P0 =", P0)
assert P0[0] == QQ(10045) / 9
assert P0[1] == -QQ(849520) / 27
print("rank =", E.rank())

points = sorted(set(integral_points_with_basis()), key=lambda P: (P[0], P[1]))
print("integral point count =", len(points))

quartic_candidates = []
common_candidates = []
r4_candidates = []
r5_candidates = []

for P in points:
    s = square_x_s(P)
    if s is None:
        continue
    quartic_candidates.append((P, s))
    for ss in {s, -s}:
        if passes_common(ss):
            common_candidates.append((P, ss))
        if passes_r4(ss):
            r4_candidates.append((P, ss))
        if passes_r5(ss):
            r5_candidates.append((P, ss))

print("X=1845*s^2 candidates =", quartic_candidates)
print("common separated candidates =", common_candidates)
print("R4 candidates =", r4_candidates)
print("R5 candidates =", r5_candidates)

assert set(s for _, s in common_candidates).issubset({ZZ(-1), ZZ(1)})
assert r4_candidates == []
assert r5_candidates == []

print("CERTIFIED: residual R4 and R5 fibers are empty after boundary saturation.")
