from flask import Flask
from routes.userRoutes import user_api
from routes.contactRoutes import contact_api

app = Flask(__name__)

app.register_blueprint(user_api)
app.register_blueprint(contact_api)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)