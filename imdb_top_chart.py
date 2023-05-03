from bs4 import BeautifulSoup
import requests
import csv
import os
import dotenv
from itertools import chain
import numpy as np

dotenv.load_dotenv()
API_KEY = os.environ["API_KEY"]
movie_url = "https://api.themoviedb.org/3/"
image_root = "https://www.themoviedb.org/t/p/w600_and_h900_bestv2"

LINK = "https://www.imdb.com/chart/top/"
CLASS_ = 'titleColumn'
response = requests.get(LINK)

site_text = response.text

soup = BeautifulSoup(site_text, 'html.parser')
tds = soup.find_all('td', class_=CLASS_)

titles = [td.find('a').text.replace("'", "`") for td in tds]
casts = [td.find('a').get('title').split(',') for td in tds]
years = [int(td.find('span').text.replace('(', '').replace(')', '')) for td in tds]

# ------------------------ RETRIEVE MORE MOVIE DATA ----------------------------
descriptions = []
imgs = []
for title in titles:
    params = {
        "api_key": API_KEY,
        "query": title
    }
    response = requests.get(url=f"{movie_url}search/movie", params=params)
    movies_results = response.json()['results'][0]
    descriptions.append(movies_results['overview'].replace("'", "`").replace('\u0142', 'l'))
    imgs.append(f'{image_root}{movies_results["poster_path"]}')

movies = [[titles[i], years[i], descriptions[i], imgs[i]] for i in range(len(titles))]
print(len(movies))
movie_fields = ["Title", "Year", "Description", "Img"]

with open("movie_data.csv", 'w', newline='') as file:
    csvwriter = csv.writer(file, delimiter=";")
    csvwriter.writerow(movie_fields)
    csvwriter.writerows(movies)

casts = [person.strip() for person in list(chain(*casts))]

movie_id = []
roles = []

for i in range(len(casts)):
    if "(dir.)" in casts[i]:
        casts[i] = casts[i].replace(" (dir.)", "")
        role = "Director"
    else:
        role = "Actor"
    roles.append(role)
    movie_id.append(1 + i // 3)


celebs = list(np.unique(np.array(casts)))
print(len(celebs))
celeb_id = [celebs.index(person) + 1 for person in casts]

cast = [[roles[i], movie_id[i], celeb_id[i]] for i in range(len(casts))]

cast_fields = ['Role', 'movie_id', 'artist_id']
print(len(cast))
with open("cast_data.csv", "w", newline='') as file:
    csvwriter = csv.writer(file, delimiter=";")
    csvwriter.writerow(cast_fields)
    csvwriter.writerows(cast)

celeb_fields = ["First Name", "Last Name"]

f_names = [celeb.split(' ')[0] for celeb in celebs]
l_names = [celeb.split(' ')[-1] for celeb in celebs]
celeb_imgs = []

# for celeb in celebs:
#     params = {
#         "api_key": API_KEY,
#         "query": celeb
#     }
#     response = requests.get(url=f"{movie_url}search/person", params=params)
#     if response.json()['total_results'] > 0:
#         celeb_results = response.json()['results'][0]
#         celeb_imgs.append(f"{image_root}{celeb_results['profile_path']}")
#     else:
#         celeb_imgs.append('NA')

artists = [[f_names[i], l_names[i]] for i in range(len(f_names))]

with open("artists_data.csv", "w", newline='') as file:
    csvwriter = csv.writer(file, delimiter=";")
    csvwriter.writerow(celeb_fields)
    csvwriter.writerows(artists)

# TODO: Add celeb image
# TODO: Create DB, input data into tables
# TODO: Create flask site
