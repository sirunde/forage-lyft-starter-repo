from Battery.nubbinBattery import NubbinBattery
from Battery.spindlerBattery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from Car import Car

class CarFactory:
    @staticmethod
    def calliope(cdate,ldate,cmile, lmile):
        engine = CapuletEngine(lmile,cmile)
        battery = SpindlerBattery(cdate,ldate)
        car = Car(engine,battery)
        return car

    @staticmethod
    def glissade(cdate,ldate,cmile, lmile):
        engine = WilloughbyEngine(lmile,cmile)
        battery = SpindlerBattery(cdate,ldate)
        car = Car(engine,battery)
        return car

    @staticmethod
    def palindome(warning, cdate,ldate):
        engine = SternmanEngine(warning)
        battery = NubbinBattery(cdate,ldate)
        car = Car(engine,battery)
        return car

    @staticmethod
    def rorschach(cdate, ldate, cmile, lmile):
        engine = WilloughbyEngine(lmile, cmile)
        battery = NubbinBattery(cdate, ldate)
        car = Car(engine, battery)
        return car

    @staticmethod
    def thovex(cdate, ldate, cmile, lmile):
        engine = CapuletEngine(lmile, cmile)
        battery = NubbinBattery(cdate, ldate)
        car = Car(engine, battery)
        return car