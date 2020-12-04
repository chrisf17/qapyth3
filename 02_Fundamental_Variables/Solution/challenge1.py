interest_rate = 0.01
n = 12 # number of times interest applied per time period
t = 1 # number of time periods elapsed

initial_principal_balance = None

while initial_principal_balance is None:
    try:
        initial_principal_balance = float(input("Enter account balance:"))
    except:
        print("Please enter a valid amount!")

final_amount = initial_principal_balance * (1 +(interest_rate/n))**(n*t) # TODO Calculate simple interest

print(f"Final Amount: {final_amount:10,.2f}") # TODO print one or more messages giving results
print(f"Interest    : {final_amount-initial_principal_balance:10,.2f}")