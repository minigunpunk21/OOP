from .abstractions import IStudent


class Student(IStudent):
    def __init__(self, id_: int, name: str, grade: int):
        self.name = name
        self.grade = grade
        self.id = id_

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self.validate_name(name)
        self._name = name

    @property
    def grade(self) -> int:
        return self._grade

    @grade.setter
    def grade(self, grade: int):
        self.validate_grade(grade)
        self._grade = grade

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id_: int):
        self._id = id_

    @staticmethod
    def validate_name(name: str):
        if not isinstance(name, str):
            raise ValueError("строка должна бвть")
        if not name:
            raise ValueError("не пустой")

    @staticmethod
    def validate_grade(grade: int):
        if not isinstance(grade, int):
            raise ValueError("оценка это число")
        if grade < 0 or grade > 10:
            raise ValueError("0<оценка<10")
