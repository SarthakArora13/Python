string=input("Enter the String:--- ")
str=string
a=0
for i in range(len(string)):#madam
    if(string[0]==string[len(string)-1]):#m or m
        string=string[1:len(string)-1]#ada
        #print(string)
        if(len(string)==1):
            break
    else:
        a=1
if(a==0):
    print("Palindrome")
else:
    print("Not")
# string=input("Enter the String")
# str=string
# a=0
# while(len(string)>1):
# #for i in range(len(string)):#madam
#     if(string[0]==string[-1]):#m or m
#         string=string[1:-2]#ada
#         # if(len(string)>0):
#         #     continue
#         # else:
#         #     break
#     else:
#         a=1
# if(a==0):
#     print("Palindrome")
# else:
#     print("Not")
