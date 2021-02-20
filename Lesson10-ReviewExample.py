# JSON Javascript object notation


# Python	JSON
# dict	Object
# list	Array
# tuple	Array
# str	String
# int	Number
# float	Number
# True	true
# False	false
# None	null


import json

from urllib.request import urlopen

my_json_string = """{
   "article": [

      {
         "id":"01",
         "language": "JSON",
         "edition": "first",
         "author": "Derrick Mwiti"
      },

      {
         "id":"02",
         "language": "Python",
         "edition": "second",
         "author": "Derrick Mwiti"
      }
   ],

   "blog":[
   {
       "name": "Datacamp",
       "URL":"datacamp.com"
   }
   ]
}
"""

# data = json.loads(my_json_string)
#
# #data_string = json.dumps(data, indent=2)
#
# print(data['article'][1]['author'])


# Python Object to JSON string  dump/dumps
# JSON String to Python Object load/loads;\

# list = [ 'Mango', 'Apple', 'Banana']
#
# json_list = json.dumps(list)
#
# print(json_list)
#
#
# flag = False
#
# json_flag = json.dumps(flag)
#
# print(json_flag)


# with open('states.json') as f:
#     data = json.load(f)
#
#
#
# states = data['states']
#
#
# for state in states:
#     del state['area_codes']
#
#
# with open('new_states.json', 'w') as f:
#     json.dump(data, f, indent=2)

try:
    with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
        data = response.read()
except:
    print("Url didn't work")

# result = json.loads(data)
#
# print(type(result))
