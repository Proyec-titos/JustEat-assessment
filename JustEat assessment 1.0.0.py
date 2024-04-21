#These are the libraries we'll use:
import requests      #this will allow us to obtain the data from the API
import json          #this will allow us to manage the data in json format

#We will first obtain the data from the API and code it as a variable to work with it:
unfiltered_list = requests.get("https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/CT12EH")

print(unfiltered_list) #This is just to check that the data is obtained correctly. DELETE IN FINAL VERSION

#Secondly, we will generate a second variable, which will be a list of dicts, 
#and add to it the filtered results with a function:

restaurants_filtered = []

def filter(data):
    filtered_restaurant = {}  #this obtains each restaurant and the relevant attributes as a dict:
    for restaurant in  unfiltered_list.get("restaurant"):
        filtered_restaurant["name"] = restaurant.get("name", "Unknown name")
        filtered_restaurant["cuisines"] = restaurant.get("cuisines", [])
        filtered_restaurant["address"] = restaurant.get("address",  "Unknown address")
        filtered_restaurant["rating"] = restaurant.get("rating").get(StarRating, 0)

        #this appends the dicts to the list
        restaurants_filtered = restaurants_filtered.append(filtered_restaurant)
        filtered_restaurant = {}

    return restaurants_filtered

#Now we print the list of the 10 first results 
print(restaurants_filtered[0:9])