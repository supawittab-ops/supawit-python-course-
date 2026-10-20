def calculate_electricity_cost(units):
    """คำนวณและแสดงรายละเอียดค่าไฟฟ้าแบบขั้นบันได"""
    if units < 0:
        print("จำนวนหน่วยไฟฟ้าต้องไม่ติดลบ")
        return None
 
    SERVICE_FEE = 25.00
 
    # (หน่วยเริ่มต้น, หน่วยสิ้นสุด, อัตราต่อหน่วย)
    tiers = [
        (1, 50, 2.50),
        (51, 100, 3.00),
        (101, 200, 3.50),
        (201, float("inf"), 4.00),
    ]
 
    print("\nรายละเอียดค่าไฟ:")
    total = 0.0
 
    for start, end, rate in tiers:
        if units < start:
            break
        used_end = min(units, end)
        used = used_end - start + 1
        amount = used * rate
        total += amount
        print(f"{start}-{used_end} หน่วย: {amount:.2f} บาท")
 
    total += SERVICE_FEE
    print(f"ค่าบริการ: {SERVICE_FEE:.2f} บาท")
    print(f"รวมค่าไฟทั้งสิ้น: {total:.2f} บาท")
    return total
 
 
def main():
    while True:
        print("\n===== โปรแกรมคำนวณค่าไฟฟ้า =====")
        print("1. คำนวณค่าไฟ")
        print("2. ออกจากโปรแกรม")
        choice = input("เลือกเมนู: ")
 
        if choice == "1":
            try:
                units = int(input("\nกรอกจำนวนหน่วยไฟฟ้า: "))
            except ValueError:
                print("กรุณากรอกเป็นตัวเลขจำนวนเต็ม")
                continue
            calculate_electricity_cost(units)
        elif choice == "2":
            print("ออกจากโปรแกรมแล้ว")
            break
        else:
            print("เลือกเมนูไม่ถูกต้อง")
 
 
main()