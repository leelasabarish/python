class Private_gs_return():
    __name = None
    __age = None

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def display(self):
        return self.__name,self.__age #here we are using return here in this program it is packed as tuple
    def  setter(self,name,age):
        self.__name=name
        self.__age=age

ob=Private_gs_return('sai',44)
temp,temp1=ob.display()
print(temp,temp1)
ob.setter('satya',2001)
print(ob.display()) # here print will unpack function return will work where it called
