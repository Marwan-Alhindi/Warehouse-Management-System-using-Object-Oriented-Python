"""
    Made By: Marwan Alhindi
    Created On: 4 Sep 2022
    Finished On: 9 Sep 2022

    Overview:
    This file/assignment is to develop programming and problem solving skills. It introduce concepts such as loops, arrays, and methods.

    [] is used in comments to reference a line.
    {} is used in comments to reference a loop.

    File goals:
    This file is a simple program for a grocery store shop to manage its inventory where an assumption has been made that the user input is always valid. The program file is written to develop the following skills:
    1. Follow coding, convention and behavioral requirements provided in this document and in the lessons.
    2. Independently solve a problem by using programming concepts taught over the first several weeks of the course.
    3. Write and debug Python code independently.
    4. Document code.
    5. Ability to provide references where due.
    6. Meeting deadlines.
    7. Seeking clarification from your “supervisor” (instructor) when needed via discussion forums.
    8. Create a program by recalling concepts taught in class, understanding and applying concepts relevant to solution, analysing components of the problem, evaluating different approaches.
    9. Demonstrate knowledge of basic concepts, syntax and control structures in programming.
    10. Devise solutions to simple computing problems under specific requirements.
    11. Encode the devised solutions into computer programs and test the programs on a computer.
    12. Demonstrate understanding of standard coding conventions and ethical considerations in programming.

    Documentation Style:
    I have used PEP 8 style guide for Python Code. I have also tried to follow PEP 20 - The Zen of Python
    https://peps.python.org/pep-0008/
    https://peps.python.org/pep-0020/ or import this to view in terminal

    What I have learnt:
    1- When you change one word/variable in the program, make sure that you have changed all of them. The shortcut to do this is to select a word/variable and then click F2.
    2- Do not comment and program simultaneously. This will make your thinking about solving an issue harder. Solve the issue logically and then comment how the program flow and the way you solved the issue.
    3- The way you solved majority of issues that you have faced during this project is:
        1- Read the instructions of what you have been asked to do VERY CAREFULLY and asks questions if you dont know exactly the requirements. A single word from the instructions can change what you are supposed to program. Dont just read the instructions one by one, make sure that you read them through all together so that you can understand how the program can be connected.
        2- Naming variables correctly in a way that you can understand can make discovering issues with the program and debug it easier. This is really important because sometimes you tend to forget how you wrote the code.
        3- Check for syntax errors and errors if you are not using the right functions or keywords.
        4- Make sure that the flow of program matches the logic of the problem you are trying to solve. Do you choose if-else or if-if-else or if-elif-else? There are many options to control the flow of the program.
        5- If you think the flow of the program is correct and the issue was not solved, dont just trust your idea of how the program should flow, DEBUG!
    4- Be efficient! When there's a function that you can import from someone else or use, then embrace their work and use it! A really good example of this is when you used isinstance() function.
    5- When you wrap up and stop working on the project, write a docstring at the end of the document to remind you the next time you open the project where you stop at and what you can do next.
    6- It's really important to create versions when you develop a project. Your mind comes with new ideas all the time. You might think the new idea will develop the program but sometimes you dont have the required knowledge to implement it or even if you developed it, the old idea might turn to be better.
    7- To make the code more readable, create functions for any repetitive code.
    8- Seperate functions to the logic of the program. Unfourtantly, you cant do that in this project, but generally speaking its a a good way to make the code more readable.
    9- Dont fall in the trap that finishing a project in one long interval is more efficient, fresh starts brings fresh ideas. Do the project on seperate days.
    10- When you finish the program, write a full story such as the following. This will make sure that you did not miss requirements:
        - Story
    11- To not get lost on what to do, writing list of tasks can help. But also sometimes applying tasks method can make coding harder! An example of this is when you was trying to write the order sumamry for a new purchase:
            # 1- know if customer is old or new to apply discount.
            # 2- get the price of each entered item and store it in a list by using .index method
            # 3- get the quantity of each item and store it in a list.
            # 4- create a price list where the price of each item purchase is item * quantity
            # 5- using the quantity of each item, multiply the quantities with the item unit price and store that in a list
            # 6- sum up the list for the total price.
            # 7- print a statement for the order history
    12- Check the program flow for an if-else inside an if-else in new_purchase function. This is a good program flow. Which condition you should put first? A really good example of this is the if-if-if-if statements in update_products function.
    13- When you construct a while loop, make sure you use the right condition. You can use while flag: or while True:. The difference is that when you use while flag, the flag changes and continue the code then the loop stops. But if you used while True and break, it instantly breaks.
    14- Dont try to fix code when you are tired, you only gonna make it worse.
    15- Print statements can be a really good way to test code and check things working as expected!
    16- If the structure of the basic features are built correctly, adding more complex features can be easier. This is because complex features could be dependant on the basic/initial features. So, make sure you get the basics correctly so that when you develop new features, you dont need to debug the old ones often.
    17- You can go to a line instantly by using the following shortcut: Ctrl+G and then type the line number.
    18- Make sure that you first understood the task clearly and then create an algorithm that make sense with the task. If you didnt understand the task clearly, you will write code that is wasted. An example where you did this is when you tried to create the table of most valuable customer:
        each_item_totalPrice = product_history.copy()
        for i in range(len(product_history)):
            for j in range(len(product_history[i])):
                single_item = product_history[i][j]
                single_item_index = products_glob.index(single_item)
                single_item_price = float(prices_glob[single_item_index])
                one_quantity = float(quantity_history[i][j])
                each_item_totalPrice[i][j] = single_item_price*one_quantity
        print(each_item_totalPrice)
    19- When you create list of lists make sure you do it the right way because if you didnt, each item in the list of lists might have the same id and so you cant change each item by itself. You can use the function id() to check the reference
    20- To iterate through two lists at the same time, use zip() function:
        for product,quantity in zip(product_list,quantity_list):
    21- Don't forget your health when you are so involved in code! Good health = Good code! :3
    22- After I have done the entire assignment, I showed my code to a friend of mine that studied software engineering in Monash University and reminded me of using dictionaries. Would I have efficient code if I used them?! The good side of this is that I practiced using lists A LOT now.
"""

