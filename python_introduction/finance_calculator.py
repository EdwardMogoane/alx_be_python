# Prompt user for financial details
monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))

# calculation monthlu income - total monthly expenses
monthly_savings = monthly_income - total_monthly_expenses 

# anual savings
projected_savings = (monthly_savings * 12 + (monthly_savings *12 *0.05))

# Print results
print(f"Monthly savings: ${monthly_savings}")
print(f"Projected annual savings: ${projected_savings:.2f}")
