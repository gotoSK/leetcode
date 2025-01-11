# Valid Parentheses


# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.

 


# Example 1:


# Input: s = "()"

# Output: valid


# Example 2:


# Input: s = "()[]{}"

# Output: valid


# Example 3:


# Input: s = "(]"

# Output: invalid


# Example 4:


# Input: s = "([)]"

# Output: invalid


# Example 5:


# Input: s = "{[]}"

# Output: valid


# Constraints:

#     1 <= s.length <= 104
#     s consists of parentheses only '()[]{}'

open_brackets = ['(', '[', '{']
stack = []

def invert(bracket):
    if bracket == '(':
        return ')'
    if bracket == '{':
        return '}'
    if bracket == '[':
        return ']'

def valid_par(s: str) -> bool:
    for x in s:
        if x in open_brackets:
            stack.append(x)
        else:
            if stack and x is invert(stack[len(stack)-1]):
                stack.pop()
            else:
                return False
    if not stack:
        return True
    return False
    
if __name__ == "__main__":
    line = input()
    if valid_par(line):
        print("Valid")
    else:
        print("Invalid")