# Danh sách: Array / List
# Thao tác CRUD: Create - Read - Update - Delete

# Create - Khởi tạo
    # Danh sách rỗng - không có phần tử
arr = []
    #  Danh sách có sẵn phần tử
nameList = ['Trung', 'Linh', 'Hùng', 'Trang']
numList = [1, 2, 5, 4, 5]
mixList = ['Trung', 25, True, 6.5]
    # len(): trả về độ dài / số lượng phần tử trong danh sách
print("nameList:", len(nameList))
print("numList:", len(numList))
print("mixList:", len(mixList))

# Read - Hiện phần tử
    # Index: chỉ số / vị trí của phần tử
    # Value: giá trị của phần tử

    # Hiện phần tử bằng chỉ số index
print(nameList[1])
print(nameList[0])      # Phần tử đầu tiên
print(nameList[-1])     # Phần tử cuối cùng

    # Duyệt và hiện các phần tử
        # Cách 1: Dùng cả index và value
for i in range(len(nameList)):
    print(f"Index: {i}, Value: {nameList[i]}")

        # Cách 2: Chỉ dùng value
for item in nameList:
    print(item)

        # Cách 3: Dùng hàm có sẵn
for index, value in enumerate(nameList):
    print(f"Index: {index}, Value: {value}")

        # Cách 4: để test
print(nameList)

# Update: Cập nhật - Chỉnh sửa
    # append(value): thêm phần tử vào cuối danh sách
nameList.append('Vân')
    # insert(index, value): thêm vào vị trí chỉ định
nameList.insert(1, 'imposter')
    # chỉnh sửa value
nameList[1] = 'Xuân'

# Delete: Xóa phần tử
    # remove(value): xóa phần tử bằng giá trị
nameList.remove('Vân')
    # pop(index): xóa bằng index
nameList.pop(1)
    # clear(): xóa toàn bộ phần tử danh sách
nameList.clear()
print(nameList)

# Sắp xếp phần tử danh sách
numList = [5, 1, 6, 3, 2, 9, 4, 8, 7]
    # Theo thứ tự từ nhỏ đến lớn
numList.sort()
    # Theo thứ tự từ lớn đến nhỏ
numList.sort(reverse=True)
print(numList)

# Tìm phần tử lớn nhất & nhỏ nhất
print('Phần tử lớn nhất:', max(numList))
print('Phần tử nhỏ nhất:', min(numList))

# round(): làm tròn
num = 3.333333333333333
print(num)
print("round():", round(num, 2))

# ============ LUYỆN TẬP ===============
# a = []
# import random
# for i in range(10):
#     a.append(random.randint(1, 100))
# print(a)

a = [5, 1, 6, 3, 2, 9, 4, 8, 7, 3.33]

# Bài 1: Viết chương trình nhập từ bàn phím danh sách a. 
# Hãy trả về kết quả các phần tử trong danh sách theo thứ tự tăng dần.
a.sort()
print(a)

# Bài 2: Viết chương trình nhập từ bàn phím danh sách a. 
# Hãy tìm ra phần tử lớn nhất và nhỏ nhất từ danh sách a và trả về kết quả.
print('Phần tử lớn nhất:', max(a))
print('Phần tử nhỏ nhất:', min(a))

# Bài 3: Viết chương trình nhập từ bàn phím danh sách a. 
# Hãy tính giá trị trung bình của các phần tử trong danh sách a và trả về kết quả giá trị trung bình.

    # Tính tổng các phần tử
sum = 0
for item in a:
    sum += item     # sum = sum + item
    # Tính trung bình
avg = sum / len(a)
print("Giá trị trung bình:", round(avg, 2))

# Bài 4: Viết chương trình nhập từ bàn phím danh sách a. 
# Tính tổng các số lẻ và tổng các số chẵn trong danh sách a.
sumEven = 0
sumOdd = 0
for item in a:
    if item % 2 == 0:
        sumEven += item
    else:
        sumOdd += item
print("Tổng các số chẵn:", sumEven)
print("Tổng các số lẻ:", sumOdd)

# Bài 5: Viết chương trình khai báo sẵn danh sách a. Viết chương trình bao gồm các chức năng: hiện toàn bộ phần tử danh sách, thêm phần tử vào danh sách, sửa phần tử danh sách, xóa phần tử trong danh sách.
while True:
    print('\n========== MENU ============')
    print('1. Print')
    print('2. Add')
    print('3. Change ')
    print('4. Erase')
    print('5. Exit')
    print('============================')
    choice = int(input('Nhap lua chon: '))

    match choice:
        case 1:
            print(a)
        case 2:
            value = int(input('input the number you want to add: '))
            a.append(value)
        case 3:
            index = int(input("where do you want to change: "))
            value = int(input('input the number you want to add: '))
            a[index] = value
        case 4:
            index = int(input("what index do you want to erase: "))
            a.pop(index)
        case 5:
            break
        case _: # default case
            print("Invalid")

# Bài 6: Nhập từ bàn phím 1 số nguyên n
# Yêu cầu: Kiểm tra xem n có phải là số nguyên tố hay không
# Biết rằng số nguyên tố là số chỉ chia hết cho 1 và chính nó

    # Nhập số nguyên n
n = int(input("Nhập số nguyên n: "))
    # Khai báo biến count: đếm số lượng ước / số lần chia hết
count = 0
    # Duyệt từ 1 đến n
for i in range(1, n+1):
    # Nếu n chia hết cho i thì count tăng lên 1
    if n % i == 0:
        count += 1

    # Kiểm tra kết quả
if count == 2:
    print(n, "là số nguyên tố")
else:
    print(n, "không phải là số nguyên tố")

# Bài 7: In ra các số nguyên tố trong khoảng [50,100] và tính tổng các số đó
    # Biến lưu tổng các số nguyên tố
sum2 = 0

    # Duyệt các số trong khoảng [50, 100]
for n in range(50,101):
    # Kiểm tra xem n có phải là số nguyên tố hay không
    count = 0
    # Nếu n chia hết cho i thì count tăng lên 1
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    # Nếu n là số nguyên tố 
    if count == 2:
        # Hiện số n / In ra số n
        print(n, end = ' ')
        # Cộng n vào tổng sum2
        sum2 += n

print("\nTổng các số nguyên tố là:", sum2)