from flask import Flask, render_template, request, make_response
from update_news import *
from news_headlines import News_Headlines
from authentication import Auth
import os

app = Flask(__name__, template_folder='html_templates')

@app.route('/', methods = ['GET', 'POST'])
def index():
    while True:
        if request.cookies.get('token') != None:
            token = request.cookies.get('token')
            login = Auth()
            login = login.refresh_token(token)
            
            if login[0] == 200:
                # news = News_Headlines()
                # tech = news.tech_news()
                # business = news.business_news()
                # political = news.political_news()
                # US_CA = news.US_CA_news()
                # ME = news.ME_news()
                # EU = news.EU_news()
                # UK = news.UK_news()
                # Asia = news.Asia_news()
                # India = news.India_news()
                # world = news.world_news()
                page = make_response(render_template('headlines.html', political = political[0], political_link = political[1], tech = tech[0], tech_link = tech[1],
                                business = business[0], business_link = business[1], US_CA = US_CA[0], US_CA_link = US_CA[1], ME = ME[0],
                                ME_link = ME[1], EU = EU[0], EU_link = EU[1], UK = UK[0], UK_link = UK[1], Asia = Asia[0], Asia_link = Asia[1],
                                India = India[0], India_link = India[1], world = world[0], world_link = world[1]))
                page.set_cookie('token', token)
                return page
                
            elif login[0] == 400:
                return render_template('login_page.html', status = login[1], title = 'My Daily News - Login')
        
        elif request.method == 'GET':
            return render_template('login_page.html', status = '', title = 'My Daily News - Login')
            
        elif request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            login = Auth()
            login = login.login(email = email, password = password)
            token = login[1]
            
            if login[0] == 200 and request.form['remember'] == 'Yes':
                news = News_Headlines()
                tech = news.tech_news()
                business = news.business_news()
                political = news.political_news()
                US_CA = news.US_CA_news()
                ME = news.ME_news()
                EU = news.EU_news()
                UK = news.UK_news()
                Asia = news.Asia_news()
                India = news.India_news()
                world = news.world_news()
                page = make_response(render_template('headlines.html', political = political[0], political_link = political[1], tech = tech[0], tech_link = tech[1],
                                business = business[0], business_link = business[1], US_CA = US_CA[0], US_CA_link = US_CA[1], ME = ME[0],
                                ME_link = ME[1], EU = EU[0], EU_link = EU[1], UK = UK[0], UK_link = UK[1], Asia = Asia[0], Asia_link = Asia[1],
                                India = India[0], India_link = India[1], world = world[0], world_link = world[1]))
                page.set_cookie('token', token)
                return page
            
            elif login[0] == 400:
                return render_template('login_page.html', status = login[1], title = 'My Daily News - Login')
            
                            
            elif login[0] == 200:
                news = News_Headlines()
                tech = news.tech_news()
                business = news.business_news()
                political = news.political_news()
                US_CA = news.US_CA_news()
                ME = news.ME_news()
                EU = news.EU_news()
                UK = news.UK_news()
                Asia = news.Asia_news()
                India = news.India_news()
                world = news.world_news()
                return render_template('headlines.html', political = political[0], political_link = political[1], tech = tech[0], tech_link = tech[1],
                                business = business[0], business_link = business[1], US_CA = US_CA[0], US_CA_link = US_CA[1], ME = ME[0],
                                ME_link = ME[1], EU = EU[0], EU_link = EU[1], UK = UK[0], UK_link = UK[1], Asia = Asia[0], Asia_link = Asia[1],
                                India = India[0], India_link = India[1], world = world[0], world_link = world[1])
                                
            else:
                return render_template('login_page.html', status = 'UNKNOWN ERROR')
                
@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    while True:
        if request.method == 'GET':
            status = ''
            return render_template('sign-up_page.html', status = status)
        elif request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            sign_up = Auth()
            sign_up = sign_up.signup(email, password)
            if sign_up[0] == 400:
                status = sign_up[1]
                return render_template('sign-up_page.html', status = status)
            elif sign_up[0] == 200:
                status = 'Success!'
                return render_template('sign-up_page.html', status = status)

if __name__ == '__main__':
    app.run('0.0.0.0', port = int(os.getenv('PORT')))