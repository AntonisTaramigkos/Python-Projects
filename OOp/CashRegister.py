import os

def clear_screen():
    os.system("cls")

dic_qty = {}
class CashRegister():
    

    def __init__(self,cashier) -> None:
        self.basket = []
        self.cashier = cashier

    def add_obj(self, list_items):
        
        for items in list_items:
            self.basket.append(items)


    def how_many_items(self, quantity=1):
        global dic_qty
        print("Num","\tItems","\t\t\tQty\n")
        
        for i, items in enumerate(self.basket):            
            print(f"{i+1}#\t{items}\t\t\t={quantity}")

        print("Choose an item and add quantity!")
        
        while True:
            obj = input("Choose object: ").capitalize()
            if obj in self.basket:
                
                qty = int(input("Choose quantity: "))
                x = dic_qty.get(obj, 0)  # Use 0 as the default value if obj doesn't exist
                if x >0:                    
                    new_qty = x + qty
                    dic_qty[obj] = new_qty
                else:
                    dic_qty.update({obj: qty})

                print(dic_qty)
                
            else:
                print("There is not that item in your list. Choose one you already have!!")
            choice = input("Do you want to add anymore?? (y/n)").lower()
            if choice == "y":
                continue
            else:
                break
        return dic_qty        
                      
      
    def show_the_list_of_products(self):
        y = self.how_many_items
        print("the list of products : ", y)  

    def remove_product(self):
        global dic_qty
        print("Do you want to remove something from you basket?")        
        for item in dic_qty.items():
            print(item)

        deleted_item = input()("\nChoose from the list",item)       
        
        if deleted_item == dic_qty.keys():
            del dic_qty[deleted_item]
            print(dic_qty)       
        

    def before_taxes(self):
        global dic_qty
        """ Here we find the prices from the dic of items 
        and we find the sum of items in the basket """
        for items in dic_qty.get("price"):
            print("f{items}\tprice: {items[price]}")

    def  total_taxes():
        pass

    def total_amount_of_purchases():
        pass


pizza = {"name": "Pizza", "price": 10.34}
burgers = {"name": "Burgers", "price": 12.50}
cola = {"name": "Cola", "price": 2.34}


clear_screen()
antonis = CashRegister("Antonis")
list_of_supermarket = ["Pizza", "Buergers", "Cola"]
antonis.add_obj(list_of_supermarket)

# antonis.how_many_items()
# antonis.show_the_list_of_products()
# antonis.remove_product()
antonis.before_taxes()