# function add used in [210] in valuable_customer() function
from operator import add

# Variables. The main object used for storing are lists.
# variables that end with _glob are responsible to store unique items. 
# variables that end with history are used to store the order history.
customers_glob = ["Linda","Jack","Zoran"] 
products_glob = ["apple","banana","cake"]
prices_glob = ["3.5","6.82","23"] 
stock_glob = ["134","52","5"]
customer_for_purchase_glob = '' # a global variable that is used for new_purchase() and proceeding_purchase().
is_old_glob = None # a variable that hold the state of the customer either new or old to apply the discount.
free_items_glob = [] # variable for the free items given to old customers.
tracking_free = [] # variable to make sure that customers who had free items before cannot have once more.
customer_history = [] 
product_history = []
total_price_history = []
quantity_history = []


def display_main_menu():
    """Displaying main menu:

    Void function.

    This function is to display the options in the main menu, and based on user choice it apply the appropriate function to display the right informations for the user.
    """
    print("-------------------------")
    print("Main Menu")
    print("1: View Existent Customers")
    print("2: View Products And Their Pricing")
    print("3: Enter a new purchase")
    print("4: View all orders history")
    print("5: Update Products")
    print("6: Increase stock of a product")
    print("7: View total orders by each customer")
    print("0: Quit")
    print("-------------------------")

    # A while loop that break after the user make the correct choice. If the input is wrong, a informative message will represent to the user.
    choice = -1
    while True:
        try:
            choice = int(input("Option: "))
            if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5 or choice == 6 or choice == 7 or choice == 0:
                break
            else: # if the number is not from the options error message
                print("Error: Invalid option")
        except ValueError: # String or characters error message
            print("Error: Only numbers are accepted")
    
    # All menu options and their functions
    if choice == 1:
        display_customers_menu()
    elif choice == 2:
        display_products_menu()
    elif choice == 3:
        new_purchase()
    elif choice == 4:
        orders_history()
    elif choice == 5:
        update_products()
    elif choice == 6:
        replenish_one()
    elif choice == 7:
        valuable_customer()
    elif choice == 0:
        end_program()


