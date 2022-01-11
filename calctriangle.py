b = int(input("Input the base : "))
h = int(input("Input the height : "))

area = b*h/2

print("area = ", area)

def gcd(x, y):
    gcd = 1
    if x % y == 0:
        return y
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break
    return gcd
print("GCD of 12 & 17 =",gcd(12, 14))
print("GCD of 4 & 6 =",gcd(2, 4))
print("GCD of 336 & 360 =", gcd(900, 936))

def sum(x, y):
    sum = x + y
    if sum in range(15, 200):
        return 875
    else: 
        return sum

print(sum(10, 6))
print(sum(10, 2))
print(sum(20, 12))
print(sum(201, 250))

input("End Program.. ")