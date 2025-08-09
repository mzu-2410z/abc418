import sys
sys.setrecursionlimit(10**7)
MOD = 998244353

N, Q = map(int, sys.stdin.readline().split())
a = [-1] * N

# We'll keep track of a[i], and after each update:
# 1. Check feasibility:
#   - a[i] >= 0 and a[i] <= i+1
#   - Non-decreasing
#   - a[i] - a[i-1] in {0,1}
# 2. Compute number of sequences satisfying constraints using DP

def feasible():
    prev_val = 0
    prev_idx = -1
    for i in range(N):
        if a[i] == -1:
            continue
        # Check bounds
        if a[i] < 0 or a[i] > i+1:
            return False
        if prev_idx != -1:
            # Check non-decreasing between known points
            if a[i] < a[prev_idx]:
                return False
            # Check increment at most 1 per step (no two coffees consecutive)
            if (a[i] - a[prev_idx]) > (i - prev_idx):
                return False
        prev_idx = i
    return True


def ways():
    # dp_tea[c], dp_coffee[c] at previous step
    dp_tea = [0] * (N+1)
    dp_coffee = [0] * (N+1)
    dp_tea[0] = 1

    for i in range(N):
        new_dp_tea = [0] * (N+1)
        new_dp_coffee = [0] * (N+1)

        # If a[i] != -1, only coffee_count = a[i] is allowed, else all coffee_count possible
        allowed = [False] * (N+1)
        if a[i] == -1:
            for c in range(N+1):
                allowed[c] = True
        else:
            if 0 <= a[i] <= N:
                allowed[a[i]] = True
            else:
                return 0

        for c in range(N+1):
            if not allowed[c]:
                continue
            # Transition to tea at i:
            val = 0
            if c <= N:
                val += dp_tea[c]
                val += dp_coffee[c]
                val %= MOD
            new_dp_tea[c] = val

            # Transition to coffee at i (only if c > 0, and prev ended with tea)
            if c > 0 and allowed[c]:
                new_dp_coffee[c] = dp_tea[c-1] % MOD

        dp_tea = new_dp_tea
        dp_coffee = new_dp_coffee

    total = 0
    for c in range(N+1):
        # Final coffee count must satisfy a[N-1] if specified
        if a[N-1] != -1 and c != a[N-1]:
            continue
        total += dp_tea[c]
        total += dp_coffee[c]
        total %= MOD
    return total

for _ in range(Q):
    X, Y = map(int, sys.stdin.readline().split())
    X -= 1
    a[X] = Y
    if feasible():
        print(ways())
    else:
        print(0)
