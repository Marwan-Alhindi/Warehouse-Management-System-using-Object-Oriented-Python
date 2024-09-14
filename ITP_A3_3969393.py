"""
Student Name: Mrwan Alhandi
Student ID: 3969393
Highest level attempted: Till part 2 from HD
Submission History: None

Explaination of the code: I was restricted in time to do this project. I assumed that if I didnt do a UML/ER diagram and started the assignment right away, I will save time. When I reached the requirements of distinction level, I started to have trouble identifying the relationships between the classes and the multiplicity. The approach I took was simply I read the whole level part and then I wrote the code.

Problems with my code and requirements that I have not met: I have done till part 2 of HD level. Due to restricted time, I assumed some of the requirements in a specific way. Otherwise, I would have asked specifically the meaning of some of the requirements. For example, I assumed that the program will end if either file customers.txt or products.txt does not exist and not both.
"""
import csv


class Customer:
    """ This class is responsible to create customers. There are two other classes inherit this class which are RetailCustomer and WholesaleCustomer."""

    def __init__(self,id,name,total_price_all):
        """
        id: the unique id of the customer.
        name: self-sufficient
        total_price_all: the total amount of money paid for all orders.
        """
        self.id = id
        self.name = name
        self.total_price_all = total_price_all
        self.list_orders = [] # All the order objects that have been made by the customer.

    # getters
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_discount(self,price):
        # if self.get_used_disc():
        #     self.set_used_disc(False)
        #     return price - (price * 0.10)
        # else:
        #     return price
        pass

    def get_list_orders(self):
        return self.list_orders

    def get_total_price_all(self):
        return self.total_price_all

    # setters
    def set_name(self,new_name):
        self.name = new_name
    
    def add_order(self,product_id,quantity,total_price):
        """
        This method is responsible to add an order object to list_orders list.
        """
        self.list_orders.append(Order(self.get_id(),product_id,quantity,total_price,'No comment'))
        self.total_price_all += total_price


class RetailCustomer(Customer):
    """
    Inherit class of customer. The main difference is the discount given for these type of customers.
    """

    discount_rate = 0.10

    def __init__(self, id, name,total_price_all,discount_rate = 0.10):
        """
        id: the unique id of the customer.
        name: self-sufficient.
        total_price_all: the total amount of money that have been paid by the customer.
        discount_rate: static variable that can be changed for all Retail Customers.
        """
        super().__init__(id, name,total_price_all)
        RetailCustomer.discount_rate = discount_rate

    # getters
    @staticmethod
    def get_discount_rate():
        return RetailCustomer.discount_rate

    def get_discount(price):
        return price * RetailCustomer.discount_rate

    def display_customer(self):
        """
        This method is to display all existent Retail Customers.
        """
        print(f"Retail Customer: {self.id},{self.name},{RetailCustomer.discount_rate}")

    # setters
    @staticmethod
    def set_discount_rate(discount_rate):
        RetailCustomer.discount_rate = discount_rate


