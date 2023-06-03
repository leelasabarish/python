print('\n*** replace function ***')

s='iam leela sabarish from git'
print(s.replace('l','LA')) #if we need to replace anything in the string
print(s)
s1=s.replace('l','LA') #u must resing to replaced the string
print(s1)
print(s.endswith(s)) # checking with total string with same string
print(s.startswith(s))# checking with total string with same string
print(s.find('LeeLa'),s.endswith('LeeLa',0,9)) # finding substring and weather it's ending with given index or not
print(s.replace('Leela','LEELA',1)) # replacing substring  for 1st time in string

