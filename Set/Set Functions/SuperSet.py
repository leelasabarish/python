''' both sub set and super set are opposite to each other '''
print('\n*** superset ***')
su={1,2,3,4,5,6,7,8,9}
su1={5,8,1}
print('set 1',su)
print('set 2',su1)
print('set 1 superset set 2',su.issuperset(su1))
print('set 2 superset set 1',su1.issuperset(su))