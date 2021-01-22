

myString = "Hello World"

# myList = []
# print(myList)

# for i in myString:
#     myList.append(i)
#
# print(myList)


# Do the same thing using comprehension

# myList = [ i+'a' for i in myString ]
#
# print(myList)

# nums = [1,2,3,4,5,6,7,8,9,10]
#
# nums_square = [ num  for num in nums if num%2 == 0 if num%5 == 0]
#
# print(nums_square)

# newList = ["even number" if i%2 == 0 else "odd number" for i in range(10) ]
# # # print(newList)


# Decorators

# def firstFunc(message):
#     print(message)
#
#
# firstFunc("Hello Word")
#
# secondFunc = firstFunc
#
# secondFunc("Hello Universe")


# def inc(x):
#     return x+1
#
# def dec(x):
#     return x-1
#
# def operate(func, x):
#
#     result = func(x)   # result = inc(2)
#     return result
#
# print(operate(dec, 2))

# def is_called():
#     def is_returned():
#         print("Hello World")
#     return is_returned
#
#
# newfunc = is_called()
#
# newfunc()

# def decorator_func(func):
#     def innerfunc():
#         print("I got decorated")
#         func()
#     return innerfunc
#
# @decorator_func
# def not_decorated():
#     print(" I am just an ordinary function")
#
#
# print(not_decorated())