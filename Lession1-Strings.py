
example_string  = "HELLO WORLD HELLO HELLO"

count_string = example_string.count('HELLO',  len(example_string)-5)

find_string = example_string.find('HELLO',  len(example_string)-5)

replaced_string = example_string.replace('HELLO', 'HI', len(example_string)-5)

print(dir(example_string.replace))
