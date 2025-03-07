import numpy as np

# 1 Prime Clusters
def checkPrime(x): 
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def containsPrimes(arr):
    array = []
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if checkPrime(arr[i, j]) == True:
                array.append(arr[i].tolist())
                break    
    print(array)
    return
            
arr = np.array([[2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 13]])
containsPrimes(arr)



# 2 Let's Play Checkers!
# 2.1 
def checkerboard():
    cb = np.zeros((8, 8))
    return cb

cb = checkerboard()
print(cb)



# 2.2
def checkerboardOdd(cb):
    for i in range(cb.shape[0]):
            if i % 2 == 0:
                for j in range(cb.shape[1]):
                    if j % 2 == 0:
                        cb[i, j] = 1
    return cb

print(checkerboardOdd(cb))



# 2.3
def checkerboardEven(cb):
    for i in range(cb.shape[0]):
            if i % 2 != 0:
                for j in range(cb.shape[1]):
                    if j % 2 != 0:
                        cb[i, j] = 1
    return cb

print(checkerboardEven(cb))



# 2.4
def reverse_checkerboard(cb):
    for i in range(cb.shape[0]):
            if i % 2 != 0:
                for j in range(cb.shape[1]):
                    if j % 2 == 0:
                        cb[i, j] = 1
    for i in range(cb.shape[0]):
            if i % 2 == 0:
                for j in range(cb.shape[1]):
                    if j % 2 != 0:
                        cb[i, j] = 1
    return cb

cb1 = checkerboard()
print(reverse_checkerboard(cb1))



# 3 The Expanding Universe
def expansion(universe, x):
    space = " "
    expanded_universe = []
    for string in universe:
         string_spaced = ""
         for char in string:
             string_spaced += char + (space * x)
         new_string = string_spaced[:-1*x]
         expanded_universe.append(new_string)
    print(expanded_universe)

universe = np.array(["galaxy", "clusters"])
expansion(universe, 2)



# 4 Second-Dimmest Star
def secondDimmest(stars):
    second_dimmest = []
    for row in stars:
         row.sort()
         second_dimmest.append(row[1])
    print(second_dimmest)

np.random.seed(123)
stars = np.random.randint(500, 2000, (5, 5))
# print(stars)
secondDimmest(stars)