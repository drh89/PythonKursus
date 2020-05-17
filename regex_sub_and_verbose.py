import re

message = 'Agent Alice gave the secret documents to Agent Bob'

nameRegex = re.compile(r'Agent \w+')
mo = nameRegex.findall(message)
print(mo)
subMo = nameRegex.sub('REDACTED',message) #Substitutes all matches with 'REDACTED'
print(subMo)

nameRegex = re.compile(r'Agent (\w)\w*') #Agent followed by a letter char, followed by 0 or more letter chars
subMo = nameRegex.sub(r'Agent \1****', message) #Substitutes all matches with "Agent" + the first letter of the name, followed by four *
print(subMo)

#####VERBOSE#####

phoneRegex = re.compile(r'''
\d\d\d   #area code
-        #first dash
\d\d\d   #first 3 digits
-        #second dash
\d\d\d\d #last four digits

''', re.VERBOSE)
mo = phoneRegex.findall('445-123-1234')
print(mo)
