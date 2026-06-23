from abc import abstractmethod

class Human:
    def __init__ (self, name, age, gender):
        self.name = name
        self.__age = age        # private (đóng gói)
        self.gender = gender

    def get_age(self):
        return self.__age

    @abstractmethod
    def speak(self):
        pass

    # Tính đa hình (cùng 1 phương thức nhưng nhiều cách thực hiện)
    def introduce(self):
        print("Xin chào, tôi là con người.")

# Kế thừa từ Human
class Student(Human):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id

    def speak(self):
        print(f'Tôi tên là {self.name}, mã học sinh: {self.student_id}')

    def introduce(self):
        print("Xin chào, tôi là học sinh.")