#import re
#re.finditer(r'\w','http://www.hackerrank.com/')
#<callable-iterator object at 0x0266C790>
#print(map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/')))
#print(re.finditer(r'\w','http://www.hackerrank.com/'))


import re
I = input()
a = re.findall(r'\w',I)
P1 = 0
P2 = 0
P3 = 0
P4 = 0
for i in a :
    print(i)
    if i in ("A", "E", "I", "O" , "U" , "a" , "e" , "i" , "o" , "u") and P1 == 1 and P2 == 0 and P3==0 and P4 ==0:

        P2 = 1

    else :
        if i in ("A", "E", "I", "O" , "U" , "a" , "e" , "i" , "o" , "u") and P1 == 1 and P2 == 1 and P3==0 and P4 ==0:
            P3 = 1
        else :
            if i in ("A", "E", "I", "O" , "U" , "a" , "e" , "i" , "o" , "u") and P1==1 and P2 == 1 and P3==1 and P4==0:
                P1 = 0
                P2 = 0
                P3 = 0
            else :
                if 1 == 1 and P2 == 1 and P3==1 and P4 ==0:
                    P4 = 1

    if P1 == 1 and P2 ==2 and P3 == 3 and P4 == 4 :
        print(i)









    print(P1)
    print(P2)
    print(P3)
    print(P4)
    print("####################")
    
