#A teacher has marks of six students in one subject. Store the marks in a list and prepare a small result summary.
marks = [42, 92, 78, 96, 38, 20]
total=0
index=0
count=len(marks)
while index<count:
    total+=marks[index]
    index+=1
print("Total marks of six students:",total)
avg=total/count
print("Average marks of six students:",avg)
greatest=0
for i in range(len(marks)):
    if marks[i]>greatest:
        greatest=marks[i]
print(greatest)
result=["","","","","",""]
index=0
while i in marks:
    if i>35:
        result[index]="PASS"
        i+=1
    else:
        result[index]="FAIL"
print(result)



                 