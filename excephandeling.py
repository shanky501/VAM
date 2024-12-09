#error handeling

#try:
#   Taberror
#catch:
 #  type of error

#
#try:
  #  print(x) #name error
#except NameError:
  #  y=1/0   #zerodivision error
 #   print(y)

# try:
#    y=1/0
#    print(y)
# except ZeroDivisionError: #zerodivision error
#     print("zeroDivision error ")

# # problem error


# #try:
#a ="shanky"
#b= int(a) #valueerror
#print(b)
#except ValueError:
#    print("string not constant is i  t error")


# import os.remove("myfile.txt")  #file is not found
# try:
#    a ="shanky"
#    b= int(a) #valueerror
#    print(b)
# except FileNotFoundError:
#     print("File is not found")



# x="shanky"
# y=4
# #c=x+4
# #print(c)
# try:
#     c=x+y
#     print(c)
# except TypeError:
#     print("Type Error")

x="pawan"
y=4
try:
    c=x+y
except TypeError:
    print("interoot range")