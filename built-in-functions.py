# # python functions
# def rectangle(length, width=15):
#     area= length* width
#     return area
# # len=int(input("Enter Length:"))
# # wid=int(input("Enter Width:"))
# print(rectangle(7,3))
# # print(rectangle(14, 7))


# def fruit(*args):
#     for item in args:
#         print (item)
# fruit("apple","mango","pineapple","passion")


# def marks(*args):
#     for mark in args:
#         print(mark)
# marks(90,20,70,89,76)

def students (**kwargs):
    for x,y in kwargs.items():
        print(x,y)
students(name="John", RegNo=1234, age="32")