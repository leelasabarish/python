print('\n *** difference update***')
s1={1,2,3,7}
s2={3,4,5,6}
s2.difference(s1)
print(s1)
s2.difference_update(s1) #both difference and  difference_update r same
print(s1)

d={1,2,3}
d1={5,6,7}
d.difference_update(d1) # difference_update
print(d1)

f={1,2,3}
f1={1,2,3}
f1.difference_update(f)
print(f1) #if both r same set then diff is zero print empty set