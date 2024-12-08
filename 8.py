# Find the Kth Smallest Element in an Array

def kth(arr, k):
    return sorted(arr)[k - 1] # if we sort array first number is smallest, second little bigger than smallest and etc. so with indexing we choose k-th number, (k - 1 because in programming count starts from 0)

print(kth([3, 2, 1, 5, 6, 4], 2))
print(kth([3, 2, 1, 5, 6, 4], 4))
print(kth([7, 10, 4, 3, 20, 15], 3))
print(kth([1, 2, 3, 4, 5], 1))
print(kth([1, 2, 3, 4, 5], 5))

# ✔