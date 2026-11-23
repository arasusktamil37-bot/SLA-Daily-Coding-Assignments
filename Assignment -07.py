# 1.List – Shopping Cart
cart = ["Pen", "Book", "Bag", "Pencil", "Box"]

cart.append("Scale")
cart.append("Eraser")

item = input("Enter item to remove: ")
cart.remove(item)

print("Available:", "Book" in cart)
print("Cart:", cart)
print("Total:", len(cart))

#2. Set – Unique Numbers
a = {10, 20, 30, 40, 50}
b = {30, 40, 50, 60, 70}

print("Union:", a | b)
print("Common:", a & b)
print("Difference:", a - b)

a.add(80)
a.remove(20)

print("Updated Set:", a)

#3. Tuple – Employee Salaries
salary = (20000, 25000, 30000, 25000, 40000)

print("First:", salary[0])
print("Last:", salary[-1])
print("Maximum:", max(salary))
print("Minimum:", min(salary))
print("Count:", salary.count(25000))

a = list(salary)
a.append(45000)

print(a)

#4. Dictionary – Student Information
student = {"id": 101,"name": "Arun","age": 21,"course": "CSE"}

print(student.keys())
print(student.values())

student["email"] = "arun@gmail.com"
student["age"] = 22

student.pop("course")

print("name" in student)
print(student)

#5. Dictionary – Mobile Phone Inventory
mobile = {"Vivo": 20000,"Oppo": 25000,"Samsung": 40000,"iPhone": 70000,"OnePlus": 35000}

for x, y in mobile.items():
    print(x, y)

mobile["Redmi"] = 15000
mobile["Vivo"] = 22000

print(mobile)
