import googlemaps
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

#THIS FILE WAS ONLY USED TO CREATE THE GRAPHS FOR THE PROJECT. THE API IS NOT USED IN THIS FILE!

#Can change the file into a different date (can be implemented later)
data = pd.read_csv("Listings_2024-05-09.csv")
#Format price into an integer

data["Price"] = data["Price"].str.replace(",", "").str.replace("$", "").astype(int)

#Get rid of listings that have incorrect formatting (NaN)
data.dropna(subset=["Baths","Beds","Beds"], inplace = True)
#Get rid of duplicate listings
data.drop_duplicates(inplace = True)
#Get rid of anomlaies where price is over 20 mil
data = data[data['Price'] <= 8000000]

#Convert dataframe into numpy array format
df = pd.DataFrame(data)
df_array = df.values
prices = df_array[:,0].astype(int)
address = df_array[:,1]
beds = df_array[:,2].astype(int)
baths = df_array[:,3].astype(int)
types = df_array[:,4]
distances = np.empty(0,dtype=float)

# API KEY
gmaps = googlemaps.Client(key='enter your api key here')

# Define the addresses
for elem in address:
    # Get the geocode for the address
    geocode_result = gmaps.geocode(elem)

    # Get the latitude and longitude of the address
    latitude = geocode_result[0]['geometry']['location']['lat']
    longitude = geocode_result[0]['geometry']['location']['lng']

    # Calculate the distance from the address to downtown Toronto
    downtown_toronto_coordinates = (43.651070, -79.347015)
    distance = gmaps.distance_matrix((latitude, longitude), downtown_toronto_coordinates)['rows'][0]['elements'][0]['distance']['value'] / 1000
    distances = np.append(distances, distance)
    
price_vs_distance = {"Price" : prices, "Distance" : distances}
df = pd.DataFrame(price_vs_distance)

#convert df into csv file
df.to_csv("Price_vs_Distance_2024-05-09.csv", sep=',', index=False, encoding='utf-8')
#print(f"The distance from {address} to downtown Toronto (Nathan Phillips Square) is approximately {distance:.2f} km.")