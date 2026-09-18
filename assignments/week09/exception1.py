try:
    num1 = float(input("ตัวเลขที่ 1: "))
    num2 = float(input("ตัวเลขที่ 2: "))
    operator = input("เครื่องหมาย (+, -, *, /): ")

    if operator not in ("+", "-", "*", "/"):
        print("เครื่องหมายต้องเป็น + - * / เท่านั้น")
    else:
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        else:  # "/"
            result = num1 / num2
        print(f"{num1} {operator} {num2} = {result}")

except ValueError:
    print("กรุณากรอกตัวเลขให้ถูกต้อง")
except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้")
except Exception:
    print("เกิดข้อผิดพลาดที่ไม่ทราบสาเหตุ")
else:
    print("คำนวณข้อมูลเรียบร้อยแล้ว")
finally:
    print("จบการทำงาน")