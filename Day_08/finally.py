# 1.The finally code block is also a part of exception handling. 
# 2.When we handle exception using the try and except block, we can include a finally block at the end.
# 3.The finally block is always executed, so it is generally used for doing the concluding
# tasks like closing file resources or closing database connection or may be
# ending the program execution with a delightful message.

# One of the important use cases of finally block is in a function which returns a value.

# try:
#     num = int(input("Enter an integer: "))
# except ValueError:
#     print("Number entered is not an integer.")
# else:
#     print("Integer Accepted.")
# finally:
#     print("This block is always executed.")


def func1():
    try:
        l = [1,2,3,4]
        i = int(input("Enter the index:"))
        print(l[i])
        return 1
    except:
        print("Some eroor ocuured")
        return 0
    finally:
        print("I am always executed")

x = func1()
print(x)