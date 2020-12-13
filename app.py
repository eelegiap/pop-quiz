from flask import Flask, render_template, request, redirect
import requests
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # opening the file (this is all done for you)
    with open('dictionary_alpha_arrays.json') as f:
        data = json.load(f)

    # if a get request (page load)
    if request.method == 'GET':
        # load the normal webpage (with nothing in the table)
        return render_template('index.html')

    # if a post request (submit button has been pressed)
    if request.method == 'POST':
        # get the user's letter input
        # TODO
        # return all the words in the dictionary that begin with that letter in the table
        # TODO
        # render the index.html template along with the needed variables
        return render_template('index.html')
