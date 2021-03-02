from typing import Any, Optional

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
    def __init__(self, filename: str):
        self._filename = filename


    def read(self) -> Sequence:
        with open(self._filename, "rb") as file:
            return pickle.load(file)


    def write(self, data: Sequence) -> None:
        with open(self._filename, "wb") as file:
            pickle.dump(data, file)

# def main():
#     driver1: IStructureDriver = JsonFileDriver("/Users/evgeniakalinina/Desktop/smfile")
#     driver2: IStructureDriver = PicleFileDriver("/Users/evgeniakalinina/Desktop/smbin")
#     a = [2, 4, 6]
#     driver1.write(a)
#     print(driver1.read())
#     driver2.write(a)
#     print(driver2.read())
#
# if __name__ == '__main__':
#     main()



class Node:
    def __init__(self, data: Any, next_node: Optional["Node"] = None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return f"({self.data})"

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise ValueError

        self._next_node = value


class DoubleNode(Node):
    def __init__(
            self, data: Any, next_node: Optional["Node"] = None, prev_node: Optional["Node"] = None
    ):
        super().__init__(data, next_node)
        self.prev_node = prev_node

    def __str__(self):
        return f"[{self.data}]"

    @property
    def prev_node(self):
        return self._prev_node

    @prev_node.setter
    def prev_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise ValueError

        self._prev_node = value


# не используется
class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __next__(self):
        if self.current is None:
            raise StopIteration

        node = self.current
        self.current = self.current.next_node
        return node.data

    def __iter__(self):
        return self


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def __str__(self):
        return "->".join(str(node) for node in self._node_iter())

    def __len__(self):
        return self._size

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError

        if item >= len(self) or item < 0:
            raise IndexError

        for i, node in enumerate(self._node_iter()):
            if i == item:
                return node.data

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError

        if key >= len(self) or key < 0:
            raise IndexError

        for i, node in enumerate(self._node_iter()):
            if i == key:
                node.data = value

    def __delitem__(self, key):
        self.delete(key)

    def __iter__(self):
        for node in self._node_iter():
            yield node.data

    def _node_iter(self):
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next_node

    def append(self, data: Any):
        new_node = Node(data)

        for current_node in self._node_iter():
            if current_node.next_node is None:  # tail!
                current_node.next_node = new_node
                break
        else:
            self.head = new_node

        self._size += 1

    def insert(self, data, index=0):
        if index < 0 or index > self._size:
            raise ValueError

        new_node = Node(data)
        self._size += 1
        if index == 0:
            new_node.next_node = self.head
            self.head = new_node
        else:
            for i, node in enumerate(self._node_iter()):
                if i == index - 1:
                    new_node.next_node = node.next_node
                    node.next_node = new_node

    def clear(self):
        self._size = 0
        self.head = None

    def index(self, data: Any):
        for i, node in enumerate(self._node_iter()):
            if node.data == data:
                return i

        raise ValueError

    def delete(self, index: int):
        if index < 0 or index >= self._size:
            raise ValueError

        self._size -= 1
        if index == 0:
            self.head = self.head.next_node
        else:
            for i, node in enumerate(self._node_iter()):
                if i == index - 1:
                    node.next_node = node.next_node.next_node


class LinkedListWithDriver(LinkedList):
    def __init__(self, driver: IStructureDriver):
        self._driver = driver
        super().__init__()

    def read(self):
        self.clear()
        for item in self._driver.read():
            self.append(item)

    def write(self):
        ll_as_list = [item for item in self]
        self._driver.write(ll_as_list)
        ...

def main():
    driver = PicleFileDriver("some.bin")
    ll = LinkedListWithDriver(driver)
    ll.append("a")
    ll.append("b")
    ll.append("c")
    ll.append("d")
    ll.append("e")
    ll.write()
    ll[2] = "g"
    print(ll)
    ll2 = LinkedListWithDriver(driver)
    ll2.read()
    print(ll2)
    # ll.insert("6", 5)
    # ll.insert("6", 2)
    # ll.insert("6", 0)
    # print(ll)

if __name__ == "__main__":
    main()
