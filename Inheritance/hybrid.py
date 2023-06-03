print('\n*** Hybrid inheritance ***')

class father:
    def dad(self):
        print('iam ur father')

class mother(father):
    def mom(self):
        print('iam ur mom')

class child(mother,father):
    pass
    def son(self):
        print('iam there son')

object=child()
object.dad()
object.mom()
