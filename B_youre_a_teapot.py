S = input().strip()
n = len(S)

max_rate = 0.0

for i in range(n):
    for j in range(i + 3, n + 1):
        sub = S[i:j]
        if sub[0] == 't' and sub[-1] == 't':
            x = sub.count('t')
            if x >= 2:
                rate = (x - 2) / (len(sub) - 2)
                max_rate = max(max_rate, rate)

print(f"{max_rate:.17f}")
