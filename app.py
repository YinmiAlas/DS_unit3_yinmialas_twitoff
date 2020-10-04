from flask import Flask, render_template, request
from .db_model import DB, User
from .twitter import add_user_tweepy

def create_app():
    '''Create and configure an instance of our Flask aplication'''
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/yinmialas/Desktop/DS_unit3_yinmialas_twitoff/twitoff.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app) # connect Flask app 
# for mac is  4 slash //// mean full path

    @app.route('/')
    def root():
        return render_template('base.html', title='Home', users=User.query.all())
    
    @app.route('/user', methods=['POST'])
    @app.route('/user/<name>', methods=['GET'])
    def add_or_update_user(name=None, message=''):
        name = name or request.values['user_name']

        try:
            if request.method == 'POST':
                add_user_tweepy(name)
                message= 'User {} succesfully added!'.format(name)
            tweets = User.query.filter(User.username == name).one().tweet 
        except Exception as e:
            print(f'Error adding {name}: {e}'.format(name, e))
            tweets = []

        return render_template('user.html', title=name, message=message)


    return app



    


# to create the sqlite db we need to run this code
# in flask shell but dont forget to have pipenv shell first
# code : from DS_unit3_yinmialas_twitoff.db_model import DB, User, Tweet
# plus DB.create_all()