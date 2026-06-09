# =================== LUYỆN TẬP ===================
# Bài 1: Viết một hàm sum_odd(numbers) để tính tổng các số lẻ trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về tổng các số lẻ trong danh sách đó.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def sum_odd(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total

# Bài 2: Viết một hàm is_prime(n) để kiểm tra xem một số nguyên dương n có phải là số nguyên tố hay không.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về True nếu n là số nguyên tố, ngược lại trả về False.
#   YC3: In ra các số nguyên tố trong khoảng [10,100].

def is_prime(n:int):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False
print('5 is prime:', is_prime(5))
print('9 is prime:', is_prime(9))


# Bài 3: Viết một hàm count_words(s) để đếm số lượng từ trong một chuỗi s.
# 	YC1: Hàm nhận vào một chuỗi ký tự s.
# 	YC2: Hàm trả về số lượng từ trong chuỗi đó.
str1 = 'This is a sample string with several words.'
def count_words(s:str):
    words = s.strip().split()
    return len(words)
print('Number of words in the string:', count_words(str1))

# Bài 4: Viết một hàm sum_of_digits(n) để tính tổng các chữ số của một số nguyên dương n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về tổng các chữ số của n.
def sum_of_digits(n:int):
    total = 0
    while n > 0:
        digit = n % 10  # Lấy chữ số cuối cùng của n
        total += digit  # Cộng chữ số cuối cùng vào tổng
        n //= 10        # Loại bỏ chữ số cuối cùng khỏi n
    return total
print('Sum of digits in 123:', sum_of_digits(123))
print('Sum of digits in 12345:', sum_of_digits(12345))

# Bài 5: Viết một hàm find_max(numbers) để tìm vị trí số lớn nhất trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về vị trí số lớn nhất trong danh sách đó.
numbers = [1, 2, 3, 4, 999, 5, 6, 7, 8, 9]
def find_max(numbers):
    max_value = max(numbers)            # Tìm giá trị của phần tử lớn nhất
    for i in range(len(numbers)):
        if numbers[i] == max_value:     # Kiểm tra nếu phần tử tại vị trí i là phần tử lớn nhất
            return i                    # Trả về vị trí của phần tử lớn nhất
print('Position of the largest number:', find_max(numbers))

# Bài 6: Viết một hàm sum_to_n(n) để tính tổng các số từ 1 đến n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	Yc2: Hàm trả về tổng các số từ 1 đến n.
def sum_to_n(n:int):
    sum = 0
    for i in range(1, n+1):  # Duyệt số từ 1 đến n
        sum = sum + i        # Tính tổng các số từ 1 đến n
    return sum
print('Tổng các số từ 1 đến 10:', sum_to_n(10))

# Bài 7: Nhập vào từ bàn phím 1 chuỗi ký tự bao gồm các số nguyên, các số này cách nhau 1 khoảng trắng (hoặc dấu ,).
str1 = '1,2,3,4,5,6,7,8,9,10,11'
#   YC1: Tách chuỗi và thêm vào danh sách có tên num_list
num_list = str1.split(',')
#   YC2: Chuyển đổi toàn bộ phần tử trong danh sách num_list thành kiểu dữ liệu int.
num_list = [int(num) for num in num_list]
print(num_list)
#   YC3: In ra màn hình số lượng số lẻ của num_list.
count_odd = 0
for num in num_list:
    if num % 2 != 0:
        count_odd += 1
print('Số lượng số lẻ:', count_odd)
#   YC4: In ra màn hỉnh tổng các số chẵn của num_list.
total_even = 0
for num in num_list:
    if num % 2 == 0:
        total_even += num
print('Tổng các số chẵn:', total_even)

# Bài 8: Dùng thư viên random để thêm ngẫu nhiên các số nguyên trong khoảng [20,50] vào 2 danh sách arr1 và arr2. 
import random
arr1 = [random.randint(20, 50) for i in range(10)]
arr2 = [random.randint(20, 50) for i in range(10)]

#   YC1: Hãy viết hàm/chương trình con in ra phần tử chung của 2 danh sách vừa tạo.
def find_common_elements(arr1, arr2):
    common = []
    for num in arr1:
        if (num in arr2) and (num not in common):
            common.append(num)
    return common
print('Phần tử chung của arr1 và arr2:', find_common_elements(arr1, arr2))

