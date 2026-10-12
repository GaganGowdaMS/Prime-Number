l=[1,9,64,898,5695,9596,10098]
for i in range(len(l)-1):
    if l[i]<l[i+1]:
        continue
    else:
        print("Unsorted List")
        break
else:
    print("Sorted List")    




