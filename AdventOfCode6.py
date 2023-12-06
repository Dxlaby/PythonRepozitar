import math

Time = [45, 97, 72, 95]
Distance = [305, 1062, 1110, 1695]
Answer = 1

for i in range(1):
    root1 = (Time[i] - math.sqrt(Time[i]**2 - 4*Distance[i]))/2
    root2 = (Time[i] + math.sqrt(Time[i]**2 - 4*Distance[i]))/2
    Answer *= math.ceil(root2) - math.floor(root1) - 1
    #print(root2, root1)

print(Answer)