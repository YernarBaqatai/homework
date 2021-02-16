asd = list(map(int, input().split()))
maxi=10
for x in asd:
    if x>0:
        if x < maxi:
            maxi = x
print(maxi)

#partial 