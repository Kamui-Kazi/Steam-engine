from valve import Valve

class Spout:
    def __init__(self, input_valve:float = 0.0, drain_valve:float = 0.0):
        self.input_valve:Valve = Valve(input_valve)
        self.drain_valve:Valve = Valve(drain_valve)

    def input(self, input_valve:float = -1):
        if input_valve >= 0:
            self.input_valve.setLevel(input_valve)
        else:
            print(self.input_valve)
    
    def drain(self, drain_valve:float = -1):
        if drain_valve >= 0:
            self.drain_valve.setLevel(drain_valve)
        else:
            print(self.drain_valve)
    
    def valves(self, input_valve:float = -1, drain_valve:float = -1):
        self.input(input_valve)
        self.drain(drain_valve)
    
    def __str__(self):
        return f"input: {self.input_valve.level}%, drain: {self.drain_valve.level}%"
        