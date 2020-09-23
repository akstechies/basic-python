#lambda

res = lambda a : a + 10

print(res(5))

mul = lambda a,b : a * b

print(mul(10,2))

add = lambda a,b,c : a+b+c
print(add(5,10,20))

print('----------------------------')

def myFun(n):
    return lambda a : a + n

adder = myFun(5)
add20 = myFun(10)

print(adder(10))
print(add20(20))