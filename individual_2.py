#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант: ((N^2+1)^2 mod 19) + 1 = 2
# Задание: Использовать словарь, содержащий следующие ключи: фамилия и
# инициалы; номер группы; успеваемость(список из пяти элементов). Написать
# программу, выполняющую следующие действия: ввод с клавиатуры данных в список,
# состоящий из словарей заданной структуры; записи должны быть упорядочены по
# возрастанию среднего балла; вывод на дисплей фамилий и номеров групп для всех
# студентов, имеющих оценки 4 и 5; если таких студентов нет, вывести
# соответствующее сообщение.

import sys
import json


def _add():
    name = input("Фамилия и инициалы? ")
    group = input("Номер группы? ")
    marks = list(map(int, input("Оценки: ").split()))

    student = {
        'name': name,
        'group': group,
        'marks': sum(marks) / 5,
    }

    students.append(student)

    if len(students) > 1:
        students.sort(key=lambda item: item.get('marks', 0))


def _list():
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 17
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^17} |'.format(
            "№",
            "Ф.И.О",
            "Номер группы",
            "Успеваемость (средний балл)",
        )
    )
    print(line)

    for idx, student in enumerate(students, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>17} |'.format(
                idx,
                student.get('name', ''),
                student.get('group', ''),
                student.get('marks', '')
            )
        )

    print(line)


def select():

    count = 0
    for student in students:
        if student.get('marks', '') >= 4:
            count += 1
            print(
                '{:>4}: {}, {}'.format(
                    count,
                    student.get('name', ' '),
                    student.get('group', ' '))
            )

    if count == 0:
        print("Студент с данным номером не найден.")

    return count


def load():
    with open(parts[1], 'r') as f:
        students = json.load(f)
        print(students)


def save():
    with open(parts[1], 'w') as f:
        json.dump(students, f)


def help_():
    print("Список команд:\n")
    print("add - добавить студента;")
    print("list - вывести список студентов;")
    print("select - запросить студентов с успеваемостью выше 4;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


def err():
    print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    students = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            _add()

        elif command == 'list':
            _list()

        elif command == 'select':
            select()

        elif command.startswith('load '):
            parts = command.split(' ', maxsplit=1)
            load()

        elif command.startswith('save '):
            parts = command.split(' ', maxsplit=1)
            save()

        elif command == 'help':
            help_()

        else:
            err()
