
"""
    1. Реализовать класс JsonFileDriver, который будет описывать логику считывания (записи) элементов из (в) json файл.
    2. Реализовать класс SimpleFileDriver, который будет описывать логику считывания (записи) элементов из (в) файл.
    3. В блоке __main__ протестировать работу драйверов
"""

from typing import Sequence
from abc import ABC, abstractmethod
import json
import pickle


class IStructureDriver(ABC):
    @abstractmethod
    def read(self) -> Sequence:
        """
        Считывает информацию из драйвера и возвращает её для объекта, использующего этот драйвер
        :return Последовательность элементов, считанная драйвером, для объекта
        """
        pass

    @abstractmethod
    def write(self, data: Sequence) -> None:
        """
        Получает информацию из объекта, использующего этот драйвер, и записывает её в драйвер
        :param data Последовательность элементов, полученная от объекта, для записи драйвером
        """
        pass


class JsonFileDriver(IStructureDriver):
    def __init__(self, filename: str):
        self._filename = filename


    def read(self) -> Sequence:
        with open(self._filename) as file:
            return json.load(file)


    def write(self, data: Sequence) -> None:
        with open(self._filename, "w") as file:
            json.dump(data, file)



class PicleFileDriver(IStructureDriver):
    ...

def main():
    driver: IStructureDriver = JsonFileDriver("/Users/evgeniakalinina/Desktop/smfile ")
    a = [2, 4, 6]
    driver.write(a)
    print(driver.read())

if __name__ == '__main__':
    main()
