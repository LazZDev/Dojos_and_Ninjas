from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    # Redirect the root URL to the "/dojos" route
    return redirect('/dojos')


@app.route('/dojos')
def dojos():
    # Retrieve all dojos using the get_all() method from the Dojo model
    dojos = Dojo.get_all()
    # Render the "index.html" template and pass the dojos data as "all_dojos"
    return render_template("index.html", all_dojos=dojos)


@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    # Save the dojo data received in the request form using the save() method from the Dojo model
    Dojo.save(request.form)
    # Redirect to the "/dojos" route after saving the dojo
    return redirect('/dojos')


@app.route('/dojo/<int:id>')
def show_dojo(id):
    # Create a dictionary with the dojo ID
    data = {
        "id": id
    }
    # Retrieve the dojo and its associated ninjas using the get_one_with_ninjas() method from the Dojo model
    dojo = Dojo.get_one_with_ninjas(data)
    # Render the "dojo.html" template and pass the dojo data as "dojo"
    return render_template('dojo.html', dojo=dojo)
