print('\n*** union ***')
u={1,2,3}
u1={4,5,6}
u2={3,9,8}
print('set 1',u)
print('set 2',u1)
print('set 3',u2)
print('set 1 union set 2',u.union(u1))#club all elements in both set but if duplicate occure it will leave it
print(u|u1)
print('set 1 union set3',u.union(u2))
print(u|u2)