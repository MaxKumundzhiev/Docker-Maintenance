import random
import requests
from bs4 import BeautifulSoup

# crawl IMDB Top 250 and randomly select a movie

URL = 'http://www.imdb.com/chart/top'

def run():
    def get_year(movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1] 
        return year

    response = requests.get(URL).text
    soup = BeautifulSoup(response, 'html.parser')

    movie_tags = soup.select('td.titleColumn')
    inner_movie_tags = soup.select('td.titleColumn a')
    rating_tags = soup.select('td.posterColumn span[name=ir]')

    years = [get_year(tag) for tag in movie_tags]
    actors_list =[tag['title'] for tag in inner_movie_tags]
    titles = [tag.text for tag in inner_movie_tags]
    ratings = [float(tag['data-value']) for tag in rating_tags] 

    n_movies = len(titles)

    while True:
        idx = random.randrange(0, n_movies)
        
        print(f'{titles[idx]} {years[idx]}, Rating: {ratings[idx]:.1f}, Starring: {actors_list[idx]}')

        user_input = input('Do you want another movie (y/[n])? ')
        if user_input.lower() != 'y':
            break
    

if __name__ == '__main__':
    run()