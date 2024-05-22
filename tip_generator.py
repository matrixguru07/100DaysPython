print("Welcome to Tip generator")

bill = float(input("Enter the Total Bill Amount: "))
tip = int(input("Enter the Tip you would like to give: "))
ppl = int(input("Enter How many people are there: "))

totalBill = tip / 100 * bill + bill
newTb = round(totalBill, 2)

print(f"The total bill after tip is : {totalBill}")
per_person = int(totalBill / ppl) * (1 + (tip / 100))
new_pp = round(per_person, 2)
print(f"The amount each should pay: {new_pp}")
