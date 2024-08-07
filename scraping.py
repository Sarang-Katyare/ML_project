import requests
from bs4 import BeautifulSoup
import pandas as pd

prices = []
address = []
suburb = []
house_type = []
no_of_rooms = []
no_of_baths = []
no_of_parking = []
area = []
date = []

# iterate through the webpages
for j in range(1, 50):
    url = "https://www.domain.com.au/sold-listings/toowoomba-city-qld-4350/?ptype=apartment-unit-flat,block-of-units,development-site,new-apartments,new-land,pent-house,studio,town-house,vacant-land&excludepricewithheld=1&landsize=50-any&landsizeunit=m2&page={}".format(j)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"}
    webpage = requests.get(url, headers=headers).text
    soup = BeautifulSoup(webpage, "html.parser")

    # finding all listings
    listings = soup.find_all("div", class_="css-qrqvvg")

    # extracting data from each listing
    for listing in listings:
        # finding prices
        price = listing.find("p", class_="css-mgq8yx").text.strip("$")
        prices.append(price.strip(" price from APM PriceFinder ") if "price" in price else price)

        # finding address
        # find address and suburb by data-testid attribute
        address_info = listing.find("h2", {"data-testid": "address-wrapper"})
        if address_info:
            address_span = address_info.find("span", {"data-testid": "address-line1"})
            suburb_span = address_info.find("span", {"data-testid": "address-line2"})
            if address_span:
                address.append(address_span.text.strip())
            else:
                address.append("")
            if suburb_span:
                suburb.append(suburb_span.text.strip())
            else:
                suburb.append("")
        else:
            address.append("")
            suburb.append("")

        # finding property features
        features = listing.find_all("span", class_="css-lvv8is")
        rooms = next((f.text.strip(" Beds") for f in features if "bed" in f.text.lower()), 0)
        baths = next((f.text.strip(" Baths") for f in features if "bath" in f.text.lower()), 0)
        parking = next((f.text.strip(" Parking") for f in features if "parking" in f.text.lower()), 0)
        area_val = next((f.text for f in features if "m²" in f.text), 0)

        no_of_rooms.append(rooms)
        no_of_baths.append(baths)
        no_of_parking.append(parking)
        area.append(area_val)

        # finding house type
        house_type_info = listing.find("div", class_="css-11n8uyu").find("span", class_="css-693528")
        house_type.append(house_type_info.text.strip())

    for i in soup.find_all("span", class_="css-1nj9ymt"):
        date.append(i.text[23:])

# Creating DataFrame
df = pd.DataFrame({
    'Price': prices,
    'Address': address,
    'Suburb': suburb,
    'House Type': house_type,
    'Number of Rooms': no_of_rooms,
    'Number of Baths': no_of_baths,
    'Number of Parking': no_of_parking,
    'Area': area,
    'Sold Date': date
})

print(df)
df.to_csv("scraped_toowoomba2.csv", index=False)
