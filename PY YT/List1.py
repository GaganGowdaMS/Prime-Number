a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
d=int(input("Enter a number:"))
e=int(input("Enter a number:"))
l=[]
l.append(a)
l.append(b)
l.append(c)
l.append(d)
l.append(e)
print(l)
print("The positive numbers are:")
for i in l:
    if i>=0:
        print(i)
print("The negative numbers are:")
for i in l:
    if i<0:
        print(i)