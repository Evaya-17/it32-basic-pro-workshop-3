shop = int(input("จำนวนร้านที่ต้องไปเก็บ: "))
kapook = 0
for i in range (1,shop+1):
    money = float(input(f"เก็บเงินร้านที่ {i}: "))
    kapook = kapook + money
    print(f"จำนวนที่เก็บมา {money} บาท")
print(f"จำนวนเงินทั้งหมด: {kapook} ")