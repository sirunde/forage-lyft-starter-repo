from engine.Engine import Engine
class CapuletEngine(Engine):
    def __init__(self, warning_light_is_on, last_service_date):
        self.last_service_date = last_service_date
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
