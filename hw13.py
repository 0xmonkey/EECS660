# imports {{{1
from __future__ import division
# ---------------------------------------------------------------------------}}}1


def modified_rod_cut(P, n):  # {{{
    """
    - P is a table of prices. P[0] = 0, and P[k] = price for a rod of length k,
      where k > 0.
    - n is the size of the rod to cut. By assumption n < len(P), so P[n] is
      defined.
    - You should return a pair C, R. C is an array holding the sizes of the pieces
      you will cut the rod into, and R is the revenue that is associated with
      these cuts.
    """
    M = [([], -1) for x in range(0, n+1)]
    for k in range(1, n+1):
        max_rev = P[k]
        max_cut = [k]
        for l in range(1, k-1):
            prev_cut, prev_rev = M[k-l]
            if (prev_rev + P[l] - len(prev_cut)) > max_rev:
                max_rev = prev_rev + P[l] - len(prev_cut)
                max_cut = prev_cut + [l]
        M[k] = max_cut, max_rev
    return M[n]
# ----------------------------------------------------------------------------}}}


P = [0, 1, 5, 8, 9, 10, 17, 17, 20]
a, b = modified_rod_cut(P, 8)
print a
print b
