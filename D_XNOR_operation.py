import sys
input = sys.stdin.readline

def main():
    N = int(input())
    T = input().strip()

    cnt = [0, 0]  
    parity = 0
    cnt[0] = 1 
    ans = 0
    for ch in T:
        if ch == '0':
            parity ^= 1
        ans += cnt[parity]
        cnt[parity] += 1

    print(ans)

if __name__ == "__main__":
    main()
