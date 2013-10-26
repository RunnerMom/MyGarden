from flask import Flask, render_template, redirect, session, url_for
from app import app
import urlparse
import oauth2 as oauth
import os
from config import CONSUMER_KEY, CONSUMER_SECRET, api_key
AUTHORIZE_URL = "/uas/oauth2/authorization?response_type=code"
from model import user, buyers


# Linkedin site for more info: http://developer.linkedin.com/documents/common-issues-oauth-authentication

consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
client = oauth.Client(consumer)

#Upon accessing the index page, run a check to see if the user has already given authorization.
@app.route('/')
def index():
    return render_template('login.html', api_key=api_key)
 
#If the user needs to give authorization, request a request token and create a link to Linkedin.
@app.route('/oauth', methods=['POST'])
def request_oauth():
    request_token_url = 'https://api.linkedin.com/uas/oauth/requestToken'
    resp, content = client.request(request_token_url, "POST")
    if resp['status'] != '200':
        raise Exception("Invalid response %s." % resp['status'])
     
    request_token = dict(urlparse.parse_qsl(content))

    session['request_token'] = request_token['oauth_token']
    session['request_token_secret'] = request_token['oauth_token_secret']
    #Create a Linkedin link containing the request token.
    authorize_link = '%s?oauth_token=%s' % (AUTHORIZE_URL,request_token['oauth_token'])
    return render_template("request_oauth.html", auth=authorize_link)

#After the user has authorized, Linkedin will generate another token and redirect back to this route.
@app.route('/access')
def get_access():
    access_token_url = 'https://api.linkedin.com/uas/oauth/accessToken'

    token = oauth.Token(session['request_token'], session['request_token_secret'])
    token.set_verifier(oauth_verifier)
    client = oauth.Client(consumer, token)
     
    resp, content = client.request(access_token_url, "POST")
    access_token = dict(urlparse.parse_qsl(content))


    session['access_token'] = access_token['oauth_token']
    session['access_token_secret'] = access_token['oauth_token_secret']
    return redirect('/')

@app.route('/logout')
def logout():
    return redirect('/')

@app.route('/buyProduct')
def buy_product():
    return render_template('buy.html', user=user)

@app.route('/profile')
def profile():
    return render_template('base.html', user=user)




if __name__ == "__main__":
    app.config['STATIC_FOLDER'] = 'static'
    # Set environment variable in Heroku; if that key doesn't exist, it means
    # I'm running locally and can use debug=True
    if os.environ.has_key('debug_status'):
          app.run(debug = False)
    else:
          app.run(debug = True)