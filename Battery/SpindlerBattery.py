from Battery.Battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, curdate, lastdate):
        self.last_service_date = lastdate
        self.current_date = curdate

    def needs_service(self):
        return False


