# =============== TẬP HỢP (SET) ===============

# Định nghĩa:
    # Tập hợp (set) là kiểu cấu trúc dữ liệu
    # Không có thứ tự
    # Không chứa phần tử trùng lặp

# Create - Khởi tạo
    # Tạo tập hợp rỗng
set1 = set()
    # Tạo tập hợp có sẵn phần tử
set2 = {1, 2, 3, 4, 5}

# Các thao tác cơ bản
    # Thêm phần tử: add()
set2.add(6)  

    # Xóa phần tử: 
        # remove() - nếu không có phần tử sẽ báo lỗi
set2.remove(6)
        # discard() - nếu không có phần tử sẽ không báo lỗi
set2.discard(7)

# Các thao tác khác
set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7, 8}
    # union(): Hợp - trả về tập hợp mới chứa tất cả phần tử từ cả 2 tập hợp
set_union = set3.union(set4)
set_union2 = set3 | set4
print("Union:", set_union)

    # intersection() - Giao: trả về tập hợp chứa phần tử chung
set_intersection = set3.intersection(set4)
set_intersection2 = set3 & set4
print("Intersection:", set_intersection)

    # difference() - Hiệu: trả về tập hợp chứa phần tử chỉ có trong tập hợp đầu tiên
set_difference = set3.difference(set4)
set_difference2 = set3 - set4
print("Difference:", set_difference)

# Duyệt phần tử
for item in set3:
    print("Item:", item)

# Kiểm tra phần tử có nằm trong tập hợp không
print("3 in set3:", 3 in set3)      # True
print("99 in set3:", 99 in set3)    # False

# =============== LUYỆN TẬP SET ===============
# Bài Tập 1: Tạo Tập Hợp Và Thực Hiện Các Thao Tác
# Yêu cầu: Tạo hai tập hợp A = {1, 2, 3, 4, 5} và B = {4, 5, 6, 7, 8}. Thực hiện các thao tác sau:
# 	1. Thêm phần tử 9 vào tập hợp A.
# 	2. Xóa phần tử 4 khỏi tập hợp B.
# 	3. Tìm hợp, giao, hiệu của hai tập hợp A và B.

# Bài Tập 2: Kiểm Tra Tập Hợp
# Yêu cầu: Cho tập hợp C = {'apple', 'banana', 'cherry'}. 
# Kiểm tra xem 'banana' và 'grape' có trong tập hợp không.