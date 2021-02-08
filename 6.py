# Ans - > y > x + i*(x*0.1)
x = int (input())
y = int (input())
i = 0
while y >= x + i*(x*0.1):
    i +=1
print (i-1)