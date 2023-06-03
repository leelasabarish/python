class Private_gs():
    __name = None
    __age = None

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def display(self): # here display method used as getter methos  it will access private attributes and print them
        print(self.__name)
        print(self.__age)
    def  setter(self,name,age):# Here setter method  will access and modify the private attributes but to print again we need getter method
        self.__name=name
        self.__age=age
ob=Private_gs('sai',100)
ob.display()
ob.setter('bye',21)
ob.display()
