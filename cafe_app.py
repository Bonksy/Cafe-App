import json
import pymysql

# Establish a database connection
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="pass1",
    database="Test"
)

# Constants
COURIER = "courier"
PRODUCTS = "product"
ORDER = "orders"
ORDER_STATUS = "order_status"
CUSTOMER = "customer"
VALUE_ERROR_MESSAGE = "Invalid entry. Please try again..."
INDEX_ERROR_MESSAGE = "Selected index does not exist. Please choose a valid index..."
INVALID_OPTION_MESSAGE = "Please enter a valid option: "
CHOOSE_OPTION_MESSAGE = "Please choose an option: "


# Helper functions

def view_table(name):   
    cursor = connection.cursor()
    query = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '{name}' AND table_schema = 'Test'"
    cursor.execute(query)
    result = cursor.fetchall()
    print("Columns in table:")
    for row in result:
        print(row)

    sql = f"SELECT * FROM {name}"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()

def view_product_table(name):   
    cursor = connection.cursor()
    sql = f"SELECT * FROM {name}"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print("\n---------------------------------------------------")
    print("| {0:<10} | {1:^19} | {2:^13} |" .format("Product ID", "Product Name", "Price"))
    print("---------------------------------------------------")

    for row in rows:
        id = row[0]
        name = row[1]
        number = row[2]

        print("| {0:<10} | {1:<19} | {2:<13} |" . format(id, name, number))
    print("---------------------------------------------------\n")
    cursor.close()

def view_courier_table(name):   
    cursor = connection.cursor()
    sql = f"SELECT * FROM {name}"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print("\n---------------------------------------------------")
    print("| {0:<10} | {1:^19} | {2:^13} |" .format("Courier ID", "Courier Name", "Courier Phone"))
    print("---------------------------------------------------")

    for row in rows:
        id = row[0]
        name = row[1]
        number = row[2]

        print("| {0:<10} | {1:<19} | {2:<13} |" . format(id, name, number))
    print("---------------------------------------------------\n")
    cursor.close()

def view_order_table(name):   
    cursor = connection.cursor()
    sql = f"SELECT * FROM {name} ORDER BY order_status_id ASC"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print("\n-------------------------------------------------------------------------------------------------------------------")
    print("| {0:<10} | {1:^13} | {2:^17} | {3:^14} | {4:^10} | {5:^15} | {6:^15} |" .format("Order ID", "Customer Name", "Customer Address","Customer Phone", "Courier ID", "Order Status ID", "Items"))
    print("-------------------------------------------------------------------------------------------------------------------")

    for row in rows:
        id = row[0]
        name = row[1]
        address = row[2]
        phone = row[3]
        c_id = row[4]
        o_id = row[5]
        items = row[6]


        print("| {0:<10} | {1:<13} | {2:<17} | {3:^14} | {4:<10} | {5:<15} | {6:<15} |" . format(id, name, address, phone, c_id, o_id, items))
    print("-------------------------------------------------------------------------------------------------------------------\n")
    cursor.close()

def view_order_status_table(name):   
    cursor = connection.cursor()
    sql = f"SELECT * FROM {name}"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print("\n---------------------------------------")
    print("| {0:<16} | {1:^16} |" .format("Order Status ID", "Order Status"))
    print("---------------------------------------")

    for row in rows:
        id = row[0]
        name = row[1]
        
        print("| {0:<16} | {1:<16} |" . format(id, name))
    print("--------------------------------------\n")
    cursor.close()

def view_customer_table(name):   
    cursor = connection.cursor()
    sql = f"SELECT * FROM {name}"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print("\n--------------------------------------------------------------------------------")
    print("| {0:<11} | {1:^17} | {2:^25} | {3:^14} |" .format("Customer ID", "Customer Name", "Customer Address", "Customer Phone"))
    print("--------------------------------------------------------------------------------")

    for row in rows:
        id = row[0]
        name = row[1]
        address = row[2]
        phone = row[3]

        print("| {0:<11} | {1:<17} | {2:<25} | {3:<14} |" . format(id, name, address, phone))
    print("--------------------------------------------------------------------------------\n")
    cursor.close()


# List functions 

def add_product(list_type):
    try:
        product_name = (input(f"Please enter the {list_type} you want to add to the catalogue: ").title())
        product_price = float(input(f"Please enter the price for {product_name}: "))
        cursor = connection.cursor()
        sql = "INSERT INTO product (product_name, price) VALUES (%s, %s)"
        values = (product_name, product_price)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        view_product_table(list_type)
        print(f"{product_name} has been added to the catalogue")
    except ValueError:
        print(VALUE_ERROR_MESSAGE)
    
