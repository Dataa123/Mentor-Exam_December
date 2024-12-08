# Primorial of a Number

def primorial(n):
    if n == 1:
        return 1

    listn = []
    res = 1

    for i in range(1, n + 1):
        if check_prime(i):
            listn.append(i)

    #########################
    # until here we just do the same thing we did in 7.py including check_prime function
    #########################

    for i in listn:
        res *= i
    # this is final solution, just multiple of numbers

    return res

def check_prime(x):
    if x == 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

print(primorial(5))
print(primorial(10))
print(primorial(1))
print(primorial(7))
print(primorial(11))

# ✔