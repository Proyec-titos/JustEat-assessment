import json
import requests 

#First let's initialize a list so we can add to it the items we want to filter out of the data in the API
RESTAURANT_LIST = []

#Then we're going to define the functions we'll use: Note that they are defined in the order that they will run,
#but they will be called in the reverse order.

#This first function is the one that constructs the list out of the pulled data:
def transform_data(data):
    restaurant_result = {}
    for restaurant in data.get("restaurants"):
        restaurant_result['name'] = restaurant.get('name', 'Unknown Restaurant Name')
        restaurant_result['cuisines'] = restaurant.get('cuisines', [])
        restaurant_result['address'] = restaurant.get('address', None)
        restaurant_result['rating'] = restaurant.get('rating').get('starRating', 0)
        RESTAURANT_LIST.append(restaurant_result)
        restaurant_result = {}  #this line "empties" the variable to use it again in the loop
    return RESTAURANT_LIST


#This function pulls the data from the API:
def pull_data(zip_code):
    global RESTAURANT_LIST
    if len(RESTAURANT_LIST) == 0:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get("https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{zip_code}".format(zip_code=zip_code), headers=headers)
        data = json.loads(response.text)
        transform_data(data)
        return RESTAURANT_LIST
    else:
        return RESTAURANT_LIST

#Finally, this function requests a zip code from the user and initiates the data pull passing the zip_code variable on to the pull_data function
#Once the nested functions have finished running, it also prints the final list:
def get_restaurants():
    zip_code = input("Please enter your zip code without spaces: ") #You can use this one: CT12EH
    restaurants = pull_data(zip_code)
    print(json.dumps(restaurants[0:9])) #You can change the items from the list that are displayed by manipulating the range of restaurants
    return json.dumps(restaurants)

#We only have to call the last function to perform the whole process:
get_restaurants()