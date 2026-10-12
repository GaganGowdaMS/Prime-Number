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
sum=0
for i in l:
    sum=sum+i
average=sum/len(l)
print("The average of the numbers is:",average)
    