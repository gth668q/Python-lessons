
example_string  = "HELLO WORLD"

string2 = "This is year 2021."

count_string = example_string.count('HELLO',  len(example_string)-5)

find_string = example_string.find('HELLO',  len(example_string)-5)

replaced_string = example_string.replace('HELLO', 'HI' )


combined_string = example_string + ', ' +  string2


name = "Edward"
age = 20

string = "My name is %s, and I am %d years old " %(name, age)

string2 = "My name is {}, and I am {} years old".format(age, name)

string3 = f"My name is {name} and I am {age} years old"

print(string3)

