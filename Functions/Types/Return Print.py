def add(a,b):
    res=a+b
    print(res)
    return res
tup=add(10,10)
print(tup)

print('\n mul and add')
def gcc(a,b):
    add=a+b
    mul=a*b
    return add,mul
value,value1=(10,20)
print(gcc(value,value1))