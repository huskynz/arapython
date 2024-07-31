# Code written by Peter
# Contact info is peter@husky.nz

# ask our user there first and last name
user_first_name = input("Please enter your first name: ").replace(" ", "").lower().capitalize()
user_last_name = input("Please enter your last name: ").replace(" ", "").lower().capitalize()

#set our class number
class_number = "BCDE101"
#print our welcome message
print(f"Pleased to meet you {user_first_name} {user_last_name}, welcome to {class_number}.")