# Simple ATM Security Check using FUNCTIONS !!!

def check_pin(entered_pin):
  if entered_pin == 1234 :
    return True
  else :
    return False

entered_pin = int(input("ENTER YOUR PIN : "))
print(check_pin(entered_pin))

#Create the Bank Action Function

def bank_action(action_type, entered_pin):

    result = check_pin(entered_pin)

    if result == True:

        if action_type == "balance":
            print("Your balance is ₹10,000")

        elif action_type == "withdraw":
            print("Withdrawal successful")

    else:
        print("Incorrect PIN, access denied.")
