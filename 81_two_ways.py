from utils import read_matrix, AStar

matrix = read_matrix("p081_matrix.txt")
W = 1 + max([x for x,y in matrix])
H = 1 + max([y for x,y in matrix])

start = (0,0)

goal = (W-1,H-1)
avg = sum(matrix.values()) / (W*H)

class M(AStar):

    def heuristic_cost_estimate(self, current, goal):
        x1, y1 = current
        x2, y2 = goal
        return abs(x2-x1) + abs(y2-y1)

    def distance_between(self, n1, n2):
        return matrix[n2]

    def neighbors(self, node):
        x,y = node
        if x < W-1:
            yield (x+1, y)
        if y < H-1:
            yield (x, y+1)

print sum([matrix[p] for p in M().astar(start, goal)])