def add_courier(list_type):
    try:
        courier_name = (input(f"Please enter the {list_type} name you want to add to the catalogue: ").title())
        courier_phone = (input(f"Please enter the phone number for {courier_name}: "))
        cursor = connection.cursor()
        sql = "INSERT INTO courier (courier_name, courier_phone) VALUES (%s, %s)"
        values = (courier_name, courier_phone)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        view_courier_table(list_type)
        print(f"{courier_name} has been added to the catalogue")
    except ValueError:
        print(VALUE_ERROR_MESSAGE)

def add_order(list_type):
    try:
        customer_name = input("Enter customer name: ").title()
        customer_address = input("Enter customer address: ").title()
        customer_phone = input("Enter customer phone number: ")
        view_courier_table(COURIER)
        courier_id = int(input("Enter courier ID of courier you want for delivery: "))
        order_status_id = 1
        view_product_table(PRODUCTS)
        item_selection = int(input("Please enter the product ID of the item you want: "))
        item_list = [item_selection]
        more_items = input("Would you like to add another item? Enter Y/N:")
        while more_items.upper() == "Y":
           view_product_table(PRODUCTS)
           items = int(input("Please enter the product ID of your additional item: "))
           item_list.append(items)
           more_items = input("Would you like to add another item? Enter Y/N:")
        cursor = connection.cursor()
        sql = "INSERT INTO orders (customer_name, customer_address, customer_phone, courier_id, order_status_id, items) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (customer_name, customer_address, customer_phone, courier_id, order_status_id, json.dumps(item_list))
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        view_order_table(list_type)
        print(f"{customer_name} has been added to the catalogue")
    except ValueError:
        print(VALUE_ERROR_MESSAGE)
    except IndexError:
        print(INDEX_ERROR_MESSAGE)
    except pymysql.err.IntegrityError:
        print("Please enter valid courier and product ID's")

def add_customer(list_type):
    try:
        customer_name = (input(f"Please enter the name of the customer {list_type} you want to add to the catalogue: ").title())
        customer_address = (input(f"Please enter the address for {customer_name}: "))
        customer_phone = (input(f"Please enter the phone number for {customer_name}: "))

        cursor = connection.cursor()
        sql = "INSERT INTO customer (customer_name, customer_address, customer_phone) VALUES (%s, %s, %s)"
        values = (customer_name, customer_address, customer_phone)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        view_customer_table(list_type)
        print(f"{customer_name} has been added to the catalogue")
    except ValueError:
        print(VALUE_ERROR_MESSAGE)

def update_product_table(list_type):
    try:
        view_product_table(list_type)
        print("If you don't want to update a field then leave the field blank and press enter")
        cursor = connection.cursor()
        product_id = int(input(f"Please enter the {list_type} ID you want to update: "))
        result = f"SELECT product_name FROM {list_type} WHERE product_id = {product_id}"
        cursor.execute(result)
        old_name, = cursor.fetchone()
        result_1 = (f"SELECT price FROM {list_type} WHERE product_id = {product_id}")
        cursor.execute(result_1)
        old_price, = cursor.fetchone()
        new_name = input(f"Please enter the new {list_type} name: ").title()
        new_price = input(f"Please enter the {new_name} price: ")

        if len(new_name.strip()) == 0:
            new_name = old_name
        if len(new_price.strip()) == 0:
            new_price = old_price
        
        sql = f"UPDATE {list_type} SET product_name = \"{new_name}\", price = {new_price} WHERE product_id = {product_id}"
        cursor.execute(sql)
        view_product_table
        print(f"Product ID {product_id} details have been updated to {new_name} and {new_price}.")
        connection.commit()
        cursor.close()
        view_product_table(list_type)
           
    except ValueError:
        print(VALUE_ERROR_MESSAGE)    
    except IndexError:
        print(INDEX_ERROR_MESSAGE)
    except pymysql.err.OperationalError:
        print("Invalid data type. Please only enter a float data type...")
    except TypeError:
        print("Invalid entry. Please try again")

