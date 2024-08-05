# Code written by Peter
# Contact info is peter@husky.nz

# Get our users first and last name
user_first_name = input("Please enter your first name: ").strip().title()
user_last_name = input(f"{user_first_name}, please enter your last name: ").title().strip()

# Get our user to input a sentance
user_sentence = input(f"{user_first_name}, please enter a sentence: ").strip()

# Report to our user there name and the length of there sentce
print(f"Report for {user_first_name} {user_last_name}'s sentence of {len(user_sentence)} characters.")

# Print our first and last character
print(f"First character: {user_sentence[0]}")
print(f"Last character: {user_sentence[-1]}")
