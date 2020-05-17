import re
lyrics = '12 drummers drumming, 11 pippers piping, 10 lords a leaping, 9 ladies dancing'

xmasRegex = re.compile(r'\d+\s\w+') # \d = digit, \s = whitspace, \w = word (any letter or number)
print(xmasRegex.findall(lyrics))


vowelRegex = re.compile(r'[aeiouyAEIOUY]') # r'(a|e|i|o|u|y)'
print(vowelRegex.findall('Robocop eats babyfood'))

vowelRegex = re.compile(r'[aeiouyAEIOUY]{2}') #finds matches with two vowels next to each other
print(vowelRegex.findall('Robocop eats babyfood'))


letterRegex = re.compile(r'[a-zA-Z]') #finds all letters from a-z and A-Z
print(letterRegex.findall('Robocop Eats Babyfood'))


consonantRegex = re.compile(r'[^aeiouyAEIOUY]') # ^ = opposite/not, will find all non-vowels
print(consonantRegex.findall('Robocop Eats Babyfood'))
