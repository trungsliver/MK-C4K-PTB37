#  ================ STACK - NGĂN XẾP ================

# Khái niệm: cấu trúc dữ liệu
# Nguyên tắc hoạt động: LIFO (Last In First Out) - Vào sau ra trước
# Ví dụ: 
    # Xếp đĩa chồng lên nhau
    # Chồng sách đặt trên bàn
    # Lịch sử trình duyệt (khi ấn nút back)

# Các thao tác cơ bản: 
    # Khởi tạo stack
stack = []

    # push/append: thêm phần tử vào đỉnh stack
stack.append(1)
stack.append(2) 
stack.append(3)
print(stack)

    # pop: loại bỏ phần tử ở đỉnh stack và trả về phần tử đó
top_element = stack.pop()
print("Popped element:", top_element)
print(stack)

    # peek:xem phần tử ở đỉnh stack (không xóa)
top_element = stack[-1]
print("Top element (peek):", top_element)

    # is_empty: kiểm tra stack có rỗng không
def is_empty(stack):
    if len(stack) == 0:
        return True
    else:
        return False
print("Is stack empty?", is_empty(stack))