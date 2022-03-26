from flask import Flask, jsonify, request, abort
from ouranos.repositories.UsersRepository import UsersRepository
from ouranos.models.entities.Admin import Admin
from ouranos.models.entities.Driver import Driver
from ouranos.models.entities.Passenger import Passenger

app = Flask(__name__)

user_repo = UsersRepository()

@app.post("/login")
def login():
    admin_data = request.json

    login = admin_data.get('login')
    password = admin_data.get('password')
    
    admin_user = user_repo.Get(lambda x: x.login == login and x.password == password)

    if admin_user is None:
        abort(404, description="Resource not found")

    return jsonify({
        "name": admin_user.name,
        "birthdate": admin_user.birthdate,
        "document": admin_user.document,
        "address": admin_user.address,
        "login": admin_user.login,
        "password": admin_user.password
    })

@app.post("/admin")
def register():
    user_data = request.json
    admin_user = Admin(
        name=user_data['name'], 
        birthdate=user_data['birthdate'], 
        document=user_data['document'], 
        address=user_data['address'],
        login=user_data['login'],
        password=user_data['password']
    )

    user_repo.Put(admin_user)

    return jsonify({
        "name": admin_user.name,
        "birthdate": admin_user.birthdate,
        "document": admin_user.document,
        "address": admin_user.address,
        "login": admin_user.login,
        "password": admin_user.password
    })

@app.post("/drivers")
def register_driver():
    driver_data = request.json
    driver = Driver(
        name=driver_data['name'], 
        birthdate=driver_data['birthdate'], 
        document=driver_data['document'], 
        address=driver_data['address'],
    )

    user_repo.Put(driver)

    return jsonify({
        "name": driver.name,
        "birthdate": driver.birthdate,
        "document": driver.document,
        "address": driver.address,
    })

@app.post("/passengers")
def register_passengers():
    passengers_data = request.json
    passengers = Passenger(
        name=passengers_data['name'], 
        birthdate=passengers_data['birthdate'], 
        document=passengers_data['document'], 
        address=passengers_data['address'],
        city=passengers_data['city'],
        state=passengers_data['state']
    )

    user_repo.Put(passengers)

    return jsonify({
        "name": passengers.name,
        "birthdate": passengers.birthdate,
        "document": passengers.document,
        "address": passengers.address,
        "city": passengers.city,
        "state": passengers.state
    })

@app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.post("/vehicles")
def register_vehicles():
    vehicles_data = request.json

    return {}    

if __name__ == "__main__":
    app.run(debug=True)
