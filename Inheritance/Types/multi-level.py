print('\n*** Multi-level inheritance ***')
class parent0():
    def grandfather(self):
        print('i have 1 child')
class child(parent0):
    def son(self):
        print('iam his son')
class child1(child):
    def daughter(self):
        print('iam his Granddaughter')

object2=child1()
object2.grandfather()
object2.son()
object2.daughter()