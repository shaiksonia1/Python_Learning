try:
    num=int(input("enter a number: "))
    print(num)
except ValueError:
    print("number entered is not an integer.\n please enter avalid number")


try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")


#finally
""" When we handle exception using the try and except block,
 we can include a finally block at the end. The finally block is always executed, 
 so it is generally used for doing the concluding tasks like closing file resources
 or closing database connection or may be ending the program execution with a delightful message."""


def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")
  # print("I am always executed")


x = func1()
print(x)