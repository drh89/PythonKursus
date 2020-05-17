spam = ['cat', 'bat', 'dog']

spam.append("Racoon")

print(spam)

spam.remove('cat')

print(spam)

del spam[0]

print(spam)

spam = [1,3,2,5,4,6,8,7]
print(spam)
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)


spam = ['A','Z','a','z']
spam.sort()
print(spam)
spam.sort(key=str.lower)
print(spam)
