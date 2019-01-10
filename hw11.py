# imports {{{1
from __future__ import division
from random import randrange
# ---------------------------------------------------------------------------}}}1


def rand_perm(size):  # {{{
    p = []
    while len(p) < size:
        r = randrange(size)
        if r not in p:
            p.append(r)
    return p
# ----------------------------------------------------------------------------}}}


def rand_cards(n, max_value=2):  # {{{
    base = []
    for value in range(1, max_value):
        max_reps = n//2 - len(base) - 1 + (n % 2)
        if max_reps == 0:
            break
        base += [value]*randrange(1, max_reps+1)
    base += [max_value]*(n-len(base))

    perm = rand_perm(n)
    base_perm = [base[perm[i]] for i in range(n)]

    return base_perm
# ----------------------------------------------------------------------------}}}


def all_same(items):
    return all(x == items[0] for x in items)


def credit_card(L):  # {{{
    # Detect whether there is an element of L that occurs more than half the time.
    # You should return the element if there is one as well as a count of the
    # number of times it occurs in L. If there is no such element, return None, 0.
    m = len(L)
    if m == 1:
        return L[0], 1
    elif m == 2:
        if L[0] == L[1]:
            return L[0], 2
        else:
            return None, -1

    set_1 = L[:len(L)//2]
    set_2 = L[len(L)//2:]

    result1, a1 = credit_card(set_1)
    if(a1 != -1):
        if result1 in L:
            return result1, a1

    result2, a2 = credit_card(set_2)
    if(a2 != -1):
        if result2 in L:
            return result2, a2

    return None, -1
# ----------------------------------------------------------------------------}}}


# test your credit_card() solution using something like this
for i in xrange(10**4):
    v = randrange(2, 30)
    s = randrange(2*v-1, v**2)
    R = rand_cards(s, v)
    A, count = credit_card(R)
    if A != v:
        print "whoops"
        print R
        print A
        print v
        print "loop: " + str(i)
        break
