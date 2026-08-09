scores = []

for i in range(1, 6):
    score = int(input(f"Enter score of student {i}: "))
    scores.append(score)

print() 

for i in range(1, 6):
    if scores[i] >= 50:
        print(f"Student {i+1}: {scores[i]} -> ผ่าน")
    else:
        print(f"Student {i+1}: {scores[i]} -> ไม่ผ่าน")