def valuable_customer():
    """Displaying table with information:

    Void function.

    This function is used to display a table to the user which have the following informations:
        1- The quantity of all products that has been ordered by each customer.
        2- All customer names
        3- The total price that the customer has paid.
    """
    # length of row and columns of the table based on customers and products
    col_len = len(customers_glob) + 1 
    row_len = len(products_glob) + 2
    
    # creating appropriate table to append info and display
    table = []
    for i in range(col_len):
        table.append([])
    
    # this counter is used to append to the table the correct customer
    count = -2

    # this counter is later assigned to the quantity of the product
    product_counter = [0] * (row_len - 2)

    # see [206] to [212] and [218]. The combination of this list and an if condition statement, make sure that the product_counter list does not append multiple times.
    allowing_if_condition = [False] * len(customers_glob)

    customer_glob_index = -1

    for i in range(col_len): # this is the first loop {1}. col_len is used because this outer loop will run for each row in the table
        count += 1 
        # skip the first iteration
        if i == 0:
            continue
        else: # after the first iteration
            table[i].append(customers_glob[count])
            # this index is responsible to change allowing_if_condition to True so that multiple appending for product quantities does not occur. see [206] to [212] and [218].
            customer_glob_index += 1

            # this index is responsible to pick the correct product and quantity inside the loop
            customer_index = -1
            for customer in customer_history: # this is the second loop {2}. This for loop is to iterate through customer_history and append all quantities the customer bought.

                customer_index += 1

                # if condition to append quantities and total price in the correct row based on customer name
                if customer == table[i][0]:
                    product_list = product_history[customer_index]
                    quantity_list = quantity_history[customer_index]
                    total_price = total_price_history[customer_index]

                    for product,quantity in zip(product_list,quantity_list): # this is the third loop {3}. After getting the correct lists for the products and their quantities, this loop is responsible to get the quantity.
                        product_index = products_glob.index(product)
                        product_counter[product_index] = int(quantity)
                    
                    # this is based on customer_glob_index. This if condition eliminate multiple appending lists of quantitiy inside the table.
                    if allowing_if_condition[customer_glob_index] == False :
                        table[i].append(product_counter)
                        table[i].append(total_price)
                    else: # adding the product_counter instead of appending it
                        res = list(map(add, table[i][1] , product_counter))
                        table[i][1] = res
                        table[i][2] += total_price

        # reseting product_counter for every iteration from the first loop {1}
        product_counter = [0] * (row_len - 2)

        # if the customer iterated before in the second loop {2}, then set its position in the list allowing_if_condition to True so that no multiple product_counter list append to the table.
        allowing_if_condition[customer_glob_index] = True
    
    # after the first loop {1} is finished, print the table using {4} and {5} loops.
    product_printing_list = []
    for i in range(1,len(products_glob)+1): # this is the third loop {4}
        product_printing_list.append(f"p{i}")
    print(f"\t{product_printing_list} Total Price $")
    for i in range(len(table)): # this is the fourth loop {5}
        print(table[i])

        
def replenish_one():
    """Increasing quantities:

    Void function.

    This function is responsible to increase the stock for the items that are available for purchase.
    """
    available_products = products_glob.copy() # not using the original because see [242].
    print(f"Available products: {available_products}") 
    # The while loop is to make sure that the product the user enter exist
    while True:
        try:
            selected_product = input("Please provide the product name that you would like to increase its stock: ")
            available_products.remove(selected_product)
        except ValueError: # if .remove cannot identify the product
            print("Sorry, no such product. Try again.")
        else: # get the increase stock number and increase the stock then print a statement the product and its stock. Finally, return to the main menu.
            selected_increase = input("Please provide the amount you want to increase the stock of product with: ")
            stock_index = products_glob.index(selected_product)
            stock_glob[stock_index] = str(int(stock_glob[stock_index]) + int(selected_increase))
            print("-------------------------")
            print(f"Stock of {selected_product} is now {stock_glob[stock_index]}")
            print("You will now return to the main menu.")
            print("-------------------------")
            display_main_menu()
            break


def display_customers_menu():
    """Displaying customers menu:

    Void function.

    This function is called to display all existent customers.
    """
    print("-------------------------")
    print("Existent Customers")

    # for loop to print all unique customers
    count = 1
    for customer in customers_glob:
        print(f"{count}- {customer}")
        count += 1
    print("-------------------------")
    # allowing the user to take the time needed to view.
    returning = input("Press 0 and then enter to return to the main menu.")
    if returning == "0":
        display_main_menu()
    

