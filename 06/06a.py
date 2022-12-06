from utils import *

i = 0
for w in mit.windowed(input_text().strip(), 4):
    if len(set(w)) == 4:
        break
    i += 1
print(i + 4)
