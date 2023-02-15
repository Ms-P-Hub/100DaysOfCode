end = int(input("How many numbers from the sequence would you like to see?\n"))

num1 = 0
num2 = 1
fibo = [num1,num2]

for i in range(end-2):
    next_num = num1 + num2
    num1 = num2
    num2 = next_num

    if next_num % 3 == 0 and next_num  % 5 == 0:
        fibo.append("FizzBuzz")
    elif next_num  % 3 == 0:
        fibo.append("Fizz")
    elif next_num  % 5 == 0:
        fibo.append("Buzz")
    else:    
        fibo.append(next_num)

print(fibo)