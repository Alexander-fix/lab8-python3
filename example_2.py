# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# В основной ветке программы вызывается функция cylinder(), которая вычисляет площадь цилиндра. В теле cylinder()
# определена функция circle(), вычисляющая площадь круга по формуле пr^2. В теле cylinder() у пользователя спрашивается,
# хочет ли он получить только площадь боковой поверхности цилиндра, которая вычисляется по формуле 2пrh, или полную
# площадь цилиндра. В последнем случае к площади боковой поверхности цилиндра должен добавляться удвоенный результат
# вычислений функции circle().


import math


def cylinder(r, h, full_s=True):
    def circle(r):
        return math.pi * (r ** 2)

    s_bor_cylinder = 2 * math.pi * r * h

    if full_s:
        return s_bor_cylinder + 2 * circle(r)
    else:
        return s_bor_cylinder


if __name__ == '__main__':
    r = float(input("Радиус: "))
    h = float(input("Высота: "))
    c = input("s_bor_cylinder or full_s?")
    s = cylinder(r, h, full_s=(c == 'full_s'))
    print(s)
