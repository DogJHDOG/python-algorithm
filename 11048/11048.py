import sys

n ,m= map(int,sys.stdin.readline().split())


arr= [[0 for j in range(m)] for i in range(n)]
result= [[-1 for j in range(m)] for i in range(n)]
for i in range(0,n):
    data = list(map(int,sys.stdin.readline().split()))
    for j in range(0,m):
        arr[i][j] = data[j]


def solving():
    #아래, 오른쪽, 대각선 아래 방향으로만 이동 가능
    dx = [1,0,1]
    dy = [0,1,1]
    q = [[0,0]]
    result[0][0] = arr[0][0]
    while(len(q)!=0):
        x,y = q.pop(0)


        for i in range(3):
            tx = x +dx[i]
            ty = y+ dy[i]
            if tx < 0 or tx >= m or ty < 0 or ty >= n:
                continue

            if(result[ty][tx]<(arr[ty][tx]+result[y][x])):
                result[ty][tx] = arr[ty][tx] + result[y][x]
                # print("index:",ty,tx," value:",result[ty][tx])
                q.append([tx,ty])

    
solving()

print(result[n-1][m-1])
