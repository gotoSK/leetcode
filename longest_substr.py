# Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input:
# s = "abcabcbb"
# Output:
# 3
# Explanation:
# The answer is "abc", with the length of 3.

# Example 2:
# Input:
# s = "bbbbb"
# Output:
# 1
# Explanation:
# The answer is "b", with the length of 1.

# Example 3:
# Input:
# s = "pwwkew"
# Output:
# 3
# Explanation:
# The answer is "wke", with the length of 3.


def length_of_longest_substring(s: str) -> str:
    max_count = 0 # length of longest substring

    for i in range(0, len(s)):
        ss = [] # stores any substring
        j = i

        while not s[j] in ss: # loop until the character dosen't match any of previous characters in the substring
            ss.append(s[j]) # append char in the substr
            if j+1 <= len(s)-1: # increment iteration counter until the last element in the string
                j += 1
            else:
                break
        
        max_count = len(ss) if len(ss) > max_count else max_count # update length of longest substring if the new length is greater

    return max_count

if __name__ == "__main__":
    line = input()
    print(length_of_longest_substring(line))