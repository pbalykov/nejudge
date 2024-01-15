from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db
from app.models import User

@app.route('/')
def home_page():
    if current_user.is_authenticated: 
        items = [{"url": "/page1", "name": "Ссылка 1"},
             {"url": "/page2", "name": "Ссылка 2"}
            ]
        return render_template('menu.html', items=items)

    return render_template("entrance.html")


@app.route('/entrance', methods=['POST'])
def entrance():
    login = request.form['login']
    password = request.form['password']
    user = User.get_user(login, password) 
    if ( user ) :
        login_user(user)
        return "YES entrance"
    return "No entrance"

@app.route('/logout', methods=["POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home_page'))


@app.errorhandler(404)
def page_not_found(e):
    if ( current_user.is_authenticated ) :
        return "Error 404"
    return redirect(url_for('home_page'), code=303)

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


