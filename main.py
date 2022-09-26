from flask import Flask
# from api import api

app = Flask(__name__)
# api = api(app)

if __name__ == '__main__':
    app.run(debug=True)
