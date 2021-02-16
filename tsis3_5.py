asd = list(map(int,input().split()))
n = int(input())
bir = asd[n:]
eki = asd[:n]
jauap = bir + eki 

for x in jauap:
    print(x, end=" ")
#partial 