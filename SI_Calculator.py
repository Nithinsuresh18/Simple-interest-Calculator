# Simple Interest Calculator

# Taking user input
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Annual Interest Rate (%): "))
years = int(input("Enter Number of Years: "))

# Calculating Simple Interest
simple_interest = (principal * rate * years) / 100
total_amount = principal + simple_interest

# Displaying the result
print(f"The total amount after {years} years will be ₹{round(total_amount, 2)}")
print(f"The interest earned is ₹{round(simple_interest, 2)}")
