from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import date



prices = []
beds = []
baths = []
addresses = []
#if address starts with a #, it is an condo
estate_type = []
links = []



for page_num in range(1,6):
    url = (f"https://www.remax.ca/on/toronto-real-estate?pageNumber={page_num}")
    html_text = requests.get(url).text
    

    soup = BeautifulSoup(html_text, 'lxml')

    listing = soup.find_all("div", class_ ="listing-card_root__RBrXm search-gallery_galleryCardRoot__dvXhP")
    for view in listing:
        
        price = view.find("h2", class_ = "listing-card_price__lEBmo").text
        bed_and_bath = view.find("div", class_="property-details_detailsWrapper__6W1XU listing-card_propertyDetailsRoot__SC_jl").text
        temp = bed_and_bath.split(" bed")
        bed = temp[0]
        bath = temp[1].replace(" bath", "").strip()
        address = view.find("div", class_="listing-address_root__g9lT5 listing-card_address__6GsHt").text
        link = view.find("a", class_ ="listing-card_listingCard__lc4CL")["href"]

        #True == Condo, False == House
        if address[0] == "#":
            address_type = True
        else:
            address_type = False

        prices.append(price)
        beds.append(bed)
        baths.append(bath) 
        addresses.append(address) 
        links.append(link)
        estate_type.append(address_type)
        
#Exporting data into a csv using pandas

data = {"Price" : prices, "Address" : addresses, "Beds" : beds, "Baths" : baths, "Type" : estate_type, "Link" : links}
df = pd.DataFrame(data)
df["Type"] = df["Type"].replace({True: "Condo", False: "House"})


#convert data into csv file
df.to_csv(f"Listings_{date.today()}.csv", sep=',', index=False, encoding='utf-8')
