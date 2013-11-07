from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required

### Start LoginHandler settings
#==============================

# lm = LoginManager()
# lm.init_app(app)
# lm.login_view = 'login'

# @lm.user_loader
# def load_user(id):
#     return session.query(User).get(id)

# @app.before_request
# def before_request():        
#         g.user = current_user


# @app.route('/login', methods=['GET','POST'])
# def login():
#         if current_user is not None:
#                 return redirect(url_for('profile'))
#         else:
#             form = LoginForm()
#             if form.validate_on_submit():

#                     user= session.query(User).\
#                               filter_by(email=form.email.data, password=form.password.data).\
#                               first()

            
#                     if user is not None:
#                             login_user(user)        
#                     else:
#                             flash("Invalid login")
                    
#                     return redirect('login')
                
        
#         return render_template('login.html')

# @app.route('/logout')
# def logout():
#         logout_user()
#         return redirect('/')

### End LoginHandler settings
#============================