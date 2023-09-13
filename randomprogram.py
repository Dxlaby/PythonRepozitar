import random as ran;
import math;

inCircle = 0
N = int(input("How many times should simulation run?"))

for i in range(N):
  x = ran.random()
  y = ran.random()
  if ((x**2 + y**2) < 1):
    inCircle+=1

print("Pi is cca {0}", inCircle*4/N)
