# Display info - Hiển thị thông tin
print('Hello world!')

# Variables - Biến số
    # Lưu trữ thông tin (store data)
    # Có thể thay đổi được (changeable)
name = 'Duc Trung'
age = 2

# 4 ways to display - 4 cách hiển thị
    # 1. Concatenation - Nối chuỗi (dùng dấu +)
print('Name: ' + name)
print('Age: ' + str(age)) 

    # 2. Comma - Dấu phẩy (dùng dấu ,)
print('Name:', name)
print('Age:', age)

    # 3. String Formatting - Định dạng chuỗi (dùng dấu {})
print(f'Name: {name}. Age: {age}.')

    # 4. Multi-line Display - Hiển thị nhiều dòng 
print(f'''
Name: {name}
Age: {age}''')

# Lưu ý: 
    # Dấu xuống dòng (newline) - \n
print('line1\nline2\nline3')
    # Dấu tab (tab) - \t
print('text1\ttext2\ttext3')