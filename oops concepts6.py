# 5. Create a class called Product that represents a product in an online store. The class should have attributes for the product's name, price, and quantity. It should also have a method called sell that reduces the quantity of the product when a sale is made. 

class product:
    name="speaker"
    price=500
    quantity=100
    print("name:",name)
    print("price:",price)
    print("quantity:",quantity)
    def sell(self,b):
        self.b=b
        sell=self.quantity-b
        print("sale:",b)
        print("balance quantity:",sell)
obj=product()
obj.sell(20)