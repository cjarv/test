"""
This is a test for Encore studios.
"""
from statistics import fmean as mean
import random
import json
import re


class TempTracker:

    def __init__(self, temperatures):
        self._temperatures = temperatures

    @property
    def temperatures(self):
        return self._temperatures

    @temperatures.setter
    def temperatures(self, value):
        self._temperatures = value

    @temperatures.getter
    def temperatures(self):
        return self._temperatures

    @temperatures.deleter
    def temperatures(self):
        self.clear()

    def get_min(self):
        """
        Gets the minimum temperature in the dataset
        return: int
        """
        return min(self._temperatures)

    def get_max(self):
        """
        Gets the ma temperature in the dataset
        return: int
        """
        return max(self._temperatures)

    def get_mean(self):
        """
        Gets the mean of the dataset
        return: float
        """
        return mean(self._temperatures)

    def clear(self):
        del self._temperatures

    def insert(self, temp):
        """
        inserts a temperature (int) into the main dataset
        ::param temp: integer
        return None
        """
        if isinstance(temp, int):
            self._temperatures.append(temp)
            return True
        else:
            return False


def unit_test():
    """
    test the tracker
    """
    try:
        tracker = TempTracker([random.randrange(0, 110, 1) for i in range(0, 7)])
        tracker.insert(88)

        tmp = tracker.__dict__
        tmp = tracker.get_min()
        tmp = tracker.get_max()
        tmp = tracker.get_mean()

        tracker.clear()
        del tmp
        del tracker
        return True
    except Exception as err:
        return err


def flatten_array(arr):
    """
    This function will flatten any arbitrary nested array
    ::param arr: list (nested integer list)
    return list
    """
    stripper = re.compile(r'[\D\W]+')
    integer_list = [int(i) for i in stripper.split(json.dumps(arr)) if len(i)]
    return integer_list


if __name__ == "__main__":
    unit_test()
    print(flatten_array([[1,2,10000,[4,66,2,69,[6]],[3]],4,[30,22,10000,[3]],[19,45]]))
