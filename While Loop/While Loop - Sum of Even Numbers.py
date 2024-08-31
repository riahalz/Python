### Print sum of first 10 even numbers ###

# Find first 10 even numbers - 2,4,6,8,10,12,14,16,18,20

count = 0
sum_even_nums = 0
current_num = 2

while count<10:
    sum_even_nums += current_num
    current_num += 2
    count +=1

print("Sum of first 10 even numbers = ", sum_even_nums)


        
