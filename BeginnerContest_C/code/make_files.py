import os
import itertools
from pathlib import Path

A = [0, 1]
B = list(range(10))
C = list(range(10))

for a, b, c in itertools.product(A, B, C):
    file_name = str(a) + str(b) + str(c) + '.py'
    if file_name not in os.listdir():
        Path(file_name).touch()
