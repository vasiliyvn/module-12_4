import logging
from unittest import TestCase
import unit1
import unittest

logging.basicConfig(level=logging.INFO, filemode="w", filename='runner_tests.log',
                            encoding='utf-8', format='%(levelname)s | %(asctime)s | %(message)s')

class RunnerTest(TestCase):
    def test_walk(self):
        try:
            w = unit1.Runner('1')
            for i in range(10):
                w.walk()
            self.assertEqual(w.distance, 50)
            logging.info(f'"test_walk" выполнен успешно')
            return 0
        except Exception as e:
            logging.error(f'Неверная скорость для Runner: {e}', exc_info=True)
            return 0
    def test_run(self):
        try:
            r = unit1.Runner('2')
            for j in range(10):
                r.run()
            self.assertEqual(r.distance, 100)
            logging.info(f'"test_run" выполнен успешно')
            return 0
        except Exception as e:
            logging.error(f'Неверный тип данных для объекта Runner: {e}', exc_info=True)
            return 0
    def test_challenge(self):
        walk1 = unit1.Runner('3')
        run1 = unit1.Runner('4')
        for k in range(10):
            walk1.walk()
            run1.run()
        self.assertNotEqual(walk1.distance, run1.distance)


if __name__ == "__main__":
    unittest.main()
