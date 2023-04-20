import unittest
import json
import os
import sqlite3
import requests


def get_data_weather(city):
    api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
    response = requests.get(api_url, headers={'X-Api-Key': 'ClqOtbxYh1QnlxYsIcDbWQ==6wVFffdvVGFwF4OI'})
    
    data = json.loads(response.text)
    
    return data

def create_weather_table(cities, cur, conn):
    
    cur.execute("DROP TABLE IF EXISTS weather")
    cur.execute("CREATE TABLE IF NOT EXISTS weather (ID INTEGER PRIMARY KEY NOT NULL, wind_speed INTEGER, wind_degrees INTEGER, temperature INTEGER, humidity INTEGER, sunrise INTEGER, sunset INTEGER, cloud_pct INTEGER, feels_like INTEGER, max_temp INTEGER, min_temp INTEGER)")
    first = cur.fetchone()

    if (first == None):
        first = 0
    else:
        first = first[0] + 1

    for city in cities[first: first + 25]:
        weather_city_data = get_data_weather(city)
        print(weather_city_data)
    #     print(city)

    




def main():

    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/airports.db')
    cur = conn.cursor()

    cities = ['Detroit', 'Marseille', 'Barcelona', 'Lisbon', 'Leipzig', 'Antwerp', 'Beijing', 'Tokyo', 'Seoul', 'San Lorenzo', 'Perugia', 'Kilkenny', 'Coventry', 'Toronto', 'Warsaw', 'Stockholm', 'Perth', 'Hoorn', 'Copenhagen', 'Reykjavik', 'Dubai', 'Vienna', 'Wellington', 'Beirut', 'Nairobi', 'Lima', "Abuja", "Accra", "Addis Ababa", "Algiers", "Amman", "Ankara", "Ashgabat", "Asmara", "Astana", "Athens", "Baku", "Bamako", "Bandar Seri Begawan", "Bangui", "Banjul", "Bishkek", "Bissau", "Bogotá", "Monrovia", "Male", "Bridgetown", "Brussels", "Bucharest", "Buenos Aires", "Bujumbura", "Cairo", "Canberra", "Maracay", "Bexon", "Chisinau", "Colombo", "Conakry", "Maseru", "Dakar", "Damascus", "Dar es Salaam", "Dhaka", "Djibouti City", "Monaco", "Doha", "Dublin", "Dushanbe", "Freetown", "Funafuti", "Gaborone", "Georgetown", "Guatemala City", "Hanoi", "Harare", "Honiara", "Islamabad", "Jakarta", "Kabul", "Kampala", "Kathmandu", "Khartoum", "Kiev", "Kigali", "Kingston", "Kingstown", "Kinshasa", "Kuala Lummpur", "Kuwait City", "La Paz", "Libreville", "Lilognwe", "Pyongyang", "Lomé", "Mayen", "Longyearbyen", "Luanda", "Lusaka", "Luxembourg City", "Zagreb"]
    # print(len(cities))

    create_weather_table(cities, cur, conn)

main()





