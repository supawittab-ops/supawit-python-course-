print("=== PERSONAL INFORMATION VALIDATOR ===")
name = input("Enter your name: ")
age_text = input("Enter your age: ")
phone = input("Enter your phone number: ")

# ตรวจชื่อ: ต้องไม่ว่าง และมีแต่ตัวอักษรกับช่องว่าง
name_valid = name.strip() != ""
for char in name:
    if not (char.isalpha() or char.isspace()):
        name_valid = False
        break

# ตรวจอายุ: ต้องเป็นตัวเลข แล้วแปลงเป็น int และอยู่ระหว่าง 18-65
age = 0
age_valid = False
if age_text.isdigit():
    age = int(age_text)
    if 18 <= age <= 65:
        age_valid = True

# ตรวจเบอร์: ตัวเลขล้วน และมี 10 หลักพอดี
phone_valid = phone.isdigit() and len(phone) == 10

print("\nValidation Results:")
if name_valid:
    print("Name: Valid (contains only letters and spaces)")
else:
    print("Name: Invalid (use letters and spaces only)")

if age_valid:
    print("Age: Valid ({} years old)".format(age))
else:
    print("Age: Invalid (must be a number between 18 and 65)")

if phone_valid:
    print("Phone: Valid (10-digit number)")
else:
    print("Phone: Invalid (must be exactly 10 digits)")

# แสดงข้อมูลที่จัดรูปแบบเมื่อผ่านทุกข้อ
if name_valid and age_valid and phone_valid:
    print("\nFormatted Information:")
    print("Name: {}".format(name.upper()))

    if age <= 30:
        group = "Young Adult (18-30)"
    elif age <= 60:
        group = "Adult (31-60)"
    else:
        group = "Senior (61-65)"
    print("Age Group: {}".format(group))

    print("Phone: +91-{}".format(phone))