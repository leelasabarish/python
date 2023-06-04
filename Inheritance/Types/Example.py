class class1():
    def parent0(self,age=int()):
        print(age)

class class2():
    def parent1(self,name=str()):
        print(name)

class class3():
    def parent2(self,height=float()):
        print(height)

class fullaccess(class1,class2,class3):
    def parent3(self,weight=float()):
        print(weight)

object=fullaccess()
print(fullaccess.mro())
print(object.parent0(age=20),object.parent1(name='sabarish'),object.parent2(height=5.10),object.parent3(weight=60.72))
