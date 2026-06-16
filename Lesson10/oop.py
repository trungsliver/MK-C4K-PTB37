# OOP - Object Oriented Programming 
# Lập trình hướng đối tượng

# Tổng quát: OOP là cách mô phỏng thế giới thực vào chương trình máy tính

# Class (lớp):          Đối tượng tổng quát
# Object (đối tượng):   Đối tượng cụ thế

# Attribute (thuộc tính):  Đặc điểm của đối tượng
# Method (phương thức):    Hành động của đối tượng

# Khai báo class (Đối tượng tổng quát)
class Human:
    # Hàm khởi tạo
    def __init__(self, name, age, gender):
        # name, age, gender là attribute (thuộc tính)
        self.name = name
        self.age = age
        self.gender = gender

    # Phương thức (method)
    # Phương thức giới thiệu bản thân
    def introduce(self):
        print(f'Xin chào, tôi là {self.name}, {self.age} tuổi và là {self.gender}')

    # Phương thức hiển thị thông tin (có sẵn)
    def __str__ (self):
        return f'''
========== HUMAN INFO ==========
Name: {self.name}
Age: {self.age}
Gender: {self.gender}
================================'''
    
    # Phương thức tìm năm sinh
    def get_birth_year(self, current_year:int):
        return current_year - self.age


# Khởi tạo object (Đối tượng cụ thể)
human1 = Human('Hải Nam', 14, 'Nam')
print(human1)
print(human1.name)
print(human1.age)
print(human1.gender)
# Gọi phương thức 
human1.introduce()
print('Năm sinh:', human1.get_birth_year(2026))