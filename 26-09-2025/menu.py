while True:
    print("______________MENU______________")
    print("1.Occurence of each word \n2.character frequency \n3.factors \n4.exit")
    choice=int(input("enter your choice"))
    if(choice==1):
            sentence=input("eneter yoyr string")
            printed=[]
            words=sentence.split()
            for word in words:
                if word in printed:
                        continue
                else:
                    printed.append(word)
                    print("occurence of",word,"in the sentence is",words.count(word))
            continue
    if(choice==2):
         word=input("enter your word")
         printed=[]
         for letter in word:
                if letter in printed:
                        continue
                else:
                    printed.append(letter)
                    print("character frequency of",letter,"in the word is",word.count(letter))
         continue
    if(choice==3):
        num=int(input("enter your number"))
        limit=int(input("enter the limit"))
        for i in range(1,limit):
            if(num%i==0):
                print(i)
        continue
    if(choice==4):
        break
    else:
        print("invalid choice. try again")
        continue
