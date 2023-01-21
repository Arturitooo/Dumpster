#day17

class User:
    def __init__(self, id, name):
        self.user_id = id
        self.user_name = name
        self.followers = 0 
        self.following = 0 

    def follow(self,user):
        user.followers += 1
        self.following += 1
    
    def user_info(self):
       print("This user has:",self.followers,"followers, and he or she follows:",self.following,"users")

user_1 = User("001", "Artur")
user_2 = User("002", "Martur")

user_1.follow(user_2)

print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)