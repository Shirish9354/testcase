import sys

products = ['Rice', 'Flours', 'Tea/Coffee', 'Vegetables', 'Fruits', 'Sugar/Jaggery', 'Snacks']
price = [209 , 200, 300, 200, 300, 299, 20]
employees = ['Sarah', 'Jason', 'Robert', 'Alan']
salary = [25000, 20000, 22000, 18000]
employees_and_salary = zip(employees, salary)

print('''
  _______ __ __ __ __                 _______             __
 |   _   |__|  |  |__.-----.-----.   |   _   .--.--.-----|  |_.-----.--------.
 |.  1   |  |  |  |  |     |  _  |   |   1___|  |  |__ --|   _|  -__|        |
 |.  _   |__|__|__|__|__|__|___  |   |____   |___  |_____|____|_____|__|__|__|
 |:  1    \                |_____|   |:  1   |_____|
 |::.. .  /                          |::.. . |
 `-------'                           `-------'
                                                                              ''')

def error_message():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
    print()

print()
print("########  GENERAL STORE ########")
print()
res1 = input("       1. ADMIN \n       2. CUSTOMER \n>>> ")
password = ''

def admin():
    if res1 == '1':
        print("Password authentication required!")
        print()
        print("No password actually!")
        guess = input("Enter your password: ")
        print()
        if guess == password:
            options = input("1. ADD PRODUCTS \n2. DELETE PRODUCTS \n3. EMPLOYEES \n>>> ")
            print()
            if options == '1':
                new_product = input("Enter the new product: ")
                print()
                print(products)
                print()
                products.append(new_product)
                print("Product has been added successfully")
                print(products)
                sys.exit()
            elif options == '2':
                delete_product = input("Enter the product to be deleted: ")
                print()
                print(products)
                print()
                products.remove(delete_product)
                print("Product has been deleted successfully!")
                print()
                print(products)
                sys.exit()
            elif options == '3':
                print(list(employees_and_salary))
                message = input("Enter \n1. ADD \n2. FIRE\n>>> ")
                if message == '1':
                    print(employees)
                    add_employee = input("Enter your new employee: ")
                    employees.append(add_employee)
                    print(employees)
                elif message == '2':
                    print(employees)
                    fire_employee = input(str("Enter the employee you want to fire: "))
                    employees.remove(fire_employee)
                    print(employees)
                sys.exit()
            else:
                error_message()
                admin()
admin()

def customer():
        if res1 == '2':
            print("Welcome to our store! Hope you have a pleasant experience!")
            print()
            print("Here is our list of products and their respective prices!")
            goods = input("1.Rice, Flours \n2.Tea/Coffee \n3.Vegetables \n4.Fruits \n5.Sugar/Jaggery \n6.Snacks \n>>> ")
            print()
            total_cost = 0
            items = 0
            if goods == '1':
                total_cost += 209
                items += 1
            elif goods == '2':
                total_cost += 200
                items += 1
            elif goods == '3':
                total_cost += 300
                items += 1
            elif goods == '4':
                total_cost += 200
                items += 1
            elif goods == '5':
                total_cost += 300
                items += 1
            elif goods == '6':
                total_cost += 20
                items += 1
            else:
                error_message()
                customer()
            print()
        message = input("Do you want to shop for more products [y] [n] >>> ")

        def bill():
            print("######## RECIEPT ########")
            print("Total cost is", total_cost)
            print("Total number of items bought", items)
            print("Thank you! Do shop from us next time again!!")
        if message == 'y':
            customer()
        elif message == 'n':
            bill()
            sys.exit()
customer()
