expenselist = []
print("||||| Welcome to EXPENSE TRACKER your wealth saviour |||||")
print("\nPress 1 to add expense.")
print("Press 2 to view expenses.")
print("Press 3 to view total spending.")
print("Press 4 to EXIT.")


while True:
    choice = int(input("\nEnter the choice: "))
    if(choice == 1):
      date = input("Enter the date of expenditure: ")
      category = input("Enter the category of expenditure: ")
      amount = float(input("Enter the amount spended: "))
      description = input("Enter the description about expenditure: ")

      expense = {"date" : date,
                 "category" : category,
                 "amount" : amount,
                 "description" : description
                }
      
      expenselist.append(expense)
      print("\nDONE! Your expenses are added successfully ;)")
    
    elif(choice == 2):
        if(len(expenselist) == 0):
          print("No expenses added yet :(")
        else:
          print("These are your expenses :)")
          count = 1
          for eachexpense in expenselist:
            print(f"Expense number {count} >>> {eachexpense["date"]} {eachexpense["category"]} {eachexpense["amount"]} {eachexpense["description"]}")
            count = count + 1
    
    elif(choice == 3):
        total = 0
        for eachexpense in expenselist:
          total = total + eachexpense["amount"]
        print("Your Total spending is: ", total)

    elif(choice == 4):
        print("THANKS FOR USING EXPENSE TRACKER. Have a nice day :)")
        break

    else:
       print("Invalid choice.")
