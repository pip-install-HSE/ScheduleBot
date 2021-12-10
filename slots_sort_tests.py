import unittest
from slots_sort import sort_slots


class Tests(unittest.TestCase):
    def test1(self):
        staff_shedule = [
            [0, 0, 0],
            [0, 0, 0]
        ]
        res = [2, 1, 0]
        self.assertEqual(res, sort_slots(staff_shedule))

    def test2(self):  # проверка на данные которые в текстовом доке
        staff_shedule = [
            [2, 2, 1, 0, 0, 2],
            [2, 0, 1, 0, 2, 1],
            [2, 0, 2, 1, 0, 1]
        ]
        res = [3, 4, 1, 5, 2, 0]
        self.assertEqual(res, sort_slots(staff_shedule))

    def test3(self):
        staff_shedule = [
            [1, 1, 1],
            [1, 1, 1]
        ]
        res = [2, 1, 0]
        self.assertEqual(res, sort_slots(staff_shedule))

    def test4(self):
        staff_shedule = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 2, 2]
        ]
        res = [0, 2, 1]
        self.assertEqual(res, sort_slots(staff_shedule))
    def test5(self):
        staff_shedule = [
            [1, 1, 1],
            [0, 1, 1],
            [0, 0, 1]
        ]
        res = [0, 1, 2]
        self.assertEqual(res, sort_slots(staff_shedule))
    def test6(self):
        staff_shedule = [
            [1, 0, 0],
            [1, 1, 0],
            [1, 1, 1]
        ]
        res = [2, 1, 0]
        self.assertEqual(res, sort_slots(staff_shedule))

    def test7(self):
        staff_shedule = [
            [2, 1, 0],
            [2, 1, 0],
            [0, 1, 1]
        ]
        res = [2, 0, 1]
        self.assertEqual(res, sort_slots(staff_shedule))