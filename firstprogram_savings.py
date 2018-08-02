# Get information from the user
print("Welcome the savings program!")
name = input("What is your name? ")
print("Hi,", name+".")
reason = input("What will are you saving for? Enter the reason: ")
# Get user input for amount to be saved
balance = float(input("Okay, " + name + ". ""Please enter how much money you will like to save your " + reason +
                      " goal: "))
if balance < 0:
    print("Looks like you already saved enough.")
    balance = 0
    payment = 1
# Get user input for how much can be deposited per pay period
else:
    payment = float(input("Please enter the amount of money you can afford to save each pay period: "))

    if payment <= 0:
        payment = float(input("Savings must be positive! Please enter a non zero value: "))
        if payment <= 0:
            print("Again, no non zero payments. Payment is being set to one.")
            payment = 1
# Calculate the number of payments that will be needed

num_remaining_payments: int = int(balance / payment)
if num_remaining_payments < balance/payment:
    num_remaining_payments = num_remaining_payments + 1

# Present the data to the user

print("You would need to make", num_remaining_payments, "payment(s) to reach the following goal:", reason)