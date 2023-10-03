import requests
import random

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json()
    print(type(categories))
    print(type(categories[0]))
    


def get_random_categorie():
    cat = str(random.choice([1,2,3]))
    r = requests.get('https://api.escuelajs.co/api/v1/categories'+'/'+cat)
    print(r.status_code)
    print(r.text)