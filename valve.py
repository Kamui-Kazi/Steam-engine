class Valve:
    def __init__(self, level:float=0):
        self.level:float = level
    
    def setLevel(self, level:float=0):
        self.level = level

    def flow(self, input:float=1) -> float:
        return input * (self.level / 100.0)
    
    def __str__(self) -> str:
        return f"level: {self.level}%"