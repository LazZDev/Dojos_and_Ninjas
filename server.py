from flask_app import app
from flask_app.controllers import dojos, ninjas

# This is the main entry point of the Flask application
if __name__ == "__main__":
    # Run the application in debug mode
    app.run(debug=True)
