# Check if state code match the jakim zones code. This is to eliminate some possible errors after adding jakim zones to 
# the JSON database.

# open the malaysia.district-jakim.geojson file
import json


with open('malaysia.district-jakim.geojson') as f:
    data = json.load(f)

    for feature in data['features']:
        properties = feature['properties']
        state = properties['state']
        try:
            jakim_code = properties['jakim_code']
        except KeyError:
            print(state, 'has no jakim_code. Skipping...')
            continue

        print(f'Checking {jakim_code} {state}', end=" ")
        
        # KDH04 becomes KDH
        initial_jakim_zone = jakim_code[0:3]

        # check if jakim_code matches state code for some states that are
        # different state code (ie jakim code is not the same as state code)
        if state == 'NSN':
            if initial_jakim_zone != 'NGS':
                print('Error: jakim_code does not match state code for', state, jakim_code)
                break
        elif state == 'LBN':
            if initial_jakim_zone != 'WLY':
                print('Error: jakim_code does not match state code for', state, jakim_code)
                break
        elif state == 'PJY':
            if initial_jakim_zone != 'WLY':
                print('Error: jakim_code does not match state code for', state, jakim_code)
                break
        elif state == 'KUL':
            if initial_jakim_zone != 'WLY':
                print('Error: jakim_code does not match state code for', state, jakim_code)
                break
        else:
            if jakim_code[0:3] != state:
                print('Error: jakim_code does not match state code for', state, jakim_code)
                break

        print('OK ✅')


