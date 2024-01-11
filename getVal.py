import requests
from bs4 import BeautifulSoup

# def scrape_random_addresses(country_code, quantity=2):
#     # url = f"https://www.bestrandoms.com/random-address-in-{country_code.lower()}?quantity={quantity}"
#     url = "https://www.bestrandoms.com/random-address-in-dk?quantity=6";
#     response = requests.get(url)
#     print(response);
#     if response.status_code != 200:
#         print("Failed to retrieve data")
#         return None

#     soup = BeautifulSoup(response.content, 'html.parser')
#     addresses = []



#     return addresses

# # Example usage
# country_code = "dk"  # Replace with the desired country code
# addresses = scrape_random_addresses(country_code)
# # for addr in addresses:
# #     print(addr)

# print(addresses)


cc_warehouse = {
    "al": "Albania",
    "dz": "Algeria",
    "ar": "Argentina",
    "am": "Armenia",
    "au": "Australia",
    "at": "Austria",
    "az": "Azerbaijan",
    "bs": "Bahamas",
    "bh": "Bahrain",
    "bd": "Bangladesh",
    "bb": "Barbados",
    "by": "Belarus",
    "be": "Belgium",
    "bol": "Bolivia",
    "bw": "Botswana",
    "br": "Brazil",
    "bn": "Brunei",
    "kh": "Cambodia",
    "cm": "Cameroun",
    "ca": "Canada",
    "ky": "Cayman Islands",
    "cl": "Chile",
    "cn": "China",
    "co": "Colombia",
    "cr": "Costa Rica",
    "hr": "Croatia",
    "cu": "Cuba",
    "cy": "Cyprus",
    "dk": "Denmark",
    "do": "Dominican Republic",
    "cd": "DR Congo",
    "ec": "Ecuador",
    "eg": "Egypt",
    "sv": "El Salvador",
    "ae": "Emirates",
    "ee": "Estonia",
    "et": "Ethiopia",
    "fj": "Fiji",
    "fi": "Finland",
    "fr": "France",
    "de": "Germany",
    "gh": "Ghana",
    "gt": "Guatemala",
    "hn": "Honduras",
    "hk": "Hong Kong",
    "hu": "Hungary",
    "in": "India",
    "id": "Indonesia",
    "ir": "Iran",
    "ie": "Ireland",
    "il": "Israel",
    "it": "Italy",
    "kt": "Ivory Coast",
    "jm": "Jamaica",
    "jp": "Japan",
    "jo": "Jordan",
    "kz": "Kazakhstan",
    "ke": "Kenya",
    "ko": "Korea",
    "kw": "Kuwait",
    "lv": "Latvia",
    "lb": "Lebanon",
    "ls": "Lesotho",
    "ly": "Libya",
    "lt": "Lithuania",
    "lu": "Luxembourg",
    "mg": "Madagascar",
    "mw": "Malawi",
    "my": "Malaysia",
    "ml": "Mali",
    "mt": "Malta",
    "mu": "Mauritius",
    "mx": "Mexico",
    "md": "Moldova",
    "ma": "Morocco",
    "mm": "Myanmar",
    "na": "Namibia",
    "np": "Nepal",
    "nl": "Netherlands",
    "nz": "New Zealand",
    "ni": "Nicaragua",
    "ng": "Nigeria",
    "no": "Norway",
    "om": "Oman",
    "pk": "Pakistan",
    "pa": "Panama",
    "pg": "Papua New Guinea",
    "py": "Paraguay",
    "pe": "Peru",
    "ph": "Philippines",
    "pl": "Poland",
    "pt": "Portuguese",
    "pr": "Puerto Rico",
    "qa": "Qatar",
    "ro": "Romania",
    "ru": "Russia",
    "rw": "Rwanda",
    "sa": "Saudi Arabia",
    "sn": "Senegal",
    "sg": "Singapore",
    "sk": "Slovakia",
    "si": "Slovenia",
    "za": "South Africa",
    "es": "Spain",
    "lk": "Sri Lanka",
    "sr": "Suriname",
    "se": "Sweden",
    "ch": "Switzerland",
    "tw": "Taiwan(China)",
    "tz": "Tanzania",
    "th": "Thailand",
    "cz": "The Czech Republic",
    "is": "The Republic of Iceland",
    "tt": "Trinidad and Tobago",
    "tn": "Tunisia",
    "tr": "Turkey",
    "ug": "Uganda",
    "ua": "Ukraine",
    "uk": "United Kingdom",
    "us": "United States",
    "uy": "Uruguay",
    "uz": "Uzbekistan",
    "ve": "Venezuela",
    "vn": "Vietnam",
    "ye": "Yemen",
    "zm": "Zambia",
    "zw": "Zimbabwe"
}




import http.client

warehouse = []
def getAddress(cc):
    conn = http.client.HTTPSConnection("www.bestrandoms.com")
    headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
    }
    payload = ""
    conn.request("GET", f"/random-address-in-{cc}?quantity=2", payload, headersList)
    response = conn.getresponse()
    result = response.read()
    # print(result.decode("utf-8"))

    soup = BeautifulSoup(result.decode("utf-8"), 'html.parser')


    addresses = []
    for li in soup.find_all("li", class_="col-sm-6"):
        address = {}
        for span in li.find_all("span"):
            text = span.get_text().strip()
            if ':' in text:
                key, value = text.split(':', 1)
                address[key.strip()] = value.strip()
        addresses.append(address)

    return {f"{cc}":addresses} 


ans = getAddress("dk")
# print(ans)

import time 
f = 0
for cc in cc_warehouse:
    f = f + 1
    ans = getAddress(cc)
    warehouse.append(ans)
    print(f," ",cc, "Completed")
   
    



import json

with open("warehouse.json", 'w') as file:
    json.dump(warehouse, file, indent=4)


