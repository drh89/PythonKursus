
#1
# spam = 0

# while spam < 5:
#     print("Hello World!")
#     spam = spam +1

#2
# name = ''

# while name != 'your name':
#     print('please type your name')
#     name = input()
# print('Thank you!')

#3

# name = ''

# while True:
#     print('please type your name')
#     name = input()
#     if name == 'your name':
#         break                               #when break is executed, it jumps out of the while loop
# print('Thank you!')


#4
spam = 0
while spam < 5:
    spam = spam +1
    if spam == 3:
        continue                #When continue is executed, it returns to beginning of the while loop and evaluates the expression again
    print("Spam is " + str(spam))