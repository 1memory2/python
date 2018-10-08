for i in range(1,10):
    for k in range(1,i):
        print(end="       ")
    for j in range(i,10):
        print("{}*{}={:2} ".format(i, j,i*j),end='')
    print()
