# method overloading

class Hotstar:
    def __init__(self,username):
        print(f'Hey {username},Welcome to the Hotstar')
    def playvideo(self):
        print("Ads will be run")
        print("Quality is low")
        print("No download option")
        print("No multiple logins")

class PremiumHotstar:
    def __init__(self,username):
        print(f'Hey {username},Welcome to the premium Hotstar')
    def playvideo(self):
        print("Ads won't run")
        print("Quality is high")
        print(" download option")
        print(" multiple logins"
