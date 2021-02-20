# import os
#
# # os.chdir("/Users/khanmo@us.ibm.com/PycharmProjects/lesson/files")
#
# os.chdir("files")
#
# # print(os.getcwd())
#
# files = os.listdir()
#
# for file in files:
#     f_name, f_ext = os.path.splitext(file)
#
#     f_title, f_subject, f_num = f_name.split('-')
#
#     f_num = f_num[1:].zfill(2)
#
#     new_name = '{}-{}{}'.format(f_num, f_title, f_ext)
#
#     os.rename(file, new_name)


# condition = False
# #
# # if condition:
# #
# #     x = 1
# # else:
# #     x = 0
# #
# # print(x)
#
# x = 1 if condition else 0
#
# print(x)

# num1 = 1000_000_000_000
# num2 = 10_000_000_000_000_000
#
# sum = num1 + num2
#
# print('{: ,}'.format(sum))


list = ["apple", 'orange', 'mango']

# index = 0
#
#
# for i in list:
#     print(index, i)
#     index += 1
#

# for index, item in enumerate(list, start=1):
#     print(index, item)


names = [ 'Peter Parker', 'Clark Kent', 'Bruce Wayne']

heroes= [ ' Spiderman', 'Superman', 'Batman']

universes = [ 'marvel' , 'DC', 'Marvel']


# for index, name in enumerate(names):
#
#     print('{} is {}'.format(name , heroes[index]))


# for name, hero in zip(names, heroes):
#     print('{} is {}'.format(name, hero))

# for i in zip(names, heroes, universes):
#     print(i)