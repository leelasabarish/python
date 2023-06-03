print('\n*** Hierarchical inheritance ***')
class hierachica_parent():
    def father(self):
        print('iam ur parent')
class child(hierachica_parent):
    def son(self):
        print('iam his son')
class child1(hierachica_parent):
    def daughter(self):
        print('iam his daughter')

object2=child()
object3=child1()
object2.father()
object2.son()
object3.daughter()
