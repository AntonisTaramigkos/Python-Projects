#Bank Account

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        

class Customer(Person):
    '''A class witch inheritage attributes from Class Person'''
    def __init__(self, firstname, lastname):
        super().__init__(firstname,lastname)  
        self.account_number = "105503234"
        self.account_balance = 0

    def __str__(self):
        '''A method to print the person personal ditails '''
        return (f"Hello {self.firstname} {self.lastname}\nYour accoun number is {self.account_number}\nAnd you current balance is {self.account_balance}")
     
    def deposite(self):
        '''A fuction to add money in account'''
        
        add_money = int(input("How many money do you want to add at your account?: "))
        self.account_balance += add_money
        print (f"You have added {add_money} and the new account balanse is {self.account_balance}")
        return self.account_balance
    
    def withdraw(self):
        '''A method to remove money in account'''
        
        remove_money = int(input("How many money do you want to remove from your account?: "))
        if self.account_balance >= remove_money:
            self.account_balance -= remove_money
            print (f"You have remove {remove_money} and the new account balanse is {self.account_balance}")            
            return self.account_balance
        else:
            print("there is insufficient balance ")

# person1 = Person("Antonis", "Taramigkos")
# customer1 = Customer(person1.firstname, person1.lastname)

def create_customer():
    first_name = input("Please enter your first name: ")
    last_name = input("Pleas enter you last name ")
    person1 = Person(first_name, last_name)    
    customer1 = Customer(person1.firstname, person1.lastname)
    
    return customer1


if __name__ == "__main__":
    customer1 = create_customer()    
    while True:    
        choice = int(input("Hello and wellcome to your personal banking\nYou can choose:\n1.See your current balance\n2.Deposit Money\n3.Withdraw Money\n4.See you Personal Info\n5.Exit\n"))
        if choice == 1:
            print(customer1.account_balance)
        elif choice == 2:
            customer1.deposite()
        elif choice == 3:
            customer1.withdraw()
        elif choice == 4:
            print(customer1)
        elif choice == 5:
            print(f"GoodBye {customer1.firstname}")
            exit()
            
