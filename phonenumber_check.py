#This program checks wether a string (arg) is an american phonenumber.

## def isPhoneNumber(text):
 ##   if len(text) != 12:
  ##      return False #not phone number sized
   ## for i in range(0,3):
    ##    if not text[i].isdecimal():
     ##       return False #No area code
   ## if text[3] != '-':
      ##  return False #missing dash
    ##for i in range(4,7):
     ##   if not text[i].isdecimal():
    #        return False #no first 3 digits
   # if text[7] != '-':
    #    return False #missing second dash
   # for i in range(8,12):
     #   if not text[i].isdecimal():
    #       return False #missing four last digits
   # return True


# message = 'Call me 445-123-1234, or at 445-222-4321 for my office line'

# foundNumber = False
# for i in range(len(message)):
   # chunk = message[i:i+12]
   # if isPhoneNumber(chunk):
    #    print('Phone number found: ' + chunk)
     #   foundNumber = True
#if not foundNumber:
  #  print('Could not find any phone numbers!')


#This code provides the same functionality as the code above:

import re
message = 'Call me 445-123-1234, or at 445-222-4321 for my office line'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
## mo = phoneNumRegex.search(message) #Finds first
mo = phoneNumRegex.findall(message)     #Finds all, makes a list
#print(mo.group()) #For finding first

print(mo)

