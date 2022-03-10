from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/new/ninja')
def show_ninja():
    ninjas = Ninja.get_all()
    dojos = Dojo.get_all()
    print(ninjas)
    return render_template("new_ninja.html", all_ninjas = ninjas, all_dojos = dojos)


@app.route('/create/ninja', methods=["POST"])
def create_ninja():
    print(request.form)
    data = {
        "first_name": request.form['fname'],
        "last_name": request.form['lname'],
        "age": int(request.form['age']),
        "dojo_id": int(request.form['dojo_id'])
    }
    print(data)
    Ninja.create(data)
    return redirect('/')

@app.route('/dojo/<int:id>')
def dojo_name(id):
    data = {
        "id":id
    }
    return render_template('show_dojos.html', dojo = Dojo.get_one_dojo_all_ninjas(data))
