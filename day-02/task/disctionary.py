# disctionary data structure 

info = {
    "name" : "sandip", 
    "age": 30 ,
    "city": "mumbai",
    "married" : True ,
    "salary": 45.50 ,
    "favourites":  ["movies" , "travelling" , 6]
}

print(info)
print(info["name"])
print(info["married"])

# but if we taken a wrong key then it will give error & if we use get function ikt does not give error  
print(info.get("ages"))
# print(info["ages"])

info.update({"channel" :"learnwithsandip"})
print(info)

# iterate dictionary 

for i,j in info.items():
    print(i,j)