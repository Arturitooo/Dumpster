#id_function

a = b = c = 1

print(a, id(a))
print(b, id(b))
print(c, id(c))

a = 2
print(a, id(a))
print(b, id(b))
print(c, id(c))

print()

aa = bb = cc = [1,2,3]

print(aa, id(aa))
print(bb, id(bb))
print(cc, id(cc))

aa.append(4)
print(aa, id(aa))
print(bb, id(bb))
print(cc, id(cc))