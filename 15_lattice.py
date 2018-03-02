
paths={}

def n_paths(x,y):
    if (x,y) in paths:
         return paths[x,y]
    if x == 0:
        return 1
    if y == 0:
        return 1
    p = n_paths(x-1,y) + n_paths(x, y-1)
    paths[x,y] = p
    return p

print n_paths(20,20)
