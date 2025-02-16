def break_in_half(x, n):
    m = 10**(n // 2)
    return x // m, x % m

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    if n % 2 != 0:
        n += 1

    xl, xr = break_in_half(x, n)
    yl, yr = break_in_half(y, n)

    a = karatsuba(xl, yl)
    b = karatsuba(xr, yr)
    c = karatsuba(xl + xr, yl + yr)
    d = c - a - b

    return (10**(n) * a) + (10**(n/2) * d) + b

print("Multiply numbers using Karatsuba's algorithm")
print("Enter the first number:")
x = int(input())
print("Enter the second number:")
y = int(input())
print(karatsuba(x, y))