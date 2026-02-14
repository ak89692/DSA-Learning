def star_inverted(n):
    for i in range(n):
        for j in range(n):
            if(j>=i):
                print('*',end="")
        print()


star_inverted(5)