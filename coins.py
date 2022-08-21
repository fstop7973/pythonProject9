print("Please enter the amount of money to convert:")

dollars = int(input("# of dollars:"))
dollars_in_cents = dollars*100
cents = int(input("# of cents:"))
total_cents = dollars_in_cents+cents

total_quarters = int(total_cents/25)
cents_after_quarters = total_cents-total_quarters*25
total_dimes = int((cents_after_quarters/10))
cents_after_dimes = cents_after_quarters-total_dimes*10
total_nickels = int(cents_after_dimes/5)
pennies = int(cents_after_dimes-total_nickels*5)



print("The coins are", total_quarters, "quarters,", total_dimes, "dimes,", total_nickels, "nickels and", pennies, "pennies")