def update_courier_table(list_type):
    try:
        view_courier_table(list_type)
        print("If you don't want to update a field then leave the field blank and press enter")
        cursor = connection.cursor()
        courier_id = int(input(f"Please enter the {list_type} ID you want to update: "))
        result = f"SELECT courier_name FROM {list_type} WHERE courier_id = {courier_id}"
        cursor.execute(result)
        old_name, = cursor.fetchone()
        result_1 = (f"SELECT courier_phone FROM {list_type} WHERE courier_id = {courier_id}")
        cursor.execute(result_1)
        old_phone, = cursor.fetchone()
        new_name = input(f"Please enter the new {list_type} name: ").title()
        new_phone = input(f"Please enter the {new_name} phone number: ")

        if len(new_name.strip()) == 0:
            new_name = old_name
        if len(new_phone.strip()) == 0:
            new_phone = old_phone
        
        sql = f"UPDATE {list_type} SET courier_name = \"{new_name}\", courier_phone = \"{new_phone}\" WHERE courier_id = {courier_id}"
        cursor.execute(sql)
        view_courier_table(list_type)
        print(f"Courier ID {courier_id} details have been updated to {new_name} and {new_phone}.")
        connection.commit()
        cursor.close()
           
    except ValueError:
        print(VALUE_ERROR_MESSAGE)    
    except IndexError:
        print(INDEX_ERROR_MESSAGE)
    except TypeError:
        print("Invalid entry. Please try again")

def update_order_status(list_type):
    try:
        view_order_table(list_type)
        cursor = connection.cursor()
        order_id = int(input(f"Please enter the order id for the status you want to update: "))
        sql = f"SELECT * FROM {list_type} WHERE orders_id = {order_id}"
        cursor.execute(sql)
        print(cursor.fetchone())
        print("\n")
        view_order_status_table(ORDER_STATUS)
        status_id = int(input(f"Please enter the new order status ID: "))
        sql = f"UPDATE {list_type} SET order_status_id = {status_id} WHERE orders_id = {order_id}"
        cursor.execute(sql)
        sql = f"SELECT order_status FROM order_status WHERE order_status_id = {status_id}"
        cursor.execute(sql)
        new_status, = cursor.fetchone()
        cursor.execute(sql)
        view_order_table(list_type)
        print(f"Order ID {order_id} status has been updated to order status {new_status}")
        connection.commit()      
        cursor.close() 
        
    except ValueError:
        print(VALUE_ERROR_MESSAGE)    
    except IndexError:
        print(INDEX_ERROR_MESSAGE)
    except TypeError:
        print(VALUE_ERROR_MESSAGE)

def update_order_table(list_type):
    try:
        view_order_table(list_type)
        cursor = connection.cursor()
        order_id = int(input(f"Please enter the {list_type} ID you want to update: "))
        result = f"SELECT * FROM {list_type} WHERE orders_id = {order_id}"
        cursor.execute(result)
        print(cursor.fetchall())
        new_customer_name = input("Please enter the new customer name: ").title()
        new_customer_address = input("Please enter the new address: ").title()
        new_customer_phone = input("Please enter the new phone number: ")
        view_courier_table(COURIER)
        new_courier_id = int(input("Please enter the new courier ID: "))
        view_order_status_table(ORDER_STATUS)
        new_order_status_id = int(input("Please enter new order status ID: "))
        view_product_table(PRODUCTS)
        new_items_selection = int(input("Please enter the new product ID: "))
        new_item_list = [new_items_selection]
        more_items = input("Would you like to add another item? Enter Y/N:")
        while more_items.upper() == "Y":
           view_product_table(PRODUCTS)
           items = int((input("Please enter the product ID of your additional item: ")))
           new_item_list.append(items)
           more_items = input("Would you like to add another item? Enter Y/N:")
        sql = f"""UPDATE {list_type} SET customer_name = \"{new_customer_name}\", customer_address = \"{new_customer_address}\",
        customer_phone = \"{new_customer_phone}\", courier_id = \"{new_courier_id}\", order_status_id = \"{new_order_status_id}\",
        items = \"{(new_item_list)}\"
        WHERE orders_id = {order_id}"""
        cursor.execute(sql)
        view_order_table(list_type)
        print(f"Order ID {order_id} details have been updated to.") 
        connection.commit()
        cursor.close()
           
    except ValueError:
        print(VALUE_ERROR_MESSAGE)    
    except IndexError:
        print(INDEX_ERROR_MESSAGE)
    except TypeError:
        print("Invalid entry. Please try again")

