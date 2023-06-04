print('*** extend function ***')
a=[1,2,3,4,1,2,3,4,1,2,3,4]
k=[1,2,3,4,5,6,7,8,9]
print('list',k)
k.extend([4,5,6]) # add the list to the given list
print('After performing extend method',k)

l1=a
l2=k
print("After performing extend with two different list",l2+l1)