#   YC2: In ra màn hình vị trí phần tử nhỏ nhất của danh sách arr1
min_value = min(arr1)            # Tìm giá trị của phần tử nhỏ nhất
for i in range(len(arr1)):
    if arr1[i] == min_value:     # Kiểm tra nếu phần tử tại vị trí i là phần tử nhỏ nhất
        print('Vị trí phần tử nhỏ nhất của arr1:', i)  # In ra vị trí của phần tử nhỏ nhất
        break  # Dừng vòng lặp sau khi tìm thấy phần tử nhỏ nhất đầu tiên

#   YC3: In ra màn hình vị trí phần tử lớn nhất của danh sách arr2
max_value = max(arr2)            # Tìm giá trị của phần tử lớn nhất
for i in range(len(arr2)):
    if arr2[i] == max_value:     # Kiểm tra nếu phần tử tại vị trí i là phần tử lớn nhất
        print('Vị trí phần tử lớn nhất của arr2:', i)  # In ra vị trí của phần tử lớn nhất
        break  # Dừng vòng lặp sau khi tìm thấy phần tử lớn nhất đầu tiên

# Bài 9: Hãy nhập từ bàn phím họ tên của bạn (viết hoa lộn xộn).
# Yêu cầu: Viết một hàm chuẩn hóa họ tên, nghĩa là viết hoa chữ cái đầu của mỗi từ và các chữ cái còn lại viết thường, xóa các khoảng trắng thừa.
name = '   bUi    dUC    TRuNg   '
def normalize_name(name:str):
    # Xóa khoảng trắng thừa ở đầu và cuối chuỗi
    name = name.strip()  
    # Tách chuỗi thành các từ dựa trên khoảng trắng
    words = name.split()  
    # Viết hoa chữ cái đầu và viết thường các chữ cái còn lại
    normalized_words = [word.capitalize() for word in words] 
    # Nối các từ đã chuẩn hóa thành một chuỗi 
    normalized_name = ' '.join(normalized_words)  
    return normalized_name
print('Tên đã chuẩn hóa:', normalize_name(name))

# Bài 10: Nhập số nguyên a và b (1 <= a < b <= 9)
# Yêu cầu: In ra tất cả các bảng cửu chương từ a đến b
a, b = 2, 5
for i in range(a, b+1):
    print(f'\nBảng cửu chương {i}:')
    for j in range(1, 10):
        print(f'{i} x {j} = {i*j}')

# Bài 11: Nhập n là số giây cần chuyển đổi (số nguyên)
#   In ra màn hình dạng h-m-s
#   Ví dụ: 3661s = 1h 1p 1s
n = 9961
hours = n // 3600  # Tính số giờ
minutes = (n % 3600) // 60  # Tính số phút còn lại sau khi trừ đi số giờ
seconds = n % 60  # Tính số giây còn lại

print(f'{n}s = {hours}h {minutes}p {seconds}s')

# Bài 12:
#   YC1: Tạo danh sách bao gồm 10 số nguyên ngẫu nhiên trong khoảng [1,100]
num_list = [random.randint(1, 100) for _ in range(10)]

#   YC2: Thêm số '-5' vào vị trí thứ 2 (index=2) trong danh sách
num_list.insert(2, -5)

#   YC3: Tính tổng các số chẵn trong danh sách
total_even = 0
for num in num_list:
    if num % 2 == 0:
        total_even += num
print('Tổng các số chẵn trong danh sách:', total_even)

#   YC4: Đếm số lượng số lẻ có trong danh sách
count_odd = 0
for num in num_list:
    if num % 2 != 0:
        count_odd += 1
print('Số lượng số lẻ trong danh sách:', count_odd)

#   YC5: Tìm giá trị phần tử lớn nhất của danh sách
max_value = max(num_list)
print('Giá trị phần tử lớn nhất trong danh sách:', max_value)

#   YC6: Tìm vị trí phần tử nhỏ nhất của danh sách
min_value = min(num_list)
for i in range(len(num_list)):
    if num_list[i] == min_value:
        print('Vị trí phần tử nhỏ nhất trong danh sách:', i)
        break
#   YC7: Viết hàm tính giá trị trung bình của các phần tử trong danh sách (làm tròn đến 2 chữ số thập phân)
def calculate_average(num_list):
    if len(num_list) == 0:
        return 0
    total = 0
    for num in num_list:
        total += num
    average = total / len(num_list)
    return round(average, 2)

#   YC8: Sắp xếp các phần tử trong danh sách theo thứ tự từ lớn đến nhỏ
num_list.sort(reverse=True)
print('Danh sách sau khi sắp xếp từ lớn đến nhỏ:', num_list)

