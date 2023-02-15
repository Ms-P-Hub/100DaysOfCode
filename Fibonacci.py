end = int(input("How many numbers from the sequence would you like to see?\n"))

num1 = 0
num2 = 1
fibo = [num1,num2]

for i in range(end-2):
    next_num = num1 + num2
    num1 = num2
    num2 = next_num

    fibo.append(next_num)

print(fibo)