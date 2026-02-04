# take input from user and print output on terminal 

env = input("enter the environment ")

print(env)

# if 

if env == "prod":
    print("its friday not time to deploye")

# if else 

if env == "test":
    print("this is testing environment")
else:
    print("this is public time")


# if elif 
choice = input("Enter the envirnment: ")

if choice == "prod":
    print("this is production envirnment")
elif choice == "test":
    print("this is test envirnment")
else:
    print("application is not deployed yet")



