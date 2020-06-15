#sum
def sum(x, y):
    return (x + y)

#differrence
def difference(x, y):
    return (x - y)

#division
def division(x, y):
    return (x / y)

#modulos
def modulos(x, y):
    return (x % y)

#mutiplication
def product(x,y):
    return(x * y)

a = int(input("enter a number... "))
b = int(input("enter another number... "))
c = sum(a, b)
d= difference(a,b)
e= division(a,b)
f= modulos (a,b)
g= product(a,b)

print("sum of", a, "and", b, "is", c)

print("difference of", a, "and", b, "is", d)

print("division of", a, "and", b, "is", e)

print("modulos of", a, "and", b, "is", f)

print("product of",a,"and",b,"is",g)
