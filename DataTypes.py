# 1) int 

i1 = 10
print(type(i1))
print(i1)
print("Value of i1:",i1)

i2 = 20
print("Value of i1: %d i2: %d" %(i1,i2))

print("Value of i1: {} i2: {}".format(i1, i2))

# 2) float

f1 = 10.34
print(type(f1))
print(f1)
print("Value of f1:",f1)

f2 = 20.40
print("Value of f1: %f f2: %f" %(f1,f2))

print("Value of f1: {} f2: {}".format(f1, f2))


# 3) str

s1 = "Codekul"
print(type(s1))
print(s1)
print("Value of s1:", s1)

s2 = 'The Gurukul for Coders!'
print("Value of s1: %s s2: %s" %(s1, s2))
print("Value of s1: {} s2: {}".format(s1, s2))


# 'Codekul'-"The Gurukul for Coders"!

s3 = """'Codekul'-"The Gurukul for Coders"!"""
print(s3)

# 4) bool

b1 = True
print(type(b1))
print(b1)
print("Value of b1:", b1)

b2 = False
print("Value of b1: %r b2: %r" %(b1, b2))
print("Value of b1: {} b2: {}".format(b1, b2))

res = b1 + b1
print(type(res))
print(res)