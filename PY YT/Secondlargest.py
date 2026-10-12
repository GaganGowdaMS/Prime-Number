l=[51,599,694,8984,-5695,-2596,98]
secondlargest=l[0]
for i in l:
    if i>secondlargest and i<max(l):
        secondlargest=i
print(secondlargest)
