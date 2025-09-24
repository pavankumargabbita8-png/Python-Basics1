# # to handle an error we use 'try','except'
# 1.ZERO DIVISION ERROR
# try:
#     num=int(input("enter num"))
#     den=int(input("enter den"))
#     div=num/den
#     print(div)
# except ZeroDivisionError:
#     print("invalid")

# 2.VALUE ERROR
# try:
#     e=int(input("enter any number"))
# except ValueError:
#     print("given input is a value error")

# 3.TYPE ERROR
# try:
#     e=str(input("enter string"))
#     f=int(input("enter value"))
#     c=e+f
#     print(c)

# except TypeError:
#     print("given input is a type error")

# 4.NAME ERROR
# try:
#     s="pavan"
#     print(g)
# except NameError:
#     print("given input is a name error")

# # 5.INDEX ERROR
# try:
#     P=[1,2,3,4,5]
#     print(P[7])
# except IndexError:
#     print("given input is a index error")

# 6.KEY ERROR
# try:
#     P={
#         "name":"pavan",
#         "roll_no":"23"}
#     print(P["branch"])
# except KeyError:
#     print("given input is a key error")

# # 7.FILE NOT FOUND ERROR
# try:
#     file = open("students.txt","w")
#     print(file1.read())
# except FileNotFoundError:
#     print("given input file does not exist")


# finally
try:
    P=[1,2,3,4,5]
    print(P[7])
except IndexError:
    print("given input is a index error")

finally:
    print("program executed")



















































































