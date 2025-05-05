import json

with open("NER_dictionnary.json", "r") as file:
    NER_dictionnary = json.load(file)

with open("data\hill_list.txt", "r") as file:
    data = file.read() 
    hill_list = data.split("\n") 

places_not_catched = 0
clean = 0
should_it_be_here = 0
good_potentially = 0
for place in hill_list:
    if place in NER_dictionnary.keys():
        clean += 1
    else:
        places_not_catched += 1
        print(place)

for place in NER_dictionnary.keys():
    if "?" == place[0]:
        should_it_be_here += 1
    if "?" == place[-1]:
        good_potentially += 1

print(f"places_not_catched: {places_not_catched}")
print(f"Clean: {clean}")
print(f"should_it_be_here: {should_it_be_here}")
print(f"good_potentially: {good_potentially}")