supplies = ['pens', 'stablers', 'flame-throwers', 'binders']

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])



cat = ['fat', 'orange', 'loud']
_size = cat[0]
_color = cat[1]
_disposition = cat[2]

print(_size)
print(_color)
print(_disposition)



size, color, disposition = cat

print(size)
print(color)
print(disposition)


a = 'AAA'
b = 'BBB'

a,b = b,a

print(a,b)
