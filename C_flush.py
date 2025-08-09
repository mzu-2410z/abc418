import sys
import bisect

input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    Bs = [int(input().strip()) for _ in range(Q)]

    A.sort()
    pref = [0] * (N + 1)
    for i in range(N):
        pref[i+1] = pref[i] + A[i]

    total = pref[N]
    maxA = A[-1]

    out_lines = []
    for B in Bs:
        if maxA < B:
            out_lines.append("-1")
            continue

        k = bisect.bisect_right(A, B-1)
        sum_le = pref[k]
        cnt_gt = N - k
        max_prevent = sum_le + cnt_gt * (B - 1)
        ans = max(B, max_prevent + 1)
        out_lines.append(str(ans))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
