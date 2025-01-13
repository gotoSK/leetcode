# Container With Most Water

# You are given an integer array 'height' of length n. There are n vertical lines drawn such that the two endpoints of the i-th line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Note: You may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation:
# The above vertical lines are represented by the array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

# Constraints:
#     n == height.length
#     2 <= n <= 10^5
#     0 <= height[i] <= 10^4


def maxArea(height: list, n: int) -> int:
    left = 0 # leftmost side of the container
    right = n-1 # rightmost side of the container
    area = 0

    for high in range(max(height)+1):
        # move the left side of container towards right until it doesn't overflow
        for i in range(left, n):
            if height[i] < high:
                left += 1
            else:
                break
        
        # move the right side of container towards left until it doesn't overflow
        for i in range(right, -1, -1):
            if height[i] < high:
                right -= 1
            else:
                break
        
        # update the area if the new area is larger
        area = (right-left) * high if (right-left) * high > area else area
        # print(left, right, high, area)

    return area

# optimized version (linear)
def maxArea_op(height: list, n: int) -> int:
    left = 0 # leftmost side of the container
    right = n-1 # rightmost side of the container
    area = 0
    
    while left < right:
        area = max(
            (right - left) * min(height[left], height[right]), 
            area
        )

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return area

if __name__ == "__main__":
    height = input("Enter your array: ")
    height = list(map(int, height.split()))
    print(maxArea_op(height, len(height)))