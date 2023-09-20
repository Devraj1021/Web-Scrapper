import requests 
from bs4 import BeautifulSoup

url = "https://www.dineout.co.in/mumbai-restaurants"

response = requests.get(url)

if (response.status_code == 200):
    print("Success")
else:
    print("Failure")

soup = BeautifulSoup(response.text, 'html.parser')

restaurants = soup.find_all('div', class_='restnt-main-wrap clearfix')

for restaurant in restaurants:
    print(restaurant.find(class_='restnt-name ellipsis').text)
    print(restaurant.find(class_='restnt-rating rating-4 hide').text)
    print()

