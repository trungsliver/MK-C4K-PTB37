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


# Bài tập 1
class Animal:
    def __init__(self, name, species):
        self.name = name            # Tên động vật
        self.species = species      # Loài động vật

    def display_info(self):
        print(f'''
======== THÔNG TIN =======
Tên:    {self.name}
Loài:   {self.species}
==========================''')

    def eat(self, food):
        print(f"{self.name} đang ăn {food}.")

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed      # giống / chủng loại
    
    # Tính đa hình
    def display_info(self):
                print(f'''
======== THÔNG TIN =======
Tên:    {self.name}
Loài:   {self.species}
Giống:  {self.breed}
==========================''')
                
    # để sử dụng được print()
    def __str__(self):
        return f"Dog(Name: {self.name}, Species: {self.species}, Breed: {self.breed})"

# Bài tập 2
class Vehicle:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price

    def start(self):
        print(f"Xe {self.brand} đang khởi động")

class Bicycle(Vehicle):
    def __init__(self, brand, color, price):
        super().__init__(brand, color, price)

    def start(self):
        print(f"Xe đạp {self.brand} đang được đạp về phía trước")

class Car(Vehicle):
    def __init__(self, brand, color, price):
        super().__init__(brand, color, price)

    def start(self):
        print(f"Xe ô tô {self.brand} đang chạy về phía trước bằng động cơ")
