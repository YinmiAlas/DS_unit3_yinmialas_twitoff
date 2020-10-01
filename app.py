from flask import Flask 
from .db_model import DB, User

def create_app():
    '''Create and configure an instance of our Flask aplication'''
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/yinmialas/Desktop/DS_unit3_yinmialas_twitoff/twitoff.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app) # connect Flask app 
# for mac is  4 slash //// mean full path

    @app.route('/')
    def root():
        return 'Welcome to Twitoff'
    
    @app.route('/<username>/<followers>')
    def add_user(username, followers):
        user = User(username=username, followers=followers)
        DB.session.add(user)
        DB.session.commit()

        return f'{username} has been added to the DB!'

    return app


# to create the sqlite db we need to run this code
# in flask shell but dont forget to have pipenv shell first
# code : from DS_unit3_yinmialas_twitoff.db_model import DB, User, Tweet
# plus DB.create_all()