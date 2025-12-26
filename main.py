# Expence tracker
expenses_list = [] # list to store expenses
print("Welcome to the Expense Tracker")
while True:
    print("====Menu====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3.Total Expense")
    print("4. Exit")
    choice = input("Enter  your choice between 1-4: \n")
    #Add Expense
    if (choice == "1"):
        date = input("Enter the date of Expenses (yyyy-mm-dd):")
        category = input("Enter the category/type of expense (e.g.,Food,Transport,Utilities):")
        description = input("Enter a brief description/details of the expenses(e.g.,gulaabjamun,samosa etc):")
        amount = float(input("Enter amount (₹): "))
        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
            }
        expenses_list.append(expense)
        print("\n Expense added successfully!")

        # 2. View Expenses
    elif (choice == "2"):
            if(len(expenses_list)==0):
                print("\n No expenses recorded yet,")
            else:
                print("==== Recorded Expenses ====")
                count = 1
                for each_expense in expenses_list:
                    print(f"Expence no. 1{count}-> Date: {each_expense["date"]},{each_expense["category"]},{each_expense["description"]},{each_expense["amount"]}")
                    count=count+1
        # 3. Total Expense
    elif (choice == "3"):
            total = 0
            for each_expense in expenses_list:
                total= total+ each_expense["amount"]
                print("\n Total Expense is:",total)
        # 4. Exit
    elif (choice == "4"):
            print("Exitint the Expense Tracker. Thanks for using our system!")
            break
    else:
         print("Invalid input :please chose the option only from 1_4 :try again")
         
         
