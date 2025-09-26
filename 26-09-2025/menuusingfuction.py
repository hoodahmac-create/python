def occurence(n):
    printed=[]
    words=n.split()
    for word in words:
                if word in printed:
                        continue
                else:
                    printed.append(word)
                    print("occurence of",word,"in the sentence is",words.count(word))
def characterFrequency(n):
    printed=[]
    for letter in n:
                if letter in printed:
                        continue
                else:
                    printed.append(letter)
                    print("character frequency of",letter,"in the word is",n.count(letter))
def factor(n):
    limit=int(input("enter the limit"))
    for i in range(1,limit):
            if(num%i==0):
                print(i)
while True:
    print("______________MENU______________")
    print("1.Occurence of each word \n2.character frequency \n3.factors \n4.exit")
    choice=int(input("enter your choice"))
    if(choice==1):
            sentence=input("eneter yoyr string")
            occurence(sentence)
            continue
    if(choice==2):
         word=input("enter your word")
         characterFrequency(word)
         continue
    if(choice==3):
        num=int(input("enter your number"))
        factor(num)
        continue
    if(choice==4):
        break
    else:
        print("invalid choice. try again")
        continue
