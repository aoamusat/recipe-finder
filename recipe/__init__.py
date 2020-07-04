from flask import Flask
from flask import render_template, redirect, request


app = Flask(__name__)
app.secret_key = "60da6e77e33f95454322c0ed82713197"
app.config['RECIPE_APP_ID'] = "2bb75ced"
app.config['RECIPE_APP_KEY'] = "9b5e1a157c78c35aac8fa38d621f57e1"
app.config['RECIPE_API_URI'] = "https://api.edamam.com/search"

from recipe import routes