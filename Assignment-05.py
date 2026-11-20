# 1st program 
class Employee:
    def __init__(self):
        self.emp_name = "SK TAMILARASU"
        self.emp_id = "43733116"
class Salary (Employee):
    def __init__(self,salary):
        super().__init__()
        self.emp_salary = salary
        Bonus = float(input("ENTER THE BONUS AMOUNT !! : "))
        self.emp_bonus = Bonus
    def updated_employee_details(self):
        if self.emp_bonus > 0:
            Total_salary = self.emp_bonus + self.emp_salary
            print(f"EMPLOYEE NAME : {self.emp_name}")
            print(f"EMPLOYEE ID : {self.emp_id}")
            print(f"EMPLOYEE SALARY: {self.emp_salary}")
            print(f"UPDATED SALARY OF THE EMPLOYEE IS : {Total_salary}")

        else:
            print("WRONG BONUS AMOUNT !!")
    

company = Salary(60000.00)
company.updated_employee_details()

# 2nd program

class Vehicle:
    def __init__(self):
        self.Vehicle_brand = "TOYOTA"
        self.Vehicle_model = "INNOVA HYCROSS"

class Car(Vehicle):
    def __init__(self,Fuel_type,Seating_capacity):
        super().__init__()
        self.fuel = Fuel_type
        self.seat = Seating_capacity
    def Car_details(self):
        print(f"CAR BRAND : {self.Vehicle_brand}")
        print(f"CAR MODEL : {self.Vehicle_model}")
        print(f"FUEL TYPE OF THE CAR : {self.fuel} litres")
        print(f"SEATING CAPACITY OF THE CAR IS : {self.seat}")

vandi = Car("2.4","8")
vandi.Car_details()
