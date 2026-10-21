a=int(input("value of a :"))
b=int(input("value of b :"))
c=int(input("value of c :"))
d=(b**2)-(4*a*c)
x1=((-b)-(d**(1/2)))/2*a
x2=((-b)+(d**(1/2)))/2*a
print("value of x1 :",x1)
print("value of x2 :",x2)
if (d>0):
    print("real roots")
elif(d==0):
    print("equal roots")
elif(d<0):
    print("complex roots")
