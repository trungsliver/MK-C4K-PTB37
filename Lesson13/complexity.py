# ALGORITHM COMPLEXITY - ĐỘ PHỨC TẠP CỦA THUẬT TOÁN

# Biểu diễn bằng Big-O Notation
    # Độ phức tạp (O) = n * số phép toán
    # n là kích thước dữ liệu đầu vào

#  Ý nghĩa: mô tả hành vi xử lý (thời gian tính toán, bộ nhớ cần dùng)

# ================================================
# O(1) - Constant Time Complexity - Độ phức tạp hằng số (gán, nhập, xuất)
name = 'Duc Trung'
age = input('Nhập tuổi của bạn: ')
print(name)

# O(n) - Linear Time Complexity - Độ phức tạp tuyến tính (vòng lặp)
    # n là kích thước dữ liệu đầu vào
num_list = [1, 2, 3, 4, 5]      # n = 5 
for num in num_list:           # 5 phép toán => O(5)
    print(num)                  

# O(n^2) - Quadratic Time Complexity - Độ phức tạp bậc hai (vòng lặp lồng nhau)
for i in num_list:          # 5 phép toán => O(5)
    for j in num_list:      # 5 phép toán => O(5)
        print(i, j)         # 25 phép toán => O(25) = O(n^2)

# O(log n) - Logarithmic Time Complexity - Độ phức tạp logarit (tìm kiếm nhị phân)
    # Giống game đoán số (luôn chia đôi khoảng tìm kiếm)