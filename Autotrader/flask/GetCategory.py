import json

def SwitchCategory(x):
    if x == 'Car':
        return 'Car'
    if x == 'Truck':
        return 'Truck'
    if x == 'Boat':
        return 'Boat'
    if x == 'Tractor':
        return 'Tractor'
    if x == 'Semi':
        return 'Heavy'
    return '0'

def GetCategory(labels):
    #json_object = json.load(labels)
    for object in labels:
        if SwitchCategory(object['Name']) != '0' and float(object['Confidence'])/100 > 0.75 :
            return { "Category" : SwitchCategory(object['Name']), "Confidence" : float(object['Confidence'])/100}
        #print(object['Name'])
        #print(object['Confidence'])

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
              "Name": "Suv"
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