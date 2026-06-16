# Bài 1: Tạo lớp Rectangle với các thuộc tính: length, width.  
# Tạo phương thức tính diện tích và chu vi của hình chữ nhật. 
class Rectangle:
    # Hàm khởi tạo
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Phương thức tính chu vi
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    # Phương thức tính diện tích
    def area(self):
        return self.length * self.width
    
hcn1 = Rectangle(5, 3)
print(f"Chu vi hình chữ nhật 1: {hcn1.perimeter()}")
print(f"Diện tích hình chữ nhật 1: {hcn1.area()}")

hc2 = Rectangle(10, 4)
print(f"Chu vi hình chữ nhật 2: {hc2.perimeter()}")
print(f"Diện tích hình chữ nhật 2: {hc2.area()}")

# Bài 2: Tạo lớp BankAccount với các thuộc tính: 
            # account_number: số tài khoản 
            # owner: tên chủ tài khoản
            # balance: số dư tài khoản
    # Tạo phương thức:
            # deposit(amount): nạp tiền vào tài khoản
            # withdraw(amount): rút tiền từ tài khoản
            # display_balance(): hiển thị số dư tài khoản
            # (amount: số tiền nạp/rút theo đơn vị $)

class BankAccount:
    # Hàm khởi tạo
    def __init__(self, account_number, owner, balance):
        # Số tài khoản
        self.account_number = account_number
        # Tên chủ tài khoản
        self.owner = owner
        # Số dư tài khoản
        self.balance = balance

    # Phương thức hiển thị số dư tài khoản
    def display_balance(self):
        print(f'''
========== SỐ DƯ TÀI KHOẢN ==========
Số tài khoản: {self.account_number}
Chủ tài khoản: {self.owner}
Số dư: ${self.balance}
=====================================
''')
        
    # Phương thức nạp tiền
    def deposit(self, amount):
        # amount: số tiền nạp vào tài khoản
        if amount > 0:
            # Cộng tiền vào số dư tài khoản
            self.balance += amount
            # Thông báo nạp tiền thành công
            print(f"Nạp thành công ${amount}!")
        else:
            # Thông báo nạp tiền thất bại
            print("Số tiền nạp vào phải lớn hơn 0.")
        # Hiển thị số dư tài khoản sau khi nạp tiền
        self.display_balance()  

    # Phương thức rút tiền
    def withdraw(self, amount):
        # amount: số tiền rút từ tài khoản
        if amount > 0 and amount <= self.balance:
            # Trừ tiền từ số dư tài khoản
            self.balance -= amount
            # Thông báo rút tiền thành công
            print(f"Rút thành công ${amount}!")
        else:
            # Thông báo rút tiền thất bại
            print("Số tiền rút không hợp lệ!")
        # Hiển thị số dư tài khoản sau khi rút tiền
        self.display_balance()

account1 = BankAccount("123456789", "Hải Nam", 1000)
account1.display_balance()
account1.deposit(500)           # Số dư: $1500
account1.deposit(-200)          # Số dư: $1500 (nạp thất bại)
account1.withdraw(1200)         # Số dư: $300
account1.withdraw(500)          # Số dư: $300 (rút thất bại)