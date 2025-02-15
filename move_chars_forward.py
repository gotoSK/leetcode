# each char in string moved x step forward. eg.: hacker -> erhack

inp = input("Enter a string: ")

# other necessities
steps = 2
str_len = len(inp)

# Processing
temp = [None] * str_len
for i in range(str_len):
    temp[(i + steps) % str_len] = inp[i]

# Convert list back to a string
result = ''.join(temp)

# Output
print("Output:", result)
