
import shelve

shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Young-gun', 'Devilspawn', 'Rafiqi', 'Cleo']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])

print(list(shelfFile.keys()))
print(list(shelfFile.values()))

shelfFile.close()
