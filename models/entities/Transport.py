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
        
        if not vehicle_repo.Exists(self.vehicle_plate):
            return False

        if len(user_repo.Query(lambda user: user.document == self.passenger_document and user.type == 'Passenger')) == 0:
            return False

        transport_repo.Put(self)
        return self