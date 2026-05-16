# Bài 1: Nhập họ tên từ bàn phím. 
# Chuẩn hóa họ tên: Xóa khoảng trắng dư thừa, viết hoa chữ cái đầu mỗi từ
text = '   bUi    DuC     tRuNg      '
words = text.split()
result = ""
for word in words:
    new_word = word[0].upper() + word[1:].lower()
    result += new_word + " "
print(result.strip())

# Bài 2: Nhập vào 1 xâu ký tự định dạng dd/mm/yyyy (01/08/2024)
    # Tách ngày, tháng, năm và hiển thị ra màn hình
date1 = '16/05/2026'

    # Cách 1: split()
x = date1.split('/')
day = x[0]
month = x[1]
year = x[2]
print("Ngày:", day, '\nTháng:', month, '\nNăm:', year)

    # Cách 2: dùng replace()
date2 = date1.replace('/', ' tháng ', 1)
date3 = date2.replace('/', ' năm ', 1)
print(date3)

# Bài 3: Nhập vào một chuỗi bất kỳ.
    # Đếm xem trong chuỗi có bao nhiêu ký tự đặc biệt.
    # Biết ký tự đặc biệt là ký tự không phải chữ cái, số, khoảng trắng
text = 'sample text! @special #characters$'
count = 0
for char in text:
    if not char.isalpha() and not char.isdigit() and char != " ":
        count += 1
print("Số ký tự đặc biệt:", count)

# Bài 4: Nhập vào một câu. Tìm từ có độ dài lớn nhất.
    # Nếu có nhiều từ cùng độ dài, in ra từ xuất hiện đầu tiên.
text = 'this is a sample sentence for testing'
words = text.split()
longest_word = words[0]
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("Từ dài nhất:", longest_word)

# Bài 5: Nhập vào một chuỗi.
    # Xóa các ký tự bị lặp, chỉ giữ lần xuất hiện đầu tiên.
text =  'abcd abcde abcdeghi abc'
result = ""
for char in text:
    if char not in result:
        result += char
print("Kết quả:", result)