# def first(x):
#     print("Starting first")
#     second(x)

# def second(x):
#     print("Starting second")
#     third(x)

# def third(x):
#     print("Starting third")
#     try:
#         result = 10 / x
#         return result
#     except:
#         x = x = 1
#         first(x)
# first(0)

"""
The issue with the above program is that it will loop the functions, so it will do first() -> second() -> third() -> first() -> second() -> third()
"""