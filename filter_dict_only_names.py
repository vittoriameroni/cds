import json

with open("NER_dictionnary_clean_only_hills.json", "r") as file:
    NER_dictionnary = json.load(file)

with open("data/hill_list.json", "r") as file:
    hill_list = json.load(file)

hill_list_translated = [item['english_name'] for key, item in hill_list.items()]
print(hill_list_translated)

NER_dictionnary_only_hill_names = dict()

for hill, entities in NER_dictionnary.items():
    new_entity_list = []
    new_entity_list.append(hill_list[hill]["english_name"])
    for entity in entities:
        if entity in hill_list_translated:
            new_entity_list.append(entity)
    NER_dictionnary_only_hill_names[hill] = list(set(new_entity_list))

with open("NER_dictionnary_only_hill_names.json", "w") as fp:
    json.dump(NER_dictionnary_only_hill_names , fp)