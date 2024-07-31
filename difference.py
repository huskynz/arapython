# Code written by Peter
# Contact info is peter@husky.nz

# ask user there name and then print it
user_name = input("Please enter your first name: ")
print(f"Hi {user_name}.")

# Ask our user to input 2 numbers
integer_1 = int(input("Please enter the first integer: "))
integer_2 = int(input("Please enter the second integer: "))

# Find our diffrence
integer_diffrence = abs(integer_1-integer_2)

# Print out our result
print(f"{user_name}, the absolute difference between {integer_1} and {integer_2} is {integer_diffrence}.")