# Code written by Peter
# Contact info is peter@husky.nz

# Ask our user there name
user_first_name = input("Please enter your first name: ")

# set our upper and lower
user_first_name_upper = user_first_name.upper()
user_first_name_lower = user_first_name.lower()
user_first_name_intro = user_first_name.lower().capitalize()

#print our output
print(f"{user_first_name_intro}, your first name in lower case is {user_first_name_lower} and in upper case is {user_first_name_upper}.")