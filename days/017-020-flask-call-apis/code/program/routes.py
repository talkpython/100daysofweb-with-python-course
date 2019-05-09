from datetime import datetime

import requests
from flask import render_template, request

from program import app

time_now = str(datetime.today())


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Template Demo', time=time_now)


@app.route('/100Days')
def p100days():
    return render_template('100Days.html')


@app.route('/chuck')
def chuck():
    joke = get_chuck_joke()
    return render_template('chuck.html',
                           joke=joke)


@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    pokemon = []
    if request.method == 'POST' and 'pokecolour' in request.form:
        colour = request.form.get('pokecolour')
        pokemon = get_poke_colours(colour)
    return render_template('pokemon.html',
                           pokemon=pokemon)


def get_chuck_joke():
    r = requests.get('https://api.chucknorris.io/jokes/random')
    data = r.json()
    return data['value']


def get_poke_colours(colour):
    r = requests.get('https://pokeapi.co/api/v2/pokemon-color/' + colour.lower())
    pokedata = r.json()
    pokemon = []

    for i in pokedata['pokemon_species']:
        pokemon.append(i['name'])

    return pokemon
