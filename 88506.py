if __name__ == '__main__':
    n = int(input())

    c=0
    s=0
    i=n

    while i>99:
        s = s + i * 10**c
        c = c + 3
        i = i - 1

    while i>9:
        s = s + i * 10**c
        c = c + 2
        i = i - 1

    while i >0:
        s = s + i * 10**c
        c = c + 1
        i = i - 1



    print(s)
