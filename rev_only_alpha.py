# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.
# Example 1:

# Input: "ab-cd"
# Output: "dc-ba"
# Example 2:

# Input: "a-bC-dEf=ghlj!!"
# Output: "j-lh-gfE=dCba!!"

def rev_only_letter(s: str) -> str:
    result = []
    i_rev = len(s)
    for char in s:
        if not char.isalpha():
            result.append(char)
        else:
            i_rev -= 1
            while not s[i_rev].isalpha():
                i_rev -= 1
            result.append(s[i_rev])
    return ''.join(result)

if __name__ == "__main__":
    line = input()
    print(rev_only_letter(line))