import urllib.request
import requests
'''
opener = urllib.request.build_opener()
response = opener.open('https://httpbin.org')
print(response.read())
response = requests.get('https://httpbin.org/get')
print(response.content)
'''
responce = requests.post('https://httpbin.org/post',
                         data ={'Test form': 'my_form'},
                         headers={'h1':'Test title'})
print(responce.text)