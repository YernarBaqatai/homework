a = list(map(int,input().split()))
b = list(map(int,input().split()))
'''cnt = 0
for i in a:
    for x in b:
        if i == x :
            cnt +=1
print(cnt)'''
result = list(set(a) & set(b))
print(len(result))