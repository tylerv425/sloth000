import turtle
import math


chain = turtle.Turtle()
chain.speed(1000)

chainLength = 16
needleSize = 15
alpha = 180 * (chainLength - 2) / (2 * chainLength) * math.pi / 180
innerCircleRadius = needleSize * ((1/math.cos(alpha)) - 1)


for i in range(1,chainLength + 1):
    chain.pu()
    chain.circle(innerCircleRadius,(360 / chainLength))
    chain.pd()
    chain.seth(180 + ((360/chainLength) * i))
    chain.circle(needleSize)
    chain.seth((360/chainLength) * i)