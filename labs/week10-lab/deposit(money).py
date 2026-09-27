def deposit(money):
    try:
        amount = float(input("กรอกจำนวนเงินที่ต้องการฝาก: "))
        if amount <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")
    except ValueError as e:
        print(f"เกิดข้อผิดพลาด: {e}")
    else:
        money += amount
        print("\nฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {money:.2f} บาท")
    finally:
        print("สิ้นสุดรายการฝากเงิน")

    return money


# ทดลองใช้ function
balance = 1000
print(f"ยอดเงินเริ่มต้น: {balance} บาท")
balance = deposit(balance)