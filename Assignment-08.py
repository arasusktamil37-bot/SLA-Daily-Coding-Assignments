#Task 1: Student Marks Management (List)
student_1 = int(input("ENTER THE MARK OF STUDENT 1 : "))
student_2 = int(input("ENTER THE MARK OF STUDENT 2 : "))
student_3 = int(input("ENTER THE MARK OF STUDENT 3 : "))
student_4 = int(input("ENTER THE MARK OF STUDENT 4 : "))
student_5 = int(input("ENTER THE MARK OF STUDENT 5 : "))

student_marks = [student_1,student_2,student_3,student_4,student_5]

print(student_marks)

student_marks.append(95)
print(f"UPDATED MARKS : {student_marks}")

student_marks.insert(1,84)
print(f"UPDATED MARKS : {student_marks}")

student_marks.remove(78)
print(f"UPDATED MARKS : {student_marks}")

highest = max(student_marks)
lowest = min(student_marks)
print(f"HIGHEST MARK : {highest}")
print(f"LOWEST MARK : {lowest}")

total = sum(student_marks)
count = len(student_marks)
avg_mark = total / count
print(f"TOTAL MARKS : {total}")
print(f"AVERAGE MARK : {avg_mark}")

student_marks.sort()
print(student_marks)

count = 0
for i in student_marks:
  if i >= 75:
    count += 1
print(f"75 + MARK ARE !! : {count}")

##Task 2: Shopping Cart Management (Tuple)
store = ("hot_wheels","foot_ball","cricket_bat","pens","books")
print(store)
print(store[0])
print(store[-1])
print(store[0:3])

for i in store:
  if i == "books":
    print("yes")

count = 0
for i in store:
  if i == "pens":
    print(count)
store.index("books")
print(store)

store2 = ("shirt","pant")

full_store = store + store2
print(full_store)

store_square = full_store*2
print(store_square)

for i in full_store:
  print(i)

count1 = 0
for i in student_marks:
  if i >= 50:
    count += 1
print(count1)
