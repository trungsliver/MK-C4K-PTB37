# ================== QUEUE - Hàng đợi ==================

# Khái niệm: cấu trúc dữ liệu
# Nguyên tắc hoạt động: FIFO (First In First Out) - Vào trước ra trước
# Ví dụ:
    # Xếp hàng đợi thanh toán trong siêu thị
    # Hàng đợi in tài liệu
    # Xe xếp hàng qua trạm thu phí

# Các thao tác cơ bản:
    # Khởi tạo:
        # Cách 1:
queue1 = []
        # Cách 2:
from collections import deque
queue2 = deque()

    # enqueue (thêm phần tử vào cuối hàng đợi):
queue1.append('A')  
queue1.append('B')  
print("Queue1 sau khi enqueue:", queue1)

queue2.append('A')  
queue2.append('B')  
print("Queue2 sau khi enqueue:", queue2)

    # dequeue (loại bỏ phần tử ở đầu hàng đợi):
        # Cách 1: tốn thời gian vì phải dịch chuyển các phần tử còn lại
item1 = queue1.pop(0)  
print("Phần tử dequeue từ Queue1:", item1)

        # Cách 2: hiệu quả hơn với deque
item2 = queue2.popleft()
print("Phần tử dequeue từ Queue2:", item2)
print("Queue2 sau khi dequeue:", queue2)

    # peek (xem phần tử ở đầu hàng đợi mà không loại bỏ nó):
front_item1 = queue1[0]
print("Phần tử ở đầu Queue1 (peek):", front_item1)
front_item2 = queue2[0]
print("Phần tử ở đầu Queue2 (peek):", front_item2)

    # is_empty (kiểm tra hàng đợi có rỗng không):
def is_empty(queue):
    if len(queue) == 0:
        return True
    else:
        return False
    
# Ví dụ: Xếp hàng mua đồ siêu thị
    # Khởi tạo hàng đợi
line_queue = deque()
    # Thêm khách hàng vào hàng đợi
line_queue.append("Minh Anh")
line_queue.append("Thu Hương")
line_queue.append("Lâm Khánh")
line_queue.append("Duy Anh")
line_queue.append("Tuấn Linh")
    # Hiển thị danh sách người xếp hàng
print("Danh sách người xếp hàng:", list(line_queue))
    # Phục vụ khách hàng theo thứ tự xếp hàng
while not is_empty(line_queue):
    current_customer = line_queue.popleft()
    print("\nPhục vụ khách hàng:", current_customer)
    # Hiển thị danh sách người xếp hàng còn lại
    print("Người xếp hàng còn lại:", list(line_queue))
print('Tất cả khách hàng đã được phục vụ.')
