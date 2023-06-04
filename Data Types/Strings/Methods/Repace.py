print('\n*** repace function ***')
a='aaa aaa aaa sasa ddas dass dsda asd aaa asdf asdf adf'
print(a)
print(a.replace('aaa','qqq',2))# replacing substring  for 1st 2 times in string
print(len(a)) #length of a string
print(a)
print(a.find('aaa'),a.endswith('aaa')) # finding substring and checking if it is ending substring or not
print(a.find('dass'),a.endswith('adf'))