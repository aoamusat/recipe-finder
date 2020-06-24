from flask import request, flash, jsonify
from flask import make_response, render_template
from flask import session, redirect, url_for
import requests as Rq
from recipe import app

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title='Homepage')


@app.route('/recipe/search')
def searchRecipe():
    query = request.args.get('q')
    health = request.args.get('health')
    diet = request.args.get('diet')
    cuisineType = request.args.get('cuisineType')

    uri = f"""https://api.edamam.com/search?q={query}&app_id={app.config['RECIPE_APP_ID']}&app_key={app.config['RECIPE_APP_KEY']}"""
    
    response = Rq.get(uri)

    if response.status_code == 200:
        response = response.json()
        return render_template('search.html', recipes = response.get('hits'))
    else:
        return str(response.json())