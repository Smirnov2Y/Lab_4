
class Watch:
    """ Базовый класс часов. """

    def __init__(self, size: int, material: str, water_resistance: float):
        """
               Создание и подготовка к работе объекта "Часы"

               :param size: Размер часов в мм
               :param material: Материла часов
               :param water_resistance: Водонепроницаемость часо в в АТМ

               Примеры:
               >>> watch = Watch(36, "Steel", 10)  # инициализация экземпляра класса
               """

        self._size = size
        self.material = material
        self._water_resistance = water_resistance

    @property
    def size(self):  # Задаётся производителем
        return self._size

    @property
    def water_resistance(self):
        return self._water_resistance

    @water_resistance.setter
    def water_resistance(self, new_water_resistance: float) -> None:  # Проверка водонероницаемости на корректность
        """Значение водопоглощаемости часов в АТМ."""
        if not isinstance(new_water_resistance, float):
            raise TypeError("Значение водопоглощаемости часов должно быть типа float")
        if new_water_resistance <= 0:
            raise ValueError("Значение водопоглощаемости часов должно быть положительным числом")
        self._water_resistance = new_water_resistance

    def __str__(self):
        return f"Часы размера {self._size}, сделанные из {self.material}" \
               f" с водонепроницаемостью равной {self._water_resistance}"

    def __repr__(self):
        return f"{self.__class__.__name__}(size={self._size!r}, material={self.material!r}, " \
               f" water_resistance={self._water_resistance})"

    def __eq__(self, other):  # Нужно для распределения материала на производстве (наследуется)
        return self.material == other.material

    def __round__(self, ndigits=0):  # Для округления значения водопоглощаемости
        return round(self.water_resistance)  # Нужно, так как удобнее работать с округлённым числом


class DigitalWatch(Watch):
    """Дочерний класс часов. """

    def __init__(self, size: int, material: str, water_resistance: int, work_time: float):
        """
                       Создание и подготовка к работе объекта "Электронные часы"

                       :param size: Размер часов в мм
                       :param material: Материла часов
                       :param water_resistance: Водонепроницаемость часо в в АТМ
                       :param work_time: Время работы часов на заряде аккумулятора в часах

                       Примеры:
                       >>> watch = DigitalWatch(36, "Steel", 10, 73)  # инициализация экземпляра класса
                       """
        super().__init__(size, material, water_resistance)
        self.work_time = work_time

    @property
    def work_time(self):
        return self.work_time

    @work_time.setter
    def work_time(self, new_work_time: int) -> None:  # Проверка часов работы на корректность
        """Длительность работы часов на заряде аккумулятора."""
        if not isinstance(new_work_time, int):
            raise TypeError("Длительность работы должна быть типа int")
        if new_work_time <= 0:
            raise ValueError("Длительность работы должна быть положительным числом")
        self._work_time = new_work_time

    def __repr__(self):  # Перегрузка, так как появился новый аргумент, нужный в дальнейшей работы фирмы
        return f"{self.__class__.__name__}(size={self._size!r}" \
               f", material={self.material!r}, water_resistance={self._water_resistance}, work_time={self.work_time})"

    def __round__(self, ndigits=0):  # Для округления значения водопоглощаемости и часов работы часов (перегружается)
        return round(self.water_resistance, self.work_time)  # Нужно, так как удобнее работать с округлённым числом


class MechanicalWatch(Watch):
    """Дочерний класс часов. """

    def __init__(self, size: int, material: str, water_resistance: int, accuracy: float):
        """
                               Создание и подготовка к работе объекта "Механические часы"

                               :param size: Размер часов в мм
                               :param material: Материла часов
                               :param water_resistance: Водонепроницаемость часо в в АТМ
                               :param accuracy: Точность часов в с в день

                               Примеры:
                               >>> watch = MechanicalWatch(36, "Steel", 10, 0.00001)  # инициализация экземпляра класса
                               """
        super().__init__(size, material, water_resistance)
        self._accuracy = accuracy

    def __repr__(self):  # Перегрузка, так как появился новый аргумент, нужный в дальнейшей работы фабрики
        return f"{self.__class__.__name__}(size={self._size!r}" \
               f", material={self.material!r}, water_resistance={self._water_resistance}, accuracy={self._accuracy!r})"

    def __round__(self, ndigits=3):  # Для округления значения водопоглощаемости и точности часов (перегружается)
        return round(self._accuracy)  # Нужно, так как удобнее работать с округлённым числом


if __name__ == "__main__":
    # Write your solution here
    pass