class WholesaleCustomer(Customer):
    """
    Inherit class of customer. The main difference is the discount given for these type of customers.
    """
    # The threshold that decide whether the customer should a type of discount or not.
    threshold = 1000
    
    def __init__(self, id, name,total_price_all,discount_rate = 0.10):
        """
        id: the unique id for the customer.
        name: self-sufficient.
        total_price_all: the total amount of money that have been paid by the customer.
        """
        super().__init__(id, name,total_price_all)
        self.discount_rate = discount_rate
        self.discount_rate_plus = discount_rate + 0.05

    def get_discount(self,price):
        """
        This method is to decide what discounts should be given to the customer based on the total amount of the order.
        """
        if price <= WholesaleCustomer.threshold:
            discount_1000 = WholesaleCustomer.threshold * self.discount_rate
            return discount_1000
        elif price > WholesaleCustomer.threshold:
            discount_1000 = WholesaleCustomer.threshold * self.discount_rate
            remaining = price - WholesaleCustomer.threshold
            remaining_discount = remaining * (self.discount_rate_plus)
            return remaining_discount + discount_1000

    # getters
    def get_discount_rate(self):
        return self.discount_rate

    def get_discount_rate_plus(self):
        return self.discount_rate_plus
    
    @staticmethod
    def get_threshold():
        return WholesaleCustomer.threshold
    
    def display_customer(self):
        """
        Printing all existent wholesale customer.
        """
        print(f"Wholesate Customer: {self.id},{self.name},{self.discount_rate},{self.discount_rate_plus}")
    
    # setters
    def set_discount_rate(self,new_discount_rate):
        self.discount_rate = new_discount_rate
        self.discount_rate_plus = self.discount_rate + 0.05

    def set_discount_rate_plus(self,new_discount_rate_plus):
        self.discount_rate_plus = new_discount_rate_plus
        self.discount_rate = self.discount_rate_plus - 0.05
    
    @staticmethod
    def set_threshold(new_threshold):
        WholesaleCustomer.threshold = new_threshold


class Product:
    """
    This class is to create a product object.
    """

    def __init__(self,id,name,price,stock):
        """
        id: the unique id of the product.
        name: the name of the product.
        price: the price of the product.
        stock: the amount available to purchase.
        """
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        
    # getters
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_stock(self):
        return self.stock

    # setters
    def set_name(self,new_name):
        self.name = new_name

    def set_price(self,new_price):
        self.price = new_price

    def set_stock(self,new_stock):
        self.stock = new_stock


class Order:
    """
    This class it to make an order instance.
    """

    def __init__(self,customer_id_or_name,products_ids,quantity,total_price,comment):
        """
        customer_id_or_name: self-sufficient.
        products_ids: a list of products or a single product item.
        quantity: a list of the quantites or a single quantity respectively with products_ids.
        total_price: the total price for the order.
        comment: some orders might need a specific comment.
        """
        self.customer_id_or_name = customer_id_or_name
        self.products_ids = products_ids 
        self.quantity = quantity
        self.total_price = total_price
        self.comment = comment

    # getters
    def get_customer_id(self):
        return self.customer_id_or_name
    
    def get_product_id(self):
        return self.product_id

    def get_quantity(self):
        return self.quantity

    def get_total_price(self):
        return self.total_price

    # setters
    def set_product_id(self,new_product_id):
        self.product_id = new_product_id

    def set_quantity(self,new_quantity):
        self.quantity = new_quantity

    def set_total_price(self,new_total_price):
        self.total_price = new_total_price


class Combo:
    """
    This class it to make a combo product.
    """
    
    def __init__(self,customer_id_or_name,combo_id,combo_name,products_list,combo_quantity,price):
        """
        customer_id_or_name: self-sufficient.
        combo_id: the unique id for the combo.
        combo_name: self-sufficient.
        products_list: the list of the products that make up the combo.
        combo_quantity: the amount of quantitiy that is available to purchase for the combo.
        """
        self.customer_id_or_name = customer_id_or_name
        self.combo_id = combo_id
        self.combo_name = combo_name
        self.product_list = products_list
        self.combo_quantity = combo_quantity
        self.price = price
        

    def printing_existing_products(self):
        """
        A method to print all the existent products.
        """
        Operations.record.readProducts('products.txt')
        print(Operations.record.existing_products)

    # getters
    def get_combo_id(self):
        return self.combo_id

    def get_combo_name(self):
        return self.combo_name

    def get_product_list(self):
        return self.product_list

    def get_combo_quantity(self):
        return self.combo_quantity

    def get_price(self):
        return self.price

    # setters
    def set_combo_name(self,new_name):
        self.combo_name = new_name

    def set_product_list(self,new_product_list):
        self.product_list = new_product_list

    def set_combo_quantity(self,new_combo_quantity):
        self.combo_quantity = new_combo_quantity

    def set_price(self,new_price):
        self.price = new_price


