# EEData Synthetic Data Generator
# Generates data for users, items, carts, orders, and returns

import csv
from datetime import datetime
from datetime import timedelta
from faker import Faker
import random


users_table: list = []
items_table: list = []
carts_table: list = []
orders_table: list = []
returns_table: list = []
items_date_listed: list = []
item_price_list: list = []
item_shipping_price_list: list = []
number_of_carts_ordered: list = []
advertisement_list: list = []

def main():
    print("Synthetic data generator for the tables: Users, Items, Carts, Orders, and Returns")
    while True:
        try:
            enter = int(input("Enter the number of rows to create: "))
            break
        except ValueError:
            pass
    
    fake = Faker()

    # Items data
    items = ["monitor", "mouse", "keyboard", "charger", "USB", "ebook", "game", "program", "plug-in", "webinar", "chair", "desk", "rug", "lamp", "shelf"]
    
    item_set: set = set()
    item_counter = 0
    for unique in items:
        item_counter = item_counter + 1
        if unique not in item_set:
            item_set.add(unique)
            # Set before overwriting
            random_shipping_price = round(random.uniform(1,25),2)

            match unique:
                case "monitor" | "mouse" | "keyboard" | "charger" | "USB":
                    item_type = "technology"

                case "ebook" | "game" | "program" | "plug-in" | "webinar":
                    item_type = "software"
                    random_shipping_price = 0

                case "chair" | "desk" | "rug" | "lamp" | "shelf":
                    item_type = "office"

            item_shipping_price_list.append(random_shipping_price)

            random_item_price = round(random.uniform(50,500),2)
            item_price_list.append(random_item_price)

            random_description_length = random.randint(10,500)
            random_reviews = random.randint(0,10000)
            random_product_images = random.randint(0,25)
            random_product_videos = random.randint(0,15)
            advertisement = random.randint(0,50000)
            advertisement_list.append(advertisement)

            # New items posted
            starting_date = datetime(2025,3,1).date()
            items_lastpost_date = datetime(2025,1,31).date()
            items_posted_date = datetime(2025,1,1).date()
            items_date = fake.date_between(start_date=items_posted_date, end_date=items_lastpost_date)
        
            # Items table data
            items_table.append({"id":item_counter, "name":unique, "type":item_type, "price":f"{random_item_price:.2f}", "shipping_price":f"{random_shipping_price:.2f}", "description_length":random_description_length, "reviews":random_reviews, "product_images":random_product_images, "product_videos":random_product_videos, "advertisement":advertisement, "date_listed":items_date})
            total = round(random_item_price + random_shipping_price,2)
            print(f"Item: {item_counter}, Total Amount: {total:.2f}")

    # Populate users, carts, orders, and returns data via user input
    num = enter

    # ID counter for the returns table
    id_counter: list = []
    for idcount in range(num):
        idcount = idcount + 1
        id_counter.append(idcount)

    return_counter = 0
    store_users: set = set()
    for i in range(num):
        # Fixed 15 items for sale
        item_id = random.sample(range(1,16),1)[0]
        print(f"User ID: {i+1}", end="\n")
        username = f"{fake.user_name()}{random.randint(1,num)}"
        email = "@" + fake.free_email_domain()
        print(username)
        print(username + email)
        address = fake.street_address()
        state = fake.state()
        print(f"Address: {address} State: {state}")
        
        # Avoid duplicate names or email addresses via a set
        while True:
            if username not in store_users:
                store_users.add(username)
                break
            else:
                username = f"{fake.user_name()}{random.randint(1,num)}"

        # Review customers on the last month of the quarter
        starting_date = datetime(2025,3,1).date()
        items_posted_date = datetime(2025,1,1).date()

        date_account_created = fake.date_between(start_date=starting_date, end_date="-1d")
        date_last_login = fake.date_between(start_date=starting_date, end_date="-1d")
        date_recent_login = fake.date_between(start_date=starting_date, end_date="-1d")
        date_order_status = fake.date_between(start_date="today", end_date="+5d")
        print("Carts Table: date_created:", date_recent_login)

        random_quantity = random.randint(1,50)
        order_status = random.choices(["processing", "pending", "shipped"], k=1)[0]

        # Let 10% of orders be returns
        weight_returned = random.choices(["returned", "kept"], weights=[10,90], k=1)[0]

        # Set and map random item prices to the orders table
        if item_id == 1:
            get_item_price = item_price_list[0]
            get_item_shipping_price = item_shipping_price_list[0]
            total_order_amount = round((get_item_price*random_quantity)+get_item_shipping_price,2)
            get_advertisement_price = advertisement_list[0]

        elif item_id == 2:
            get_item_price = item_price_list[1]
            get_item_shipping_price = item_shipping_price_list[1]
            total_order_amount = round((get_item_price*random_quantity)+get_item_shipping_price,2)
            get_advertisement_price = advertisement_list[1]

        elif item_id == 3:
            get_item_price = item_price_list[2]
            get_item_shipping_price = item_shipping_price_list[2]
            total_order_amount = round((get_item_price*random_quantity)+get_item_shipping_price,2)
            get_advertisement_price = advertisement_list[2]

        elif item_id == 4:
            get_item_price = item_price_list[3]
            get_item_shipping_price = item_shipping_price_list[3]
            total_order_amount = round((get_item_price*random_quantity)+get_item_shipping_price,2)
            get_advertisement_price = advertisement_list[3]

        elif item_id == 5:
            get_item_price = item_price_list[4]
            get_item_shipping_price = item_shipping_price_list[4]
            total_order_amount = round((get_item_price*random_quantity)+get_item_shipping_price,2)
            get_advertisement_price = advertisement_list[4]

        elif item_id == 6:
            get_item_price = item_price_list[5]
            get_item_shipping_price = item_shipping_price_list[5]
            total_order_amount = round((get_item_price*random_quantity)+get_item_shipping_price,2)
            get_advertisement_price = advertisement_list[5]

        elif item_id == 7:
            get_item_price = item_price_list[6]
            get_item_shipping_price = item_shipping_price_list[6]
            total_order_amount = round((get_item_price*random_quantity)+get_item_shipping_price,2)
            get_advertisement_price = advertisement_list[6]

        elif item_id == 8:
            get_item_price = item_price_list[7]
            get_item_shipping_price = item_shipping_price_list[7]
            total_order_amount = round((get_item_price*random_quantity)+get_item_shipping_price,2)
            get_advertisement_price = advertisement_list[7]

        elif item_id == 9:
            get_item_price = item_price_list[8]
            get_item_shipping_price = item_shipping_price_list[8]
            total_order_amount = round((get_item_price*random_quantity)+get_item_shipping_price,2)
            get_advertisement_price = advertisement_list[8]

        elif item_id == 10:
            get_item_price = item_price_list[9]
            get_item_shipping_price = item_shipping_price_list[9]
            total_order_amount = round((get_item_price*random_quantity)+get_item_shipping_price,2)
            get_advertisement_price = advertisement_list[9]

        elif item_id == 11:
            get_item_price = item_price_list[10]
            get_item_shipping_price = item_shipping_price_list[10]
            total_order_amount = round((get_item_price*random_quantity)+get_item_shipping_price,2)
            get_advertisement_price = advertisement_list[10]

        elif item_id == 12:
            get_item_price = item_price_list[11]
            get_item_shipping_price = item_shipping_price_list[11]
            total_order_amount = round((get_item_price*random_quantity)+get_item_shipping_price,2)
            get_advertisement_price = advertisement_list[11]

        elif item_id == 13:
            get_item_price = item_price_list[12]
            get_item_shipping_price = item_shipping_price_list[12]
            total_order_amount = round((get_item_price*random_quantity)+get_item_shipping_price,2)
            get_advertisement_price = advertisement_list[12]

        elif item_id == 14:
            get_item_price = item_price_list[13]
            get_item_shipping_price = item_shipping_price_list[13]
            total_order_amount = round((get_item_price*random_quantity)+get_item_shipping_price,2)
            get_advertisement_price = advertisement_list[13]
        
        elif item_id == 15:
            get_item_price = item_price_list[14]
            get_item_shipping_price = item_shipping_price_list[14]
            total_order_amount = round((get_item_price*random_quantity)+get_item_shipping_price,2)
            get_advertisement_price = advertisement_list[14]

        # Set weights for advertisement
        if get_advertisement_price <= 20000:
                cart_ordered = random.choices([0,1], weights=[100,0], k=1)[0]
        elif 30000 > get_advertisement_price > 20000:
            cart_ordered = random.choices([0,1], weights=[50,50], k=1)[0]
        elif get_advertisement_price >= 30000:
            cart_ordered = random.choices([0,1], weights=[0,100], k=1)[0]

        # Dates can all be the same, otherwise sort oldest to newest
        if date_account_created == date_last_login == date_recent_login == date_order_status:
            # Append carts for sum
            number_of_carts_ordered.append(cart_ordered)

            print("Carts Table: date_created:", date_recent_login)
            print(f"Cart Table: become_orders INT: {cart_ordered}", end="")
            print(date_account_created, "Users table: date_account_created")
            print(date_last_login, "Users table: date_last_login")
            print(date_recent_login, "Users table: date_recent_login")
            print(date_order_status, "Orders table: date_order_status")
            print(items_date, "Items table: items_date")

            if cart_ordered == 1:
                print(" - Cart became an order with INT 1")
                
                # Order table data
                orders_table.append({"id":item_counter, "cart_id": i+1, "item_quantity":random_quantity, "total_amount":f"{total_order_amount:.2f}", "date_placed":date_recent_login, "order_status":order_status, "date_order_status":date_order_status})
                # Cart table data
                carts_table.append({"id":i+1, "user_id":i+1, "item_id":item_id, "date_created":date_recent_login, "date_cart_transition":date_recent_login, "became_order":cart_ordered})

                if weight_returned == "kept":
                    print("Customer kept the order. There will be no return date displayed.")
                    pass
                else:
                    print(f"User ID: {i+1}")
                    date_item_returned = fake.date_between(start_date="+5d", end_date="+10d")
                    print(date_item_returned, "date_item_returned")

                    # Only shipped orders can be returned and the return ID must not exceed the number of placed orders
                    if order_status == "shipped":
                        item_return_reason = random.choices(["damaged", "quality issues", "incorrect item", "not needed"], k=1)[0]

                        # Change software items to have different return reasons
                        if item_id == 6 or item_id == 7 or item_id == 8 or item_id == 9 or item_id == 10:
                            item_return_reason = random.choices(["quality issues", "incorrect item"], k=1)[0]
                        date_item_returned = fake.date_between(start_date="+5d", end_date="+10d")
                        return_counter = return_counter + 1

                        # Return table data
                        returns_table.append({"id":return_counter, "order_id":i+1, "reason": item_return_reason, "date_returned":date_item_returned})
                    else:
                        pass
            else:
                # Users can remove created carts on the date_recent_login and carts will expire 7 days after the date they were created
                cart_transition_choice = random.choices([date_recent_login,(date_recent_login + timedelta(days=7))],k=1)[0]
                carts_table.append({"id":i+1, "user_id":i+1, "item_id":item_id, "date_created":date_recent_login, "date_cart_transition":cart_transition_choice, "became_order":cart_ordered})

                # Cart did not become an order. There will not be an order status date or date returned
                print(" - Cart did not become an order with INT 0")
                print(date_account_created, "Users table: date_account_created")
                print(date_last_login, "Users table: date_last_login")
                print(date_recent_login, "Users table: date_recent_login")
                print(date_order_status, "Orders table: date_order_status")
                print(items_date, "Items table: items_date")

            # Users table data
            users_table.append({"id":i+1, "username":username, "email":username+email, "address":address, "state":state, "date_account_created":date_account_created, "date_last_login":date_last_login, "date_recent_login":date_recent_login})

        elif date_account_created <= date_last_login <= date_recent_login <= date_order_status:
            # Append cart for sum
            number_of_carts_ordered.append(cart_ordered)
            print("Carts Table: date_created:", date_recent_login)
            print(f"Cart Table: become_orders INT: {cart_ordered}", end="")

            if cart_ordered == 1:
                print(" + Cart became an order with INT 1")
                print(date_account_created, "Users table: date_account_created")
                print(date_last_login, "Users table: date_last_login")
                print(date_recent_login, "Users table: date_recent_login")
                print(date_order_status, "Orders table: date_order_status")
                print(items_date, "Items table: items_date")

                # Order table data
                orders_table.append({"id":item_counter, "cart_id": i+1, "item_quantity":random_quantity, "total_amount":f"{total_order_amount:.2f}", "date_placed":date_recent_login, "order_status":order_status, "date_order_status":date_order_status})
                # Cart table data
                carts_table.append({"id":i+1, "user_id":i+1, "item_id":item_id, "date_created":date_recent_login, "date_cart_transition":date_recent_login, "became_order":cart_ordered})
                
                if weight_returned == "kept":
                    print("Customer kept the order. There will be no return date displayed.")
                    pass
                else:
                    print(f"User ID: {i+1}")
                    date_item_returned = fake.date_between(start_date="+5d", end_date="+10d")
                    print(date_item_returned, "date_item_returned")

                    # Only shipped orders can be returned and the return ID must not exceed the number of placed orders
                    if order_status == "shipped":
                        item_return_reason = random.choices(["damaged", "quality issues", "incorrect item", "not needed"], k=1)[0]

                        # Change software items to have different return reasons
                        if item_id == 6 or item_id == 7 or item_id == 8 or item_id == 9 or item_id == 10:
                            item_return_reason = random.choices(["quality issues", "incorrect item"], k=1)[0]
                        date_item_returned = fake.date_between(start_date="+5d", end_date="+10d")
                        return_counter = return_counter + 1
                        
                        # Return table data
                        returns_table.append({"id":return_counter, "order_id":i+1, "reason": item_return_reason, "date_returned":date_item_returned})
                    else:
                        pass
            else:
                # Users can remove created carts on the date_recent_login and carts will expire 7 days after the date they were created
                cart_transition_choice = random.choices([date_recent_login,(date_recent_login + timedelta(days=7))],k=1)[0]
                carts_table.append({"id":i+1, "user_id":i+1, "item_id":item_id, "date_created":date_recent_login, "date_cart_transition":cart_transition_choice, "became_order":cart_ordered})

                # Cart did not become an order. There will not be an order status date or date returned
                print(" - Cart did not become an order with INT 0")
                print(date_account_created, "Users table: date_account_created")
                print(date_last_login, "Users table: date_last_login")
                print(date_recent_login, "Users table: date_recent_login")
                print(date_order_status, "Orders table: date_order_status")
                print(items_date, "Items table: items_date")

            # Users table data
            users_table.append({"id":i+1, "username":username, "email":username+email, "address":address, "state":state, "date_account_created":date_account_created, "date_last_login":date_last_login, "date_recent_login":date_recent_login})
        else:
            while date_account_created > date_last_login or date_last_login > date_recent_login or date_recent_login > date_order_status:
                date_account_created = fake.date_between(start_date=starting_date, end_date="-1d")
                date_last_login = fake.date_between(start_date=starting_date, end_date="-1d")
                date_recent_login = fake.date_between(start_date=starting_date, end_date="-1d")
                date_order_status = fake.date_between(start_date=starting_date, end_date="-1d")
                date_item_returned = fake.date_between(start_date="+5d", end_date="+10d")

                # Let 10% of orders be returns
                weight_returned = random.choices(["returned", "kept"], weights=[10,90], k=1)[0]

                if date_account_created <= date_last_login <= date_recent_login <= date_order_status:
                    number_of_carts_ordered.append(cart_ordered)
                    print("Carts Table: date_created:", date_recent_login)
                    print(f"Cart Table: become_orders as an INT: {cart_ordered}", end="")
                    if cart_ordered == 1:
                        print(" + Cart became an order with INT 1")
                        print(date_account_created, "Users table: date_account_created")
                        print(date_last_login, "Users table: date_last_login")
                        print(date_recent_login, "Users table: date_recent_login")
                        print(date_order_status, "Orders table: date_order_status")
                        print(items_date, "Items table: items_date")

                        # Order table data
                        orders_table.append({"id":item_counter, "cart_id": i+1, "item_quantity":random_quantity, "total_amount":f"{total_order_amount:.2f}", "date_placed":date_recent_login, "order_status":order_status, "date_order_status":date_order_status})
                        # Cart table data
                        carts_table.append({"id":i+1, "user_id":i+1, "item_id":item_id, "date_created":date_recent_login, "date_cart_transition":date_recent_login, "became_order":cart_ordered})
                
                        if weight_returned == "kept":
                            print("Customer kept the order. There will be no return date displayed.")
                            pass
                        else:
                            print(f"User ID: {i+1}")
                            date_item_returned = fake.date_between(start_date="+5d", end_date="+10d")
                            print(date_item_returned, "date_item_returned")

                            # Only shipped orders can be returned and the return ID must not exceed the number of placed orders
                            if order_status == "shipped":
                                item_return_reason = random.choices(["damaged", "quality issues", "incorrect item", "not needed"], k=1)[0]

                                # Change software items to have different return reasons
                                if item_id == 6 or item_id == 7 or item_id == 8 or item_id == 9 or item_id == 10:
                                    item_return_reason = random.choices(["quality issues", "incorrect item"], k=1)[0]
                                date_item_returned = fake.date_between(start_date="+5d", end_date="+10d")
                                return_counter = return_counter + 1

                                # Return table data
                                returns_table.append({"id":return_counter, "order_id":i+1, "reason": item_return_reason, "date_returned":date_item_returned})
                            else:
                                pass
                    else:
                        # Users can remove created carts on the date_recent_login and carts will expire 7 days after the date they were created
                        cart_transition_choice = random.choices([date_recent_login,(date_recent_login + timedelta(days=7))],k=1)[0]
                        carts_table.append({"id":i+1, "user_id":i+1, "item_id":item_id, "date_created":date_recent_login, "date_cart_transition":cart_transition_choice, "became_order":cart_ordered})

                        # Cart did not become an order. There will not be an order status date or date returned
                        print(" - Cart did not become an order with INT 0")
                        print(date_account_created, "Users table: date_account_created")
                        print(date_last_login, "Users table: date_last_login")
                        print(date_recent_login, "Users table: date_recent_login")
                        print(date_order_status, "Orders table: date_order_status")
                        print(items_date, "Items table: items_date")

                    # Users table data
                    users_table.append({"id":i+1, "username":username, "email":username+email, "address":address, "state":state, "date_account_created":date_account_created, "date_last_login":date_last_login, "date_recent_login":date_recent_login})
                    break
        print()
        print("Total number of carts ordered:", sum(number_of_carts_ordered))
        print()

    cart_id_ints: list = []
    # Update orders table ID column counter
    restart_order_count = 0
    for i in orders_table:
        restart_order_count = restart_order_count + 1
        i["id"] = restart_order_count
        cart_id_ints.append(i["cart_id"])

    # Index the orders table cart_id to display the return order_id
    for order in returns_table:
        print("Cart ID:", order["order_id"],"Order ID:", (cart_id_ints.index(order["order_id"])+1))
        indexkey = cart_id_ints.index(order["order_id"])+1        
        order["order_id"] = indexkey

    display_users_data()
    display_items_data()
    display_carts_data()
    display_orders_data()
    display_returns_data()

    users_table_csv()
    items_table_csv()
    carts_table_csv()
    orders_table_csv()
    returns_table_csv()


