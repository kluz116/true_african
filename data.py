import json

#Load a Json data file
with open('data.json') as json_file:
    data = json.load(json_file)

#Method that returns a list of recipes
def getListRecipe():
    list_reciep = []
    for list_item in data:
        for key in list_item:
            if key == 'recipe':
                list_reciep.append(list_item[key])
    return list_reciep

#Method that returns a list of postcodes
def getListPostCodes():
    list_postcodes = []
    for list_item in data:
        for key in list_item:
            if key == 'postcode':
                list_postcodes.append(list_item[key])
    return list_postcodes