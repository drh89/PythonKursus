import requests


#Saves the text in a response variable
res = requests.get('http://automatetheboringstuff.com/files/rj.txt')

try:
    res.raise_for_status()
except requests.exceptions.HTTPError:
    print('End destination does not exist')

playFile = open('RomeoAndJuliet.txt','wb')
for chunk in res.iter_content(100000):
          playFile.write(chunk)
