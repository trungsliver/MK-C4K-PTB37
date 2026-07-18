# Bài 1: Tạo Queue đơn giản
# Yêu cầu:
# 	- Tạo Queue
queue = []
# 	- Thêm các số: 10, 20, 30
queue.append(10)
queue.append(20)
queue.append(30)
# 	- Lấy ra 1 phần tử
item = queue.pop(0)
print("Phần tử lấy ra từ Queue:", item)
# 	- In Queue
print("Queue hiện tại:", queue)

# Bài 2: Mô phỏng hàng đợi học sinh xếp hàng ở canteen
# Yêu cầu:
# 	- Danh sách học sinh: ["Nam", "Lan", "Minh"]
students_queue = ["Nam", "Lan", "Minh"]
# 	- Phục vụ từng học sinh theo thứ tự
while len(students_queue) > 0:
    served_student = students_queue.pop(0)
    print("Phục vụ học sinh:", served_student)
    print("Học sinh còn lại trong hàng đợi:", students_queue)

# Bài 3: Mô phỏng máy in (Printer Queue)
# Yêu cầu:
# 	- Có danh sách tài liệu cần in
printer_queue = ["doc1.pdf", "image.png", "report.docx"]
# 	- In lần lượt từng tài liệu
while len(printer_queue) > 0:
    current_document = printer_queue.pop(0)
    print("Đang in tài liệu:", current_document)
    print("Tài liệu còn lại trong hàng đợi:", printer_queue)

# Bài 4: Mô phỏng hệ thống hàng đợi khách hàng (OOP)
# Giả sử bạn đang mô phỏng một hàng đợi khách hàng tại một siêu thị. 
# Mỗi khách hàng có một số nhận dạng duy nhất. 
# Viết chương trình sử dụng queue để quản lý khách hàng vào hàng đợi và phục vụ khách hàng.
# Gợi ý: cần 3 phương thức
#     1. arrive: thêm khách hàng vào hàng đợi
#     2. serve: phục vụ khách hàng đầu tiên trong hàng đợi
#     3. waiting: số lượng khách hàng đang chờ
class SupermarketQueue:
    def __init__(self):
        # Danh sách khách hàng đợi thanh toán (thuộc tính)
        self.customers_queue = []

    # Phương thức thêm khách hàng vào hàng đợi (khách mới xếp hàng)
    def arrive(self, customer_name):
        # Thêm khách hàng vào cuối hàng đợi
        self.customers_queue.append(customer_name)
        # Thông báo khách hàng đã đến
        print(f"Khách hàng {customer_name} đã xếp hàng.")

    # Phương thức phục vụ khách hàng đầu tiên trong hàng đợi
    def serve(self):
        if len(self.customers_queue) == 0:
            print("Không có khách hàng nào trong hàng đợi.")
            return None
        # Lấy khách hàng đầu tiên ra khỏi hàng đợi
        served_customer = self.customers_queue.pop(0)
        # Thông báo khách hàng đã được phục vụ
        print(f"Đang phục vụ khách hàng: {served_customer}")
        return served_customer
    
    # Phương thức kiểm tra số lượng khách hàng đang chờ
    def waiting(self):
        # Trả về số lượng khách hàng trong hàng đợi
        print(f"Số lượng khách hàng đang chờ: {len(self.customers_queue)}")

    # Test
    # Tạo đối tượng hàng đợi siêu thị
supermarket_queue = SupermarketQueue()
    # Thêm khách hàng vào hàng đợi
for customer in ["Minh Anh", "Thu Hương", "Lâm Khánh", "Duy Anh", "Tuấn Linh"]:
    supermarket_queue.arrive(customer)
supermarket_queue.waiting()
    # Phục vụ khách hàng theo thứ tự xếp hàng
while len(supermarket_queue.customers_queue) > 0:
    supermarket_queue.serve()
supermarket_queue.waiting()

# Bài 5: Mô phỏng hệ thống nghe nhạc MP3 (OOP)
# Yêu cầu chức năng: 
# 	- Thêm bài hát vào playlist (next up - bài hát phát kế tiếp)
# 	- Kiểm tra playlist (hiển thị các bài trong playlist)
# 	- Nghe bài kế tiếp
# 	- Bỏ qua bài hát (skip)

class MP3Player:
    def __init__(self):
        # Danh sách bài hát trong next-up playlist (thuộc tính)
        self.playlist = []
        # Bài hát hiện tại
        self.current_song = None

    # Phương thức thêm bài hát vào playlist
    def add_song(self, song_name):
        # Thêm bài hát vào cuối playlist
        self.playlist.append(song_name)
        # Thông báo bài hát đã được thêm
        print(f"Đã thêm bài hát '{song_name}' vào playlist.")

    # Phương thức kiểm tra playlist
    def show_playlist(self):
        if len(self.playlist) == 0:
            print("Playlist hiện tại trống.")
        else:
            print("\n========== Playlist hiện tại ==========")
            for index, song in enumerate(self.playlist):
                print(f"{index + 1}. {song}")
            print("========================================")

    # Phương thức nghe bài kế tiếp
    def play_next(self):
        if len(self.playlist) == 0:
            print("Không có bài hát nào trong playlist.")
        else:
            # Lấy bài hát đầu tiên ra khỏi playlist
            self.current_song = self.playlist.pop(0)
            # Thông báo bài hát đang được phát
            print(f"Đang phát bài hát: {self.current_song}")

    # Phương thức bỏ qua bài hát (skip qua 1 bài - nghe bài thứu 2 trong hàng đợi)
    def skip_song(self):
        if len(self.playlist) >= 2:
            # Bỏ qua bài đầu tiên trong hàng đợi
            self.playlist.pop(0)
            # Nghe bài kế tiếp
            self.play_next()
        else:
            print("Không đủ bài hát để skip.")   

    # Hiển thị bài hát đang phát
    def current_song_info(self):
        if self.current_song:
            print(f"Bài hát hiện tại đang phát: {self.current_song}")
        else:
            print("Chưa có bài hát nào đang phát.")

    # Test
    # Khởi tạo MP3 Player
mp3_player = MP3Player()
    # Tạo menu
while True:
    print("\n===== MP3 Player Menu =====")
    print("1. Thêm bài hát vào playlist")
    print("2. Hiển thị playlist")
    print("3. Nghe bài kế tiếp")
    print("4. Bỏ qua bài hát")
    print("5. Hiển thị bài hát hiện tại")
    print("6. Thoát")
    print("=============================")
    # Nhập lựa chọn người dùng
    choice = input("Chọn một tùy chọn (1-6): ")

    match choice:
        case '1':
            song_name = input("Nhập tên bài hát: ")
            if song_name.strip() != "":
                mp3_player.add_song(song_name)
            else:
                print("Tên bài hát không được để trống.")

        case '2':
            mp3_player.show_playlist()

        case '3':
            mp3_player.play_next()

        case '4':
            mp3_player.skip_song()

        case '5':
            mp3_player.current_song_info()

        case '6':
            print("Thoát khỏi MP3 Player.")
            break

        case _: # default (nếu không khớp các case trên)
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")  