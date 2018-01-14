## HW 1
## SI 364 W18
## 1000 points
## Malcolm Maturen
## uniqname: malc

#################################

## List below here, in a comment/comments, the people you worked with on this assignment AND any resources you used to find code (50 point deduction for not doing so). If none, write "None".
# Get list of values from form checkboxes: https://stackoverflow.com/questions/34072525/getting-information-from-html-form-with-checkboxes-with-python-flask



## [PROBLEM 1] - 150 points
## Below is code for one of the simplest possible Flask applications. Edit the code so that once you run this application locally and go to the URL 'http://localhost:5000/class', you see a page that says "Welcome to SI 364!"

import requests
import json
from flask import Flask, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
app = Flask(__name__)
app.debug = True


class NumberForm(Form):
	num = TextField('num', validators=[validators.required()])


@app.route('/')
def hello_to_you():
    return 'Hello!'

@app.route('/class')
def welcome():
	return 'Welcome to SI 364!'


## [PROBLEM 2] - 250 points
## Edit the code chunk above again so that if you go to the URL 'http://localhost:5000/movie/<name-of-movie-here-one-word>' you see a big dictionary of data on the page. For example, if you go to the URL 'http://localhost:5000/movie/ratatouille', you should see something like the data shown in the included file sample_ratatouille_data.txt, which contains data about the animated movie Ratatouille. However, if you go to the url http://localhost:5000/movie/titanic, you should get different data, and if you go to the url 'http://localhost:5000/movie/dsagdsgskfsl' for example, you should see data on the page that looks like this:

# {
#  "resultCount":0,
#  "results": []
# }
@app.route('/movie/<movieName>')
def movieData(movieName):
	params = {'term': movieName, 'country': 'US', 'media': 'movie'}
	baseURL = 'https://itunes.apple.com/search'
	itunesRaw = requests.get(baseURL, params = params)
	return itunesRaw.text


## You should use the iTunes Search API to get that data.
## Docs for that API are here: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
## Of course, you'll also need the requests library and knowledge of how to make a request to a REST API for data.

## Run the app locally (repeatedly) and try these URLs out!

## [PROBLEM 3] - 250 points

## Edit the above Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question, you see a form that asks you to enter your favorite number.
## Once you enter a number and submit it to the form, you should then see a web page that says "Double your favorite number is <number>". For example, if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4". Careful about types in your Python code!
## You can assume a user will always enter a number only.

def doubleIn():
	s = """<!DOCTYPE html>
			<html>
			<body>
			<form action="/question" method="post">
				Favorite Number:<br>
				<input type="text" name="num" value="0">
				<br>
				<input type="submit" value="Submit">
			</form>
			</body>
			</html>"""
	return s


def doubleRes(res):
	s = """<!DOCTYPE html>
			<html>
			<body>
			<form action="/question" method="post">
				Favorite Number:<br>
				<input type="text" name="num" value={}>
				<br>
				<input type="submit" value="Submit">
			</form>
			<p>Double your favorite number is {}</p>
			</body>
			</html>""".format(res, res * 2)
	return s


@app.route('/question', methods = ['POST', 'GET'])
def numberForm():
	if request.method == 'POST':
		return doubleRes(float(request.form['num']))
	else:
		return doubleIn()
## [PROBLEM 4] - 350 points

## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, and build it into the above code for a Flask application, following a few requirements.

## You should create a form that appears at the route: http://localhost:5000/problem4form

## Submitting the form should result in your seeing the results of the form on the same page.

## What you do for this problem should:
# - not be an exact repeat of something you did in class
# - must include an HTML form with checkboxes and text entry
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the submission form and is readable by humans (more readable than e.g. the data you got in Problem 2 of this HW). The new data should be gathered via API request or BeautifulSoup.

# You should feel free to be creative and do something fun for you --
# And use this opportunity to make sure you understand these steps: if you think going slowly and carefully writing out steps for a simpler data transaction, like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; you do not need to handle errors or user confusion. (e.g. if your form asks for a name, you can assume a user will type a reasonable name; if your form asks for a number, you can assume a user will type a reasonable number; if your form asks the user to select a checkbox, you can assume they will do that.)

