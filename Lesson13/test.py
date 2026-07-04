#  Đề bài: Tạo Mysterious Game
    # Yêu cầu: tạo ra 1 số đặc biệt để đoán (random)
    # Người chơi cần nhập đến khi nào đoán đúng số đặc biệt thì dừng game

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