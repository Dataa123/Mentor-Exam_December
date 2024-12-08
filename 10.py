# Sum Fractions Using GCD and LCM

def frac(frac1, frac2):
    l = lcm(frac1[1], frac2[1]) # find lcm of denominators

    if l == frac1[1] and l == frac2[1]:
        return ((frac1[0] + frac2[0]), l) # we check this because if denominators are same we just have to add numerators
    
    return (frac1[0] * (l // frac1[1]) + frac2[0] * (l // frac2[1]), l) # we just use very basic second grade addition of fractions

def gcd(a, b):
    x = 0
    while a % b > 0:
        x = a % b
        a = b
        b = x
    return x
# just gcd function

def lcm(a, b):
    if gcd(a, b) == 0:
        return a
    return abs(a * b) // gcd(a, b)
# just lcm function

print(frac((1, 2), (1, 3))) # 5/6
print(frac((1, 4), (1, 4))) # 1/2
print(frac((2, 5), (1, 5))) # 3/5
print(frac((3, 4), (5, 6))) # 19/12
print(frac((5, 12), (7, 15))) # 53/60

# ✔