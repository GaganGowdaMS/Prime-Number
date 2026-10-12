a=input("Enter the string:")
b=""
for i in range(len(a)-1,-1,-1):
    b=b+a[i]
if a==b:
    print("It is a Palindrome")
else:
    print("It is not a palindrome")