class Records:
    """
    This class is responsible to read a record of existent customers,products, and orders.
    """
    # A static list that keep all read files.
    all_files = []

    def __init__(self):
        """
        self.existing_customers: A list that hold all the customers from the file.
        self.existing_products: A list that hold all the products from the file.
        self.existing_all_orders: A list that hold all the recorded orders from the file.
        """
        self.existing_customers = []
        self.existing_products = []
        self.existing_all_orders = []
        
    # getters
    def get_existing_customers(self):
        return self.existing_customers
    
    def get_existing_products(self):
        return self.existing_products
        
    def readCustomers(self,customer_file):
        """
        This method is to read all the customers and assign the type of the customer from the file.
        """
        with open(customer_file) as f:
            reader = csv.reader(f)
            for row in reader:
                if row[2].strip() == 'W':
                    self.existing_customers.append(WholesaleCustomer(row[0].strip(),row[1].strip(),float(row[4].strip()),float(row[3].strip()))) # There are three more fields reserved for later parts
                elif row[2].strip() == 'R':
                    self.existing_customers.append(RetailCustomer(row[0].strip(),row[1].strip(),float(row[4].strip()),float(row[3].strip())))

    def readProducts(self,products_file):
        """
        This method is to read all the products and assign the type of the product from the file whether its a single product or a combo.
        """
        with open(products_file) as f:
            reader = csv.reader(f)
            for row in reader:
                row[0] = row[0].strip()
                if row[0][0] == 'P':
                    self.existing_products.append(Product(row[0].strip(),row[1].strip(),row[2].strip(),row[3].strip())) # There are three more fields reserved for later parts
                elif row[0][0] == 'C':
                    combo_wombo = []
                    [combo_wombo.append(i) for i in row[2:len(row)-1]]
                    self.existing_all_orders.append(Combo('None',row[0].strip(),row[1].strip(),combo_wombo,row[len(row)-1].strip(),price= 0))

    def readOrders(self):
        """
        This method is to read all the orders written in a file. If the order have no comment, then the order instance will have an attribute 'no comment'.
        """

        file_name = input('Please provide the file name for orders. Make sure you provide the extension: ')
        if file_name not in self.all_files:
            self.all_files.append(file_name)
            with open(file_name) as f:
            
                data = f.readlines()
                for row in data:
                    row = row.split(',')
                    if len(row) == 3:
                        self.existing_all_orders.append(Order(row[0].strip(),row[1].strip(),row[2].strip(),None,'No comments'))
                    elif len(row) == 4:
                        self.existing_all_orders.append(Order(row[0].strip(),row[1].strip(),row[2].strip(),None,row[3].strip()))

                    
    def findCustomer(self,customer_id):
        """
        This method is to look if the customer exist in self.existing_customers list. If it does, return the object of that customer. Otherwise, return None.
        """
        for customer in self.existing_customers:
            if customer.get_id() == customer_id:
                return customer  
        return None

    def findProduct(self,product_id):
        """
        This method is to look if the product exist in self.existing_products list. If it does, return the object of that product. Otherwise, return None.
        """
        for product in self.existing_products:
            if product.get_id() == product_id:
                return product 
        return None

    def findCombo(self,combo_id):
        """
        This method is to look if the combo exist in self.existing_orders list. If it does, return the object of that combo. Otherwise, return None.
        """
        for combo in self.existing_all_orders:
            if type(combo) == Combo() and combo.get_combo_id() == combo_id:
                return combo
        return None

    def listCustomers(self):
        """
        Printing all customers.
        """
        print("All Customers:")
        for customer in self.existing_customers:
            print(f"{customer.get_id()},{customer.get_name()}") # there could be more fields
    
    def listProducts(self):
        """
        Printing all products.
        """
        print("All Products: ")
        for product in self.existing_products:
            print(f"{product.get_id()},{product.get_name()},{product.get_price()},{product.get_stock()}") # there could be more fields


