import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.worldometers.info/coronavirus/country/us/')

soup = BeautifulSoup(response.text, 'html.parser')

def clean(number):
    """
    Remove all commas and newlines
    """
    remove_characters = [',', '\n']
    for character in remove_characters:
        number = number.replace(character, '')
    return number

def get_stats():
    """
    Returns the COVID-19 stats from https://www.worldometers.info/coronavirus/country/us/
    """
    posts = soup.find_all(class_='maincounter-number')
    total_cases = posts[0].get_text().replace('\n', '')
    deaths = clean(posts[1].get_text())
    recovered = clean(posts[2].get_text())
    date = soup.select('.label-counter')[0].find_next_sibling().get_text()

    stats = {'total_cases': total_cases, 'deaths': deaths, 'recovered': recovered, 'date': date}
    return stats

