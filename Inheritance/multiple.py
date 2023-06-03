print('\n*** Multiple inheritance ***')
class parent():
    def dad(self):
        print('iam ur father')

class parent2():
    def mom(self):
        print('iam ur mom')

class child(parent,parent2):
    pass
    def son(self):
        print('iam there son')

object1=child()
object1.dad()
object1.mom()
object1.son()
