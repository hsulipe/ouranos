from flask import Flask
from ouranos.controllers.users import UserController

app = Flask(__name__)


users = UserController()

@app.post('/users/login', endpoint=users.login)

@app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)
