from flask import Flask, render_template, redirect, session, url_for, g, flash
from app import app
import urlparse
import oauth2 as oauth
import os
from config import CONSUMER_KEY, CONSUMER_SECRET, api_key
AUTHORIZE_URL = "/uas/oauth2/authorization?response_type=code"
from model import user, User, buyers
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from forms import LoginForm


# Linkedin site for more info: http://developer.linkedin.com/documents/common-issues-oauth-authentication

### Start LoginHandler settings
#==============================

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

@lm.user_loader
def load_user(id):
    return session.query(User).get(id)

@app.before_request
def before_request():        
        g.user = current_user


from config import CONSUMER_KEY, CONSUMER_SECRET
from model import user, buyers
from forms import AddProduct

# Linkedin site for more info: http://developer.linkedin.com/documents/common-issues-oauth-authentication

consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
client = oauth.Client(consumer)


#Upon accessing the index page, run a check to see if the user has already given authorization.
@app.route('/')
def index():
    return render_template('login.html', api_key=api_key)


@app.route('/login', methods=['GET','POST'])
def login():
        if current_user is not None:
                return redirect(url_for('profile'))

        form = LoginForm()
        if form.validate_on_submit():

                user= session.query(User).\
                          filter_by(email=form.email.data, password=form.password.data).\
                          first()

        
                if user is not None:
                        login_user(user)        
                else:
                        flash("Invalid login")
                
                return redirect(request.args.get("next") or url_for('profile'))
                
        
        return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
        logout_user()
        return redirect('/')

### End LoginHandler settings
#============================

#===============================================
consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
client = oauth.Client(consumer)

#If the user needs to give authorization, request a request token and create a link to Linkedin.

@app.route('/oauth', methods=['POST'])
def request_oauth():
    request_token_url = 'https://api.linkedin.com/uas/oauth/requestToken'
    resp, content = client.request(request_token_url, "POST")
    if resp['status'] != '200':
        raise Exception("Invalid response %s." % resp['status'])

@app.route('/request_oauth')
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
    return redirect('/profile')

#     session['access_token'] = access_token['oauth_token']
#     session['access_token_secret'] = access_token['oauth_token_secret']
#     return redirect('/')


@app.route('/profile')
@login_required
def profile():
    return render_template('base.html', user=user)


@app.route('/buyProduct')
@login_required
def buy_product():
    return render_template('buy.html', user=user)

@app.route('/addProduct')
def add_product():
    form = AddProduct()
    if form.validate_on_submit():

        product = model.Product()
        product.category = form.category.data
        product.nametag = form.description.data
        product.quantity = form.quantity.data
        product.expiration = form.expiration.data
        product.unit = form.unit.data
        product.price = form.price.data
        product.image_url = form.image_url.data
        product.user_id = user.id

        model.session.add(product)
        model.session.commit()

        flash("Your product has been added to the market!")
        return render_template('add_product.html', form=form, user=user)

    return render_template('add_product.html', form=form, user=user)





if __name__ == "__main__":
    app.config['STATIC_FOLDER'] = 'static'
    # Set environment variable in Heroku; if that key doesn't exist, it means
    # I'm running locally and can use debug=True
    if os.environ.has_key('debug_status'):
          app.run(debug = False)
    else:
          app.run(debug = True)