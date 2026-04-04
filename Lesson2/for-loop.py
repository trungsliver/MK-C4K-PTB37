# ================= For Loops =================
# Vòng lặp hữu hạn - biết trước số lần lặp

# Cú pháp đầy đủ: range(start, stop, step)
    # start: số bắt đầu (không bắt buộc, default = 0)
    # stop: số kết thúc (bắt buộc)
    # step: bước nhảy (không bắt buộc, default = 1)
# Lưu ý: chạy từ start đến stop-1 (không bao gồm stop)

# TH1: range(start, stop, step)
for i in range(1, 10, 2):
    print(i)
    print('Hai Nam')

# TH2: range(start, stop)
for i in range(1, 10):
    print(i)

# TH3: range(stop)
for i in range(10):
    print(i)

# =============== ví dụ =============
# Ví dụ:
# range(5,10): 5 -> 9
# range(2, 10, 2): 2,4,6,8
# range(-5): không chạy
# range(-10, -5): -10 -> -6
# range(1): 0
# range(2,8,3): 2, 5
# range(2): 0,1
# range(-5, 2): -5, 1

# Bài 1: Nhập 2 số nguyên a và b từ bàn phím.
# In ra các số nguyên trong khoảng [a, b]
a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
print(f'Các số trong khoảng [{a}, {b}] là:')
for i in range(a, b+1):
    print(i, end = ' ')

# Bài 2: Nhập 2 số nguyên a và b từ bàn phím.
# In ra các số nguyên trong khoảng [a, b] nếu b >= a
# In ra các số nguyên trong khoảng [b, a] nếu a > b
a = int(input('Nhập a: '))
b = int(input('Nhập b: '))

if b >= a:
    print(f'Các số trong khoảng [{a}, {b}] là:')
    for i in range(a, b+1):
        print(i, end = ' ')
else:
    print(f'Các số trong khoảng [{b}, {a}] là:')
    for i in range(b, a+1):
        print(i, end = ' ')

# Bài 3: Nhập 1 số nguyên a trong khoảng [1, 10]
# In ra màn hình bảng cửu chương a b
a = int(input('Nhập a (1-10): '))
print(f'Bảng cửu chương {a}:')
for i in range(1, 11):
    print(f'{a} x {i} = {a*i}'  )

# Bài 4: In ra màn hình bảng cửu chương từ 2 => 9
for a in range(2,10):
    print(f'\nBảng cửu chương {a}:')
    for i in range(1, 11):
        print(f'{a} x {i} = {a * i}')