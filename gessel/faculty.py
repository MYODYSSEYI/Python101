print("=============< Faculty Calculator >=============")
num = int(input("Enter a number: "))

times = 0 # while loop
answer = 1 # while loop
answer2 = 1 # for loop

while times != num:
    times += 1 
    answer *= times

print(f"The answer is: {answer}")

for i in range(1, num+1):
    answer2 *= i
print(f"The answer is: {answer}")

def factorial(n):
    # Base case
    if n == 0:
        return 1
    # Recursive case subtracts 1 from n and calls itself until n == 0 for instance n = 4 then it returns 4*3*2*1 = 24
    return n * factorial(n - 1)
 
print(f"Factorial of {num} is: {factorial(num)}")
