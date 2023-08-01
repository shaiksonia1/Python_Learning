a=int(input("enter your age"))

def agechecker(a):
    if(a>50):
        print("you are old")
    elif(a<=18):
        print("you are an adult")
agechecker(a)

#default argurmrnts

def average(a=2,b=5):
    print("the average is", (a+b)/2)

average(3) # the secomd value taken as default value 
#where as 1st value is given by user if we want to change the second value we can mention it as b=8

#keyword arguements

def name(fname, mname, lname):
    print("hello,", fname,mname,lname)
name(mname = "Peter", lname = "Wesker", fname = "Jade")

#the order of keyword doesnt matter because the intrepreter recognizes thr arguements by the parameter name


def name(fname, mname, lname):
    print("hello,", fname,mname,lname)
name("shaik","sonia","ali" )

#s