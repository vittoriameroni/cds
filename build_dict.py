import re
import spacy
import json
import Levenshtein

nlp = spacy.load('en_core_web_sm')

with open("data\\translated_text.txt", "r") as file:
    translated_file = file.read()

pattern = r"About\s+(.*?)\n([\s\S]*?)(?=About\s+|\Z)"
matches = re.findall(pattern, translated_file)

NER_dictionnary = dict()

for match in matches:
    text_hill = nlp(match[1])
    NER_dictionnary[match[0]] = []
    for ent in text_hill.ents:
        if ent.label_ not in ["CARDINAL", "DATE", "TIME", "QUANTITY","ORDINAL", "LAW"]:
            NER_dictionnary[match[0]].append(ent.text) 
            print(f"{ent.text}:{ent.label_}")
        
with open("NER_dictionnary.json", "w") as fp:
    json.dump(NER_dictionnary , fp)