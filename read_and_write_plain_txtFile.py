import os

##reading mode
helloFile = open(os.path.join(os.getcwd(),'hello.txt'))
print(helloFile.read())
# print(helloFile.readlines()) #returns list of lines
helloFile.close()

##write mode

helloFile = open(os.path.join(os.getcwd(),'hello2.txt'),'w')
helloFile.write('Hello!!!!\n')
helloFile.write('Hello!!!!\n')
helloFile.write('Hello!!!!\n')
helloFile.close()
##append mode

helloFile = open(os.path.join(os.getcwd(),'hello.txt'),'a')
helloFile.write('\n\nYeah buddy, enough out of you!')
helloFile.close()

 
