from datetime import datetime
from ...repositories.TransportRepository import TransportRepository
from ...repositories.VehiclesRepository import VehiclesRepository
from ...repositories.UsersRepository import UsersRepository

class Transport:
    def __init__(
        self,
        vehicle_plate: str,
        passenger_document: str,
        datetime: datetime,
        distance_in_km: int,
        value: float
    ):
        self.vehicle_plate = vehicle_plate
        self.passenger_document = passenger_document
        self.datetime = datetime
        self.distance_in_km = distance_in_km
        self.value = value

    def Register(
        self,
        user_repo: UsersRepository,
        vehicle_repo: VehiclesRepository,
        transport_repo: TransportRepository
    ):
        if vehicle_repo == None or user_repo == None or transport_repo == None:
            return False
        
        if vehicle_repo.exists(self.vehicle_plate) or not user_repo.exists(self.passenger_document):
            return False
        
        vehicle_repo.Insert(self)