def update_customer_table(list_type):
    try:
        view_customer_table(list_type)
        print("If you don't want to update a field then leave the field blank and press enter")
        cursor = connection.cursor()
        customer_id = int(input(f"Please enter the {list_type} ID you want to update: "))
        result = f"SELECT customer_name FROM {list_type} WHERE customer_id = {customer_id}"
        cursor.execute(result)
        old_customer_name, = cursor.fetchone()
        result_1 = (f"SELECT customer_address FROM {list_type} WHERE customer_id = {customer_id}")
        cursor.execute(result_1)
        old_customer_address, = cursor.fetchone()
        result_2 = f"SELECT customer_phone FROM {list_type} WHERE customer_id = {customer_id}"
        cursor.execute(result_2)
        old_customer_phone, = cursor.fetchone()
        new_customer_name = input(f"Please enter the new {list_type} name: ").title()
        new_customer_address = input(f"Please enter the {new_customer_name} address: ")
        new_customer_phone = input(f"Please enter the {new_customer_name} phone number: ")

        if len(new_customer_name.strip()) == 0:
            new_customer_name = old_customer_name
        if len(new_customer_address.strip()) == 0:
            new_customer_address = old_customer_address
        if len(new_customer_phone.strip()) == 0:
            new_customer_phone = old_customer_phone

        sql = f"""UPDATE {list_type} 
        SET customer_name = \"{new_customer_name}\", customer_address = \"{new_customer_address}\",
        customer_phone = \"{new_customer_phone}\" 
        WHERE customer_id = {customer_id}"""

        cursor.execute(sql)
        view_customer_table(list_type)
        print(f"Customer ID {customer_id} details have been updated to {new_customer_name}, {new_customer_address}, {new_customer_phone}.")
        connection.commit()
        cursor.close()
    except ValueError:
        print(VALUE_ERROR_MESSAGE)    
    except IndexError:
        print(INDEX_ERROR_MESSAGE)
    except pymysql.err.OperationalError:
        print("Error")
    except TypeError:
        print("Invalid entry. Please try again")

def delete_from_table(list_type):
    view_table(list_type)
    try:
        delete_item = int(input(f"Please enter the {list_type} ID you want to delete: "))
        cursor = connection.cursor()
        sql = f"SELECT * FROM {list_type} WHERE {list_type}_id = {delete_item}"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
        sql = f"DELETE FROM {list_type} WHERE {list_type}_id = {delete_item}"
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        view_table(list_type)
        print(f"{result} has been deleted from the {list_type} catalogue.")
    except ValueError:
        print(VALUE_ERROR_MESSAGE) 
    except IndexError:
        print(INDEX_ERROR_MESSAGE)

def delete_from_product_table(list_type):
    try:
        view_product_table(list_type)
        delete_item = int(input(f"Please enter the {list_type} ID you want to delete: "))
        cursor = connection.cursor()
        sql = f"SELECT * FROM {list_type} WHERE {list_type}_id = {delete_item}"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
        sql = f"DELETE FROM {list_type} WHERE {list_type}_id = {delete_item}"
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        view_product_table(list_type)
        print(f"\n{result} has been deleted from the {list_type} catalogue.")
    except ValueError:
        print(VALUE_ERROR_MESSAGE) 
    except IndexError:
        print(INDEX_ERROR_MESSAGE)

def delete_from_courier_table(list_type):
    try:
        view_courier_table(list_type)
        delete_item = int(input(f"Please enter the {list_type} ID you want to delete: "))
        cursor = connection.cursor()
        sql = f"SELECT * FROM {list_type} WHERE {list_type}_id = {delete_item}"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
        sql = f"DELETE FROM {list_type} WHERE {list_type}_id = {delete_item}"
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        view_courier_table(list_type)
        print(f"\n{result} has been deleted from the {list_type} catalogue.")
    except ValueError:
        print(VALUE_ERROR_MESSAGE) 
    except IndexError:
        print(INDEX_ERROR_MESSAGE)

def delete_from_order_table(list_type):
    try:
        view_order_table(list_type)
        delete_item = int(input(f"Please enter the {list_type} ID you want to delete: "))
        cursor = connection.cursor()
        sql = f"SELECT * FROM {list_type} WHERE {list_type}_id = {delete_item}"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
        sql = f"DELETE FROM {list_type} WHERE {list_type}_id = {delete_item}"
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        view_order_table(list_type)
        print(f"{result} has been deleted from the {list_type} catalogue.")
    except ValueError:
        print(VALUE_ERROR_MESSAGE) 
    except IndexError:
        print(INDEX_ERROR_MESSAGE)

def delete_from_customer_table(list_type):
    try:
        view_customer_table(list_type)
        delete_item = int(input(f"Please enter the {list_type} ID you want to delete: "))
        cursor = connection.cursor()
        sql = f"SELECT * FROM {list_type} WHERE {list_type}_id = {delete_item}"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
        sql = f"DELETE FROM {list_type} WHERE {list_type}_id = {delete_item}"
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        view_customer_table(list_type)
        print(f"\n{result} has been deleted from the {list_type} catalogue.")
    except ValueError:
        print(VALUE_ERROR_MESSAGE) 
    except IndexError:
        print(INDEX_ERROR_MESSAGE)


# Menu functions 

