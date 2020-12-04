import re
import decimal
claimed_mileage_cost = 0
actual_mileage_cost = 0
claimed_expense_cost = 0

mileage_expr = re.compile(r"(\d{4}(-\d{2}){2})[ ]?M[ ]?(\d{1,10}.\d{2}) (\d{1,4}) ([A-Z]{1,2}\d{1,2}\d[A-Z]{2}) ([A-Z]{1,2}\d{1,2}\d[A-Z]{2}) (\d{1,10}.\d{2})")

with open("expenses01.txt") as expenses_file:

    for line in expenses_file:
        match = mileage_expr.match(line)
        if match:
            date, _, rate, miles, from_code, to_code, total = match.groups()
            actual_mileage_cost += decimal.Decimal(rate) * decimal.Decimal(miles)
            claimed_mileage_cost += decimal.Decimal(total)

print(claimed_mileage_cost, actual_mileage_cost, claimed_mileage_cost-actual_mileage_cost)


# print(sum(float(line[0])*float(line[1])
#           for line in
#             [(line.groups()[2], line.groups()[3])
#                 for line in
#                     map(mileage_expr.match,
#                         [line for line in open("expenses01.txt")]) if line is not None]))
