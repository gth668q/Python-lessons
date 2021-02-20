import csv


names = []

html_output = ''

with open('patrons.csv' , 'r') as f:

    csv_data = csv.reader(f)
    next(csv_data)
    next(csv_data)

    for line in csv_data:


        if line[0] == 'No Reward':
            break

        names.append(f'{line[0]} {line[1]}')

html_output += f'<p> These are {len(names)} winners. </p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)

    # csv_data = csv.reader(f)
    #
    # element = next(csv_data)
    #
    #
    #
    # for line in csv_data:
    #     # print(line)
    #     with open('new_support.csv', 'w') as fw:
    #
    #         csv_writer = csv.writer(fw, delimiter=':')
    #
    #         csv_writer.writerow(line)