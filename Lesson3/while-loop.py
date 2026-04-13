# =============== While Loop ===============
# Vòng lặp vô hạn - không biết trước số lần lặp

# Ví dụ: In ra các số từ 0 đến 5
for i in range(6):
    print(i, end=' ')

i = 0
while i < 6:
    print(i, end=' ')
    i += 1  

# Các lệnh thoát khỏi vòng lặp:
    # break: thoát khỏi vòng lặp, bỏ qua tất cả các lần lặp còn lại
    # continue: bỏ qua lần lặp hiện tại, tiếp tục với lần lặp tiếp theo

print("\nSử dụng break:")
for i in range(10):
    if i == 5:
        break
    print(i, end=' ')

print("\nSử dụng continue:")
for i in range(10):
    if i == 5:
        continue
    print(i, end=' ')

# ============== Bài tập ===============
# Bài 1: Nhập số nguyên n trong khoảng [0,100]
# nếu nhập sai (n<0 hoặc n>100) thì yêu cầu nhập lại 
n = int(input("\nNhập số nguyên n trong khoảng [0,100]: "))
while n < 0 or n > 100:
    print('Bạn đã nhập sai, vui lòng nhập lại!')
    n = int(input("Nhập số nguyên n trong khoảng [0,100]: "))
print('Bạn đã nhập đúng.')

#  Bài 2: Tạo Mysterious Game
    # Yêu cầu: tạo ra 1 số đặc biệt để đoán (random) trong khoảng [0,100]
    # Người chơi cần nhập đến khi nào đoán đúng số đặc biệt thì dừng game
    # Nếu người chơi đoán sai, có gợi ý (số cần tìm lớn hơn / nhỏ hơn)
    # Đếm sỗ lần người chơi đoán đến khi chiến thắng

import random
number = random.randint(0, 100)
guess = int(input("Đoán số đặc biệt (0-100): "))
count = 1
while guess != number:
    if guess < number:
        print("Số cần tìm lớn hơn.")
    else:        
        print("Số cần tìm nhỏ hơn.")
    count += 1
    guess = int(input("\nĐoán số đặc biệt (0-100): "))
print(f"Bạn đã đoán đúng sau {count} lần đoán!")