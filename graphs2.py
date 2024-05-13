import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
#Plotting the graph

#Can change the file into a different date (can be implemented later)
data = pd.read_csv("price_vs_distance_2024-05-09.csv")

#Convert dataframe into numpy array format
df = pd.DataFrame(data)
df_array = df.values
prices = df_array[:,0].astype(int)
distances = df_array[:,1].astype(float)
beds = df_array[:,2].astype(int)
baths = df_array[:,3].astype(int)
types = df_array[:,4]
address = df_array[:,5]

beds_2 = np.array([])
price_bed_2 = np.array([])
baths_bed_2 = np.array([])
address_bed_2 = np.array([])
#Create a list of prices for 2 bedroom listings
for elem in df_array:
    if elem[2] == 2:
        beds_2 = np.append(beds_2, elem[1])
        price_bed_2 = np.append(price_bed_2, elem[0])
        baths_bed_2 = np.append(baths_bed_2, elem[3])
        address_bed_2 = np.append(address_bed_2, elem[5])

fig, ax = plt.subplots()
#Plot the data
ax.scatter(beds_2,price_bed_2)
ax.set_xlabel("Distance from Toronto (km) where # of Beds = 2")
ax.set_ylabel("Price")
ax.set_title("Prices vs. Distance from Toronto where # of Beds = 2")
# Fit the trend line
z = np.polyfit(beds_2, price_bed_2, 1) 
p = np.poly1d(z)
plt.plot(beds_2, p(beds_2), "r", label="Trend line") 
plt.legend() 

# Custom formatter for y-axis to display values in millions
formatter = FuncFormatter(lambda x, pos: '{:.0f}M'.format(x * 1e-6))
ax.yaxis.set_major_formatter(formatter)
    
plt.show()