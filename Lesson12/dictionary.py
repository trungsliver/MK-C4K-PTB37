# CRUD: Create, Read, Update, Delete

# Create
dict1 = {}
dict2 = {
    # các cặp key-value
    'name': 'Duc Trung',
    'age': 20,
    'gender': 'Male'
}

# Read
    # Truy cập bằng key
print(dict2['name'])            # Output: Duc Trung
    # Sử dụng phương thức get()
print(dict2.get('age'))         # Output: 20
        # Nếu không tồn tại key => None / Giá trị mặc định
print(dict2.get('money'))       # Output: None
print(dict2.get('money', 0))    # Output: 0
    # Duyệt toàn bộ key-value
for key, value in dict2.items():
   print(f"{key}: {value}")

# Update - chỉnh sửa
    # Thêm cặp key - value
dict2['laptop'] = 'MSI'
    # Chỉnh sửa value
dict2['name'] = 'Hai Nam'
print(dict2)

# Delete - Xóa 
    # Xóa theo key - del
del dict2['laptop']
    # Xóa theo key, trả về value - pop()
# dict2.pop('gender')
print(dict2.pop('gender'))

# Kiểm tra key tồn tại
print('name' in dict2)          # Output: True
print('girlfriend' in dict2)    # Output: False

# Lấy tất cả cặp key - value: items()
print(dict2.items())
# Lấy tất cả key: keys()
print(dict2.keys())
# Lấy tất cả value: values()
print(dict2.values())

# Hàm map(function, itertable)
    # function: hàm biến đổi dữ liệu
    # itertable: bảng dữ liệu

# Yêu cầu: dùng map() để thêm tên lớp vào sau tên hs
arr = ['Trung', 'Nam', 'Hải', 'Kiệt', 'Vinh']
    # cách 1: dùng function
def add_class(student_name, class_name = 'MindX'):
    return f"{student_name} - {class_name}"
arr1 = list(map(add_class, arr))
print(arr1)

    # cách 2: dùng lambda function
arr2 = list(map(lambda student: f"{student} - MindX", arr))
print(arr2)