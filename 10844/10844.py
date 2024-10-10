N = int(input())

arr = [1]*10


for i in range(N-1):
    temp = [0]*10
    for j in range(10):
        if(j==0):
            temp[0]= arr[1]
        elif(j==9):
            temp[9]= arr[8]
        else:
            temp[j] = arr[j-1] + arr[j+1]
    arr = temp

result = 0
for i in range(1,10):
    result += arr[i]

print(result%1000000000)