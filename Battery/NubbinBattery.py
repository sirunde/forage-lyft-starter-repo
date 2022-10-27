from Battery.Battery import Battery

class NubbinBattery(Battery):
    def __int__(self, lastDate, curDate):
        self.last_service_date = lastDate
        self.current_date = curDate

    def needs_service(self):
        pass

