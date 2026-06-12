# Restaurant Management System
from datetime import datetime

class Food_Item:
    item_id = 1000  # Class-level variable to keep track of IDs globally
    
    def __init__(self):
        Food_Item.item_id += 1
        self.item_code = Food_Item.item_id
        self.name = ""
        self.price = 0.0
        self.category = ""

    def reg_new_food_item(self):
        print("\n--- Register New Food Item ---")
        self.name = input("Enter Name For the Food Item: ")
        try:
            self.price = float(input("Enter the fixed Price for this Food Item: "))
        except ValueError:
            print("Invalid input. Setting price to 0.0.")
            self.price = 0.0
            
        self.category = input("Enter the category of the Food item (Drink/Main Course/Dessert): ")

        item_dict = {
            "Item_Code" : self.item_code,
            "Name"  : self.name,
            "Price" : self.price,
            "Category"  : self.category,
        }
        print(f"Food Item '{self.name}' registered successfully with Item Code: {self.item_code}")
        return item_dict


class Menu:
    def __init__(self):
        self.drinks = []
        self.main_course = []
        self.dessert = []

    def add_food_item(self, food_item):
        if food_item["Category"].lower() == "drink":
            self.drinks.append(food_item)
        elif food_item["Category"].lower() == "main course":
            self.main_course.append(food_item)
        elif food_item["Category"].lower() == "dessert":
            self.dessert.append(food_item)
        else:
            print("Invalid category. Food item not added to the menu.")

    def get_all_drinks(self):
        if len(self.drinks) == 0:
            print("\nThere are no drinks in the menu.")
            return
        print("\n--- Drinks ---")
        print("Item code   |   Name   |   Price")
        for item in self.drinks:
            print(f"{item['Item_Code']}        |   {item['Name']}   |   ${item['Price']:.2f}")

    def get_all_main_course(self):
        if len(self.main_course) == 0:
            print("\nThere are no main courses in the menu.")
            return
        print("\n--- Main Course ---")
        print("Item code   |   Name   |   Price")
        for item in self.main_course:
            print(f"{item['Item_Code']}        |   {item['Name']}   |   ${item['Price']:.2f}")

    def get_all_dessert(self):
        if len(self.dessert) == 0:
            print("\nThere are no desserts in the menu.")
            return
        print("\n--- Dessert ---")
        print("Item code   |   Name   |   Price")
        for item in self.dessert:
            print(f"{item['Item_Code']}        |   {item['Name']}   |   ${item['Price']:.2f}")

    def get_food_item_by_id(self, item_code):
        for item in self.drinks + self.main_course + self.dessert:
            if item["Item_Code"] == item_code:
                print("\n--- Food Item Details ---")
                print(f"Item Code: {item['Item_Code']}")
                print(f"Name: {item['Name']}")
                print(f"Price: ${item['Price']:.2f}")
                print(f"Category: {item['Category']}")
                return
        print(f"No food item found with Item Code: {item_code}")


class Customer:
    c_id = 100000

    def __init__(self):
        Customer.c_id += 1 # Increment in init
        self.customer_id = Customer.c_id
        self.c_name = ""
        self.c_mobile_no = 0
        self.c_mail = ""
        self.c_date_joined = ""
        self.c_points = 0

    def create_new_customer(self):
        print("\nREGISTER NEW CUSTOMER")
        self.c_name = input("Enter Full Name : ")
        try:
            self.c_mobile_no = int(input("Enter Mobile Number : "))
        except ValueError:
            print("Invalid Input, Setting mobile to 0.")
            self.c_mobile_no = 0
        self.c_mail = input("Enter email address  : ")
        self.c_date_joined = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.c_points = 100

        customer_dict = {
            "ID" : self.customer_id,
            "Customer Name" : self.c_name,
            "Mobile No" : self.c_mobile_no,
            "Email" : self.c_mail,
            "Date Joined" : self.c_date_joined,
            "Points" : self.c_points
        }
        print(f"Customer '{self.c_name}' registered successfully with Customer ID: {self.customer_id}")
        return customer_dict


