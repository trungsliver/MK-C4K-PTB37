# ================== For loop Practice ==================
# Dạng 1: In / Hiển thị ra màn hình
    # 1.1. In ra màn hình các số từ 0 đến n
n = int(input('Nhập n: '))
for i in range(n + 1):
    print(i, end=' ')

    # 1.2. In ra màn hình các số trong khoảng [a, b]
a = int(input('\nNhập a: '))
b = int(input('Nhập b: '))
for i in range(a, b + 1):
    print(i, end=' ')

    # 1.3. In ra các số chẵn trong khoảng [a, b]
a = int(input('\nNhập a: '))
b = int(input('Nhập b: '))
print("\nCác số chẵn trong khoảng [a, b]:")
for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end=' ')

    # 1.4. In ra các số lẻ trong khoảng [a, b]
a = int(input('\nNhập a: '))
b = int(input('Nhập b: '))
print("\nCác số lẻ trong khoảng [a, b]:")
for i in range(a, b + 1):
    if i % 2 != 0:
        print(i, end = ' ')

# Dạng 2: Tính tổng
    # 2.1. Tính tổng các số trong khoảng [a, b]
a = int(input('\nNhập a: '))
b = int(input('Nhập b: '))
total = 0
for i in range(a, b + 1):
    total += i
print(f"Tổng các số trong khoảng [{a}, {b}] là: {total}")

    # 2.2. Tính tổng các số chẵn trong khoảng [a, b]
a = int(input('\nNhập số nguyên a: '))
b = int(input('Nhập số nguyên b: '))
sum = 0
for i in range(a, b+1):
    if i % 2 == 0:
        sum += i    # sum = sum + i
print(f'Tổng các số chẵn trong khoảng [{a},{b}] là: {sum}')

    # 2.3. Tính tổng các số dương (> 0) trong khoảng [a, b]
a = int(input('\nNhập số nguyên a: '))
b = int(input('Nhập số nguyên b: '))
sum = 0
for i in range(a, b+1):
    if i > 0:
        sum += i    # sum = sum + i
print(f'Tổng các số dương trong khoảng [{a},{b}] là: {sum}')

# Dạng 3: Đếm số lượng 
    # 3.1. Đếm số lượng số chẵn trong khoảng [a, b]
a = int(input('\nNhập số nguyên a: '))
b = int(input('Nhập số nguyên b: '))
count = 0
for i in range(a, b+1):
    if i % 2 == 0:
        count += 1    # count = count + 1
print(f'Số lượng số chẵn trong khoảng [{a},{b}] là: {count}')

    # 3.2. Đếm số lượng số chia hết cho 5 trong khoảng [a,b]
a = int(input('\nNhập số nguyên a: '))
b = int(input('Nhập số nguyên b: '))
count = 0
for i in range(a, b+1):
        if i % 5 == 0:
            count += 1
print(f'Số lượng số chia hết cho 5 trong khoảng [{a},{b}] là: {count}')