# class and object


class Flipkart:

    discount = 10

    @classmethod
    def updatediscount(cls,newdiscount):
        cls.discount = newdiscount

        
    def userinfo(self,name,phonenumber):
        self.name = name
        self.phonenumber = phonenumber
        print(f'username: {self.name}')
        print(f'phone number: {self.phonenumber}')



    @staticmethod
    def banner():
        
        print("Welcome to the flipcart\n10% discount is going on,shop now")




praveen = Flipkart()
pravven.userinfo('praveen',98766543210)

praveen.updatediscount(30)
Flipkart.updatediscount(40)

praveen.banner()
Flipkart.banner()

sapnil = Flipkart()
saaketh= Flipkart()
