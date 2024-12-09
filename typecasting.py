#typecasting convert one data type to another data types

price= 90,50
print(price)
print(type(price))


#convert the integer
payprice =int(price)
print(type(payprice))

#converte int to string
amount=2500
stringamount= str(amount)
print(amount,"and data type is", type(stringamount))
#convert strint to int
gender="male"
#ctrl+/ to give the line comment
#genderintoinint(gender)


#conversion is not possible because string doesn't have ascaii number
#print(gender,"datatype is", gendertintoint)
#sto take the input from user c language scanf
myName= input("Enter your name")
#input function has default return type as str
myAge= input("Enter your age")
print("my name is"+ myName +"and age is" +myAge)
#find the age in years when bornyear and currentyear given by user
#currency convertor ruppes to USD:= 1 usd = 84r
#it generate the type arror, reason string only concatenate with string not int 
# #solution 1: replace+ by, when data type is not string
print("MY name is"+ name +"and salary",salary,"and age",age)
#solution 2: TYPEcast the data into string
print("my name is {name} salary is {salary} and age {age}")
#solution 3: typecast the data into string
salarystring=str(salary)
agestring=str(age)
print("My name is "+ name +"and salary"+salarystring+"and age "+agestring)


#To find the type of data we need to use type()function
print(type(name))
print(type(age))
print(type(salary))
