from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def main():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("new_dojo.html", all_dojos = dojos)


@app.route('/create/dojo', methods=["POST"])
def create_dojo():
    data = {
        "name": request.form['name']
    }
    Dojo.create(data)
    return redirect('/')

@app.route('/dojo/<int:id>')
def show(id):
    data = {
        "id":id
    }
    return render_template('show_dojos.html', dojo = Dojo.get_one_dojo_all_ninjas(data))
