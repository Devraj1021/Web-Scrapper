import requests 
from bs4 import BeautifulSoup
import csv

url = "https://www.mouthshut.com/Restaurants-ProID-169"

try:
    response = requests.get(url)

    # if (response.status_code == 200):
    #     print("Success")
    # else:
    #     print("Failure")

    soup = BeautifulSoup(response.text, 'html.parser')

    restaurants = soup.find_all('div', class_='listing-prod-card card')

    with open('restaurants.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Name', 'Rating'])

        for restaurant in restaurants:
            name = restaurant.find(class_='listing-prod-title text-truncate').text.strip()
            rating = restaurant.find('span', {'class':'rating-no'}).text.strip()
            writer.writerow([name, rating])


except requests.exceptions.HTTPError as e:
    print(e)
    print("Some error occurred")

