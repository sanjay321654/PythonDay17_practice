class User:
    def __init__(self, user_id, user_name ):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0

user = User("000", "Praba")
# print(user.id, user.name)
user_2 = User("111", "Sanjay")
print(user_2.id, user_2.name, user.id, user.name)





# user = User()
# user.id = "456"
# print(user.id)
# user2 = User()
# user2.id = "000"
# print(user2.id)

"""Attributes - the attributes is the variables that are associated with the object.
    e.g : car = Car()
         car.number = "tn19bv1487"
        In this the (number) after the dot is the attribute(variable), that is associated with the object.
 
 methods - The methods are the thing that the object does.
           The functions that are associated with the object is called method"""