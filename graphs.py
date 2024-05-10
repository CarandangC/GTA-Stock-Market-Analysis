import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

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

#Convert datafram into numpy array format
df = pd.DataFrame(data)
df_array = df.values
prices = df_array[:,0].astype(int)
address = df_array[:,1]
beds = df_array[:,2].astype(int)
baths = df_array[:,3].astype(int)
types = df_array[:,4]


# Creating a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Price vs. Beds
axes[0, 0].scatter(beds,prices)
axes[0, 0].set_xlabel("# of Beds")
axes[0, 0].set_ylabel("Price")
axes[0, 0].set_title("Prices vs. Beds")
# Fit the trend line
z = np.polyfit(beds, prices, 1) 
p = np.poly1d(z)
axes[0, 0].plot(beds, p(beds), "r", label="Trend line") 
axes[0, 0].legend()  

# Price vs. Baths
axes[0, 1].scatter(baths, prices)
axes[0, 1].set_xlabel("# of Baths")
axes[0, 1].set_ylabel("Price")
axes[0, 1].set_title("Prices vs. Baths")
# Fit the trend line
z = np.polyfit(baths, prices, 1) 
p = np.poly1d(z)
axes[0, 1].plot(baths, p(baths), "r", label="Trend line") 
axes[0, 1].legend()

# Price vs. Baths + Bath
bed_bath = np.empty(0,dtype=int)
for i in range(len(prices)):
    bed_bath = np.append(bed_bath, (beds[i]+baths[i]))
axes[1, 0].scatter(bed_bath, prices)
axes[1, 0].set_xlabel("# of Beds + Baths")
axes[1, 0].set_ylabel("Price")
axes[1, 0].set_title("Price vs. # of Beds + Baths")
# Fit the trend line
z = np.polyfit(bed_bath, prices, 1) 
p = np.poly1d(z)
axes[1, 0].plot(bed_bath, p(bed_bath), "r", label="Trend line") 
axes[1, 0].legend()


# Custom formatter for y-axis to display values in millions
formatter = FuncFormatter(lambda x, pos: '{:.0f}M'.format(x * 1e-6))
for ax in axes.flat:
    ax.yaxis.set_major_formatter(formatter)
    
# Optional: Remove the empty subplot
fig.delaxes(axes[1, 1])

# Adjust layout
plt.tight_layout()

print(prices)
plt.show()

