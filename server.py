from flask_app import app
import flask_app.controllers.dojos
import flask_app.controllers.ninjas
# from env import KEY


if __name__ == "__main__":
    app.run(debug=True,port=5001)