# Display the data from each table
def display_users_data():
    print("Users Table")
    for _ in users_table:
        print(_)


def display_items_data():
    print("Items Table")
    for _ in items_table:
        print(_)


def display_carts_data():
    print("Carts Table")
    for _ in carts_table:
        print(_)


def display_orders_data():
    print("Orders Table")
    for _ in orders_table:
        print(_)


def display_returns_data():
    print("Returns Table")
    for _ in returns_table:
        print(_)
    if len(returns_table) == 0:
        print("No returns were made")


# Users Table CSV Data
def users_table_csv():
    with open("../data/users.csv", "w", newline="\n") as file:
        headers = ["id","username","email","address","state","date_account_created","date_last_login","date_recent_login"]
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for user in users_table:
            writer.writerow({"id":user["id"],"username":user["username"],"email":user["email"],"address":user["address"], "state":user["state"],"date_account_created":user["date_account_created"],"date_last_login":user["date_last_login"],"date_recent_login":user["date_recent_login"]})


# Items Table CSV Data
def items_table_csv():
    with open("../data/items.csv", "w", newline="\n") as file:
        headers = ["id","name","type","price","shipping_price","description_length","reviews","product_images","product_videos","advertisement","date_listed"]
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for item in items_table:
            writer.writerow({"id":item["id"],"name":item["name"],"type":item["type"],"price":item["price"],"shipping_price":item["shipping_price"],"description_length":item["description_length"],"reviews":item["reviews"],"product_images":item["product_images"],"product_videos":item["product_videos"],"advertisement":item["advertisement"],"date_listed":item["date_listed"]})


