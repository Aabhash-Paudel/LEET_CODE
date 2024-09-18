nums = [3, 10, 2]
leng = len(nums) - 1  # Start with length - 1
j = 0
for i in nums[::-1]:
    print(i)
    print(leng)
    j += i * (10 ** leng)
    print(j)
    leng -= 1

print(j)