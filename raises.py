#in python we can custom errors by using the keyword RAISE

a = int(input("enter a value between 5 and 9"))
if(a<5 or a>9):
    raise ValueError("number should be between 5 and 9")