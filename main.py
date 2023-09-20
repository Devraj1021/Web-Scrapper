import requests 
from bs4 import BeautifulSoup

url = "https://www.dineout.co.in/mumbai-restaurants"

response = requests.get(url)

if (response.status_code == 200):
    print("Success")
else:
    print("Failure")

soup = BeautifulSoup(response.text, 'html.parser')

restaurants = soup.find_all('div', attrs={'class':'restnt-info cursor'})

for restaurant in restaurants:
    print(restaurant.find('a').text)
    # print(restaurant.find('p').text)
    # print(restaurant.find('span').text)
    print()
