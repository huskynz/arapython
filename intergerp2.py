# Code written by Peter
# Contact info is peter@husky.nz

#ask user there name and print it
user_name = input("Please enter your first name: ")
print(f"Hi {user_name}.")

#this asks our use to enter a number
user_number = int(input("Please enter the first integer: "))
user_number_2 = int(input("Please enter the second integer: "))

#do our opration
numbers_division = user_number / user_number_2
numbers_remainder = user_number - (user_number_2 * numbers_division)


#we print our result
print(f"{user_name}, the answer to {user_number} divided by {user_number_2} is {numbers_division:.0f} with a remainder of {numbers_remainder}.")