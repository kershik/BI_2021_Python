import unittest
from linked_list import LinkedList


def subtests(cases):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            for case in cases:
                with self.subTest(case):
                    func(*((self, case) + args), **kwargs)
        return wrapper
    return decorator

class TestLinkedList(unittest.TestCase):


    def setUp(self):
        self.items = LinkedList()
        for i in range(10, 30):
            self.items.add(i)
        for i in range(10, 20):
            self.items.add(i)
        self.control_list = list(range(10, 30)) + list(range(10, 20))

    def test_contains(self):
        self.assertIn(12, self.items)
        self.assertFalse(100 in self.items)
    
    @subtests(cases=(
        [1], [], [5, 5, 5],
        list(range(100)),
        list(range(9, 0, -1))
        ))
    def test_extend(self, case):
        self.items.extend(case)
        extended_list = self.items.to_list()
        self.control_list.extend(case)
        self.assertEqual(extended_list, self.control_list)

    @subtests(cases=(
            ([5, 5], 3),
            (list(range(100)), 1)
        ))
    def test_extend_with_index(self, case):
        self.items.extend(case[0], case[-1])
        extended_list = self.items.to_list()
        self.control_list[case[-1]:case[-1]] = case[0]
        self.assertEqual(extended_list, self.control_list)

    @subtests(cases=(None, 2, 5, 10, 15))
    def test_pop(self, case):
        pop_el = self.items.pop(case) if case is not None else self.items.pop()
        pop_list = self.items.to_list()
        pop_control = self.control_list.pop(case) if case is not None \
            else self.control_list.pop()
        self.assertEqual(pop_list, self.control_list)
        self.assertEqual(pop_el, pop_control)

    def test_remove_last_occurence(self):
        self.items.remove_last_occurence(11)
        removed_list = self.items.to_list()
        self.control_list.reverse()
        self.control_list.remove(11)
        self.control_list.reverse()
        self.assertEqual(removed_list, self.control_list)

    def test_index_raises(self):
        self.assertRaises(IndexError, self.items.add, 10, index=1000)
        self.assertRaises(IndexError, self.items.extend, [10], index=1000)
        self.assertRaises(IndexError, self.items.pop, 1000)

    def test_value_raises(self):
        self.assertRaises(ValueError, self.items.remove_last_occurence, 1000)


if __name__ == "__main__":
    unittest.main()
