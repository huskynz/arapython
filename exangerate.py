# Code written by Peter
# Contact info is peter@husky.nz

# ask user there name
user_name = input("Please enter your first name: ")

# ask for exange rate
exchange_rate_au_nz = float(input(f"Hi {user_name}. Please enter the NZ/AU exchange rate: "))

#ask how mutch they want to exange
user_exchange_amount = float(input("Please enter the amount of NZ $'s you want to exchange: "))

#do the rate
nzd_to_aud = user_exchange_amount * exchange_rate_au_nz

#print the output
print(f"{user_name}, I can exchange NZ ${user_exchange_amount:.2f} into AU ${nzd_to_aud:.2f} for you.")
