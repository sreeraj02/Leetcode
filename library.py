fulllibrary=[{"id":111,"name":"The Ascent of Money","author":"bob","price":566,"available":2},{"id":112,"name":"The Disciplined Trader","author":"niko","price":896,"available":5}]
class product:
    def __init__(self):
        self.product_id=""
        self.product_name=""
        self.author=""
        self.price=0
        self.availability=0
        self.count=0
        self.purchased=""

    # def adding(self):
    #     self.product_id=int(input("enter the product id"))
    #     self.product_name=input(("enter the product name"))
    #     self.author=input(("enter the product author"))
    #     self.price=int(input("enter the product price"))
    #     self.availability=int(input("enter the product availability"))
    #     productset={"id":self.product_id,"name":self.product_name,"author":self.author,"price":self.price,"available":self.availability}
    #     fulllibrary.append(productset)
    #     print(fulllibrary)

    
    def display(self):
        if len(fulllibrary)==0:
            print("No books")
        else:
            for i in fulllibrary:
                print(i,"\n")
    def available(self):
        tempid=int(input("enter the id"))  
        for i in fulllibrary:
            if i["id"]==tempid:
                qty=int(input("enter the value"))
                if i["available"]>=qty:
                    print(i["available"],"available")
                else:
                    print("not available")
    def buybook(self):
        bookname=input("enter the book to buy")
        for i in fulllibrary:
            if i["name"]==bookname:
                quant=int(input("enter how much quantity to buy"))
                if i["available"]>=quant:
                    i["available"]-=quant
                    self.count+=1
                    self.purchased=bookname
                    print("done successfully")
                else:
                    print("not available")
        else:
            print("book not available")
    def status(self):
        if self.count>=1:
            print("status \n you have now currently purchased a book named:",self.purchased)
        else:
            print("status\n your cart is empty")
obj=product()
while True:
    print("1.TO display all books details")
    print("2.display specific book")
    print("3.buy book")
    print("4.status of book")
    print("5.exit")
    m=input("enter")
    if m=="1":
        obj.display()
    if m=="2":
        obj.available()
    if m=="3":
        obj.buybook()
    if m=="4":
        obj.status()
    if m=="5":
        break
    





