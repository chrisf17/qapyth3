import re
import decimal
claimed_mileage_cost = 0
actual_mileage_cost = 0
claimed_expense_cost = 0

mileage_expr = re.compile(r"")

with open("expenses01.txt") as expenses_file:

    for line in expenses_file:
        match = mileage_expr.match(line)
        if match:
            # TODO: Extract the mileage data and calculate total
            # actual_mileage_cost
            # claimed_mileage_cost
            pass

print(claimed_mileage_cost, actual_mileage_cost, claimed_mileage_cost-actual_mileage_cost)


