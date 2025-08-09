import sys
import math
from collections import defaultdict

def slope(p1, p2):
    """
    Calculates the slope of the line between two points and returns it as a
    simplified fraction in a canonical form.
    """
    # ... (rest of the function is the same)
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    
    if dx == 0:
        return ('inf', 0)
    
    common_divisor = math.gcd(abs(dx), abs(dy))
    dy //= common_divisor
    dx //= common_divisor
    
    if dx < 0:
        dy *= -1
        dx *= -1
        
    return (dy, dx)

def solve():
    try:
        input = sys.stdin.readline
        N_str = input().strip()
        if not N_str:
            raise ValueError("Input for N is empty.")
        N = int(N_str)
        
        pts = []
        for _ in range(N):
            line = input().strip()
            if not line:
                raise ValueError(f"Input for point {len(pts) + 1} is empty.")
            coords = tuple(map(int, line.split()))
            if len(coords) < 2:
                raise ValueError(f"Point {len(pts) + 1} does not have two coordinates.")
            pts.append(coords)

        # ... (rest of the solve function is the same)
        slopes_count = defaultdict(int)
        for i in range(N):
            for j in range(i + 1, N):
                s = slope(pts[i], pts[j])
                slopes_count[s] += 1
        
        total_parallel_pairs = 0
        for count in slopes_count.values():
            if count >= 2:
                total_parallel_pairs += count * (count - 1) // 2
    
        midpoints_count = defaultdict(int)
        for i in range(N):
            for j in range(i + 1, N):
                mid_x = pts[i][0] + pts[j][0]
                mid_y = pts[i][1] + pts[j][1]
                midpoints_count[(mid_x, mid_y)] += 1
        
        total_parallelograms = 0
        for count in midpoints_count.values():
            if count >= 2:
                total_parallelograms += count * (count - 1) // 2
        
        ans = total_parallel_pairs - total_parallelograms
        print(ans)
        
    except (IOError, ValueError) as e:
        print(f"An error occurred: {e}", file=sys.stderr)

solve()