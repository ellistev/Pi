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
        if switchResult != '0' and float(object['Confidence'])/100 > 0.60 :
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
            "Confidence": 73.99286651611328,
            "Name": "Automobile"
        },
        {
            "Confidence": 73.99286651611328,
            "Name": "Car"
        },
        {
            "Confidence": 73.99286651611328,
            "Name": "Coupe"
        },
        {
            "Confidence": 73.99286651611328,
            "Name": "Sports Car"
        },
        {
            "Confidence": 73.99286651611328,
            "Name": "Vehicle"
        },
        {
            "Confidence": 73.6723861694336,
            "Name": "Suv"
        },
        {
            "Confidence": 67.18011474609375,
            "Name": "Sedan"
        },
        {
            "Confidence": 54.11397171020508,
            "Name": "Bumper"
        },
        {
            "Confidence": 52.00517272949219,
            "Name": "Engine"
        },
        {
            "Confidence": 52.00517272949219,
            "Name": "Machine"
        },
        {
            "Confidence": 52.00517272949219,
            "Name": "Motor"
        },
        {
            "Confidence": 51.60227966308594,
            "Name": "Caravan"
        },
        {
            "Confidence": 51.60227966308594,
            "Name": "Van"
        }
          ]
    print(GetCategory(labels))