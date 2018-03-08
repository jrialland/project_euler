
def read_matrix(filename):
    matrix={}
    y, s =0, 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line:
                for x, v in enumerate(line.split(',')):
                    matrix[x,y] = int(v)
            y +=1
    return matrix

#---------

_primes=set([2, 3, 5, 7, 521, 11, 13, 527, 17, 19, 529, 23, 943, 29, 31, 547, 37, 649, 41, 43, 557, 47, 563, 53, 569, 59, 769, 61, 577, 67, 991, 71, 73, 587, 79, 593, 83, 599, 89, 607, 97, 101, 103, 617, 107, 109, 113, 787, 629, 631, 121, 127, 641, 131, 601, 647, 137, 139, 653, 143, 823, 659, 149, 151, 667, 157, 671, 673, 163, 677, 167, 683, 517, 173, 541, 179, 181, 697, 187, 701, 191, 193, 197, 199, 713, 859, 719, 209, 211, 727, 731, 733, 223, 737, 227, 229, 743, 233, 239, 241, 979, 757, 761, 251, 253, 257, 773, 263, 269, 271, 643, 277, 281, 283, 797, 799, 913, 289, 803, 293, 809, 811, 619, 709, 307, 821, 311, 313, 827, 317, 319, 323, 829, 839, 841, 331, 337, 739, 341, 857, 347, 349, 863, 523, 353, 571, 869, 359, 691, 877, 367, 881, 883, 373, 887, 379, 383, 899, 389, 391, 907, 397, 911, 661, 401, 407, 409, 751, 929, 419, 781, 421, 937, 583, 941, 431, 433, 947, 439, 901, 953, 443, 449, 451, 967, 457, 971, 461, 463, 977, 467, 919, 983, 473, 851, 989, 479, 997, 487, 491, 493, 613, 499, 503, 509, 853])
_max_kprime = max(_primes)

def is_prime(n):
  if n in _primes: return True
  if n < _max_kprime: return False
  if n%2 == 0 or n%3 == 0 or n%5 == 0: return False
  r = int(n**0.5)
  f = 7
  while f <= r:
    if n%f == 0 or n%(f+2) == 0: return False
    f +=6
  _primes.add(n)
  return True


#---------
from abc import ABCMeta, abstractmethod
from heapq import heappush, heappop
import math

Infinite = float('inf')


class AStar:
    __metaclass__ = ABCMeta
    __slots__ = ()

    class SearchNode:
        __slots__ = ('data', 'gscore', 'fscore',
                     'closed', 'came_from', 'out_openset')

        def __init__(self, data, gscore=Infinite, fscore=Infinite):
            self.data = data
            self.gscore = gscore
            self.fscore = fscore
            self.closed = False
            self.out_openset = True
            self.came_from = None

        def __lt__(self, b):
            return self.fscore < b.fscore

    class SearchNodeDict(dict):

        def __missing__(self, k):
            v = AStar.SearchNode(k)
            self.__setitem__(k, v)
            return v

    @abstractmethod
    def heuristic_cost_estimate(self, current, goal):
        """Computes the estimated (rough) distance between a node and the goal, this method must be implemented in a subclass. The second parameter is always the goal."""
        raise NotImplementedError

    @abstractmethod
    def distance_between(self, n1, n2):
        """Gives the real distance between two adjacent nodes n1 and n2 (i.e n2 belongs to the list of n1's neighbors).
           n2 is guaranteed to belong to the list returned by the call to neighbors(n1).
           This method must be implemented in a subclass."""
        raise NotImplementedError

    @abstractmethod
    def neighbors(self, node):
        """For a given node, returns (or yields) the list of its neighbors. this method must be implemented in a subclass"""
        raise NotImplementedError

    def is_goal_reached(self, current, goal):
        """ returns true when we can consider that 'current' is the goal"""
        return current == goal

    def reconstruct_path(self, last, reversePath=False):
        def _gen():
            current = last
            while current:
                yield current.data
                current = current.came_from
        if reversePath:
            return _gen()
        else:
            return reversed(list(_gen()))

    def astar(self, start, goal, reversePath=False):
        if self.is_goal_reached(start, goal):
            return [start]
        searchNodes = AStar.SearchNodeDict()
        startNode = searchNodes[start] = AStar.SearchNode(
            start, gscore=.0, fscore=self.heuristic_cost_estimate(start, goal))
        openSet = []
        heappush(openSet, startNode)
        while openSet:
            current = heappop(openSet)
            if self.is_goal_reached(current.data, goal):
                return self.reconstruct_path(current, reversePath)
            current.out_openset = True
            current.closed = True
            for neighbor in [searchNodes[n] for n in self.neighbors(current.data)]:
                if neighbor.closed:
                    continue
                tentative_gscore = current.gscore + \
                    self.distance_between(current.data, neighbor.data)
                if tentative_gscore >= neighbor.gscore:
                    continue
                neighbor.came_from = current
                neighbor.gscore = tentative_gscore
                neighbor.fscore = tentative_gscore + \
                    self.heuristic_cost_estimate(neighbor.data, goal)
                if neighbor.out_openset:
                    neighbor.out_openset = False
                    heappush(openSet, neighbor)
        return None

