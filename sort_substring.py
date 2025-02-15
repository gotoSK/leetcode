# given string S and two integers N, M - sort the characters inclusively between N and M indicies in descending order

alphabets = 'abcdefghijklmnopqrstuvwxyz'
alphabets_reversed = alphabets[::-1]

s = list(input("String: "))
n = int(input("N = "))
m = int(input("M = "))

def swap(a, b):
    temp = s[a]
    s[a] = s[b]
    s[b] = temp

for alphabet in alphabets_reversed:
    for i in range(n, m+1):
        if alphabet == s[i].lower():
            swap(n, i)
            n += 1

print("Result: ", ''.join(s))
