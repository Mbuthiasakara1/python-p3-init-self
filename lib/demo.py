# is a specila parameter used in instance methods to refer to the instance of the class itself,its like a placeholder for the object being worked on


# class Dog:
#     def __init__(self,name,colour):
#         self.name=name
#         self.colour=colour

#     def bark(self):
#         print(f"{self.name} was born and his fur is {self.colour}!")  

    

# fido=Dog("fido","yellow")   
# fido.bark()

class Dog:
    def __init__(self,name,favorite_toy="Any"):
        self.name=name
        self.favorite_toy=favorite_toy
    def bark(self):
        print("fido will woof!")  
    def get_adopted(self,owner_name):
        self.owner=owner_name 
        print(f"{self.owner} is the one who takes care of {self.name}")

Fido=Dog("Fido","lego")  
print(Fido.favorite_toy)
Fido.get_adopted("Sophie")    