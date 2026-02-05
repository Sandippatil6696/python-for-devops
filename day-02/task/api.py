import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"

response=requests.get(url=api_url)

print(response.json())

# i will get response in such format 

#{
#  "userId": 1,
#  "id": 1,
#  "title": "delectus aut autem",
#  "completed": false
#}

for i ,j in response.json().items():
    print(i , j)

for key,value in response.json().items():
    if key == "completed":
        if value == False:
            print("record is not completed") 

for m , n in response.json().items():
    if m == "userId":
        if n in [5,2,4,1]:
            print("userid is present")