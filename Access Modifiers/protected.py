class protected():
    a=10
    _b=20 #protected class member/ class variable
object1=protected()
print(object1.a)
print('accessing',object1._b)
object1._b=100
print('modification',object1._b) #modification can be possiable by using object in protected class
