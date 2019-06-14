# 1) String

str1 = "Codekul"
str2 = 'The Gurukul for Coders!'

# 'Codekul' - "The Gurukul for Coders!"

str3 = """'{}'
    "{}"
        Python""".format(str1, str2)

'''
\n
\b
\t
\r
'''

str4 = 'Codekul - \rThe Gurukul for Coders!'

str5 = str4.replace(' ','_',-1)

# print(str5)

# 2) List

list1 = [1,2,3,4,5,"Six", "Seven", 9.10, True]
list2 = ["A", "B", "C"]

list3 = list1 + list2

list3.append('New')
list3.remove("Six")

c = list3.count("A")

length = len(list3)

# print(list3)

# print(length)

# 3) Dictionary

dict1 = {"Key1": "Value1", "Key2": "Value2", "Key3": 3}

dict2 = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 5: 'Five', 'Dict1': dict1}

# print(dict2)

# print(dict1["Key1"])

# 4) Tuple

t1 = (1,2,3,4,5)

# t1.remove(6)

# print(t1)

c1 = complex(10, 20)
print(c1)
c2 = complex(5, 10)
print(c2)

c3 = c1 + c2

c3 = c2 - c1

c3 = c1 * c2

print(c3)
