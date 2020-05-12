s = set([1,2,3])
t = set([3,4,5])

U = s.union(t) # set([1,2,3,4,5])
I = s.intersection(t) # set([3])
D = s.difference(t) # set([1,2])

print('Union: ',U)
print('Intersección: ',I)
print('Diferencia: ',D)
