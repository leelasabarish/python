print('\n*** Single inheritance ***')
class parent():
    def mom(self):
        print('iam ur mom')


class child(parent):
    def son(self):
        print('iam her child')


obj = child()
obj.mom()
obj.son()