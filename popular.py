
print(__name__)

def myfunc():
    print("I am being called from the popular file")


if __name__ == '__main__':
    myfunc()
else:
    print("I am being called from outside")