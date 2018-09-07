import requests
from string import Template
from flask import Flask, render_template
import json


app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
	return render_template('index.html')

#@app.route('/<pokename>', methods=['GET'])
#def pokename_page(pokename):
 #   return(NAME_TEMPLATE.substitute(name=pokename, idnum='4'))

@app.route("/pokemon/<query>/") 
def getPokemon(query): 
	r = requests.get('http://pokeapi.co/api/v2/pokemon/' + query + '/', verify=False)
	pokemon = json.loads(r.text)
	if query.isdigit() : 
		return 'The pokemon with id ' + query + ' is ' + str(pokemon['name'])
	else:
		return query + ' has id ' + str(pokemon['id'])


if __name__ == '__main__':
   app.run(use_reloader=True, debug=True)
