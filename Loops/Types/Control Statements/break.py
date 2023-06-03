# Break brings control out of the loop
i = 0
print('where i = 0 so index 0 = element 0 upto index 6 but break statement so it prints up to index 4 = element = 3')
while i < 6:
  i += 1
  print(i)
  if i == 3:
    break # it breaks if i=3 does not execute up to index 6
