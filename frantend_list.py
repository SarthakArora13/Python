# print("hello")
l1=[9,10,['a','b','c'],11]
l2=[]
for i in l1:
    if(type(i)==list):
        for a in i:
            l2.append(a)
    else:
        l2.append(i)        
print(l2)
# f.extend(l1[2])