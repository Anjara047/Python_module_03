#!/usr/bin/env python3
import math


def get_player_pos() -> tuple:
    while True:
        try:
            s = input("Enter new coordinates as floats in format 'x,y,z': ")

            i = s.find(',')
            j = s.rfind(',')

            if i == -1 or j == -1 or i == j:
                raise ValueError("Invalid format")

            p1 = s[:i]
            p2 = s[i + 1:j]
            p3 = s[j + 1:]

            try:
                x = round(float(p1), 1)
            except ValueError:
                print(f"Error on parameter '{p1}': ", end="")
                print(f"could not convert string to float: '{p1}'")
                continue

            try:
                y = round(float(p2), 1)
            except ValueError:
                print(f"Error on parameter '{p2}': ", end="")
                print(f"could not convert string to float: '{p2}'")
                continue

            try:
                z = round(float(p3), 1)
            except ValueError:
                print(f"Error on parameter '{p3}': ", end="")
                print(f"could not convert string to float: '{p3}'")
                continue

            return (x, y, z)

        except Exception:
            print("Invalid syntax")


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===\n")
    x1 = 0
    y1 = 0
    z1 = 0

    print("Get a first set of coordinates")
    x2, y2, z2 = get_player_pos()
    distance = math.sqrt(((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2))
    print(f"Got a first tuple: ({x2}, {y2}, {z2})")
    print(f"It includes: X={x2}, Y={y2}, Z={z2}")
    print(f"Distance to center: {round(distance, 4)}\n")

    print("Get a second set of coordinates")
    x3, y3, z3 = get_player_pos()
    distance = math.sqrt(((x3 - x2)**2 + (y3 - y2)**2 + (z3 - z2)**2))
    print(f"Distance beetween the 2 sets of coordinates: {round(distance, 4)}")


if __name__ == "__main__":
    ft_coordinate_system()
