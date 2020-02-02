import json
import math

with open('chargepoint-dist.json') as json_file:
    dist_data = json.load(json_file)

with open('charger_need_score.json') as json_file:
    score_data = json.load(json_file)

final_data = []
for i, num in enumerate(dist_data):
    bob = {}
    bob['lat'] = score_data['lat'][str(i)]
    bob['long'] = score_data['long'][str(i)]
    bob['income'] = score_data['income'][str(i)]
    bob['charger_dist'] = num*53
    bob['charger_need_score'] = score_data['charger_need_score'][str(i)]
    final_data.append(bob)

with open('final_score_data.json', 'w') as fp:
    json.dump(final_data, fp)    



#print(type(dist_data))
lats = score_data['lat'] 
#print(lats['2'])
""" long
income
charger_dist
income_scaled
distance_scale
charger_need_score """