def wee():#---->function name global scope
    print('1') # print are local scope
    print('2')
wee()

temp=wee()
print('\n',temp) # prints return type
