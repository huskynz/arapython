# Code written by Peter
# Contact info is peter@husky.nz

user_first_name = input("Please enter your first name: ").strip().capitalize()
user_last_name = input(f"{user_first_name}, please enter your last name: ").strip().capitalize()

user_message = input(f"{user_first_name}, please enter a message: ").strip()


user_position_1 = int(input("Please enter the start position: "))
user_position_2 = int(input("Please enter the end position: "))

string_at_position = user_message[user_position_1:user_position_2 + 1]


print(f"Report for {user_first_name} {user_last_name}'s sentence of {len(user_message)} characters.")
print(f"The characters '{string_at_position}' can be found in position {user_position_1} to position {user_position_2} inclusively.")