from math import sin, cos
from os import system
from numpy import arange
from time import sleep

A, B, C = 0.0, 0.0, 0.0

width = 160
height = 44

zBuffer = []
buffer = []

distanceFromCam = 100
horizontalOffset = 0.0
K1 = 40
incrementSpeed = 0.6


def calculateX(i, j, k):
    return j * sin(A) * sin(B) * cos(C) - k * cos(A) * sin(B) * cos(C) + j * cos(A) * sin(C) + k * sin(A) * sin(
        C) + i * cos(B) * cos(C)


def calculateY(i, j, k):
    return j * cos(A) * cos(C) + k * sin(A) * cos(C) - j * sin(A) * sin(B) * sin(C) + k * cos(A) * sin(B) * sin(
        C) - i * cos(B) * sin(C)


def calculateZ(i, j, k):
    return k * cos(A) * cos(B) - j * sin(A) * cos(B) + i * sin(B)


def calculateForSurface(cubeX, cubeY, cubeZ, ch):
    x = calculateX(cubeX, cubeY, cubeZ)
    y = calculateY(cubeX, cubeY, cubeZ)
    z = calculateZ(cubeX, cubeY, cubeZ) + distanceFromCam

    ooz = 1 / z

    xp = int((width / 2 + horizontalOffset + K1 * ooz * x * 2))
    yp = int((height / 2 + K1 * ooz * y))

    idx = xp + yp * width

    if 0 <= idx < (width * height):
        if ooz > zBuffer[idx]:
            zBuffer[idx] = ooz
            buffer[idx] = ch


def clear():
    system('cls||clear')


def cube(cube_width, Offset):
    global horizontalOffset
    if Offset == 0:
        horizontalOffset = cube_width
    else:
        horizontalOffset = Offset * cube_width
    for cubeX in arange(-cube_width, cube_width, incrementSpeed):
        for cubeY in arange(-cube_width, cube_width, incrementSpeed):
            calculateForSurface(cubeX, cubeY, -cube_width, '.')
            calculateForSurface(cube_width, cubeY, cubeX, ',')
            calculateForSurface(-cube_width, cubeY, -cubeX, '-')
            calculateForSurface(-cubeX, cubeY, cube_width, '~')
            calculateForSurface(cubeX, -cube_width, -cubeY, '/')
            calculateForSurface(cubeX, cube_width, cubeY, '`')


def fbuffer(sizeX=width, sizeY=height):
    global zBuffer, buffer
    zBuffer = []
    buffer = []
    for _ in range(sizeX * sizeY):
        zBuffer.append(0.0)
        buffer.append(' ')


if __name__ == '__main__':
    system('cls||clear')
    while True:
        fbuffer()

        cube(12, 3)
        cube(15, -0.5)
        cube(12, -4)

        clear()

        print("".join(buffer))

        A += 0.05
        B += 0.05
        C += 0.01

        sleep(0.1)
