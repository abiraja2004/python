import string
alpha = set(string.ascii_lowercase)
i1 = 'abcdefghijklmnopqrstuvwxyz'
#print(alpha)
#print(set(input.lower()))
print(set(i1.lower()) >= alpha)
i2 = 'sdgfsdhjfgsandkhglaucabshgyu'
print(set(i2.lower()) >= alpha)

