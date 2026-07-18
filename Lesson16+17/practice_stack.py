# Bài 1: Tạo Stack và thực hiện push/pop
# Yêu cầu:
# 	- Tạo Stack
stack = []
# 	- Thêm các số: 1, 2, 3
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack after pushes:", stack)
# 	- Lấy ra 1 phần tử
popped_element = stack.pop()
print("Popped element:", popped_element)
# 	- In Stack
print("Current stack:", stack)

# Bài 2: Đảo ngược chuỗi bằng Stack
# Yêu cầu:
# 	- Nhập chuỗi "python"
# 	- Dùng Stack để đảo ngược
input_string = "python"
stack = []

for char in input_string:
    stack.append(char)

reversed_string = ""
while len(stack) > 0:
    reversed_string += stack.pop()

print("Reversed string:", reversed_string)

# Bài 3: Kiểm tra dấu ngoặc hợp lệ
# Chuỗi được gọi là hợp lệ nếu:
#     	1. Các dấu ngoặc mở và ngoặc đóng khớp với nhau đúng thứ tự: () [] {}
#     	2. Mỗi dấu ngoặc mở phải có dấu ngoặc đóng tương ứng
# Gợi ý:
#     	- Dùng stack để lưu các dấu ngoặc mở.
#     	- Khi gặp dấu ngoặc đóng, kiểm tra xem nó có khớp với dấu ngoặc mở trên cùng của stack không.
def is_valid_parentheses(input:str):
    stack = []
    for char in input:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if len(stack) == 0:
                return False
            top = stack.pop()
    return len(stack) == 0

str1 = "([]){}"     # Hợp lệ
str2 = "([))]"      # Không hợp lệ
str3 = ")([]"       # Không hợp lệ
print(f"{str1} is valid: {is_valid_parentheses(str1)}")
print(f"{str2} is valid: {is_valid_parentheses(str2)}")
print(f"{str3} is valid: {is_valid_parentheses(str3)}")


# Bài 4: Đóng vai trò là 1 lập trình viên xây dựng ứng dụng web đơn giản. Hãy phát triển 2 chức năng:
# 	- Back: quay lại trang web trước đó
# 	- Forward: tiến tới trang web bạn vừa quay lại
# Yêu cầu: xây dựng lớp Browser có 3 phương thức (visit_page, back, forward)
# Gợi ý: sử dụng 2 stack để lưu lịch sử back và lịch sử forward

class Browser:
    # Hàm khởi tạo
    def __init__(self):
        # Stack lưu lịch sử web đã truy cập
        self.back_stack = []
        # Stack lưu lịch sử web đã quay lại
        self.forward_stack = []

    # Phương thức truy cập website mới
    def visit_page(self, url):
        self.back_stack.append(url)
        self.forward_stack.clear()  # Xóa lịch sử forward khi truy cập trang mới
        print(f"Visited: {url}")

    # Phương thức quay lại trang trước đó
    def back(self):
        if len(self.back_stack) > 1:
            current_page = self.back_stack.pop()
            self.forward_stack.append(current_page)
            print(f"Going back to: {self.back_stack[-1]}")
        else:
            print("No previous page to go back to.")

    # Phương thức tiến tới trang đã quay lại
    def forward(self):
        if len(self.forward_stack) > 0:
            next_page = self.forward_stack.pop()
            self.back_stack.append(next_page)
            print(f"Going forward to: {next_page}")
        else:
            print("No forward page to go to.")

# Testing
    # Khởi tạo browser
browser = Browser()

    # Truy cập các trang web
browser.visit_page("www.google.com")
browser.visit_page("www.facebook.com")
browser.visit_page("www.youtube.com")
browser.visit_page("www.github.com")

    # Quay lại 2 trang
browser.back()
browser.back()

    # Tiến tới 1 trang
browser.forward()
browser.forward()
browser.forward()  # Thử tiến tới khi không có trang forward