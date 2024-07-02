def add(x,y):
    return x+y

def isEven(x):
    if x % 2 == 0:
        print(f"{x} is even :)")
    else:
        print(f"{x} is odd:/")

def maxOf3(x,y,z):
    return max(x,y,z)

def fact(x):
    fact = 1
    for i in range(1,x+1):
        fact = i*fact
    return fact

def rev(x):
    return x[::-1]

print(add(1,2))
isEven(3.4)
print(maxOf3(1,2,3))
print(fact(23))
print(rev([1,2,3,4,5]))