'''in pop when u give a key the  value will be deleted but in the pop item then whole key and value will be deleted  '''
print('\n ***pop function ***')
Person={1:'sabarish','english':73,'math':80,'arts':21,'draw':75}
print("person dict",Person)
# only value will be deleted if need we can update the key value
print('\npop the value in the dictionary :-',Person.pop(1))
print("Update person dist",Person)