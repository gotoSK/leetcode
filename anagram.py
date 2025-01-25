# Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# Constraints:

#     1 <= s.length, t.length <= 5 * 10^4
#     s and t consist of lowercase English letters.

def isAnagram(s: str, t: str) -> bool:
    for x in s:
        if x in t:
            t = t.replace(x, '', 1)
        else:
            return False
    return True

if __name__ == "__main__":
    s = input()
    t = input()
    print(isAnagram(s, t))