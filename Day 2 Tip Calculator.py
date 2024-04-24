print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $\n"))
tip = int(input("What perccentage tip would you like to give? 10, 12, or 15\n"))
people = int(input("How many people to split the bill?\n"))

#Calculating TIP Percentange
tip_as_percent = tip / 100
# Total Tip Amount
total_tip_amount = bill * tip_as_percent
# Adding Tip to the Total Bill
total_bill = total_tip_amount + bill
# Splitting the Bill Among all the People
bill_per_person = total_bill / people
# Rounding off the Bill to 2 Decimal Places
# final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay:{final_amount}$\n")
