# Generate Pascal’s Triangle Up to a Given Row

def pascal(num):
    res = [[1], [1, 1]]
    # prevalues for less complicity
    
    for i in range(2, num):
        x = [] # temporary list
        for i in range(len(res[-1]) - 1): # for loop on previous list
            x.append(res[-1][i] + res[-1][i+1]) # sum of two numbers
        res.append([1] + x + [1]) # append temporary list in res surrounded by ones

    return res[:num]

print(pascal(1)) # [[1]]
print(pascal(2)) # [[1], [1, 1]]
print(pascal(3)) # [[1], [1, 1], [1, 2, 1]]
print(pascal(4)) # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
print(pascal(5)) # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
print(pascal(6)) # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
print(pascal(0)) # []

# [[1]]        
# [[1], [1, 1]]
# [[1], [1, 1], [1, 1, 1]]
# [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1]]
# []