
"""asd = list(map(int, input().split()))
for x in asd:
    if x%2==1:
        print(x,end=" ")
"""
#alternative
asd = list(map(int, input().split()))
bir = asd[::2]
for x in bir:
    print(x, end=" ")