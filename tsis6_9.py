a = int(input())
i = 1
cnt = 0
while a >= i:
    if a % i == 0:
        cnt += 1
    i +=1
if cnt==2:
    print("YES")
else:
    print("NO")