def display_products_menu():
    """Displaying products menu:

    Void function.

    This function is used to display all existent products and their prices.
    """
    print("-------------------------")
    print("Products And Their Pricing")

    # for loop to print all unique products
    count = 1
    for i in range(len(products_glob)):
        print(f"{count}- {products_glob[i]} with a unit price of ${prices_glob[i]} and current quantity {stock_glob[i]}.")
        count += 1
    print("-------------------------")
    # allowing the user to take the time needed to view.
    returning = input("Please 0 and then enter to return to the main menu.")
    if returning == "0":
        display_main_menu()


def new_purchase():
    """Making new purchase:

    Void function.

    This function allow the user to make a new purchase and store the purchase details.
    """
    global customer_history
    global product_history
    global total_price_history
    global is_old_glob
    global customer_for_purchase_glob
    free_items_glob = []
    is_old_glob = None

    customer_for_purchase_glob = input("\nPlease enter the name of the customer: ")
    if customer_for_purchase_glob in customers_glob: # the else statement is [374]. This condition comes first to append new customers and know that the customer is old or new.
        print(f"Thank you for buying again! A 10% discount because you are awesome!")
        if customer_for_purchase_glob in tracking_free: # this is the second if condition because free items are given only if the first condition is met. This if condition is to make sure the old customer only get free items for one time.
            print("Sorry, you can only have free items one time.")
            proceed_purchase = input("Would you like to proceed to purchase or quit? Y/N")
            if proceed_purchase == "Y": # allowing the user to choose
                proceeding_purchase()
            elif proceed_purchase == "N":
                display_main_menu()
        else: # if the customer is old and did not have free items
            print("Also, you can have two free items!")
            print("Welcome back old customer!")
            print("Here are the list of free items you can have:")
            print("")
            # printing available free products
            for i in range(len(products_glob)):
                if prices_glob[i] == "0":
                    print(f"{products_glob[i]}")
            print("")
            is_old_glob = True # so that the customer cannot ask for free items the second time
            free_or_no = input("Would you like to have any two items from those? Y/N")
            # this while loop have two if conditions. In the first if condition [340], the while loop will break after appending the two free items and then after the user decision to proceed purchase or not. In the second if condition [346], the while loop will break after the user decision to proceed purchase or not 
            while True:
                if free_or_no == "Y":
                    order_free_one = input("What's the first free items would you like to get?")
                    order_free_two = input("What's the second free item that you would like to get?")
                    free_one_index = products_glob.index(order_free_one)
                    free_two_index = products_glob.index(order_free_two)
                    # checking whether the free items chosen by the user exist and the quantity exits too.
                    if order_free_one in products_glob and order_free_two in products_glob and int(stock_glob[free_one_index]) > 0 and  int(stock_glob[free_two_index]) > 0 and customer_for_purchase_glob not in tracking_free:
                        free_items_glob.append(order_free_one)
                        free_items_glob.append(order_free_two)
                        tracking_free.append(customer_for_purchase_glob)
                        # decreasing the quantity by one of the two items chosen
                        stock_glob[free_one_index] = int(stock_glob[free_one_index]) - 1
                        stock_glob[free_two_index] = int(stock_glob[free_two_index]) - 1 
                        proceed_purchase = input("Would you like to proceed to purchase or quit? Y/N")
                        # allowing the user to choose
                        if proceed_purchase == "Y":
                            proceeding_purchase()
                            break
                        elif proceed_purchase == "N":
                            display_main_menu()
                            break

                        break # this break statement is incase the user has entered something wrong in the proceed purchase input
                    else:
                        print("The item you have asked for is not available from the list you have been shown.")
                        continue
                elif free_or_no == "N": # if the user decided to not have free items
                    proceed_purchase = input("Would you like to proceed to purchase or quit? Y/N")
                    if proceed_purchase == "Y":
                        proceeding_purchase()
                        break
                    elif proceed_purchase == "N":
                        display_main_menu()
                        break
    else: # if the customer is new, append it to customer_glob which have all the unique customers. Then, proceed to purchase function which allow the user to enter a new purchase
        customers_glob.append(customer_for_purchase_glob)
        is_old_glob = False
        proceeding_purchase()
    customer_history.append(customer_for_purchase_glob) # whether the customer made purchase or not, after the user enter the name of customer, customer_history will always show the attempts of purchases.
    display_main_menu()


