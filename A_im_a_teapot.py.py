import sys

_ = sys.stdin.readline()  # Read N (not used)
S = sys.stdin.readline().strip()

print("Yes" if S.endswith("tea") else "No")
