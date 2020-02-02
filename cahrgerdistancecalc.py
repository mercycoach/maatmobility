import json
import math

# Pick a point
# Sort list of 10 lats closest to point
# Get list of 

center_sm_lat= 37.40
center_sm_long= -122.17

with open('sub-chargepoints.json') as json_file:
    data = json.load(json_file)

    distList = []
    for i in range(20):
        for j in range(25):
            currDist = 100
            for p in data:
                lat = center_sm_lat+ 0.005 + i*0.01;
                lng = center_sm_long+0.005 + j*0.01;

                temp = (lat-p['Latitude'])**2 + (lng-p['Longitude'])**2
                dist = math.sqrt(temp)
                if (dist < currDist ):
                    currDist = dist
            distList.append(currDist)

print(max(distList))
print(min(distList))
with open('chargepoint-dist.json', 'w') as fp:
    json.dump(distList, fp)    


