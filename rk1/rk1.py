# Рубежный контроль №1 по курсу ПиК ЯП
# Вариант запросов А, предметная область №3 (Водитель - Автопарк)
# Выполнил: Бауман Д. Г., группа ИУ5-31Б

# используется для сортировки
from operator import itemgetter


class Driver:
    """Водитель"""

    def __init__(self, id, surname, salary, park_id):
        self.id = id
        self.surname = surname
        self.salary = salary  # количественный признак
        self.park_id = park_id  # для связи один-ко-многим


class Autopark:
    """Автопарк"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class DriverPark:
    """Водители автопарка (для реализации связи многие-ко-многим)"""

    def __init__(self, driver_id, park_id):
        self.driver_id = driver_id
        self.park_id = park_id


# Автопарки
parks = [
    Autopark(1, 'Северный автопарк'),
    Autopark(2, 'Южный автопарк'),
    Autopark(3, 'Восточный автопарк'),
    Autopark(4, 'Резервная автобаза'),
]

# Водители
drivers = [
    Driver(1, 'Абрамов', 62000, 1),
    Driver(2, 'Петров', 71000, 1),
    Driver(3, 'Алексеев', 58000, 2),
    Driver(4, 'Сидоров', 65000, 2),
    Driver(5, 'Николаев', 80000, 3),
]

# Водители автопарков
drivers_parks = [
    DriverPark(1, 1),
    DriverPark(1, 3),
    DriverPark(2, 1),
    DriverPark(3, 2),
    DriverPark(4, 2),
    DriverPark(4, 4),
    DriverPark(5, 3),
]


def get_one_to_many():
    """Соединение данных один-ко-многим: (фамилия, зарплата, автопарк)"""
    return [(d.surname, d.salary, p.name)
            for p in parks
            for d in drivers
            if d.park_id == p.id]


def get_many_to_many():
    """Соединение данных многие-ко-многим: (фамилия, зарплата, автопарк)"""
    return [(d.surname, d.salary, p.name)
            for p in parks
            for dp in drivers_parks
            for d in drivers
            if p.id == dp.park_id and d.id == dp.driver_id]


def task_1(one_to_many):
    """Все связанные водители и автопарки, сортировка по автопаркам"""
    return sorted(one_to_many, key=itemgetter(2))


def task_2(one_to_many):
    """Автопарки с суммарной зарплатой водителей, по её убыванию"""
    result = []
    for p in parks:
        salaries = [salary for _, salary, park_name in one_to_many
                    if park_name == p.name]
        # Автопарки без водителей в результат не попадают
        if salaries:
            result.append((p.name, sum(salaries)))
    return sorted(result, key=itemgetter(1), reverse=True)


def task_3(many_to_many):
    """Автопарки со словом «автопарк» в названии и их водители"""
    return {p.name: [surname for surname, _, park_name in many_to_many
                     if park_name == p.name]
            for p in parks
            if 'автопарк' in p.name}


def main():
    """Основная функция"""
    one_to_many = get_one_to_many()
    many_to_many = get_many_to_many()

    print('Задание А1')
    print(task_1(one_to_many))

    print('\nЗадание А2')
    print(task_2(one_to_many))

    print('\nЗадание А3')
    print(task_3(many_to_many))


if __name__ == '__main__':
    main()
