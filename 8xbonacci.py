# Xbonacci Sequence

def xbonacci(x, n):
    listn = []

    for _ in range(x): # add first X numbers as 1
        listn.append(1)

    while len(listn) < n: # check length on every iteration
        listn.append(sum(listn[len(listn) - x:len(listn)])) # append sum of previous X numbers
    
    return listn[:n] # choose first n numbers


print(xbonacci(3, 10))
print(xbonacci(2, 10))
print(xbonacci(4, 6))
print(xbonacci(5, 8))
print(xbonacci(3, 1))

# ✔