# Carts Table CSV Data
def carts_table_csv():
    with open("../data/carts.csv", "w", newline="\n") as file:
        headers = ["id","user_id","item_id","date_created", "date_cart_transition", "became_order"]
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for cart in carts_table:
            writer.writerow({"id":cart["id"],"user_id":cart["user_id"],"item_id":cart["item_id"],"date_created":cart["date_created"],"date_cart_transition":cart["date_cart_transition"],"became_order":cart["became_order"]})


# Orders Table CSV Data
def orders_table_csv():
    with open("../data/orders.csv", "w", newline="\n") as file:
        headers = ["id","cart_id","item_quantity","total_amount","date_placed","order_status","date_order_status"]
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for order in orders_table:
            writer.writerow({"id":order["id"],"cart_id":order["cart_id"],"item_quantity":order["item_quantity"],"total_amount":order["total_amount"],"date_placed":order["date_placed"],"order_status":order["order_status"],"date_order_status":order["date_order_status"]})


# Returns Table CSV Data
def returns_table_csv():
    with open("../data/returns.csv", "w", newline="\n") as file:
        headers = ["id","order_id","reason","date_returned"]
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for returnable in returns_table:
            writer.writerow({"id":returnable["id"],"order_id":returnable["order_id"],"reason":returnable["reason"],"date_returned":returnable["date_returned"]})


if __name__ == "__main__":
    main()