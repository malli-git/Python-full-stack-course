'''#constructor a special method which is automatically created 


class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        print(f"Hey{self.username},Welcome to the Instagram!!!")

sapnil = Instagram('sapnil','s@123')
varsha = Instagram('varsha','v@123')
'''
#inheritance
class Instagramv1:
    
    def __init__(self,username,password):
        self.username = username
        print(f"Hey{self.username},Welcome to the Instagram!!!")


    def reels(self):
        print("you can upload and scroll the reels")

    def posts(self):
        print("you can post your pics")


class Instagramv2(Instagramv1):

    def __init__(self,username):
        super().__init__(username)

    def story(self):
        print("You can upload the story")

class Instagramv3(Instagramv2):
    
    def __init__(self,username):
        super().__init__(username)
    def note(self):
        print("You can upload a note")
class Live:
    def lauchlive(self):
        print("now you can go on live")


class verification:
    def verify(self):
        print("You can verify your account for better features")


class Instagramv4(Instagramv3,Live,verification):
    def __init__(self,username):
        super().__init__(username)


sapnil = Instagramv1('sapnil','s@123')
sapnil.reels()
sapnil.posts()



varsha = Instagramv2('varsha')
varsha.reels()
varsha.posts()
varsha.story()

malli = Instagramv3('malli')        
malli = note()

malli = Instgramv4('malli')
malli = live()
malli = verification()
