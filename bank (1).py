class Customer:
    def __init__(self, cID, first_name, second_name, address, balance):
        self.__cID = cID
        self.__first_name = first_name
        self.__second_name = second_name
        self.__address = address
        self.__balance = balance
 
    def get_cID(self):
        return self.__cID
     
    def set_cID(self, c_id): 
        self.__cID
        
    def get_first_name(self):
        return self.__first_name

    def set_(self,  f_name):
        self.__first_name
    def get_second_name(self):
        return self.__second_name
    
    def set_second_name(self, s_name):
        self.__second_name
  
    def get_address(self):
        return self.__address
    def set_address(self, addObj):
        self.__address =addObj
    def get_balance(self):
        return self.__balance
   
    def set_balance(self, value):
        self.__balance = value

    def deposit(self,value):
        self.__balance+=value

    def withdraw(self,value):
        self.__balance-=value

    def check_balance(self):
        return self.__balance 

class Address:
    def __init__(self, number, street, town, post_code):
        self.__number = number
        self.__street = street
        self.__town = town
        self.__post_code = post_code

  
    def get_number(self):
        return self.__number
  
    def set_number(self, value):
        self.__number = value

  
    def get_street(self):
        return self.__street
    
    def set_street(self, value):
        self.__street = value

 
    def get_town(self):
        return self.__town
 
    def set_town(self, value):
        self.__town = value

  
    def get_post_code(self):
        return self.__post_code
    
    def set_post_code(self, value):
        self.__post_code = value

    def change_address(self,new_address):
        self.number = new_address.number
        self.street = new_address.street
        self.town = new_address.town
        self.post_code= new_address.post_code

    def __str__(self):
        return f"{self.__number},{self.__street},{self.__town},{self.__post_code}"

def new_customer():

    cid= int(input("Enter customer id number: "))
    f_name= input( "Enter first name: ")
    s_name= input("Enter second name: ")
    address_input = input("Enter address (number, street, town, postCode): ")
    while len(address_input.split(',')) != 4:
        address = input( "Please re-enter address (number, street, town, postCode): ")
    address_values= address_input.split(',')
    address_obj = Address(address_values[0],address_values[1],address_values[2], address_values[3])
    balance = float(input("Enter balance:"))
    return Customer(cid, f_name, s_name, address_obj,balance)



def save_cRecords(lst):
    with open('client_list.txt','w')as file:
        for customer in lst:
            file.write(f"{customer.get_cID()}, {customer.get_first_name()},{customer.get_second_name()},"
                       f"{customer.get_address()},{customer.get_balance()}\n")


def read_customerRecords(data_file):
    customers = []
    with open(data_file, 'r')as file:
        for line in  file:
            data = line.strip().split(',')
            cID, first_name, second_name = data[:3]
            address = Address(data[3], data[4], data[5], data[6])
            balance =float(data[7])
            customer.append(customer(cID, first_name, second_name, address, balance))
    return customers
c1 = Customer('12A','Rea','Koch',Address('42','Curzon Street','Birmingham', 'B4 2SU'),888)
c2 = Customer('11A','Liora','Koci',Address('42b','Curzon Street2','Birmingham2', 'B4 2SU'),33)    
c = Customer('12A','Anna','Duka',Address(42,'Curzon Street','Birmingham', 'B4 2SU'),888)

save_cRecords([c1,c2])  




