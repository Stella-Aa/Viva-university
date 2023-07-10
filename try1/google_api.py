import googlemaps
import pandas as pd
from os.path import exists
# time will be an important tool when we will be iterating through the API calls because if we do multiple requests in
# row with an extremely short break between in between page token might not be updated and we will receive the same
# results several times in a row. Hence, we use time to slow down the iteration

import time


# km to meters converter function (google maps api takes in meters, but its more convinient to provide km)

def km_to_meters(km):
    """
    The function transforms kilometers to meters

    km: number of kilometers you want as radius

    """

    try:
        return km * 1000
    except:
        return 0


# as an output of the api we will get a json file that stores the recieved coordinates. In order to convert them to tuples
# which will be later used to plot the points on a polygon we implement the following function

def convert_to_tuple(jsonfile):
    latitude = jsonfile['location']['lat']
    longitude = jsonfile['location']['lng']

    return latitude, longitude

# API key

API_KEY = 'AIzaSyAHxdTayKQ3b1GKVDlqbvT1FMZN1lUSFbs'

# activating and connecting to the API

map_client = googlemaps.Client(API_KEY)

# Parameters required for the API.search_nearby to run

# center of our search
location = (39.5183, 46.3378)

# defining the type of objects are we looking for
search_string = 'restaurant'

# radius to search in (centered at 'location')
distance = km_to_meters(2.828)

# list that will store the results of the requests made through the API

business_list = []

# running the API for the first time in order to get the "next_page_token" parameter. Without this step we will not be able
# to iterate through the API requests later because we need to provide the 'next_page_token'

response = map_client.places_nearby(location = location, keyword = search_string, radius = distance)
business_list.extend(response.get('results'))
next_page_token = response.get('next_page_token')

# iteration through the API requests in order to get all needed objects in a set area (the previuos cell is required
# for this to work)

while next_page_token:
    time.sleep(2)
    response = map_client.places_nearby(
        location=location,
        keyword=search_string,
        radius=distance,
        page_token=next_page_token)

    business_list.extend(response.get('results'))
    next_page_token = response.get('next_page_token')

# converting list to data frame as it becomes much more readible

df = pd.DataFrame(business_list)

# extracting coordinates of needed places

df['coordinates'] = df['geometry'].apply(convert_to_tuple)

# saving the results to excel


df.to_excel('data.xlsx')