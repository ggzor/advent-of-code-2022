from utils import *

i = 0
for w in mit.windowed(input_text().strip(), 14):
    if len(set(w)) == 14:
        break
    i += 1
print(i + 14)
