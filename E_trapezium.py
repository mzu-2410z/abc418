import sys
import math
from collections import defaultdict

def slope(p1, p2):
    """
    Calculates the slope of the line between two points and returns it as a
    simplified fraction in a canonical form.
    """
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]

    if dx == 0:
        return ('inf', 0)
    
    common_divisor = math.gcd(abs(dx), abs(dy))
    dy //= common_divisor
    dx //= common_divisor
    
    # Ensure a canonical form where dx is always positive
    if dx < 0:
        dy *= -1
        dx *= -1
        
    return (dy, dx)

def solve():
    input = sys.stdin.readline
    N = int(input())
    pts = [tuple(map(int, input().split())) for _ in range(N)]

    # Step 1: Count pairs of parallel line segments
    slopes_count = defaultdict(int)
    for i in range(N):
        for j in range(i + 1, N):
            s = slope(pts[i], pts[j])
            slopes_count[s] += 1
    
    total_parallel_pairs = 0
    for count in slopes_count.values():
        if count >= 2:
            total_parallel_pairs += count * (count - 1) // 2

    # Step 2: Count parallelograms using midpoints
    midpoints_count = defaultdict(int)
    for i in range(N):
        for j in range(i + 1, N):
            # Use sums to represent midpoints and avoid floating-point issues
            mid_x = pts[i][0] + pts[j][0]
            mid_y = pts[i][1] + pts[j][1]
            midpoints_count[(mid_x, mid_y)] += 1
    
    total_parallelograms = 0
    for count in midpoints_count.values():
        if count >= 2:
            total_parallelograms += count * (count - 1) // 2
    
    # Step 3: Calculate the final answer by correcting for double-counting
    ans = total_parallel_pairs - total_parallelograms
    print(ans)

solve()