def proceeding_purchase():
    """Proceeding purchase after new_purchase():

    Void function.

    This function is responsible to register the order of the customer to customer history. This function is called in new_purchase().
    """
    global customer_history
    global product_history
    global total_price_history
    global is_old_glob
    global customer_for_purchase_glob
    products = []
    ordered_quantities = []
    free_items_glob = []

    # this while loop is to make sure that the user can enter as many products as wanted. It breaks when multiple_purchases variable is not "Y", which is after the else condition for the last if condition is done. Also, when the product is enetered again by the user.

        #1- the first if condition is to make sure that the product is not entered again
        #2- the second if condition is to make sure that the product exist in the grocery store.
            #1- The first if condition inside the second outer if condition is to make sure that stock quantity exist for chosen product
            #2- The second if condition inside the second outer if condition is to make sure that the chosen product neither has no price or free.
        # After these if conditions, another if condition statement is based on user input to continue entering products or not.
    while True:
        product_name = input("Please provide the name of the product that is purchased: ")
        if product_name in products: # checking that the product havent entered again.
            print("\n!!!!You cannot enter the same product again. You should have enetered the correct quantity. Program will restart.!!!!\n")
            products.clear()
            ordered_quantities.clear()
            display_main_menu()
            break
        if product_name in products_glob: # checking whether the product exist
            product_name_index = products_glob.index(product_name)
            ordered_quantity = input("Please provide the quantity of the product you have entered earlier: ")
            if int(stock_glob[product_name_index]) > 0 and int(stock_glob[product_name_index]) >= int(ordered_quantity) : # checking whether the product is available based on user quantity
                if prices_glob[product_name_index] != "no price" and prices_glob[product_name_index] != "0": # checking if the product is not free nor hidden from customers.
                    products.append(product_name)
                    ordered_quantities.append(ordered_quantity)
                    stock_glob[product_name_index] = int(stock_glob[product_name_index]) - int(ordered_quantity)
                else:
                    print("The product has no price and therefore cannot be purchased.")
            else:
                print(f"!!!!The product is out of stuck or the quantity is high. Current Quantity is {stock_glob[product_name_index]}. Please try again.!!!!")
                continue
        else:
            print("The product is not available. Please try again.")
            continue
        multiple_purchases = input("Continue (Y/N)")
        if multiple_purchases == "Y":
            continue
        else: # when the user enter all the products purchased by the customer, this else statement is excuted. It will print the order summary, calculate the total price and set the customer as old after the first purchase.
            # printing order summary without total price
            print("-------------------------")
            print("\nYou have entered the following purchases:")
            print(f"Customer Name: {customer_for_purchase_glob}")
            print("Order Summary:")
            for i in range(len(products)):
                product_name_index = products_glob.index(products[i])
                price = prices_glob[product_name_index]
                print(f"{products[i]} with a unit price of {price} and quantity of {ordered_quantities[i]}")
            print("")
            for i in range(len(free_items_glob)):
                print("You have also got these two free items:")
                print(f"{free_items_glob[i]}")
            print("")
            # getting the price for each unit from the prices_glob
            unitPrice_local = []
            for i in range(len(products)):
                product_name_index = products_glob.index(products[i])
                try:
                    float(prices_glob[product_name_index])
                except TypeError:
                    unitPrice_local.append(prices_glob[product_name_index])
                else:
                    unitPrice_local.append(float(prices_glob[product_name_index]))
            # calculating the total price of each product by multiplying it price with the quantity chosen by the user
            unitPrice_times_quantities = []
            for i in range(len(ordered_quantities)):
                unitPrice_times_quantities.append(float(unitPrice_local[i])*float(ordered_quantities[i]))

            # suming all individual total prices for each product
            total_price = sum(unitPrice_times_quantities)

            # changing the state of the customer to old and applying the discount if the customer is old to the total price. Finally, break the loop
            if is_old_glob == True:
                discount_applied = (total_price - (total_price*0.10))
                print(f"The total price is {discount_applied}.")
                total_price_history.append(discount_applied)
            else:
                print(f"The total price is {total_price}.")
                total_price_history.append(total_price)
            print("You have registered the new purchases successfully. You will now return to the main menu!\n")
            print("-------------------------")
            break
    # append the quantity and product history
    quantity_history.append(ordered_quantities) 
    product_history.append(products)


