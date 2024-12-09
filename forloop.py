#for loop is used to complete the iterration or repeating the task
name= input("Enter your name")
#alterate my name using for loop
#eg. in c for(int i=0;i<10.i++)
for i in name:
        print(i)

#print the no.1 to 10
for x in range(1,11):
        print(x)
#print this pattern using for loop 1 2 3 5 7 9 11 solve step size
for x in range(1,12,2):
 print(x)
 #print this patttern for loop 1 3 5 7 9 11

 for x in range(1,12):
       if x %2 !=0:
             print(x)
#print the even no. and odd no using for loop from 1 to 20
for y in range(1,21):
      if y % 2 ==0:
            print("ITS EVEN NO.")
      else:
            print("Its ODD NO.")
