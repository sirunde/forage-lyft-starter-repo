from Battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, curdate, lastdate):
        self.last_service_date = lastdate
        self.current_date = curdate

    def needs_service(self):
        return (self.current_date - self.last_service_date >= 2)