def orders_history():
    """Displaying all orders made by user:

    Void function.

    This function is responsible to display the orders that have been made from the function new_purchase() and proceeding_purchase().
    """
    # printing all the information stored in variables that end with _history using the for loop
    print("-------------------------")
    print("The following are all the orders that have been made:")
    print(len(customer_history))
    print(len(total_price_history))
    for i in range(len(customer_history)):
        print(f"{i}:\n")
        print(f"Customer name: {customer_history[i]}")
        print(f"Purchased {product_history[i]}")
        print(f"With a total price of {total_price_history[i]}")
        print("")
    returning = input("Press 0 and then enter to return to the main menu.")
    print("-------------------------")
    if returning == "0": # allowing the user to take time to see the order history.
        display_main_menu()


def update_products():
    """Update the products the grocery store have:

    Void function.

    This function is responsible to update the products that the grocery store have. 
    """
    # Local variables for this function.
    products = []
    prices = []
    stock = []
    # Global variables
    global products_glob
    global prices_glob
    global stock_glob
    # Reseting these global variables
    prices_glob = []
    products_glob = []
    stock_glob = []

    # will the user provide quantities or not for the products.
    yesno_stock = input("Will you provide stock quantities for the products you will be adding? Y/N ")
    # if no, then append 0 for the length of entered products from the user
    if yesno_stock == "N":
        for time in range(len(products)):
            stock.append("0")

    # there are three while loops.
        # The first while loop is to make sure 
        # The second while loop {2} is to make sure that the product is entered correctly. 
        # The third whle loop {3} is to make sure that the price is entered correctly with the appending the correct appropriate type of price for the product. Whether the price is free, hidden, or bigger than 0.
    while True: #{1}
        while True: #{2}
            added_product = input("Please provide the new product that you would like to add: ")
            if ' ' in added_product:
                print("only alphanumeric charachters are allowed.")
                continue # allow the while loop {2} to reset and the user to enter a correct format of product
            elif added_product in products:
                print("The product is already in the list.")
                continue # allow the while loop {2} to reset and the user to enter a correct format of product
            else: # if the product is entered in a correct format, then excute the else statement which will check that the price is entered correctly with the while loop {3} and append the product.
                products.append(added_product)
                while True: #{3} Appending the appropriate price for each product the user entered.
                    added_price = input("Please add the price for the item you entered. If the product is hidden, type H: ")
                    try:
                        if added_price == "0":
                            prices.append("0")
                            break # break {3} 
                        if added_price == "H":
                            prices.append("no price")
                            break # break {3}
                        if int(added_price) < 0:
                            print("Price cannot be negative!")
                            continue # continue will allow the loop to restart to allow the user to enter a correct price because price cannot be negative.
                        if int(added_price) > 0 and added_price != "H" and added_price != "0":
                            int(added_price)
                            prices.append(added_price)
                            break # if the first three condition met, then append the price and break {3}
                    except ValueError:
                        print("Only float/integers are allowed.") # if there;s a value error then print the following message.
                break # {2}
        if yesno_stock == "Y": # allowing the user to enter stock quantitiy
            added_stock = input("Please add the available stock for the item you will enter: ")
        stock.append(added_stock) # appending it 
        more_products = input("Would you like to add another product? Y/N: ")
        if more_products == "Y":
            continue # if more products, then reset the outer most while loop {1} and do the same process again.
        else:
            break # break {1}
    # pasting the local variables to global.
    products_glob = products.copy()
    prices_glob = prices.copy()
    stock_glob = stock.copy()
    # finally, printing a message to the user to show all the changes that have been made.
    print("-------------------------")
    print("You have made the following changes:")
    print(f"You have updated the products to : {products_glob}")
    print(f"You have updated the prices for the above products as follows: {prices_glob}")
    print(f"You have updated the stock for the above products as follows: {stock_glob}")
    print("You will now return to the main menu.")
    print("-------------------------")
    display_main_menu()


def end_program():
    """Ending program:
    
    Void function.
    This function is responsible to end the program if the user choose to from display_main_menu().
    """
    print("")
    print("Program ending ...")
    quit()

# starting the program with the menu
display_main_menu()