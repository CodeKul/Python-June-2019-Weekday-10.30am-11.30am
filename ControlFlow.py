a = 30
b = 20

if a < b:
    # true part
    print("a is less than b")
elif a == b:
    print("a and b both are equal")
else:
    # false part
    print("a is greater than b")
    print("This is result!")

if a == 10:
    print("a is equal to 10")
else:
    if a < 10:
        print("a is less than 10")
    else:
        print("a is greater than 10")

# Loops

'''
initialisation
while condition:
    statements
    incr/decr
'''

i = 0
while i < 10:
    print("Codekul - ",i)
    i += 1

'''
for item in collection:
    statements
'''
ods = 0
evns = 0

for n in (1,4,6,2,6,8,9):
    if n % 2 == 0:
        evns += n
    else:
        ods += n

print("Odd Sum:", ods)
print("Even Sum:", evns)