##### Ch 1

## 1.1
def unique(string): #O(n^2)
    for x in string:
        if string.count(x) > 1:
            return False
    return True

def uniquedestroy(string): #O(n log n)
    lst = sorted(string)
    for idx in lst:
        if lst[idx] == lst[idx+1]:
            return False
    return True

def uniquewithdct(string):
    dct = {}
    for x in string:
        if x in dct:
            return False
        else:
            dct[x] = True
    return True

# Official Solution O(n)
def uniquechars(string):
    char_set = [False] * 256
    for x in string:
        val = ord(x)
        if char_set[val] == True:
            return False
        else:
            char_set[val] = True
    return True

## 1.2
def reverseC(string):
    return string[-2::-1] + string[-1]

# def reverseinplace(string):
#     tmp = ""


## 1.3
def removeduplicates(string):

## 1.4 Anagrams
def anagrams(string1, string2):
    # dct1 = {x: string1.count(x) for x in string1}
    dct = {}
    for x in string1:
        dct[x] = dct.get(x, 0) + 1
    for c in string2:
        # doesn't take into account string1 having char not in string2
        if c not in dct or dct[c] != string2.count(c): #Has potential to be O(n^2)
            return False
    return True

def anagrams(string1, string2):
    visited = set()
    for x in string1+string2:
        if x not in visited and string1.count(x) != string2.count(x):
            return False
        visited.add(x)
    return True

# Official, O(n log n)
def anagrams(string1, string2):
    return sorted(string1) == sorted(string2)

## 1.5
def replacespaces(string):
    lst = string.split()
    for idx in range(len(lst)):
        if not lst[idx]:
            lst[idx] = '%20'
    return "".join(lst)

## 1.6
def rotate(matrix): # Still broken
    n = len(matrix)
    matrix2 = [[]] *n
    # triangle = 0
    for row in range(1):
        for col in range(n):
            # matrix2[col].append(matrix[col][row])
            matrix2[col].append(matrix[row][col])
        # triangle += 1
        print(matrix2)
    return matrix2

def rotateinplace(matrix):
    n = len(matrix)
    for row in range(1):
        for col in range(n):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

## 1.7
def settozero(matrix):
    m, n = len(matrix), len(matrix[0])
    rows = [False]* m
    cols = [False] * n
    for i in range(m):
        for j in range(n):
            if not matrix[i][j]:
                rows[i] = True
                cols[j] = True
    for x in range(m):
        for y in range(n):
            if rows[x] or cols[y]:
                matrix[x][y] = 0


