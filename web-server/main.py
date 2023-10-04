from store import get_categories, get_random_categorie
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/') 
def index():
    return 'hola mundo platzi'

@app.get('/contact', response_class=HTMLResponse)
def contact():
    return """
        <h1>Hola soy un endpoint</h1>
        <p>soy un parrafo</p1>
"""


'''
def run():
    get_categories()
    get_random_categorie()

if __name__ == '__main__':
    run()
'''


