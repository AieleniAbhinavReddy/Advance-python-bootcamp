#parent method
class Parent :
    #Constructor
    def __init__(self,name = None,age = None) :
        self.name = name
        self.age = age
    def func(self) :
        print('This is Parent class method')
    def func(self,name) :
        print(f'My name is {name}')
#child class
# class Child :
#     def func(self) :
#         print('This is child class method')
#main method
def main() :
    obj = Parent()
    obj.func()
    obj.func('Abhinav')
if __name__ == '__main__' :
    main()
