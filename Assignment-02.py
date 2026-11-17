# python program for printing 50 even numbers using loop

for i in range(2,51,2):
  print(i)

#PYTHON PROGRAM FOR PRINTING NUMBERS UPTO 30 SKIPPING MULTIPLES OF TREE !!

for i in range(1,31):
  if i % 3 == 0:
    continue
  print(i)

#Stop at a Specific Number: Get a number from the user and print numbers from 1 up to that number. Stop the loop when the number reaches 15 using break.

num = int(input("ENTER THE NUMBER TO PRINT !!  : "))
for i in range(1,num+1):
  if i == 15:
    break
  print(i)

#Positive and Negative Numbers: Get 10 numbers from the user. Check whether each number is positive, negative, or zero. Stop the loop if the user enters 0.

for i in range(1,11):
  num = int(input("ENTER THE NUMBER"))
  if num > 0:
    print("THE GIVEN NUMBER IS POSITIVE !!")
  elif num < 0:
    print("THE GIVEN NUMBER IS NEGATIVE !!")
  else:
    break
