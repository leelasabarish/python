''' both sub set and super set are opposite to each other '''
print('\n *** sub set***')
s={1,2,3,4,5,6,7,8,9}
s1={5,8,1}
print('set1',s)
print('set2',s1)
print('set 1 subset set 2',s.issubset(s1))
print('set 2 subset set 1',s1.issubset(s))