#print("Hii this is my first API")
import requests
import json

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

#print(response)  #prints the response code for the request
#print(response.json()['items'])   #prints the actual response json for the req
#print(type(response))

for data in response.json()['items']:
    if data['answer_count'] == 0:
        print(data['title'])
        print(data['link'])
    else:
        print('skipped')
    print()

