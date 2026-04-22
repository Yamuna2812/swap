a=[]
for i in range(6):
    a.append(int(input("enter the marks")))
print("the marks  entered before swapping is",a)
for i in range(6):
   for j in range(5):
     if a[j]>a[j+1]:
         a[j],a[j+1]=a[j+1],a[j]
      
print("Marks from Heighest to Lowest")      
print(a)