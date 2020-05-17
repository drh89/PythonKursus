import re

batRegex = re.compile(r'Bat(man|mobile|girl|copter)') #Regular expression
mo = batRegex.search('Batmobile lost a wheel') #Searches string for matches in regex
print(mo.group())


batRegex = re.compile(r'Bat(wo)?man') #(wo)? = "wo" can be present 0 or 1 time
mo = batRegex.search('The adventures of Batwoman')
print(mo.group())


batRegex = re.compile(r'Bat(wo)*man') # (wo)* = "wo" can be present 0 or more times
mo = batRegex.search('The Adventures of Batwowoman')
print(mo.group())


batRegex = re.compile(r'Bat(wo)+man') # (wo)+ = "wo" must be present 1 or more times
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())


regex = re.compile(r'\+\*\?') # Backslash if you want to create a regex with the symbols
mo = regex.search('I learned about +*? regex syntax')
print(mo.group())


haRegex = re.compile(r'(Ha){3}') # regex is "Ha" 3 times({3})
mo = haRegex.search('He said "HaHaHa"')
print(mo.group())


haRegex = re.compile(r'(Ha){1,5}')
mo = haRegex.findall('He said "HaHaHa", she said "HaHa", but then he said "HaHaHaHaHa' +
                    'and finally she said "HaHaHaHaHaHa"')
print(mo)