# Points will be assigned for each specification in the problem.

def blankForm():
	s = """<!DOCTYPE html>
			<html>
			<body>
			<h1> iTunes Price Finder </h1>
			<p>Finds the price of the most popular item on iTunes with the given search term and chosen fields.</p>
			<form action="/problem4form" method="post">
				iTunes Search Term:<br>
				<input type="text" name="term" value="">
				<br>
				Media Type(s)<br>
				<label><input type="checkbox" name="media" value="movie"> Movies</label><br>
				<label><input type="checkbox" name="media" value="music"> Music</label><br>
				<label><input type="checkbox" name="media" value="musicVideo"> Music Videos</label><br>
				<label><input type="checkbox" name="media" value="audiobook"> Audiobooks</label><br>
				<label><input type="checkbox" name="media" value="tvShow"> TV Shows</label><br>
				<label><input type="checkbox" name="media" value="ebook"> ebooks</label><br>
				<label><input type="checkbox" name="media" value="all"> All</label><br>
				<input type="submit" value="Submit">
			</form>
			</body>
			</html>"""
	return s

def priceForm(name, imgURL, price):
	s = """<!DOCTYPE html>
			<html>
			<body>
			<h1> iTunes Price Finder </h1>
			<p>Finds the price of the most popular item on iTunes with the given search term and chosen fields.</p>
			<form action="/problem4form" method="post">
				iTunes Search Term:<br>
				<input type="text" name="term" value="">
				<br>
				Media Type(s)<br>
				<label><input type="checkbox" name="media" value="movie"> Movies</label><br>
				<label><input type="checkbox" name="media" value="music"> Music</label><br>
				<label><input type="checkbox" name="media" value="musicVideo"> Music Videos</label><br>
				<label><input type="checkbox" name="media" value="audiobook"> Audiobooks</label><br>
				<label><input type="checkbox" name="media" value="tvShow"> TV Shows</label><br>
				<label><input type="checkbox" name="media" value="ebook"> ebooks</label><br>
				<label><input type="checkbox" name="media" value="all"> All</label><br>
				<input type="submit" value="Submit">
			</form>
			</body>
			<p>Top Result: {}</p>
			<p>Price: {}</p>
			<img src={}>
			</html>""".format(name, price, imgURL)
	return s

def cleanSearch(term):
	'''
	returns term in unicode-formatted string, aka '+' in place of ' '
	'''
	if len(term.split()) > 1:
		words = term.split()
		term = '+'.join(words)
	return term

def iTunesRequest(term, media):
	params = {'term': term, 'country': 'US', 'media': media, 'limit': 1}
	baseURL = 'https://itunes.apple.com/search'
	itunesRaw = requests.get(baseURL, params = params)
	return json.loads(itunesRaw.text)['results'][0]

def cleanData(data):
	book = {}
	if 'kind' in data and data['kind'] == 'ebook':
		book['trackName'] = data['trackName']
		book['artworkUrl100'] = data['artworkUrl100']
		book['trackPrice'] = data['formattedPrice']
		return book
	elif data['wrapperType'] == 'audiobook':
		book['trackName'] = data['collectionName']
		book['artworkUrl100'] = data['artworkUrl100']
		book['trackPrice'] = data['collectionPrice']
		return book
	return data

@app.route('/problem4form', methods = ['POST', 'GET'])
def prob4():
	if request.method == 'POST':
		term = cleanSearch(request.form['term'])
		medias = request.form.getlist('media')
		data = {}
		if len(medias) > 1:
			data = iTunesRequest(term, request.form.getlist('media'))
		else:
			data = iTunesRequest(term, request.form['media'])
		# writeF = open('cache.json', 'w')
		# writeF.write(json.dumps(data, indent=2))
		# writeF.close()
		data = cleanData(data)
		return priceForm(data['trackName'], data['artworkUrl100'], data['trackPrice'])
	else:
		return blankForm()


if __name__ == '__main__':
    app.run()


