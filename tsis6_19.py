def test(a):
    def test1(b):
        nonlocal a
        a +=1
        return a+b
    return test1
n = int(input())
func = test(n)
print(func(n))