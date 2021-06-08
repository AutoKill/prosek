import json
f = open('predmeti.json',)
data = json.load(f)
ocene = []
for i in data['predmeti']:
    print(i + ":")
    ocena = input()
    ocene.append(int(ocena))
f.close()
zbir = 0
for i in ocene:
    zbir += i

print("PROSEK:")
print(zbir / len(ocene))

input("Press enter to continue") 
