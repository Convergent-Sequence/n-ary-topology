""""
The following packages are necessary to compute some sets operations 
"""
from itertools import chain, combinations, product

"""
Here we define the basic sets operations
for n-ary sets
"""

def power_set(s:set):
    return list(set(x) for x in chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

def cartesian_product(*sets):
  return list(list(x) for x in product(*sets))

def n_ary_complement(*sets,ntuple):
  return [s-ntuple[i] for i,s in enumerate(sets)]

def n_ary_union(tuple1,tuple2):
  union = [tuple1[i].union(tuple2[i]) for i in range(len(tuple1))]
  return union

def n_ary_intersection(tuple1,tuple2):
  intersection = [tuple1[i].intersection(tuple2[i]) for i in range(len(tuple1))]
  return intersection

def is_contained(tuple1, tuple2):
    return all(p1.issubset(p2) for p1, p2 in zip(tuple1, tuple2))

def multiple_intersection(tuples):
    components = list(zip(*tuples))  # Transpose the pairs
    intersections = [set.intersection(*map(set, comp)) for comp in components]
    return intersections

def multiple_union(tuples):
    components = list(zip(*tuples))  # Transpose the pairs
    intersections = [set.union(*map(set, comp)) for comp in components]
    return intersections

"""
We can now verify whether a given collection is an n-ary topology
In order to do so, we create functions to verify closeness under unions and intersections
"""

def verify_intersection(M):
  for i in range(len(M)-1):
    for j in range(i+1,len(M)):
      if n_ary_intersection(M[i],M[j]) not in M :
        return False # Exit the loop if an intersection doesn't belong
  return True

def verify_union(M):
  for i in range(len(M)-1):
    for j in range(i+1,len(M)):
      if n_ary_union(M[i],M[j]) not in M:
        return False
  return True

def is_n_ary_topology(*sets,M):
  return verify_intersection(M) and verify_union(M) and [set() for _ in range(len(sets))] in M and list(sets) in M

"""
Now we define a function to create n-ary topologies from a given collection
We first verify that the given collection is adecuate
"""

def is_delta_type(delta, *sets):
    components = [[inner_list[i] for inner_list in delta]for i in range(len(delta[0]))]
    for element in cartesian_product(*map(set, sets)):
      for i in range(len(element)):
        if not any({element[i]}.issubset(s) for s in components[i]):
          return False
    return True

def extend_intersections(s):
  for i in range(len(s)-1):
    for j in range(i+1,len(s)):
      if n_ary_intersection(s[i],s[j]) not in s:
        s.append(n_ary_intersection(s[i],s[j]))
  return s

def extend_unions(s):
  for i in range(len(s)-1):
    for j in range(i+1,len(s)):
      if n_ary_union(s[i],s[j]) not in s:
        s.append(n_ary_union(s[i],s[j]))
  return s

def generate_n_ary_topology(*sets,delta):
  if is_delta_type(delta,*sets):
    while verify_intersection(delta) != True:
      extend_intersections(delta)
    while verify_union(delta) != True:
      extend_unions(delta)
    if [set() for _ in range(len(delta[0]))] not in delta:
      delta.append([set() for _ in range(len(delta[0]))])
    return delta
  else:
    return "Not possible"
  
"""
Now we obtain the n-ary closure and interior of n-ary sets
"""

def interior(M,nelement):
  tuples = []
  for element in M:
    if is_contained(element,nelement):
      tuples.append(element)
  return multiple_union(tuples)

def closure(*sets,M,nelement):
  tuples = []
  power_sets = list(map(power_set,sets))
  for element in cartesian_product(*power_sets):
    if is_contained(nelement,element) and n_ary_complement(*sets,ntuple=element) in M:
      tuples.append(element)
  return multiple_intersection(tuples)

"""
Until here everything worked correctly fo n ary spaces (with n geq 2 of course).
So now we need code for n = 1, i.e. usual topological spaces.
"""


def verify_unions_usual(B):
  for i in range(len(B)-1):
    for j in range(i+1,len(B)):
      if B[i].union(B[j]) not in B:
        return False
  return True

def extend_unions_usual(B):
  for i in range(len(B)-1):
    for j in range(i+1,len(B)):
      if B[i].union(B[j]) not in B:
        B.append(B[i].union(B[j]))
  return B

def verify_intersections_usual(B):
  for i in range(len(B)-1):
    for j in range(i+1,len(B)):
      if B[i].intersection(B[j]) not in B:
        return False
  return True

def extend_intersections_usual(B):
  for i in range(len(B)-1):
    for j in range(i+1,len(B)):
      if B[i].intersection(B[j]) not in B:
        B.append(B[i].intersection(B[j]))
  return B

def sub_to_tau(subbasis):
    while verify_intersections_usual(subbasis) != True: 
      extend_intersections_usual(subbasis) 
    while verify_unions_usual(subbasis) != True:
      extend_unions_usual(subbasis)
    if set() not in subbasis:
      subbasis.append(set())
    return subbasis

def generate_tau(basis):
    while verify_unions_usual(basis) != True:
      extend_unions_usual(basis)
    if set() not in basis:
      basis.append(set())
    return basis

def usual_closure(z, tau, s):
    closure = []
    for elementp in power_set(z):
        if s.issubset(elementp) and (z - elementp) in tau:
            closure.append(elementp)
    if not closure:
        return set()  # This point shouldnt be reached, yet we implement it
    return set.intersection(*closure)

def usual_interior(z, tau, s):
    interior = []
    for elementp in power_set(z):
        if elementp.issubset(s) and elementp in tau:
            interior.append(elementp)
    if not interior:
        return set()  # Return the empty set if interior is empty
    return set.union(*interior)

def is_usual_topology(z,tau):
  return verify_intersections_usual(tau) and verify_unions_usual(tau) and set() in tau and z in tau
