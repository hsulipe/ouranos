from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from functools import reduce

from .repositories.UsersRepository import UsersRepository
from .repositories.VehiclesRepository import VehiclesRepository
from .repositories.TransportRepository import TransportRepository

from .models.entities.Admin import Admin
from .models.entities.Driver import Driver
from .models.entities.Passenger import Passenger
from .models.entities.Vehicle import Vehicle
from .models.entities.Transport import Transport

from .models.enums.VehicleTypes import VehicleTypesEnum

app = Flask(__name__)
CORS(app)

user_repo = UsersRepository()
vehicle_repo = VehiclesRepository()
transport_repo = TransportRepository()

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

    result = admin_user.Register(user_repo)

    if not result:
        abort(409, description="Admin already registered") 

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

    result = driver.Register(user_repo)

    if not result:
        abort(409, description="Admin already registered") 

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

    result = passengers.Register(user_repo)

    if not result:
        abort(409, description="Admin already registered") 

    return jsonify({
        "name": passengers.name,
        "birthdate": passengers.birthdate,
        "document": passengers.document,
        "address": passengers.address,
        "city": passengers.city,
        "state": passengers.state
    })

@app.post("/vehicles")
def register_vehicles():
    vehicles_data = request.json
    vehicles = Vehicle(
        plate=vehicles_data['plate'], 
        type=VehicleType[vehicles_data['type']], 
        model=vehicles_data['model'], 
        year=vehicles_data['year'],
        num_passengers=vehicles_data['num_passengers'],
        drivers_document=vehicles_data['drivers_document']
    )

    result = vehicles.Register(user_repo, vehicle_repo)

    if not result:
        abort(409, description="Admin already registered") 

    return jsonify({
        "plate": vehicles.plate,
        "type": vehicles.type,
        "model": vehicles.model,
        "year": vehicles.year,
        "num_passengers": vehicles.num_passengers,
        "drivers_document": vehicles.drivers_document
    })

@app.post("/transports")
def register_transports():
    transports_data = request.json
    transport = Transport(
        plate=transports_data['plate'], 
        type=VehicleTypesEnum[transports_data['type']], 
        model=transports_data['model'], 
        year=transports_data['year'],
        num_passengers=transports_data['num_passengers'],
        drivers_document=transports_data['drivers_document']
    )

    result = transport.Register(user_repo, vehicle_repo)

    if not result:
        abort(409, description="Admin already registered") 

    
    return jsonify({
        "plate": transport.plate,
        "type": transport.type,
        "model": transport.model,
        "year": transport.year,
        "num_passengers": transport.num_passengers,
        "drivers_document": transport.drivers_document
    })

@app.get('/financial_reports')
def get_financial_reports():
    financial_report_data = request.json

    transports = transport_repo.Query(
        lambda transport: transport.datetime >= financial_report_data.start_date 
            and transport.datetime <= financial_report_data.end_date
    )

    if not transports:
        abort(404, description="Not Found")

    return jsonify({
        "total_value": reduce(lambda a, b: a + b.value, transports),
        "quantity": len(transports),
    })

if __name__ == "__main__":
    app.run(debug=True)
