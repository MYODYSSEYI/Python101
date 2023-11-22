
'''
When this code is finished...
it should start in the Terminal, count from 0 to 100 and put out 
Fizz if something is only dividable by 3 
Buzz if something is only dividable by 5
FizzBuzz if something is dividable by both.
'''

for i in range(101):
    print(i)
    if ((i%5==0)&(i%3==0)):
        print("FizzBuzz")        
    elif (i%3==0):
        print("Fizz")
    elif (i%5==0):
        print("Buzz")