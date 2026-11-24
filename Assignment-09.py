#Task 1: Unique Number Analyzer (Set)
#Write a Python program to manage and analyze a collection of numbers using a set.
numbers = set()
for i in range(10):
  num = int(input("ENTER THE NUMBER : "))
  numbers.add(num)
print(f'SET OF NUMBERS : {numbers}')
numbers.add(99)
print(numbers)

numbers.discard(100)
print(numbers)

for i in numbers:
  if i == 77:
    print("yes")

my_set = {35,45,55,65,75,}
my_new_set = numbers.union(my_set)
print(my_new_set)

my_intersection = numbers.intersection(my_set)
print(my_intersection)

my_diff = numbers.difference(my_set)
print(my_diff)

total = len(numbers)
print(total)

#Task 2: Employee Details Management (Dictionary)
employee = {
    "id": 101,
    "name": "Arun",
    "age": 22,
    "department": "IT",
    "salary": 30000
}

print("EMPLOYEE DETAILS:", employee)

print("Employee Name:", employee["name"])
print("Employee Salary:", employee["salary"])

employee["experience"] = "2 Years"

employee["salary"] = 35000

employee.pop("age")

print("Keys:", employee.keys())

print("Values:", employee.values())

for key, value in employee.items():
    print(key, ":", value)

if "department" in employee:
    print("Department key exists")
else:
    print("Department key does not exist")
