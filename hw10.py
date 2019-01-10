# imports {{{1
from __future__ import division
from random import randrange
from sys import maxint
#---------------------------------------------------------------------------}}}1

def MSP_bad(A): # {{{
  sum_key = lambda x: x[2]
  S = [ (i, j, sum(A[i:j])) for i in range(len(A)) for j in range(i,len(A)+1) ]
  max_sum_triple = max(S, key=sum_key)

  return max_sum_triple
#----------------------------------------------------------------------------}}}
def rand_MSP(n, max_delta): # {{{
  max_delta_0 = max_delta // 2

  return [ randrange(-max_delta_0, max_delta_0+1) for _ in range(n) ]
#----------------------------------------------------------------------------}}}

def MSP(A, low, high):	
  if(len(A) == 0):
    return (0, 0, 0)
  if(len(A) == 1):
    return(low, high, max(0, A[0]))
  m = (low + high) / 2
  lmax = 0
  v_sum = 0
  i = int(m)
  while(i >= low):
    v_sum += A[i]
    if (v_sum > lmax):
      lmax = v_sum
    i += -1
  i = int(m + 1)
  rmax = 0
  l_sum = 0
  while(i < high):
    l_sum += A[i]
    if(l_sum > rmax):
      rmax = l_sum
    i += 1
  return (low, high, max(max(MSP(A, low, m)[2], MSP(A, m + 1, high)[2]), lmax + rmax))
#----------------------------------------------------------------------------}}}


# run this to test out your algorithm
for _ in range(10**3):
  A = rand_MSP(randrange(1,51), randrange(101))
  B = MSP_bad(A)
  G = MSP(A, 0, len(A))
  if not ( sum(A[G[0]:G[1]]) == G[2] == B[2] ):
    print "whoops"
    print A
    print B
    print G
    break