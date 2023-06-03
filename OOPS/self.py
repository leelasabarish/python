''' class name.  we can access the methods and function outside the class  '''
class wish():
    temp='hello guys'
    print(temp)
    def greet(self): #if we are calling with object we need self|but using class name self is not necessary
        print('inside greet method in class good afternoon')

#object name is ur wish
object=wish()
object.greet()