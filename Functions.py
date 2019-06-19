'''
def my_function():
    print("my_function")

my_function()

def function_with_param(a1, a2, a3=100):
    print("id(a1):",id(a1))
    a1 = 20
    print("id(a1):",id(a1))
    a1 = 200
    print("id(a1):",id(a1))

    print("Value of a1:",a1)
    print("Value of a2:",a2)
    print("Value of a3:",a3)

b = "Codekul"
function_with_param(b, 10)
'''

def function_list(list1):
    print(id(list1))
    print(list1)
    # list1.append(6)
    # print(id(list1))
    # print(list1)
    list1 = [9,8,7,6]
    print(id(list1))
    print(list1)

l1 = [1,2,3,4,5]
print("id(l1)",id(l1))
print(l1)
function_list(l1)
print("id(l1)",id(l1))
print(l1)

def function_returning(a):
    a += " - The Gurukul for Coders!"
    return a

s = function_returning("Codekul")
print(s)
