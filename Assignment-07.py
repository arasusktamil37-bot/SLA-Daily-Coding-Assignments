#Write a Python program to analyze a student's full name. USING (STRING OPERATIONS)
first_name = input("ENTER THE FIRST NAME : ")
last_name = input("ENTER THE LAST NAME : ")
full_name = first_name +" "+last_name
print(full_name)

print(full_name.upper())
print(full_name.lower())
print(len(full_name))

for i in full_name:
  print(i)

for i in full_name:
  if i == " ":
    continue
  else:
    print(i)

if full_name[0] == "T":
  print("YES THE NAME STARTS  WITH T !!")
else:
  print("NO THE NAME DOSENT STARTS WIITH T !!")

print(full_name[0:3])
print(full_name[-3:])
