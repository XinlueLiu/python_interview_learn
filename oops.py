#oops is about class and object
#including inheritance,polymorphism,data abstraction and encapsulation
#object could be anything exists in real-time, with characteristics and functions
#to group related functions for reusibility
#to create a template/blueprint

#class is the combination of attributes and methods
#any changes to the instance stays with instance. NOT with the class
class Names:
    def get_name_age(self,name,age):
        self.name = name
        self.age = age
    def display_details(self):
        print(f'name is {self.name}')
        print(f'age is {self.age}')