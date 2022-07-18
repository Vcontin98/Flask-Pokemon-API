from flask import redirect, render_template, redirect, url_for
from . import bp as app
from app.blueprints.main.models import Pokemon
from flask_login import login_required, current_user

@app.route("/")
#@login_required
def home():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    
    poki = Pokemon.query.filter(Pokemon.user_id==current_user.id).all()

    #poki = Pokemon.query.all()
    #poki = Pokemon.query.filter(current_user.id)
    poki.sort(key=lambda post: post.date_created, reverse=True)
    
    print(poki)
    
    
    context = {
        "poki": poki,
        "user": "Victr",
        "poki_type": "fire"

    }
    
    return render_template('index.html', **context)
    
@app.route("/login")
def login():
    return render_template('login.html')
    
@app.route("/register")
def register():
    return render_template('register.html')


# @app.route('/poki', methods=['GET','POST'])
# def explorer():
#     form = SearchForm()
#     if form.validate_on_submit():
#         return redirect(url_for('display', pokemon_name=form.pokemon_name.data))
    
#     if form.errors:
#         flash(f'You have to add a name before pressing this button.', category='danger') 
    #return render_template('explorer.html', title='Explorer',form=form)  
    
@app.route("/poki")
def poki():
    return render_template('poki.html')   

