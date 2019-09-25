import json
with open('jsonfile.json', 'r') as f:
    datastore = json.load(f)
print(datastore)
# with open('jsonfile.json', 'a') as f1:
#     datastore=json.load(f1)
#     json.dump(datastore, f1)