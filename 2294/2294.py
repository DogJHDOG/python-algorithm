n, k = map(int, input().split())

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
#         1 2 3 4 5 2  3  4  5  6  3
#                         1  2  3  3
#                               1  2
coin = []
for i in range(n):
    coin.append(int(input()))
    
dp = [10001] * (k+1)
dp[0] = 0

for c in coin:
    for i in range(c,k+1):
        if dp[i]>0:
            dp[i] = min(dp[i], dp[i-c]+1)

if dp[k]==10001:
    print(-1)
else:
    print(dp[k])

