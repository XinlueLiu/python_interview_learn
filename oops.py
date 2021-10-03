#oops is about class and object
#including inheritance,polymorphism,data abstraction and encapsulation
#object could be anything exists in real-time, with characteristics and functions
#to group related functions for reusibility
#to create a template/blueprint

#class is the combination of attributes and methods
#any changes to the instance stays with instance. NOT with the class
#instance always passed to class as first argument, self

#constructor is called by default whenever create an object from a class
#can pass initialization information

#can delete object using dels obj
#however, not that neede since python has a garbage collector that handles memory automatically
#destructor

#inheritence. exchange object to parent class name

#python protect _
#python privite __
class Names(object):
    __age = 0
    __count = 0
    def __init__(self):
        Names.__count += 1
        print(f'initialization method. current count is {Names.__count}')
        return None
    def get_name_age(self,name,age):
        self.name = name
        self.__age = age
        return None
    def display_details(self):
        print(f'name is {self.name}')
        print(f'age is {self.__age}')
        return None
    def increase_age(self, count):
        self.__age += count

def main():
    name = Names()
    name.get_name_age("luelue", 22)
    name.display_details()
    name.increase_age(10)
    name.display_details()
    name1 = Names()
    name1.name = "test"
    name1.age = 10
    name1.display_details()
    name1.increase_age(10)
    name1.display_details()
    #this is still 0! no change
    #print(Names.age)
    #Names.age += 10
    #print(Names.age)
    #name2 = Names()
    #print(name2.age)
    #print(Names.count)
    del name, name1

if (__name__ == "__main__"):
    main()