from flask import Flask, template_rendered


## Instance of flask class
app = Flask(__name__)
## debug=True ## here or below. need to remoce when production

## Create the route
@app.route('/')
def index():
	return 'INDEX'


if __name__ == '__main__':
	app.run(debug=True) ## Use to activate debug mode
	##app.run()  ## Use when producton mode