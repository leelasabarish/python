# Break brings control out of the loop
i = 0
print('where i = 0 so index 0 = element 0 upto index 6 but break statement so it prints up to index 4 = element = 3')
while i < 6:
  i += 1
  print(i)
  if i == 3:
    break # it breaks if i=3 does not execute up to index 6

print("*break*")
for i in range(3,7):
    if i==5:
        print("break")
        break
    else:
        print(i)

print("**** break with else ")
# if we use break in while loop then else block terminated automatically
i = 0
while i < 3:
  print(i)
  i += 1
  break
else:
  print("loop ends ")

print("*** with out break ****")
for i in range(3):
  print(i)
else:
  print("loop ends")

