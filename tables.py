
while True:
    n = int(input("enter a number between 1 and 1000 inclusive..."))
    if (n <= 0):
        break
    else:
        for i in range(1, 21):
            print (n, 'X', i, '=', n * i)