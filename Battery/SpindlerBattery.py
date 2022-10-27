from Battery.Battery import Battery

class SpindlerBattery(Battery):
    def __int__(self, lastDate, curDate):
        self.last_service_date = lastDate
        self.current_date = curDate

    def needs_service(self):
        return False


