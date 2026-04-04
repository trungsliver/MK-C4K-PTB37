# If - else statement (3 dạng câu điều kiện)
    # Dạng thiếu:
age = 2
if age >= 18:
    print('Bạn đủ tuổi lái xe')

    # Dạng đủ:
num = 10
if num % 2 == 0:
    print(num, 'là số chẵn')
else:
    print(num, 'là số lẻ')

    # Dạng đa nhánh:
score = 8.5
if 8 <= score <= 10:
    print('Học lực: Giỏi')
elif 6.5 <= score < 8:
    print('Học lực: Khá')
elif 5 <= score < 6.5:
    print('Học lực: Trung bình')
elif 0 <= score < 5:
    print('Học lực: Yếu')
else:
    print('Điểm không hợp lệ')

# Switch-case statement
day = 3
match day:
    case 1:
        print('Sunday')
    case 2:
        print('Monday')
    case 3:
        print('Tuesday')
    case 4:
        print('Wednesday')
    case 5:
        print('Thursday')
    case 6:
        print('Friday')
    case 7:
        print('Saturday')
    case _: # default case
        print('Day is not valid')