def main_menu():
    print("----------------------")
    print("Main Menu\n")
    print("0: Exit App")
    print("1: Product Menu")
    print("2: Courier Menu")
    print("3: Order Menu")
    print("4: Customer Menu \n")
    print("----------------------")

def list_menu(name):
    print("-------------------------------")
    print(f"{name} Menu Options \n")
    print(f"0: Return to Main Menu")
    print(f"1: Display {name} Catalogue")
    print(f"2: Create {name}")
    print(f"3: Update {name}")
    print(f"4: Delete {name} \n")
    print("-------------------------------")

def order_menu(name):
    print("-------------------------------")
    print(f"{name} Menu Options \n")
    print(f"0: Return to Main Menu")
    print(f"1: Display {name} Catalogue")
    print(f"2: Create {name}")
    print(f"3: View {ORDER_STATUS} Table")
    print(f"4: Update {name} Status")
    print(f"5: Update {name}")
    print(f"6: Delete {name} \n")
    print("-------------------------------")

def list_product_menu(list_type):
    list_menu_count = 5
    while True:
        list_menu(list_type.title())
        try:
            menu_option = int(input(CHOOSE_OPTION_MESSAGE))
        except ValueError:
            print(VALUE_ERROR_MESSAGE)
            continue
        if menu_option not in range(list_menu_count):
            print(INVALID_OPTION_MESSAGE)
        if menu_option == 0:
            break
        elif menu_option == 1:
            print(view_product_table(list_type), "\n")
        elif menu_option == 2:
            add_product(list_type)
        elif menu_option == 3:
            update_product_table(list_type)
        elif menu_option == 4:
            delete_from_product_table(list_type)

def list_courier_menu(list_type):
    list_menu_count = 5
    while True:
        list_menu(list_type.title())
        try:
            menu_option = int(input(CHOOSE_OPTION_MESSAGE))
        except ValueError:
            print(VALUE_ERROR_MESSAGE)
            continue
        if menu_option not in range(list_menu_count):
            print(INVALID_OPTION_MESSAGE)
        if menu_option == 0:
            break
        elif menu_option == 1:
            print(view_courier_table(list_type), "\n")
        elif menu_option == 2:
            add_courier(list_type)
        elif menu_option == 3:
            update_courier_table(list_type)
        elif menu_option == 4:
            delete_from_courier_table(list_type)

def list_order_menu(list_type):
    list_menu_count = 7
    while True:
        order_menu(list_type.title())
        try:
            menu_option = int(input(CHOOSE_OPTION_MESSAGE))
        except ValueError:
            print(VALUE_ERROR_MESSAGE)
            continue
        if menu_option not in range(list_menu_count):
            print(INVALID_OPTION_MESSAGE)
        if menu_option == 0:
            break
        elif menu_option == 1:
            print(view_order_table(list_type), "\n")
        elif menu_option == 2:
            add_order(list_type)
        elif menu_option == 3:
            view_order_status_table(ORDER_STATUS)
        elif menu_option == 4:
            update_order_status(list_type)
        elif menu_option == 5:
            update_order_table(list_type)
        elif menu_option == 6:
            delete_from_order_table(list_type)
        
def list_customer_menu(list_type):
    list_menu_count = 5
    while True:
        list_menu(list_type.title())
        try:
            menu_option = int(input(CHOOSE_OPTION_MESSAGE))
        except ValueError:
            print(VALUE_ERROR_MESSAGE)
            continue
        if menu_option not in range(list_menu_count):
            print(INVALID_OPTION_MESSAGE)
        if menu_option == 0:
            break
        elif menu_option == 1:
            print(view_customer_table(list_type), "\n")
        elif menu_option == 2:
            add_customer(list_type)
        elif menu_option == 3:
            update_customer_table(list_type)
        elif menu_option == 4:
            delete_from_customer_table(list_type)


# Cafe App 
def main():
    main_menu_count = 6
    print("Welcome to the Cafe App")
    while True:
        main_menu()
        try:
            main_menu_option = int(input(CHOOSE_OPTION_MESSAGE))
        except ValueError:
            print(VALUE_ERROR_MESSAGE)
            continue
        if main_menu_option not in range(main_menu_count):
            print(INVALID_OPTION_MESSAGE)
        if main_menu_option == 0:
            connection.close()   
            print("Exiting App")
            quit()
        elif main_menu_option == 1:
            list_product_menu(PRODUCTS)
        elif main_menu_option == 2:
            list_courier_menu(COURIER)
        elif main_menu_option == 3:
            list_order_menu(ORDER)
        elif main_menu_option == 4:
            list_customer_menu(CUSTOMER)

        

        
main()