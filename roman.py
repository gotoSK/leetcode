# Integer to Roman

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M.
# Symbol	Value
# I	        1
# V	        5
# X	        10
# L	        50
# C	        100
# D	        500
# M	        1000

# For example:
#     2 is written as II in Roman numeral, just two ones added together.
#     12 is written as XII, which is simply X + II.
#     The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five, we subtract it making four. The same principle applies to the number nine, which is written as IX.

# There are six instances where subtraction is used:
#     I can be placed before V (5) and X (10) to make 4 and 9.
#     X can be placed before L (50) and C (100) to make 40 and 90.
#     C can be placed before D (500) and M (1000) to make 400 and 900.

# Problem
# Given an integer, convert it to a Roman numeral.

# Example 1:
# Input:
# num = 3
# Output:
# "III"
# Explanation: 3 is represented as 3 ones.

# Example 2:
# Input:
# num = 58
# Output:
# "LVIII"
# Explanation: L = 50, V = 5, III = 3.

# Example 3:
# Input:
# num = 1994
# Output:
# "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90, and IV = 4.

# Constraints:
#     1 <= num <= 3999

map_table = [
    [1, 'I'],
    [5, 'V'],
    [10, 'X'],
    [50, 'L'],
    [100, 'C'],
    [500, 'D'],
    [1000, 'M']
]

def map_to_roman(y: int, n: int, pv: int) -> str:
    r = "" # roman equivalent

    if pv == 1000: # for thousands
        i = pv
        while i <= y: # 'M' for each 1000
            r += map_table[n][1]
            i += pv
    
    elif y < map_table[n+1][0]: # for 1*pv <= values < 5*pv, where pv = placevalue/facevalue
        if y < map_table[n+1][0] - pv: # for values 1*pv, 2*pv, 3*pv
            i = map_table[n][0]
            while i <= y:
                r += map_table[n][1]
                i += pv
        else: # for value 4*pv
            r = map_table[n][1] + map_table[n+1][1]

    elif y == map_table[n+2][0] - pv: # for value 9*pv
        r = map_table[n][1] + map_table[n+2][1]

    else: # for 5*pv <= values < 9*pv
        r = map_table[n+1][1]
        i = map_table[n+1][0]
        while i < y:
            r += map_table[n][1]
            i += pv

    return r

def int_to_roman(num: int) -> str:
    r = "" # roman equivalent
    i = 1000 # starting from highest place value
    n = 6 # index in the map table

    while i >= 1:
        y = num // i # extracting the face value
        if y != 0: # only compute if face value not 0, since no value for 0 in Roman
            y *= i # place value
            num -= y # updating the number by removing the current face value from it, for next operation
            r += map_to_roman(y, n, i) # keep adding the roman values for each face value
        i //= 10 # moving to next face value right to left
        n -= 2 # update the pointer to map_table

    return r

if __name__ == "__main__":
    num = input()
    print(int_to_roman(int(num)))