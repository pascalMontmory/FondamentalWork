#!/usr/bin/env bash
set -euo pipefail

# Exact Mordell-Weil certificate for the residual prefix-8 elliptic curve:
#   Y^2 = X^3 - 128 X^2 - 215865 X.
#
# Requires eclib's `mwrank` in PATH.

printf '[0,-128,0,-215865,0]\n' | mwrank -q -v 1 -o
