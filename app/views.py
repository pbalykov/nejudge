from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User

@app.route('/')
def entrance():
    return render_template("entrance.html")

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('entrance'), code=303)

@app.route('/registration', methods = ['GET', 'POST'])
def registration():
    if request.method == "GET":
        return render_template('registration.html')

    name = request.form['name']
    login = request.form['login']
    password = request.form['password']
        
    new_user = User.add_user(name, login, password, password)
    if ( not(new_user) ) :
        return "No"
    db.session.add(new_user)
    db.session.commit()

    print(request.form) 
    return "YES"


