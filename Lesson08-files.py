##The Basics:
#f = open("test.txt", "r")
#f = open("test.txt", "w")
#f = open("test.txt", "a")
#f = open("test.txt", "r+")
#print(f.name)
#print(f.mode)

#
# try:
#    fh = open("testfile", "w")
#    fh.write("This is my test file for exception handling!!")
# except IOError:
#    print "Error: can\'t find file or read data"
# else:
#    print "Written content in the file successfully"
#    fh.close()

# try:
#     f = open('test.txt', 'r')
#     f.read()
#
# except Exception:
#     print("Trying to write on a file file which is read only")
#
# else:
#
#     f.close()
#
# finally:
#     print("We are in finally")


with open("test.txt", "r") as f:

    size_to_read = 10
    file_contents = f.read(size_to_read)
    while len(file_contents) > 0:
        print(file_contents)
        print(f.seek(200))
        file_contents = f.read(size_to_read)






