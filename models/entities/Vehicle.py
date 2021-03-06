from ..enums.VehicleTypes import VehicleTypesEnum
from ...repositories.VehiclesRepository import VehiclesRepository
from ...repositories.UsersRepository import UsersRepository
class Vehicle:
    def __init__(
        self, 
        type: VehicleTypesEnum, 
        plate: str, 
        model: str, 
        year: int, 
        num_passengers: int, 
        drivers_document: str
    ):
        self.type = type
        self.plate = plate
        self.model = model
        self.year = year
        self.num_passengers = num_passengers
        self.drivers_document = drivers_document

    def Register(
        self, 
        userRepo: UsersRepository,
        vehicleRepo: VehiclesRepository 
    ):
        if vehicleRepo == None or vehicleRepo.Exists(self.plate):
            return False
        
        if len(userRepo.Query(lambda user: user.document == self.drivers_document and user.type == "Driver")) == 0:
            return False
        
        vehicleRepo.Put(self)

        return self
        