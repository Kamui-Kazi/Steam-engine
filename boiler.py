from scipy import constants as const
import math
from spout import Spout
from flame import Flame
from valve import Valve

class Boiler:
    def __init__(self):
        self.tank:float = 0.0
        self.temp:float = 0.0
        self.pressure:float = 0.0
        self.relif_valve:Valve = Valve(0.0)
        self.output_valve:Valve = Valve(0.0)
        self.spout = Spout(0.0)
        self.flame = Flame()
    def step(self):
        self.temp = self.temp * self.flame.temp
        self.boil()
        
    def boil(self):
        a = 1 - (373.15/self.temp)
        self.pressure = 013.25 * ((13.3185 - (1.97 + (0.6445 + (0.1299*a))**a)**a)**a)

    def intake(self):
        pass

    def output(self):
        pass