class Order: # Fixed class capitalization naming conflict
    order_id = 500000
    
    def __init__(self):
        Order.order_id += 1
        self.current_order_id = Order.order_id
        self.c_id = 0
        self.item_codes_with_quantity = [] # Fixed: initialized cleanly without empty inner list

    def create_new_order(self):
        print("\n--- Create New Order ---")
        try:
            self.c_id = int(input("Enter the Customer ID : "))
        except ValueError:
            print("Invalid Customer ID.")
            return None
            
        while True:
            print("\n1. To add items to order")
            print("2. Finish Order & Exit")
            try:
                choice = int(input("Enter Your Choice : "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == 1:
                try:
                    item_code = int(input("Enter the Item Code : "))
                    quantity = int(input("Enter the Quantity : "))
                    self.item_codes_with_quantity.append([item_code, quantity])
                except ValueError:
                    print("Invalid input. Numbers expected.")
                    continue

                more = input("Do you want to add more items? (yes/no): ").strip().lower()
                if more != 'yes':
                    break
            elif choice == 2:
                break

        order_dict = {
            "Order ID" : self.current_order_id,
            "Customer ID" : self.c_id,
            "Items" : self.item_codes_with_quantity,
        }
        print(f"Order created successfully with Order ID: {self.current_order_id}")
        return order_dict
                

class Bill:
    bill_id = 900000
    
    def __init__(self):
        Bill.bill_id += 1
        self.current_bill_id = Bill.bill_id
        self.order_id = 0
        self.total_amount = 0.0

    def create_new_bill(self, registered_orders, active_menu):
        print("\n--- Create New Bill ---")
        try:
            target_order_id = int(input("Enter the Order ID : "))
        except ValueError:
            print("Please Enter Valid Order ID.")
            return None

        # Find the matching order from the restaurant database
        target_order = None
        for o in registered_orders:
            if o["Order ID"] == target_order_id:
                target_order = o
                break
        
        if not target_order:
            print("Order ID not found.")
            return None

        self.order_id = target_order_id
        self.total_amount = 0.0
        
        # Combine all food categories to check prices
        all_items = active_menu.drinks + active_menu.main_course + active_menu.dessert
        
        # Calculate pricing logic: (Price * Quantity)
        for ordered_item in target_order["Items"]:
            code = ordered_item[0]
            qty = ordered_item[1]
            
            # Find the price of this specific item code
            for menu_item in all_items:
                if menu_item["Item_Code"] == code:
                    self.total_amount += menu_item["Price"] * qty

        bill_dict = {
            "Bill ID" : self.current_bill_id,
            "Order ID" : self.order_id,
            "Total Amount" : self.total_amount,
        }
        print(f"Bill created successfully with Bill ID: {self.current_bill_id} and Total Amount: ${self.total_amount:.2f}")
        return bill_dict
    
    def print_bill(self):
        print("\n--- Bill Details ---")
        print(f"Bill ID: {self.current_bill_id}")
        print(f"Order ID: {self.order_id}")
        print(f"Customer ID: {self.c_id}")
        print("Items:")
        for ordered_item in self.item_codes_with_quantity:
            print(f"  Item Code: {ordered_item[0]}, Quantity: {ordered_item[1]}")
        print(f"Total Amount: ${self.total_amount:.2f}")
    

class Restaurant:
    def __init__(self):
        self.menu = Menu()
        self.customers = []
        self.orders = []
        self.bills = []

    def create_new_food_item(self):
        food_item = Food_Item()
        item_data = food_item.reg_new_food_item() 
        self.menu.add_food_item(item_data)
    
    def create_new_customer(self):
        customer = Customer()
        customer_data = customer.create_new_customer()
        self.customers.append(customer_data)
    
    def create_new_order(self):
        new_order_obj = Order() # Fixed naming collision conflict
        order_data = new_order_obj.create_new_order()
        if order_data:
            self.orders.append(order_data)

    def create_new_bill(self):
        bill = Bill()
        # Pass data context down into bill calculation engine
        bill_data = bill.create_new_bill(self.orders, self.menu)
        if bill_data:
            self.bills.append(bill_data)
    
    def get_menu(self):
        self.menu.get_all_drinks()
        self.menu.get_all_main_course()
        self.menu.get_all_dessert()

    def get_customer_by_id(self, c_id):
        for customer in self.customers:
            if customer["ID"] == c_id:
                print(f"\nCustomer ID: {customer['ID']}")
                print(f"Name: {customer['Customer Name']}")
                print(f"Mobile No: {customer['Mobile No']}")
                print(f"Email: {customer['Email']}")
                print(f"Date Joined: {customer['Date Joined']}")
                print(f"Points: {customer['Points']}")
                return
        print(f"No customer found with ID: {c_id}")

    def get_order_by_id(self, order_id):
        for o in self.orders:
            if o["Order ID"] == order_id:
                print(f"\nOrder ID: {o['Order ID']}")
                print(f"Customer ID: {o['Customer ID']}")
                print("Items:")
                for item in o["Items"]:
                    print(f"  Item Code: {item[0]}, Quantity: {item[1]}")
                return
        print(f"No order found with Order ID: {order_id}")

    def get_bill_by_id(self, bill_id):
        for b in self.bills:
            if b["Bill ID"] == bill_id:
                print(f"\nBill ID: {b['Bill ID']}")
                print(f"Order ID: {b['Order ID']}")
                print(f"Total Amount: ${b['Total Amount']:.2f}")
                return
        print(f"No bill found with Bill ID: {bill_id}")

    def get_food_item_by_id(self, item_code):
        self.menu.get_food_item_by_id(item_code)


# --- Execution Flow ---
print("Welcome to the Restaurant Management System!")
restaurant = Restaurant()

while True:
    print("\n--- Main Menu ---")
    print("1. Create New Food Item")
    print("2. Create New Customer")
    print("3. Create New Order")
    print("4. Create New Bill")
    print("5. Get Menu")
    print("6. Get Customer by ID")
    print("7. Get Order by ID")    
    print("8. Get Bill by ID")
    print("9. Get Food Item by ID")
    print("10. Exit")

    choice = input("Enter your choice (1-10): ").strip()

    if choice == "1":
        restaurant.create_new_food_item()
    elif choice == "2":
        restaurant.create_new_customer()
    elif choice == "3":
        restaurant.create_new_order()
    elif choice == "4":
        restaurant.create_new_bill()
        restaurant.
    elif choice == "5":
        restaurant.get_menu()
    elif choice == "6":
        try:
            c_id = int(input("Enter the Customer ID: "))
            restaurant.get_customer_by_id(c_id)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == "7":
        try:
            order_id = int(input("Enter the Order ID: "))
            restaurant.get_order_by_id(order_id)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == "8":
        try:
            bill_id = int(input("Enter the Bill ID: "))
            restaurant.get_bill_by_id(bill_id)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == "9":
        try:
            item_code = int(input("Enter the Item Code: "))
            restaurant.get_food_item_by_id(item_code)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == "10":
        print("Thank you for using the Restaurant Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 10.")