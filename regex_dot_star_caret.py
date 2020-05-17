import re

beginsWithHelloRegex = re.compile(r'^Hello') # ^ String must start with "Hello"
print(beginsWithHelloRegex.search('Hello There!'))

endsWithWorldRegex = re.compile(r'world!$') # $ String must end with "world!"
print(endsWithWorldRegex.search('Hello world!'))


allDigitsRegex = re.compile(r'^\d+$') # ^ $   String must contain digits from start to end


atRegex = re.compile(r'.at') # . all words with a letter followed by "at"

print(atRegex.findall('The cat in the hat live in a flat and took a chat'))


nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') #Groups what is after first and last name into tupel
print(nameRegex.findall('First Name: Dennis Last Name: Hansen'))


serve = '<To serve humans> for dinner>'

nongreedy = re.compile(r'<(.*?)>') #non greedy - will only take what is inside the anglebrackets
print(nongreedy.findall(serve))


greedy = re.compile(r'<(.*)>') # greedy - takes everything after the first anglebracket
print(greedy.findall(serve))

vowelRegex = re.compile(r'[aeiouy]', re.IGNORECASE) #ignores case sensitivity
mo = vowelRegex.findall('Al, why does your programs not work')
print(mo)


