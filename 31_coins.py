# -*- coding: utf-8 -*-
import time
cointypes = [1, 2, 5 , 10 , 20, 50, 100 , 200]

cache={}
def ways_to_get(x):
    if x in cache:
        return cache[x]
    if x == 0:
		return []
    if x == 1:
        return set([(1,)])
    if x == 2:
        return set([(2,), (1,1)])
    w = set([(x,)]) if x in cointypes else set([])
    for picked in filter(lambda c:c<x, cointypes):
        for t in ways_to_get(x - picked):
            l = list(t) + [picked]
            l.sort()
            w.add(tuple(l))
    cache[x] = w
    return w

print len(ways_to_get(200)) #73682, takes around 42s


                     
                         
