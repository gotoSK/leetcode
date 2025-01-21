# Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2³¹, 2³¹ - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

# Constraints:
# -2³¹ <= x <= 2³¹ - 1

def valid_range(y: int) -> bool:
    return False if y<-2**31 or y>2**31-1 else True

def reverse_integer(x: int, n: int) -> int:
    y = 0 # store the reversed integer
    i = int('1' + '0'*(n-1)) # 10 ^ (total digits in the number)
    while i >= 1:
        temp = int(x/10)
        y += (round((x/10 - temp), 1) * 10) * i # extracting the last digit and multiplying it my its place value
        y = int(y)
        x = temp # updating the initial no. such that the last digit is removed, for next iteration to extract the new last digit
        i /= 10
    return y if valid_range(y) else 0


if __name__ == "__main__":
    x = input()
    print(reverse_integer(
            int(x),
            len(x) if int(x)>0 else len(x)-1 # total no. of digits
        )
    )