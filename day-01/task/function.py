# print table function 

def print_table():

    num = int(input("enter the number for table"))
    for i in range(1,11):
        print(f"{num} * {i} = {num * i} ")

# this is function calling 
print_table()