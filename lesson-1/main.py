from time import time
from functools import wraps


# constants
NUM_TYPE_EVEN = 'even'
NUM_TYPE_ODD = 'odd'
NUM_TYPE_SIMPLE = 'simple'

# varible types

# String
hello = "Hello"
# show string
print(hello)
print(hello[0])
print(hello[-1])
print(hello[0:-2])

# Int
intt = 1

# Float
floatt = 12.54234234

# List
lissts = ['foo', 'bar', 3, True, [1, 2, 3]]
print(lissts)
print(lissts[0])

# Tuples
tupless = (1, 2, 'foo', 'bar', ('spamm', 'eggs', 3))
print(tupless)
print(tupless[-1])

# Sets
setss = {1, 2, 3, 4, 'foo', 'bar', False}
print(setss)

# Dictionaries
dicts = {1: 'foo', 2: 'bar', 'spamm': 'eggs', 3: {'baz': 1}}
print(dicts)
print(dicts['spamm'])


# Decoratot function
def leadTimeDecor(func):


# Function of exponentiation
def degreeUp(nums, factor=2):
    numDict = {}
    for n in nums:
        numDict[n] = n ** factor
    return numDict


print(degreeUp((1, 2, 3, 4, 5, 6, 7, 8)))


# Nums auto-filter functions
def numsFilter(nums):
    numDict = {}
    for i, n in enumerate(nums):
        if n % 2 == 0:
            key = 'ev-' + str(i)
            numDict[key] = n
        if n % 2 > 0:
            key = 'od-' + str(i)
            numDict[key] = n
        if n == 2:
            key = 'si-' + str(i)
            numDict[key] = n
        if n != 2:
            d = 2
            flag = True
            while d < n:
                if n % d == 0:
                    flag = False
                    break
                d += 1
            if flag:
                key = 'si-' + str(i)
                numDict[key] = n
    return numDict

print(numsFilter((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)))

# Nums arg-filter functions
def numsFilterArgs(nums, type=NUM_TYPE_EVEN):
    numList = []
    for n in nums:
        if (type == 'odd') and (n % 2 > 0):
            numList.append(n)
        if (type == 'even') and (n % 2 == 0):
            numList.append(n)
        if (type == 'simple'):
            if n == 2:
                numList.append(n)
            if n != 2:
                d = 2
                flag = True
                while d < n:
                    if n % d == 0:
                        flag = False
                        break
                    d += 1
                if flag:
                    numList.append(n)

    return numList

print(numsFilterArgs((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), NUM_TYPE_SIMPLE))


