string=input("Enter the String")
index=0
index1=0
str=""
l=string.split()
check=input("Enter the Checking element")
change=input("Enter the swaping element")
#checking the index for old word
for i in l:
    if(i==check):
        break
    else:
        index=index+1
#checking the index of swaping word
for i in l:
    if(i==change):
        break
    else:
        index1=index1+1
#print(index)
temp=l[index1]
l[index1]=l[index]
l[index]=temp
#print(l)
for i in l:
    str=str+i+" "
print(str)