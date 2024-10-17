num = 98800435
digits = [int(d) for d in str(num)]
for i in range(len(digits) - 1):
    if digits[i] < digits[i+1]:
        temp = digits[i+1]
        digits[i+1] = digits[i]
        digits[i] = temp 
        break


result = int(''.join(map(str, digits)))
print(result)