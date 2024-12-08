#  Find All Prime Numbers in a Given Range

def find_prime(start, end):
    listn = []

    for i in range(start, end + 1): # made for loop to go in range from start to including end
        if check_prime(i): # check prime
            listn.append(i) # append prime number in result list

    return listn

def check_prime(x): # created function to check prime numbers
    if x == 1: # 1 is not a prime number so we return False
        return False
    for i in range(2, int(x ** 0.5) + 1): # used one of the many ways to see if number is prime or not
        if x % i == 0:
            return False
    return True

print(find_prime(10, 20))
print(find_prime(1, 10))
print(find_prime(20, 30))
print(find_prime(24, 25))
print(find_prime(1, 1))

# ✔