class Operations:
    """
    This class is the main class for this program. It handles almost all the functionalites of this program.
    """
    # Keeping an instance of a record when starting the program.
    record = Records() 

    def __init__(self):
        """
        When this class is first called/initialized, it check if customers.txt and products.txt exists. If it does not, end the program from the method end_program.
        """
       
       # checking if customers.txt exists. Otherwise, end the program.
        try:
            Operations.record.readCustomers('customers.txt')
        except FileNotFoundError:
            print(f"Sorry, the file customers.txt does not exist.")
            self.end_program()

        # checking if products.txt exists. Otherwise, end the program.
        try:
            Operations.record.readProducts('products.txt')
        except FileNotFoundError:
            print("Sorry, the file products.txt does not exist.")
            self.end_program()

        # if both files exists, call the main menu using the method menu_setup.
        self.menu_setup()

    def menu_setup(self):
        """Displaying main menu:

        Void function.

        This function is to display the options in the main menu, and based on user choice it apply the appropriate function to display the right informations for the user.
        """
        print("-------------------------")
        print("Main Menu")
        print("1: View All Customers")
        print("2: View All Products")
        print("3: Make a new order (individual items only)")
        print("4: Make a new order (combo only)")
        print("5: View Orders")
        print("0: Quit")
        print("-------------------------")

        # A while loop that break after the user make the correct choice. If the input is wrong, a informative message will represent to the user.
        choice = -1
        while True:
            try:
                choice = int(input("Option: "))
                if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5 or choice == 0:
                    break
                else: # if the number is not from the options error message
                    print("Error: Invalid option")
            except ValueError: # String or characters error message
                print("Error: Only numbers are accepted")
        
        # All menu options and their functions
        if choice == 1:
            self.display_customers_menu()
        elif choice == 2:
            self.display_products_menu()
        elif choice == 3:
            self.make_order()
        elif choice == 4:
            self.make_order_combo()
        elif choice == 5:
            self.view_orders()
        elif choice == 0:
            self.end_program()

    def end_program(self):
        """Ending program:
        
        Void function.
        This function is responsible to end the program if the user choose to from display_main_menu().
        """
        print("")
        print("Program ending ...")
        quit()
    
    def display_customers_menu(self):
        """Displaying customers menu:

        Void function.

        This function is called to display all existent customers.
        """
        print("-------------------------")
        print("All Customers:")
        for customer in Operations.record.existing_customers:
            print(f"{customer.get_id()},{customer.get_name()}") # there could be more fields
        print("-------------------------")
        # allowing the user to take the time needed to view.
        returning = input("Press 0 and then enter to return to the main menu.").strip()
        if returning == "0":
            self.menu_setup()
        
    def display_products_menu(self):
        """Displaying customers menu:

        Void function.

        This function is called to display all existent customers.
        """
        print("-------------------------")
        print("All Products:")
        for product in Operations.record.existing_products:
            if float(product.get_price()) > 0:
                print(f"{product.get_id()},{product.get_name()},{product.get_price()},{product.get_stock()}") # there could be more fields
        print("-------------------------")
        # allowing the user to take the time needed to view.
        returning = input("Press 0 and then enter to return to the main menu.")
        if returning == "0":
            self.menu_setup()
    
    def make_order(self):
        """
        This method is responsible to read the file orders.txt and then create an Order instance and append it to the customer instance. After the read of the file is done, it ask the user for Order attributes and then make an order for that customer whether if the customer is new or old.
        """
        while True:
            try:
                Operations.record.readOrders()
            except FileNotFoundError:
                print("Sorry, the file orders.txt does not exist.")
            else:
                customer_id_input = input("Please provide the customer id: ")
                customer_instance = Operations.record.findCustomer(customer_id_input)
                if customer_instance == None:
                    user_ans = input('This customer does not exist. Would you like to create a new customer? (Y/N)')
                    if user_ans == 'Y':
                        cust_type = input('Please provide whether the customer is wholesale or retail? (W/R): ')
                        cust_name = input('Please provide the customer name or N to pass: ')

                        if cust_type == 'W':
                            customer_instance = WholesaleCustomer(f"C{len(Operations.record.existing_customers)+1}",cust_name,0,discount_rate= 0)
                            customer_instance.discount_rate_plus = 0
                        elif cust_type == 'R':
                            customer_instance = RetailCustomer(f"C{len(Operations.record.existing_customers)+1}",cust_name,0,discount_rate= 0 )
                            
                        while True:
                            break_holder = False
                            product_ids_input = input("Please provide the product ids. Note: if there are more than one product, type it in this format: product_id1,product_id2...etc: ")
                            quantity_input = input("Please provide the quantity respectivly. Note: if there are more than one product type the quantites respectivly in this format: quantity1,quantity2..etc: ")
                            quantity_list = quantity_input.split(',')
                            float_quantity_list = []
                            for quantity in quantity_list:
                                float_quantity_list.append(float(quantity))
                        
                            prices_list = []
                            products_name = []
                            product_instances = []
                            count = -1
                            product_ids_list = product_ids_input.split(',')
                            for product_id in product_ids_list:
                                count += 1
                                product_instance = Operations.record.findProduct(product_id)

                                # product ID doesnt exist error handling
                                if product_instance == None:
                                    print(f"The product {product_id} provided does not exists.")
                                    break_holder = True
                                    float_quantity_list.clear()
                                    prices_list.clear()
                                    products_name.clear()
                                    product_instances.clear()
                                    break
                                # stock < quantity error handling
                                if float(product_instance.get_stock()) < float_quantity_list[count]:
                                    print(f'The product {product_instance.get_id()} have a current stock of {product_instance.get_stock()}. The quantity for this product is larger. You must re enter your order.')
                                    break_holder = True
                                    float_quantity_list.clear()
                                    prices_list.clear()
                                    products_name.clear()
                                    product_instances.clear()
                                    break
                                # free items error handling
                                if product_instance.get_price() == '0':
                                    print('Product with zero price are free and cannot be accessed yet.')
                                    print('You will now return to the main menu.')
                                    self.menu_setup()
                                else:
                                    product_price = product_instance.get_price()
                                    product_instance.set_stock(float(product_instance.stock) - float_quantity_list[count])
                                    products_name.append(product_instance.get_name())
                                    prices_list.append(float(product_price))
                                    product_instances.append(product_instance)

                            if break_holder == True:
                                continue
                            else:
                                break
                    
                        print("-------------------------")
                        total_price = 0
                        for i in range(len(prices_list)):
                            total_price += prices_list[i] * float_quantity_list[i]

                        for i in range(len(prices_list)):
                            print(f"{customer_instance.get_name()} purchased {float_quantity_list[i]} x {products_name[i]}")
                            print(f"Unit price: {prices_list[i]}")
                            print(f"Total price of this product: {float_quantity_list[i] * prices_list[i]}")
                            print(f"Remaining stock: {product_instances[i].stock}")
                            print("-------------------------")
                        print(f"The total price of all products: {total_price}")

                        customer_instance.add_order(product_ids_list,quantity_list,total_price)
                        
                        customer_instance.total_price_all = total_price

                        if user_ans == 'Y':
                            Operations.record.existing_customers.append(customer_instance)
                        
                        Operations.record.existing_all_orders.append(Order(customer_id_input,product_ids_list,quantity_list,total_price))
                        
                        return Order(customer_id_input,product_ids_list,quantity_list,total_price),self.menu_setup()
                    else:
                        print("You can't make a new order with no customer information.")
                        print('You will now return to the main menu.')
                        self.menu_setup()
                else:
                    if type(customer_instance) == WholesaleCustomer:
                            customer_instance = WholesaleCustomer(f"C{len(Operations.record.existing_customers)+1}",customer_instance.name,0,discount_rate= 0)
                            customer_instance.discount_rate_plus = 0
                    elif type(customer_instance) == RetailCustomer:
                        customer_instance = RetailCustomer(f"C{len(Operations.record.existing_customers)+1}",customer_instance.name,0,discount_rate= 0 )

                    while True:
                        break_holder = False
                        product_ids_input = input("Please provide the product ids. Note: if there are more than one product, type it in this format: product_id1,product_id2...etc: ")
                        quantity_input = input("Please provide the quantity respectivly. Note: if there are more than one product type the quantites respectivly in this format: quantity1,quantity2..etc: ")
                        quantity_list = quantity_input.split(',')
                        float_quantity_list = []
                        for quantity in quantity_list:
                            float_quantity_list.append(float(quantity))
                    
                        prices_list = []
                        products_name = []
                        product_instances = []
                        count = -1
                        product_ids_list = product_ids_input.split(',')
                        for product_id in product_ids_list:
                            count += 1
                            product_instance = Operations.record.findProduct(product_id)

                            # product ID doesnt exist error handling
                            if product_instance == None:
                                print(f"The product {product_id} provided does not exists.")
                                break_holder = True
                                float_quantity_list.clear()
                                prices_list.clear()
                                products_name.clear()
                                product_instances.clear()
                                break
                            # stock < quantity error handling
                            if float(product_instance.get_stock()) < float_quantity_list[count]:
                                print(f'The product {product_instance.get_id()} have a current stock of {product_instance.get_stock()}. The quantity for this product is larger. You must re enter your order.')
                                break_holder = True
                                float_quantity_list.clear()
                                prices_list.clear()
                                products_name.clear()
                                product_instances.clear()
                                break
                            # free items error handling
                            if product_instance.get_price() == '0':
                                print('Product with zero price are free and cannot be accessed yet.')
                                print('You will now return to the main menu.')
                                self.menu_setup()
                            else:
                                product_price = product_instance.get_price()
                                product_instance.set_stock(float(product_instance.stock) - float_quantity_list[count])
                                products_name.append(product_instance.get_name())
                                prices_list.append(float(product_price))
                                product_instances.append(product_instance)

                        if break_holder == True:
                            continue
                        else:
                            break
                
                    print("-------------------------")
                    total_price = 0
                    for i in range(len(prices_list)):
                        total_price += prices_list[i] * float_quantity_list[i]

                    for i in range(len(prices_list)):
                        print(f"{customer_instance.get_name()} purchased {float_quantity_list[i]} x {products_name[i]}")
                        print(f"Unit price: {prices_list[i]}")
                        print(f"Total price of this product: {float_quantity_list[i] * prices_list[i]}")
                        print(f"Remaining stock: {product_instances[i].stock}")
                        print("-------------------------")
                    print(f"The total price of all products: {total_price}")

                    customer_instance.add_order(product_ids_list,quantity_list,total_price)
                    
                    customer_instance.total_price_all = total_price
                    
                    Operations.record.existing_all_orders.append(Order(customer_id_input,product_ids_list,quantity_list,total_price,'No comment'))
                    

                    return Order(customer_id_input,product_ids_list,quantity_list,total_price,'No comment'),self.menu_setup()
                break
        
    def make_order_combo(self):
        """
        This method is responsible to make a combo order.
        """
        # customer
        customer_id_input = input("Please provide the customer id: ")
        customer_instance = Operations.record.findCustomer(customer_id_input)
        if customer_instance == None:
            user_ans = input('This customer does not exist. Would you like to create a new customer? (Y/N)')
            if user_ans == 'Y':
                cust_type = input('Please provide whether the customer is wholesale or retail? (W/R): ')
                cust_name = input('Please provide the customer name or N to pass: ')

                if cust_type == 'W':
                    customer_instance = WholesaleCustomer(f"C{len(Operations.record.existing_customers)+1}",cust_name,0,discount_rate= 0)
                    customer_instance.discount_rate_plus = 0
                elif cust_type == 'R':
                    customer_instance = RetailCustomer(f"C{len(Operations.record.existing_customers)+1}",cust_name,0,discount_rate= 0 )
        
        # changing the price that was placed when reading the file to 0
        for combo in Operations.record.existing_all_orders:
            prices_total = 0
            for product_id in combo.product_list:
                product_instance = Operations.record.findProduct(product_id.strip())
                prices_total += float(product_instance.price)
            combo.set_price(prices_total * 0.90)

        while True:
            combo_id = input('Please provide the combo id you would like to purchase: ')
            combo_instance = Operations.record.findCombo(combo_id)
            if combo_instance == None:
                print('The combo ID you provided does not exist. Please try again.')
                continue
            else:
                if combo_instance.quantity < 0:
                    print('The combo you have selected is out of stock.')
                    continue
                else:
                    print("-------------------------")
                    print(f"{customer_instance.get_name()} purchased the combo ID: {combo_instance.combo_id} with the name of: {combo_instance.combo_name} with the price of: {combo_instance.price}.")
                    print("You will now return to the main menu.")
                    customer_instance.add_order(combo_instance.combo_id,1,combo_instance.price)
                    break
        return Combo('None',combo_instance.combo_id,combo_instance.combo_name,combo_instance.products_list,combo_instance.combo_quantity,combo.price),self.menu_setup()

    def view_orders(self):
        """
        This method is responsible to view all the orders that have been read from the file and all the orders that have been made from the user.
        """

        col_len = len(Operations.record.existing_customers) + 1 
    
        table = []
        for i in range(col_len):
            table.append([])

        table[0].append('     ')
        
        for product in Operations.record.existing_products:
            table[0].append(product.id.strip())

        for combo in self.record.existing_all_orders:
            if type(combo) == Combo:
                table[0].append(combo.combo_id.strip())

        count = 0
        for customer in Operations.record.existing_customers:
            count += 1
            table[count].append(customer.name.strip())

        products_combos_all = table[0][1:].copy()

        cust_count = 0
        for customer in Operations.record.existing_customers:
            cust_count += 1
            products_combos_count = [0] * len(products_combos_all)
            for order in Operations.record.existing_all_orders:
                if type(order) == Order:
                    if order.customer_id_or_name.strip() == customer.id.strip() or order.customer_id_or_name.strip() == customer.name.strip():
                        try:
                            product_index = products_combos_all.index(order.products_ids)
                        except ValueError:
                            for product in Operations.record.existing_products:
                                # when ordering multiple products, all of this doesnt work
                                if product.id.strip() == order.products_ids[0].strip():
                                    product_instance = product
                                    product_id = product_instance.id
                                    product_index = products_combos_all.index(product_id.strip())
                                    products_combos_count[product_index] += int(order.quantity[0])
                        else:
                            products_combos_count[product_index] += int(order.quantity[0])
                elif type(order) == Combo:
                    if order.customer_id_or_name.strip() == customer.id.strip() or order.customer_id_or_name.strip() == customer.name.strip():
                        try:
                            product_index = products_combos_all.index(order.combo_id)
                        except ValueError:
                            for product in Operations.record.existing_products:
                                if product.id.strip() == order.combo_id.strip():
                                    product_instance = product
                                    product_id = product_instance.id
                                    product_index = products_combos_all.index(product_id.strip())
                                    products_combos_count[product_index] += int(order.combo_quantity)
                        else:
                            products_combos_count[product_index] += int(order.combo_quantity)
            table[cust_count].append(products_combos_count)
            
        for row in table:
            print(row)
        
        table.clear()
        print(table)
        print('Returning to the main menu....')
        self.menu_setup()

# Calling Operations instance so that the program starts
Operations()
