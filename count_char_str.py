str=input("Enter the String")
dict={}
count=0
for i in str:
    count=count+1
    dict[count]=i
    #print(i)
print("Number of Characters in a given string is..",count)
print(dict[1])