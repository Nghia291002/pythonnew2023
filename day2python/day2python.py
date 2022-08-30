from msilib.schema import Billboard


print("Welcome to the tip calculator")
print("What was the total bill?")
q=float(input())
print(q)
print("What percentage tip would you like to give? 10, 12, or 15?")
w=int(input())
print("How many people to split the bill?")
e=int(input())
tip_as_percent = q / 100
tong_tip = q * tip_as_percent
tong_bill = q + tong_tip
bill_nguoi = tong_bill / e
ket_qua = round(bill_nguoi, 2)
print(f"Each person should pay: ${ket_qua}")
