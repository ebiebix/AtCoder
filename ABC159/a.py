n,m = map(int,input().split())
import itertools
def permutations_count(n,r):
    return len(list(itertools.combinations(range(n), r)))
print(permutations_count(int(n),2)+permutations_count(int(m),2))