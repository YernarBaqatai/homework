s=input()
cnt = cnt1 = 0
for i in s:
    if(i.islower()):
        cnt +=1
    else:
        cnt1 +=1
print(cnt,cnt1)