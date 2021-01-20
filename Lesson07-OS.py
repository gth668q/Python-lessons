import os

# print(os.getcwd())

os.chdir('/Users/khanmo@us.ibm.com/PycharmProjects/')

#
# print(os.getcwd())
#
# # print(os.listdir())
#
# # os.makedirs("NewDirectory/InsideDirectory")
#
# print(os.listdir())
#
# os.chdir("NewDirectory")
#
# print(os.stat("InsideDirectory"))


# for dirpath, dirnames, filenames in os.walk('/Users/khanmo@us.ibm.com/PycharmProjects/'):
#     print('Current Path', dirpath)
#     print('Directories:', dirnames)
#     print("Files:", filenames)
#     print()

basepath = os.environ.get("HOME")

my_file = "text.txt"

combined_path = os.path.join(basepath ,my_file)

print(combined_path)