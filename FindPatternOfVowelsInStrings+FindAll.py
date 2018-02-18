#Question
#Task
#You are given a string . It consists of alphanumeric characters, spaces and symbols(+,-).
#Your task is to find all the substrings of  that contains  or more vowels.
#Also, these substrings must lie in between  consonants and should contain vowels only.


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
c = 0

Vowel = ''
for i in a :
    #print("Starting of FOR,P1" ,P1)
    #print("Starting of FOR,P2" , P2)


    if i in ("A", "E", "I", "O" , "U" , "a" , "e" , "i" , "o" , "u") :
        if P1 ==1 :
            P2 = P2 + 1
            FirstVowel = i
            Vowel = "".join((Vowel, FirstVowel))


    else :
        if P1 == 1 and P2 >= 2 :
            print(Vowel)
            c = 1
            #print("After PRINT P1" , P1)
            #print("After PRINT P1" , P2)
            Vowel = ''
            P2 = 0

        else :
            P1 = 1
            P2 = 0
            Vowel = ''


if c != 1 :
    print("-1")
