
a = int(input("enter the number... "))
c = int(input("enter another number... "))
b = str(input("enter the operation.. "))

if(b=="+"):
    print(a, b, c, " is ",  (a+c))
elif(b=="-"):
    print(a,b,c,"is", (a-c))
elif(b=="*"):
    print(a,b,c,"is", (a*c))
elif(b=="/"):
    print(a,b,c, "is", (a/c))
elif(b=="%"):
    print(a,b,c, "is", (a%c))
else:
    print("invalid operation")





