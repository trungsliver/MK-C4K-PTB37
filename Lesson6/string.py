# Strings - chuỗi / xâu ký tự
name = 'Hai Nam'

# Độ dài string - len()
print('length of name ', len(name))

# Truy cập từng ký tự trong string (duyệt string)
    # Truy cập theo index
print('name[0]:', name[0]) 
print('name[1]:', name[1]) 
print('name[2]:', name[-1]) 

    # Duyệt string
        # cách 1: Dùng cả index và value
for i in range(len(name)):
    print(f'name[{i}] = {name[i]}')

        # cách 2: Dùng value
for char in name:
    print(f'char = {char}')

# Xâu con (substring)
str1 = 'Ho Hai Nam'
str2 = 'Hai Nam'
str3 = 'vui vẻ'

    # Kiểm tra xâu con: in
print('str2 in str1:', str2 in str1)
print('str3 in str1:', str3 in str1)

    # Tìm vị trí xâu con: find() => index
print('str1.find(str2):', str1.find(str2))
print('str1.find(str3):', str1.find(str3))

# Cắt string: slicing()
name = 'hahahihihuhu'
    # cắt ở vị trí trí bất kì [start:end:step]
print('name[4:8]:', name[4:8])
    # cắt từ đầu string đến vị trí bất kì [:end]
print('name[:4]:', name[:4])
    # cắt từ vị trí bất kì đến cuối string [start:]
print('name[8:]:', name[8:])

# Tách string: split()
    # Mặc định tách khi gặp khoảng trắng
str1 = '1 2 3 4 5 6 7 8 9'
arr1 = str1.split()
print('arr1:', arr1)

    # Tách khi gặp ký tự bất kì
str2 = 'a,b,c,d,e,f,g,h,i'
arr2 = str2.split(',')
print('arr2:', arr2)

# Xóa khoảng trắng ở đầu và cuối string: strip()
name = '    Hai Nam     '
print('name:', name)
print('name.strip():', name.strip())

# Thay thế substring: replace()
song = 'baby shark doo doo doo doo doo doo'
    # Thay thế toàn bộ
song1 = song.replace('doo', 'nam')
print('song1:', song1)
    # Thay thế một phần
song2 = song.replace('doo', 'nam', 3)
print('song2:', song2)

# Kết hợp chuỗi - join
arr = ['r','o','n','a','l','d','o']
str1 = ''.join(arr)
print('str1:', str1)
str2 = '-'.join(arr)
print('str2:', str2)
str3 = ' '.join(arr)
print('str3:', str3)

# Viết hoa, viết thường
name = 'hO hAi NaM'
    # Viết hoa tất cả - upper()
print('name.upper():', name.upper())
    # Viết thường tất cả - lower()
print('name.lower():', name.lower())
    # Viết hoa chữ cái đầu của mỗi từ - title()
print('name.title():', name.title())

# Ví dụ: x - tên gốc, y - input tìm kiếm
x = 'MindX Technology School'
y = 'mindx'
print('x == y:', x == y)
print('y.lower() in x.lower():', y.lower() in x.lower())

# Chuyển đổi kiểu dữ liệu danh sách
arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # string
    # cách 1: 
numList1 = []
for item in arr:
    newItem = int(item)
    numList1.append(newItem)
print('numList1:', numList1)
    # cách 2: 
numList2 = [int(item) for item in arr]
print('numList2:', numList2)

# Tính tổng phần tử danh sách
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Cách cũ:
total = 0
for item in arr:
    total += item   
print('total:', total)
    # Cách mới:
total2 = sum(item for item in arr)

# Đếm số lượng số lẻ trong danh sách
    # cách cũ:
count = 0
for item in arr:
    if item % 2 != 0:
        count += 1
print('count:', count)
    # cách mới:
count2 = sum(1 for item in arr if item % 2 != 0)
print('count2:', count2)