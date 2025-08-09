import sys
import math
import itertools

input = sys.stdin.readline

def slope(p, q):
    dx = q[0] - p[0]
    dy = q[1] - p[1]
    if dx == 0:
        return ('inf', 0)
    g = math.gcd(dx, dy)
    return (dy // g, dx // g)

def parallel(p, q, r, s):
    return slope(p, q) == slope(r, s)

N = int(input())
pts = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for quad in itertools.combinations(range(N), 4):
    points = [pts[i] for i in quad]
    found = False
    # Try all cyclic permutations (fix first point, permute the rest)
    for perm in itertools.permutations(points):
        A, B, C, D = perm
        # Check opposite sides: AB//CD and BC//DA
        ab_cd = parallel(A, B, C, D)
        bc_da = parallel(B, C, D, A)
        if ab_cd ^ bc_da:  # exactly one pair parallel
            found = True
            break
    if found:
        ans += 1

print(ans)
