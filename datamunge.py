import json

outList = []
with open('chargepoints.json') as json_file:
    data = json.load(json_file)
    for p in data:
        cp = {}
        cp['Id'] = p['ID']
        cp['Title'] = p['AddressInfo']['Title']
        cp['Latitude'] = p['AddressInfo']['Latitude']
        cp['Longitude'] = p['AddressInfo']['Longitude']
        cp['Postcode'] = p['AddressInfo']['Postcode']
        outList.append(cp)

#for p in outList:
    #print(p['Title'])
print(len(outList))

with open('sub-chargepoints.json', 'w') as fp:
    json.dump(outList, fp)    