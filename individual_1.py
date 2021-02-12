#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант: ((N+5)^2 mod 19) + 1 = 8
# Задание:  Использовать словарь, содержащий следующие ключи: название пункта
# назначения; номер поезда; время отправления. Написать программу, выполняющую
# следующие действия:
# ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть упорядочены по номерам поездов;
# вывод на экран информации о поезде, номер которого введен с клавиатуры;
# если таких поездов нет, выдать на дисплей соответствующее сообщение.

import sys


def _add():
    name = input("Пункт назначения? ")
    number = input("Номер поезда? ")
    time = input("Время отправления? ")

    train = {
        'name': name,
        'number': number,
        'time': time,
    }

    trains.append(train)

    if len(trains) > 1:
        trains.sort(key=lambda item: item.get('number', ''))


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
            "Название пункта назначения",
            "Номер поезда",
            "Время отправления",
        )
    )
    print(line)

    for idx, train in enumerate(trains, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>17} |'.format(
                idx,
                train.get('name', ''),
                train.get('number', ''),
                train.get('time', '')
            )
        )

    print(line)


def select():

    count = 0
    for train in trains:
        if train.get('number', '') == parts[1]:
            count += 1
            print(
                '{:>4}: {}, {}, {}'.format(
                    count,
                    train.get('name', ' '),
                    train.get('number', ' '),
                    train.get('time', ' '))
            )

    if count == 0:
        print("Поезд с данным номером не найден.")

    return count


def help_():
    print("Список команд:\n")
    print("add - добавить поезд;")
    print("list - вывести список поездов;")
    print("select <стаж> - запросить номер поезда;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


def err():
    print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    trains = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            _add()

        elif command == 'list':
            _list()

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            select()

        elif command == 'help':
            help_()

        else:
            err()

