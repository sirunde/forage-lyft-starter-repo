from servieable import Serviceable

class Car(Serviceable):
    def __init__(self,engine,battery):
        self.battery = battery
        self.engine = engine

    def need_service(self):
        return self.engine.need_service() or self.battery.needs_service()