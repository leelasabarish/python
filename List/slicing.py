l=[1,2,3,4,5,6,7,8,9,10]
print(*l)
print("1 printing list=",l)
print('2.printing only elements=',*l)
print("3.slicing from 0 to 3rd index=",l[0:3])
print("4.index value of 2=",l[2])
print("5.indexing value -2=",l[-2]) # from last butone
print("6.indexing value -3=",l[-3]) # from last 3rd value
#slicing
print("7.slicing of index value 0 to 3=",l[0:3])# n-1
print(l[3:3])
print(l[::])#slicing operation work as range operation
print("8.increment by 1=",l[::2])
print(l[::-1]) #backwords

