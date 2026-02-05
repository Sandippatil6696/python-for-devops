# first type to declare list
b = [110,220,41.5,"hellow" , True] 

print(b)
print(type(b))

b.append("hellow dosto")
b.append(2)
print(b)

print(b[0])
print(b[3])
print(b[-1])
print(b[-2])


# second way to declare list

clouds = list()
print(type(clouds))

clouds.append("aws")
clouds.append("azure")
clouds.append("gcp")
clouds.append("utho")

print(clouds)
print("length of list is : " ,len(clouds))

print("world leader for cloud service is : ",clouds[0])

# dir function show what will you do with current object here clouds i.e list then it shows what you will you do with lists
print(dir(clouds))

# __doc__ shows documents for fuctions 
print(clouds.count.__doc__)
print(clouds.copy.__doc__)
#print(clouds.sort.__doc__)

for i in clouds:
    if i == "aws":
        print("market leader")
    elif i == "azure" or i == "utho":
        print("devops zero to hero")
    else:
        print("baki no competetion")

    


