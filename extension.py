a = str(input("Enter The File Name: "))
python="py"
java="java"
b = a.split(".")
c=b[-1]
print(c)
if(c==python):
    print("The extension of the file is : 'python'")
elif(c==java):
   print("The extension of the file is : 'java'")
