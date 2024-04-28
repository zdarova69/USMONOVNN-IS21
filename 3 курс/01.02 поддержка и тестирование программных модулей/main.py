from datetime import datetime
from typing import List

class StudentManager:
    def min_avg(self, marks: List[str]) -> float:
        if not marks:
            raise ValueError("List of marks is empty")
        return sum(map(float, marks)) / len(marks)

    def get_count_truancy(self, marks: List["Mark"]) -> int:
        truancy_count = sum(1 for mark in marks if mark.estimation.lower() == "прогул")
        return truancy_count

    def get_count_disease(self, marks: List["Mark"]) -> int:
        disease_count = sum(1 for mark in marks if mark.estimation.lower() == "болезнь")
        return disease_count

    def get_stud_number(self, year: int, group: int, fio: str) -> str:
        fio_parts = fio.split()
        initials = "".join(part[0].upper() for part in fio_parts)
        return f"{year}.{group}.{initials}"

    def get_marks(self, now: datetime, students: List[str]) -> List["Mark"]:
        # Здесь должен быть код для генерации оценок для переданных студентов
        pass

class Mark:
    def __init__(self, date: datetime, estimation: str):
        self.date = date
        self.estimation = estimation
