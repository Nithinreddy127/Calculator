from CsvReader import CsvReader
import math


def addition(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result


class CSVStats(Calculator):
    data = []

    def __init__(self, data_file):
        self.data = CsvReader(data_file)
        pass
