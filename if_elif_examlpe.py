age = 3000
name = 'Bob'

if name == 'Alice':
    print('Hej Alice')
elif age < 12:
    print("You are not Alice, kiddo")
elif age > 2000:
    print("Unlike you, Alice is not an undead, immortal vampire") #It will execute this line
elif age > 100:
    print("You are not Alice granny") #It will not execute this line since the code block above it was executed


#elif statements execute the first true expression