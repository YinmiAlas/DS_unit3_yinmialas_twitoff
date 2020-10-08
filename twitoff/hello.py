from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, WORLD!!!'

@app.route('/new_page')
def new_page():
    return 'This is another page!'

# HOW RUN WEBAPP ON MAC WE NEED THIS CODE IN THE TERMINAL:
# FLASK_APP=hello.py flask run


#if i add this is will run the code as:
# python hello.py
if __name__ == '__main__':
    app.run(debug=True)

