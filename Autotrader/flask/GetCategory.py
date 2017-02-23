import json

def SwitchCategory(x):
    if x == 'Car':
        return 'Car'
    if x == 'Atv':
        return 'ATV'
    if x == 'Rv':
        return 'RV'
    if x == 'Suv':
        return 'SUV'
    if x == 'Boat':
        return 'Boat'
    if x == 'Yacht':
        return 'Yacht'
    if x == 'Jet Ski':
        return 'Watercraft'
    if x == 'Watercraft':
        return 'Watercraft'
    if x == 'Trailer Truck':
        return 'Heavy Truck'
    if x == 'Motorcycle':
        return 'Motorcycle'
    if x == 'Pickup Truck':
        return 'Truck'
    if x == 'Tractor':
        return 'Tractor'
    return '0'

def GetCategory(labels):
    #json_object = json.load(labels)
    result = {"Category": "0", "Confidence": float('1.0') / 100}
    for object in labels:
        switchResult = SwitchCategory(object['Name'])
        if switchResult != '0' and float(object['Confidence'])/100 > 0.75 :
            result = {"Category": SwitchCategory(object['Name']), "Confidence": float(object['Confidence']) / 100}
            break;

        #return { "Category" : SwitchCategory(object['Name']), "Confidence" : float(object['Confidence'])/100}
        #print(object['Name'])
        #print(object['Confidence'])
    if result['Category'] != '0':
        return result
    return { "Category" : "Not Sure", "Confidence" : float('1.0')}


if __name__ == '__main__':
    labels= [
            {
              "Confidence": 75.41276550292969,
              "Name": "Automobile"
            },
            {
              "Confidence": 75.41276550292969,
              "Name": "Car"
            },
            {
              "Confidence": 75.41276550292969,
              "Name": "Vehicle"
            },
            {
              "Confidence": 75.28437805175781,
              "Name": "Caravan"
            },
            {
              "Confidence": 75.28437805175781,
              "Name": "Van"
            },
            {
              "Confidence": 68.32386016845703,
              "Name": "Coupe"
            },
            {
              "Confidence": 68.32386016845703,
              "Name": "Sports Car"
            },
            {
              "Confidence": 66.4803466796875,
              "Name": "far"
            },
            {
              "Confidence": 57.00609588623047,
              "Name": "Sedan"
            },
            {
              "Confidence": 51.035552978515625,
              "Name": "Antique Car"
            }
          ]
    print(GetCategory(labels))