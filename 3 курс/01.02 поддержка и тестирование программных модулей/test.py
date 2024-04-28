import unittest
from datetime import datetime
from your_module import StudentManager, Mark

class TestStudentManager(unittest.TestCase):
    def setUp(self):
        self.student_manager = StudentManager()

    def test_min_avg(self):
        # Проверка вычисления среднего арифметического
        marks = ["4", "5", "3", "4"]
        self.assertEqual(self.student_manager.min_avg(marks), 4.0)

        marks = ["5", "5", "5", "5"]
        self.assertEqual(self.student_manager.min_avg(marks), 5.0)

    def test_get_count_truancy(self):
        # Проверка подсчета количества прогулов
        marks = [Mark(datetime.now(), "прогул") for _ in range(5)]
        self.assertEqual(self.student_manager.get_count_truancy(marks), 5)

        marks = [Mark(datetime.now(), "4") for _ in range(5)]
        self.assertEqual(self.student_manager.get_count_truancy(marks), 0)

    def test_get_count_disease(self):
        # Проверка подсчета количества пропусков по болезни
        marks = [Mark(datetime.now(), "болезнь") for _ in range(3)]
        self.assertEqual(self.student_manager.get_count_disease(marks), 3)

        marks = [Mark(datetime.now(), "5") for _ in range(5)]
        self.assertEqual(self.student_manager.get_count_disease(marks), 0)

    def test_get_stud_number(self):
        # Проверка генерации номера студенческого билета
        self.assertEqual(self.student_manager.get_stud_number(2023, 1, "Иванов Иван Иванович"), "2023.1.ИИИ")

        self.assertEqual(self.student_manager.get_stud_number(2022, 2, "Петров Петр Петрович"), "2022.2.ППП")

    def test_get_marks(self):
        # Здесь тесты для метода get_marks
        pass

if __name__ == '__main__':
    unittest.main()
