# =========== SEARCH ALGORITHMS - THUẬT TOÁN TÌM KIẾM ===========

num_list = [2, 5, 3, 1, 9, 7, 4, 8, 6]

# ĐÊ BÀI: Tìm kiếm vị trí của phần tử có giá trị = 7
for i in range(len(num_list)):
    if num_list[i] == 7:
        print(f"Phần tử 7 nằm ở vị trí {i}")
        break

# Linear Search - Tìm kiếm tuyến tính / tuần tự (O(n))
def linear_search(array, target):
    # Duyệt từng phần tử trong danh sách
    for i in range(len(array)):       # O(n)
        if array[i] == target:
            return i                  # Trả về vị trí tìm thấy
    return -1                         # Nếu không tìm thấy, trả về -1

    # test linear_search
result = linear_search(num_list, 7)
if result != -1:
    print(f"Phần tử 7 nằm ở vị trí {result}")
else:
    print("Không tìm thấy phần tử 7 trong danh sách.")

# Binary search - tìm kiếm nhị phân (danh sách phải được sắp xếp trước)
def binary_search(array, target):
    # left, right là chỉ số index bắt đầu và kết thúc của danh sách
    left = 0 
    right = len(array) - 1

    while left <= right:               # O(log n)
        # Tìm chỉ số index ở giữa
        mid = (left + right) // 2
        # So sánh phần tử ở giữa với target
        if array[mid] == target:
            return mid                 # Trả về vị trí tìm thấy
        elif array[mid] < target:
            left = mid + 1             # Tìm bên phải
        else:
            right = mid - 1            # Tìm bên trái
    return -1                         # Nếu không tìm thấy, trả về -1

    # test binary search
sorted_arr = sorted(num_list)  # Sắp xếp mảng trước khi tìm kiếm
result = binary_search(sorted_arr, 7)
if result != -1:
    print("Phần tử 7 nằm ở vị trí:", result)
else:
    print("Phần tử 7 không được tìm thấy")

# ===================== SO SÁNH HIỆU SUÂT =========================
import time, random

def measure_time(search_function, array, target):
    # Thời gian bắt đầu
    start_time = time.time()
    # Thực hiện tìm kiếm
    search_function(array, target)
    # Thời gian kết thúc
    end_time = time.time()
    # Trả về thời gian thực hiện
    return end_time - start_time

# Khởi tạo danh sách 
random_list = [random.randint(0, 500000000) for _ in range(500000000)]
target_value = random.choice(random_list)

# Linear search
linear_time = measure_time(linear_search, random_list, target_value)
print(f"Thời gian tìm kiếm tuyến tính: {linear_time:.8f} giây")

# Binary search
sorted_random_list = sorted(random_list)
binary_time = measure_time(binary_search, sorted_random_list, target_value)
print(f"Thời gian tìm kiếm nhị phân: {binary_time:.8f} giây")