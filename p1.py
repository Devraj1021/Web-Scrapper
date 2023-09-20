import requests 
from bs4 import BeautifulSoup

url = "https://www.mouthshut.com/Restaurants-ProID-169"

response = requests.get(url)

if (response.status_code == 200):
    print("Success")
else:
    print("Failure")

soup = BeautifulSoup(response.text, 'html.parser')

restaurants = soup.find_all('div', class_='listing-prod-card card')

for restaurant in restaurants:
    name = restaurant.find(class_='listing-prod-title text-truncate').text
    rating = restaurant.find('span', {'class':'rating-no'}).text
    print(name, rating)
    # print()

