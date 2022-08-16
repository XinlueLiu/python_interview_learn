from unicodedata import name


class Dog():
    #class object attibute
    #same for any instance of a class
    species = 'mammal'

    #init as constructor of class
    #self is like an instance of the object itself
    #we take in the argument and assign it using self.attibute_name
    #we an retrieve the attibute_name later via instance
    def __init__(self,breed = 'xx',name = 'xx', spots = False):
        self.breed = breed
        self.name = name
        #expecting boolean t/f
        self.spots = spots

    #methods like a function in a class
    def bark(self, number = 0):
        print("bb! my name is {}, number is {}".format(self.name, number))

# my_dog = Dog(breed='PP', name = 'xx', spots = False)
my_dog = Dog()
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)
my_dog.bark('test')

# class B inherit from A
class B(A):
    def __init__(self, num):
        A.__init__(self)
        # inherit all methods of parent class
        super().__init__(p0,p1,p2)

#inheritance
class Cat(Dog):
    def __init__(self, breed = 'll', name = "xx", spots = True):
        Dog.__init__(self)
        #inherit all methods and properties of parent class
        #can be nice if has multiple layers of inheritance
        super().__init__(breed, name, spots)
        print("Cat Created")

    #use the same name to override parent method
    def bark(self):
        print("i cant bark I am a cat")

my_cat = Cat()
my_cat.bark()
print(my_cat.species)

# polymorphism
# same function name being used for different types
# Method Overriding: when work with inherience that child has same method name as parent

# can user define __str__ method when printing, __len__ when len, __del__ when try to delete

# __name__ get assigned when run the script. If __name__ = "__main__", it is ran directly
# so by checking this we can see if its being run directly or being imported