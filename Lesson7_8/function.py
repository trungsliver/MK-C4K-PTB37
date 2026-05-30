# Fuction - Hàm / chương trình con

# 1. No parameter, no return value - Không tham số, không giá trị trả về
def say_hello():
    print('Hello Nam!')
    print('Hello Trung!')
# say_hello()

# 2. Parameter, no return value - Có tham số, không giá trị trả về
def say_hello_2(name):
    print(f'Hello {name}!')
say_hello_2('Đăng')
say_hello_2('Linh')

# 3. Parameter, return value - Có tham số, có giá trị trả về
def perimeter_rectangle(length, width):
    return 2 * (length + width)
result = perimeter_rectangle(5, 3)
print('Result:', result)

# Bonus:
    # Default parameter - Tham số mặc định
def greet(name='MindX'):
    print(f'Hello {name}!')
greet()                 # Sử dụng tham số mặc định
greet('MK-C4K-PTB37')   # Ghi đè tham số mặc định

    # Type of parameter - Kiểu dữ liệu của tham số
def area_rectangle(length: float, width: float) -> float:
    return length * width