num = int(input("Enter a number: "))

sum = 0
for digit in str(num):
    sum += int(digit)


print(f"The sum of digits of {num} is {sum}.")