class Private():
    a=100
    _b=200
    __c=300
object2=Private()
print(object2.a)
print(object2._b)
#print(object2.__c) #in Private modification can not be done by using object also


class Private1():
    a = 99
    _b = 290
    __c = 340
    spy=__c # with class method we can access class members either public,private,protected
object3=Private1()
print(object3.spy)

class Private2():
    __name=None
    __age=None
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def display(self):
        print(self.__name)
        print(self.__age)
obj=Private2('sun',20)
obj.display()