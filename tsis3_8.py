a = list(map(int,input().split()))
b = list(map(int,input().split()))
result = set(a) & set(b)
for x in result:
    print(x,end=" ")