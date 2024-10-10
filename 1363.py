n = int(input())
print(n)

key_num = int(input())
arr =[0]*(key_num*2)
for i in range(0,key_num):
    arr[i] = int(input())    

sorted_arr = sorted(arr,reverse=True)

last_num = 0

for i in range(1, n+1):
    temp = key_num // 2
    root = 1
    ntemp = -1  # ntemp 초기값을 -1로 설정

    while True:
        root += 1
        if sorted_arr[temp] == i or temp == 0 or temp >= key_num - 1:
            root -= 1
            break
        elif sorted_arr[temp] > i:
            temp = (temp // 2) + temp
        else:
            temp = temp // 2
        
        # ntemp와 temp가 같아지면 루프를 종료
        if ntemp == temp:
            root -= 1
            break
        # ntemp에 temp 값을 업데이트
        ntemp = temp

    last_num += root

print(last_num)
