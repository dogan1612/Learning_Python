
import requests

url = 'https://jsonplaceholder.typicode.com/photos'

# GET REQUEST
response = requests.get(url)                    #get the data about the photos
print(response.json())                          # to print all the objects  ==> [{...},{...},{...}]         ==>  {'albumId': 98, 'id': 4863, 'title': 'voluptas doloremque minima', 'url': 'https://via.placeholder.com/600/624bac', 'thumbnailUrl': 'https://via.placeholder.com/150/624bac'},

# POST REQUEST
jsonPayload = {'albumId': 1, 'title': 'test', 'url': 'nothing.com', 'thumbnailUrl': 'nothing.com'}          # let's define a JSON payload
response = requests.post(url,json=jsonPayload)
print(response.json())
# Line 13 will return:  {'albumId': 1, 'title': 'test', 'url': 'nothing.com', 'thumbnailUrl': 'nothing.com', 'id': 5001}
# We can see that we've added a new photo with the ID of 5001 so now there's an additional photo in the album.
# Terminal'den ayni islemi yaparken, sadece response.json() yeterli

# PUT REQUEST
url = 'https://jsonplaceholder.typicode.com/photos/100'
response = requests.put(url,json=jsonPayload)
print(response.json())
# We can see here that we've modified photo ID 100 to include the new information that we defined.
# {'albumId': 1, 'title': 'test', 'url': 'nothing.com', 'thumbnailUrl': 'nothing.com', 'id': 100}

# DELETE REQUEST
response = requests.delete(url)
print(response.json())
# {}


