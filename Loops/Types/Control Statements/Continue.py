# Continue returns the control to the beginning of the loop.
i = 0
print('where i = 0 so index 0 = element 0 upto index 6 = element 6')
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

print("*** continue ***")
for i in range(3,7):
    if i==5:
        continue
    else:
        print(i)


