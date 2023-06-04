def res(pi,*r):#non key word / var length length argument
    print(pi)
    print(r)
res('\n',3,5.10,'leela',25) # 3 mapped to pi and all other values to *r *r is a tuple

print('\nexp1')#exp1
a=((5)*4)*2
print(a)

print('\nexp2')#exp2
n=(1,'Two','3',4.0),
print(n[0][1])

print('\nexp3')#exp3
t=tuple('abc')
x=tuple(t)
print(x==t)

print('\nexp4')#exp4
q=(420,377),
y=(377)
print('1',y not in q)

print('\nexp5')#exp5
a=6,12,18,24
b=7,13,19,25
c=a+b;a+=b
print(c==a)

print('\nexp6')#exp6
p,q,r,s=(1,),((2),),(((3,))),(4,),
print(p,q,r,s)

print('\nexp7')#exp7
s=(8,6,3,4,8)
x=s in s
print(x)

print('\nexp8')#exp7
m='str','int',[],(),
string,integer,lists,tuples=m
m=string,integer,lists,tuples
print('\n',m)
m1=98,72,58,96,100
m2=20,54,78,62,34
m3=50,78,66,24,99
a1=m1,m2,m3
print('\n',a1)

print('\nexp9')#exp9
s=(1,2)
s1=((1,2),(1,2))
x1=s in s1
print('2',x1)


