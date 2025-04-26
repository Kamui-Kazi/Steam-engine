import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import boiler

b = boiler.Boiler()
b.temp = 100
b.flame.temp = 10
b.step()
print(b.pressure)
b.step()
print(b.pressure)
b.step()
print(b.pressure)
b.step()
print(b.pressure)
