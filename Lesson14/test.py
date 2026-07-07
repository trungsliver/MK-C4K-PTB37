import sort

# Ví dụ sử dụng
sort.bubble_sort([64, 25, 12, 22, 11, 90, 34, 78, 56, 43])

# ============= LUYỆN TẬP =============
# Bài 1: So sánh tốc độ 3 thuật toán sắp xếp vừa học với mảng có kích thước lớn
import time
import random

def measure_time(sort_function, array):
    # Thời gian bắt đầu
    start_time = time.time()
    # Thực hiện tìm kiếm
    sort_function(array)
    # Thời gian kết thúc
    end_time = time.time()
    # Trả về thời gian thực hiện
    return end_time - start_time

# Khởi tạo danh sách lớn
random_list = [random.randint(1, 20000000) for _ in range(5000)]

# Test 5 lần 
n = 5
sum_bubble = 0
sum_selection = 0
sum_insertion = 0
for i in range(n):
    print(f"\nLần thử nghiệm thứ {i + 1}:")

    # Đo thời gian sắp xếp với bubble sort
    time_bubble = measure_time(sort.bubble_sort, random_list.copy())
    # print(f"Thời gian sắp xếp với Bubble Sort: {time_bubble} giây")
    sum_bubble += time_bubble

    # Đo thời gian sắp xếp với selection sort
    time_selection = measure_time(sort.selection_sort, random_list.copy())
    # print(f"Thời gian sắp xếp với Selection Sort: {time_selection} giây")
    sum_selection += time_selection

    # Đo thời gian sắp xếp với insertion sort
    time_insertion = measure_time(sort.insertion_sort, random_list.copy())
    # print(f"Thời gian sắp xếp với Insertion Sort: {time_insertion} giây")
    sum_insertion += time_insertion

print("\nKết quả trung bình sau 5 lần thử nghiệm:")
print(f"Thời gian trung bình Bubble Sort: {sum_bubble / n} giây")
print(f"Thời gian trung bình Selection Sort: {sum_selection / n} giây")
print(f"Thời gian trung bình Insertion Sort: {sum_insertion / n} giây")

# Bài 2: Sắp xếp danh sách sản phẩm dạng dictionary (giá giảm dần)
products = [
    {"name": "Sữa", "price": 30},
    {"name": "Bánh quy", "price": 20},
    {"name": "Gạo", "price": 15},
    {"name": "Dầu ăn", "price": 40}
]

def selection_sort_products(products):
    n = len(products)
    for i in range(n - 1):

        min_index = i

        # Tìm sản phẩm có price nhỏ nhất
        for j in range(i + 1, n):
            if products[j]["price"] < products[min_index]["price"]:
                min_index = j
        
        # Đổi chỗ 
        products[i], products[min_index] = products[min_index], products[i]
    return products
# Sắp xếp sản phẩm theo giá giảm dần
sorted_products = selection_sort_products(products)[::-1]
print("\nDanh sách sản phẩm sau khi sắp xếp theo giá giảm dần:")
for product in sorted_products:
    print(f"Tên: {product['name']}, Giá: {product['price']}")