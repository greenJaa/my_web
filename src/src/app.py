from flask import Flask



app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world'

@app.route('/<name>')
def hello(name):
    return f'Hello {name}'

#@app.route ('/check_file/<filename>')

#def check_file(file_name)
#    try:
#        with open(file_name) FILE
#            data=FILE
#    except print(0):
#        pass


app.run(host='0.0.0.0',port=5000,debug=True)