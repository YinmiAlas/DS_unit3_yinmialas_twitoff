'''Populate TwitOff with users'''
import requests

URL = 'https://unit3-twitoff-yinmi.herokuapp.com/'
​
USERNAMES = [
    'BarackObama','justinbieber','katyperry','rihanna','taylorswift13',
    'Cristiano','ladygaga','TheEllenShow','realDonaldTrump','YouTube'
]
​
def populate_twitoff(url, usernames):
'''POST to url for each name in usernames'''
    with requests.Session() as session:
        for username in usernames:
            print(username)
            r = session.post(url, data={'user_name': username})
​
if __name__ == '__main__':

populate_twitoff(URL, USERNAMES)
