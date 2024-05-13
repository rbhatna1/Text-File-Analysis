def space(): #To make it look good and have proper demarcations
    print()
    print("**********************************************************")
    print()

def bytes():
    a=open("story.txt")
    b=a.readlines()
    lenght=0
    for c in b:
        d=c.strip()
        lenght+=len(d)
    print("The number of bytes in the following program is",lenght)
    a.close()

def numberofalphabets():
    a=open("story.txt")
    words=a.read()
    count=0
    for c in words.split():
        for d in c:
            if ord(d.upper())>65 and ord(d.upper())<92:
                count+=1
    print("The number of alphabets are",count)
    a.close()
    
def digits():
    a=open("story.txt")
    words=a.read()
    count=0
    for c in words.split():
        for d in c:
            if d.isdigit():
                count+=1
    print("The number of digits are",count)
    a.close()
    
def upperandlowercase():
    a=open("story.txt")
    words=a.read().strip()
    uppercount=0
    lowercount=0
    for c in words.split():
        for d in c:
            if d.isupper():
                uppercount+=1
            elif d.islower():
                lowercount+=1
    print("The number of uppercount are",uppercount,"lowercount are:",lowercount)
    a.close()
    
def vowels():
    a=open("story.txt")
    words=a.read()
    vowels=0
    for c in words.split():
        for d in c:
            if d.lower() in ["a","e","i","o","u"]:
                vowels+=1
    print("The number of vowels are",vowels)
    a.close()

def numberofwords():
    a=open("story.txt")
    words=a.read()
    count=0
    for c in words.split():
        count+=1
    print("The number of words are",count)
    a.close()

def numberofsentences():
    a=open("story.txt")
    lines=a.readlines()
    print("The number of lines are:",len(lines))
    
def averageofwordssize():
    a=open("story.txt")
    b=a.read()
    avgsize=0
    number=0
    for words in b.split():
        avgsize+=len(words)
        number+=1
    print("The averge size of the words are",avgsize/number)

def occurnacesofto():
    a=open("story.txt","r")
    x=a.read()
    c=0
    for d in x.split():
        if d in ["TO","to"]:
            c+=1
    print("The number of words are:",c)
    a.close()

def numberofa():
    a=open("story.txt")
    words=a.read()
    count=0
    for c in words.split():
        for d in c:
            if d.lower()=="a":
                count+=1
    print("The number of a are",count)
    a.close()

def numberofmnstartingwords():
    a=open("story.txt")
    words=a.read()
    count=0
    for c in words.split():
        if c[0].lower() in ["m","n"]:
            count+=1
    print("The number of words are",count)
    a.close()

def wordsmorethan5letters():
    a=open("story.txt","r")
    x=a.read()
    count=0
    for d in x.split():
        if len(d)>=5:
            count+=1
    print("The number of words with more than 5 letters are:",count)
    a.close()

def occurnacesoftheaan():
    a=open("story.txt","r")
    x=a.read()
    c=0
    for d in x.split():
        if d.lower() in ["the","a","an"]:
            c+=1
    print("The number of words are:",c)
    a.close()

def printingmorethan5():
    a=open("story.txt","r")
    x=a.read()
    count=0
    for d in x.split():
        if len(d)>=5:
            print(d)
    a.close()

def printingbegingingwithmn():
    a=open("story.txt","r")
    x=a.readlines()
    c=0
    for d in x:
        if d[0].lower() in ["m","n"]:
            c+=1
    print("The number of lines are:",c)
    a.close()

def beginningwitha():
    a=open("story.txt","r")
    x=a.readlines()
    c=0
    for d in x:
        if d[0] in ["a","A"]:
            c+=1
    print("The number of lines are:",c)
    a.close()

def linestouppercase():
    a=open("Text_file.txt","r")
    b=open("story.txt","a+")
    x=a.readlines()
    c=0
    for d in x:
        print(d.upper().strip(),file=b,flush=True)
    a.close()
    b.close()

def spacewithstar():
    a=open("Text_file.txt","r")
    b=open("story.txt","a+")
    x=a.readlines()
    c=0
    for d in x:
        if e==" ":
            print("*",file=b,flush=True,end="")
        else:
            print(e,file=b,flush=True,end="")
    a.close()
    b.close()
    
def noofwords():
    with open("Text_file.txt","r") as A:
        x=A.read().strip()
        y=len(x.split())
        print(y)
        
choice=0

while choice!=20:
    print("Choose from one of the following options")
    print("1)To return the number of bytes.")
    print("2)To return the count of number of alphabets.")
    print("3)To return the count of number of digits")
    print("4)To return the count of number of uppercase and lower case letters.")
    print("5)To return the count of number of vowels.")
    print("6)To return the count of number of words")
    print("7)To return the count of number of sentences.")
    print("8)To return the average word size")
    
    print("9)To count and return the number of occurrences of ‘to’ as an independent word in the text file")
    print("10)To count and return the count of times the alphabet ‘A’ or ‘a’ exists in the file.")
    print("11)To return the count of all words beginning with ‘M’ or ‘N")
    print("12)To return the count of words having more than 5 characters in it")
    
    print("13)To return the count of all the articles “the”, “a” and “an” present in the file")
    print("14)To return the count of total number of sentences from the file, assuming each sentence is ended with a new line character")

    print("15)To display those lines which are beginning with either an M or N")
    print("16)To create another file “Mystory.txt” which should contain words starting with A")
    print("17)Create another file “Newfile.txt” by converting each line into uppercase string")
    print("18)Read a text file “MyStory.txt” and create another file “Star.txt” by replacing every space in the existing file with a ‘*’.")
    print("19)To count the number of words")
    print("20)To exit the program")
    choice=int(input("Enter the choice"))
    
    if choice==1:
        space()
        bytes()
        space()
        
    elif choice==2:
        space()
        numberofalphabets()
        space()
        
    elif choice==3:
        space()
        digits()
        space()
        
    elif choice==4:
        space()
        upperandlowercase()
        space()
        
    elif choice==5:
        space()
        vowels()
        space()
        
    elif choice==6:
        space()
        numberofwords()
        space()
        
    elif choice==7:
        space()
        numberofsentences()
        space()
        
    elif choice==8:
        space()
        averageofwordssize()
        space()
        
    elif choice==9:
        space()
        occurnacesofto()
        space()
        
    elif choice==10:
        space()
        numberofa()
        space()
        
    elif choice==11:
        space()
        numberofmnstartingwords()
        space()
        
    elif choice==12:
        space()
        wordsmorethan5letters()
        space()
        
    elif choice==13:
        space()
        occurnacesoftheaan()
        space()
        
    elif choice==14:
        space()
        printingmorethan5()
        space()
        
    elif choice==15:
        space()
        printingbegingingwithmn()
        space()
        
    elif choice==16:
        space()
        beginningwitha()
        space()
        
    elif choice==17:
        space()
        linestouppercase()
        space()
        
    elif choice==18:
        space()
        spacewithstar()
        space()
        
    elif choice==19:
        space()
        noofwords()
        space()
