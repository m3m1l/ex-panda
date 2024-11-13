import json
import os
import re


abbrv_dict = {}
abbrv_filename = os.path.join(os.getcwd(), 'abbrv_list.txt')

with open(abbrv_filename, 'r') as abbr_file:
    for line in abbr_file:
        match = re.match(r"'([^']*)' '((?:[^'\\]|\\.)*)'", line.strip())
        if match:
            key = match.group(1)
            abbrv = match.group(2).replace("\\'", "'").replace("\\n", "\n")
            abbrv_dict[key] = abbrv


json_data = json.dumps(abbrv_dict, sort_keys=True, indent=2)
print(json_data)

with open("abbreviations.json", "w") as file:
    json.dump(abbrv_dict, file, indent=2, sort_keys=True)