# Code written by Peter
# Contact info is peter@husky.nz

#ask our user our first number and our second number
first_user_number = int(input("Please enter the first integer: "))
second_user_number = int(input("Please enter the second integer: "))

first_user_number_perm = first_user_number
second_user_number_perm = second_user_number
# do our oprations 
#first_and_second_number_multiply = first_user_number * second_user_number
#first_and_second_number_divide = first_user_number / second_user_number
#first_and_second_number_subtract = first_user_number - second_user_number
#first_and_second_number_addition = first_user_number + second_user_number

#print our out put
#print(f'''{first_user_number} + {second_user_number} is {first_and_second_number_addition}\n {first_user_number} - {second_user_number} is {first_and_second_number_subtract}\n {first_user_number} * {second_user_number} is {first_and_second_number_multiply}\n {first_user_number} / {second_user_number} is {first_and_second_number_divide}  ''')

first_user_number += second_user_number
print(f"{first_user_number_perm} + {second_user_number_perm} is {first_user_number}")
first_user_number = first_user_number_perm

first_user_number -= second_user_number
print(f"{first_user_number_perm} - {second_user_number_perm} is {first_user_number}")
first_user_number = first_user_number_perm

first_user_number *= second_user_number
print(f"{first_user_number_perm} * {second_user_number_perm} is {first_user_number}")
first_user_number = first_user_number_perm

first_user_number /= second_user_number
print(f"{first_user_number_perm} / {second_user_number_perm} is {first_user_number}")
first_user_number = first_user_number_perm


