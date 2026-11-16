#1. Shopping Discount Eligibility

sshopping_amount = float(input("ENTER THE TOTAL AMOUNT : "))
Member = input("ARE YOU A MEMBER ?? : ")
if shopping_amount >= 2000.00 and Member.strip().lower() == "yes":
  print("Eligible for 20% discount")
else :
  print("NOT Eligible for 20% discount")


#2. Student Exam Eligibility

student_attendance = int(input("ENTER THE TOTAL ATTENDANCE PERCENTAGE : "))
student_internalmark = int(input("ENTER YOUR INTERNAL MARK : "))
if student_attendance >= 75 and student_internalmark >= 40 :
  print("ELIGIBLE FOR EXAMINATION !!")
else :
  print("NOT ELIGIBLE FOR EXAMINATION!!")

