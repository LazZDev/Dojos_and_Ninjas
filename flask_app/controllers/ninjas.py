from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja


@app.route('/ninjas')
def ninjas():
    # Retrieve all dojos using the get_all() method from the Dojo model
    dojos = dojo.Dojo.get_all()
    # Render the "ninja.html" template and pass the dojos data as "dojos"
    return render_template('ninja.html', dojos=dojos)


@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    # Save the ninja data received in the request form using the save() method from the Ninja model
    ninja.Ninja.save(request.form)
    # Redirect to the root URL after saving the ninja
    return redirect('/')
