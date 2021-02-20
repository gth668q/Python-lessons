import requests



r = requests.get('http://httpbin.org/delay/2', timeout= 3)


print(r.status_code)

# r = requests.get('http://httpbin.org/basic-auth/test/testing', auth=('test', 'testing') )
#
# print(r.text)

# print(r.content)
#
# with open('image.jpg', 'bw') as f:
#     f.write(r.content)