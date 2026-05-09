# Array / List : Danh sách
# Thao tác cơ bản CRUD (Create, Read, Update, Delete)

# Create - Khởi tạo
    # Empty list - Danh sách rỗng (không có phần tử)
arr = []
    # List with elements - Danh sách có phần tử
nameList = ["Đức Trung", 'Hải Nam', 'Đức Minh']
numList = [1, 2, 3, 4, 5]
mixedList = [1, 'Đức Trung', 3.14, True]
    # len() - trả về độ dài / số lượng phần tử trong danh sách
print("Độ dài của nameList:", len(nameList)) 
print("Độ dài của numList:", len(numList)) 
print("Độ dài của mixedList:", len(mixedList)) 


# Read - Hiện thị phần tử
    # Index: chỉ số / vị trí của phần tử
    # value: giá trị / nội dung của phần tử

    # Hiện phần tử bằng chỉ số index (first = 0, last = -1)
print("Phần tử đầu tiên của nameList:", nameList[0])
print("Phần tử thứ hai của numList:", numList[1])
print("Phần tử thứ cuối cùng của mixedList:", mixedList[-1])

    # Duyệt và hiện các phần tử
        # Cách 1: Dùng cả index và value
for i in range(len(nameList)):
    print(f'Index: {i}, Value: {nameList[i]}')

        # Cách 2: Chỉ dùng value
for item in numList:
    print(f'Value: {item}')

        # Cách 3: Dùng hàm có sẵn
for index, value in enumerate(mixedList):
    print(f'Index: {index}, Value: {value}')

        # Cách 4: test
print(mixedList)

# Update - cập nhật - chỉnh sửa
    # append(value): thêm phần tử vào cuối danh sách
nameList.append("Hải Đăng")
    # insert(index, value): thêm phần tử vào vị trí index
nameList.insert(1, "Đan Khanh")
    # Chỉnh sửa value
nameList[1] = "imposter"

# Delete - xóa
    # remove(value): xóa phần tử bằng value
nameList.remove("Hải Đăng")
    # pop(index): xóa phần tử bằng index
nameList.pop(1)
    # clear(): xóa tất cả phần tử trong danh sách
nameList.clear()

# Sắp xếp phần tử
numList = [5, 1, 6, 3, 2, 9, 4, 8, 7]
    # sắp xếp tăng dần
numList.sort()
    # sắp xếp giảm dần
numList.sort(reverse=True)
print(numList)

# Tìm phần tử lớn nhất và nhỏ nhất
print("Phần tử lớn nhất:", max(numList))
print("Phần tử nhỏ nhất:", min(numList))

# round() - làm tròn số
rounded_value = round(3.14159, 2)
print("Giá trị làm tròn:", rounded_value)