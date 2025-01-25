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
    # immediately invalidate if the length of the strings are different
    if len(s) != len(t):
        return False

    # create hash-map for both the strings
    s_map = {}
    t_map = {}

    # and fill with values as frequency of the character's occurance in the string
    for i in range(len(s)):
        
        #obtain the ith character from the string
        s_char = s[i]
        t_char = t[i]

        # update the value if exists else create and initialize
        # for 's'
        try:
            s_map[s_char] += 1
        except:
            s_map[s_char] = 1
        # for 't'
        try:
            t_map[t_char] += 1
        except:
            t_map[t_char] = 1

    # for i in range(len(s)):

    # for x in s:
    #     if x in t:
    #         t = t.replace(x, '', 1)
    #     else:
    #         return False
    # return True

if __name__ == "__main__":
    s = input()
    t = input()
    print(isAnagram(s, t))