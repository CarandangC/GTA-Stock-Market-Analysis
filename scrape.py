from selenium import webdriver
from bs4 import BeautifulSoup
import requests


prices = []
beds = []
baths = []
addresses = []
#if address starts with a #, it is an condo
estate_type = []
links = []

url = requests.get("https://www.remax.ca/on/toronto-real-estate?pageNumber=1").text

html_text = url

soup = BeautifulSoup(html_text, 'lxml')

listing = soup.find("div", class_ ="listing-card_root__RBrXm search-gallery_galleryCardRoot__dvXhP").text
price = soup.find("h2", class_ = "listing-card_price__lEBmo").text
bed_and_bath = soup.find("div", class_="property-details_detailsWrapper__6W1XU listing-card_propertyDetailsRoot__SC_jl").text
temp = bed_and_bath.split("bed")
bed = temp[0] + "bed"
bath = temp[1]
address = soup.find("div", class_="listing-address_root__g9lT5 listing-card_address__6GsHt").text
link = soup.find("a", class_ ="listing-card_listingCard__lc4CL")["href"]

#True == Condo, False == House
if address[0] == "#":
    address_type = True
else:
    address_type = False

print(listing + "\n")
print(price + "\n")
print(bed + "\n")
print(bath + "\n")
print(address + "\n")
print(link)
print(address_type)
