import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from spout import Spout

t = Spout(100.0, 10)
print(t)
t.input(1.0)
print(t)
t.drain(1.0)
print(t)
