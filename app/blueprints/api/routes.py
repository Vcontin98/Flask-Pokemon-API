from flask import jsonify, request, redirect, flash, url_for
from . import bp as app
from app.blueprints.main.models import Pokemon
from flask_login import current_user
from app import db


@app.route("/users")
def users():
    user_dict = {
        "Q": {
            "eyeColor": "blue",
            "hairColor": "brown"
        },
        "Vic": {
            "eyeColor": "gray",
            "hairColor": "black"
        },
        "kobe": {
            "eyeColor": "brown",
            "hairColor": "blonde"
        }
    }

    return jsonify(user_dict)



@app.route("/status-update", methods=["POST"])
def status_update():
    
    status_input = request.form['statusInput']
    type_input = request.form['typeInput']
    stat_input = request.form['statInput']
    user = current_user.id
    
    new_pokemon = Pokemon(poki_name=status_input, poki_type=type_input, description=stat_input, user_id=user)
    
    db.session.add(new_pokemon)
    db.session.commit()
    
    flash('New Pokemon added successfully', 'success')
    
    return redirect(url_for("main.home"))
    
    