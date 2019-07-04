'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
'''

f = open("abc.txt", "r")
# f.write(" - The Gurukul for Coders!")

# str = f.read()

# str = f.readline()
# str += f.readline(5)

# str = f.readlines()

f.seek(3, 0)
str = f.readline()
print(str)

f.seek(3, 1)
str = f.readline()
print(str)


f.seek(3, 1)
str = f.readline()
print(str)


f.seek(3, 1)
str = f.readline()
print(str)


f.close()