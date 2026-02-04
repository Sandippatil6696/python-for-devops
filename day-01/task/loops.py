# if we want to do a same task multiple time then we used loops 

for i in range(5):
    print("hellow dosto")


for j in range(1 ,6):
    print(j)


# print the table of any number 

num = int (input("enter the number for which you want table to print: "))

for i in range(1 , 11):
    print(i*num)

# String formating 

num2 = int (input("enter the number for which you want table to print: "))

for i in range(1 , 11):
    print(f"{num2} * {i} = {num2 * i}")


# while loop 
choice = ""
while choice != "q":
   num3 = int (input("enter the number for which you want table to print: "))
   for i in range(1 , 11):
       print(f"{num3} * {i} = {num3 * i}")
   choice = input("Press q to quit, or any other key to continue: ")
    
    

