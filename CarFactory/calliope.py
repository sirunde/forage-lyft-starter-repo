from datetime import datetime
from Battery.spindlerBattery import SpindlerBattery
from engine.capulet_engine import CapuletEngine


class Calliope(SpindlerBattery,CapuletEngine):
    def __init__(self, cDate,lSDate,cMile,lSMile):
        self.current_date = cDate
        self.last_service_date = lSDate
        self.last_service_mileage = lSMile
        self.current_mileage = cMile
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
