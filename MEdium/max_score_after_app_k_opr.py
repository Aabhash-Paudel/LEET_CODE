print(-(-10 // 3))  # This will print 4

nums = [10,10,10,10,10]
k = 5
j = 5 # Assign `k` and `j` separately
i = 0
sum = 0  # Initialize sum

def abc(j):
    global i, sum  # Declare sum as global
    if j == 0:  # Base case should check for `j`
        return
    num1 = max(nums)  # Find the maximum number in the list
    num2 = num1  # Store the original max value
    num1 = -(-num1 // k)  # Apply ceiling division to num1
    mx_index = nums.index(max(nums))  # Find the index of the maximum element
    nums[mx_index] = num1  # Replace max element with the result of ceiling division
    sum += num2  # Add the original max value to the sum
    i += 1  # Increment index counter
    abc(j - 1)  # Recursive call with decremented `j`

abc(k)

print("Final nums:", nums)
print("Final sum:", sum)