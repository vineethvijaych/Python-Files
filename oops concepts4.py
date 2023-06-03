# 3. Create a Book class with attributes title, author, and price. Implement a method discounted_price(percent) that calculates and returns the discounted price of the book based on the given percentage.

class book:
    title="aadujeevitham"
    author="benyamin"
    print(title)
    print(author)
    price=int(input("price:"))
    percentage=10
    def discounted_price(self):
        discounted=self.price-((self.percentage/100)*self.price)
        
        print(discounted)
obj=book()
obj.discounted_price()