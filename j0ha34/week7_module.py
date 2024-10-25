# Demo of an external module:

import random
import turtle

print("Generating a random number")
num = random.randint(1,10)

print(num)

draw = [1,2,3,4,5]
random.shuffle(draw)
print(draw)

for value in draw:
    turtle.forward(value*100)
    turtle.setheading((turtle.heading()+90)%360)

sleep(3000)
