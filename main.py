from fastapi import FastAPI
from data import *



app = FastAPI()

@app.get('/unique_recipe_count')
def getUniqueRecipeCount():
    response = {'unique_recipe_count':len(set(getListRecipe()))}
    return response

    
@app.get('/count_per_recipe')
def getCountForRecipe():
    list_of_item = getListRecipe()
    recipe_dict = [{"Recipe":x,"Count":list_of_item.count(x)} for x in list_of_item]
    b = list({ item['Recipe'] : item for item in recipe_dict}.values())
    recipe_obj = {"count_per_recipe":b}
    return recipe_obj

@app.get('/busiest_postcode')
def getBusietPostCode():
    list_of_item = getListPostCodes()
    postcode_dict = [{"postcode":x,"delivery_count":list_of_item.count(x)} for x in list_of_item]
    b = list({ item['postcode'] : item for item in postcode_dict}.values())
    
    busiest_postcode = max(b, key=lambda x:x['delivery_count'])
    return {"busiest_postcode":busiest_postcode}

@app.get('/match_by_name/{recipe_name}')
def getListNamesFilter(recipe_name):
    list_recips = getListRecipe()
    x = [i for i in list_recips if recipe_name  in i ]
    return {"match_by_name":x}

