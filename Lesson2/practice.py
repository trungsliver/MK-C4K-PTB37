# Bài 1: Chuyển đổi USD sang VND
    # Nhập số lượng USD muốn chuyển đổi (float)
usd = float(input("Nhập số lượng USD muốn chuyển đổi: "))
    # Đổi USD sang VND, tỉ giá 1 USD = 27000 VND
vnd = usd * 27000
    # Hiển thị số tiền sau chuyển đổi (VD: 10 USD = 250000 VND)
print(f'{usd} USD = {vnd} VND')

# Bài 2: Nhập chiều dài, chiều rộng hình chữ nhật.
# Tính chu vi, diện tích HCN và hiển thị ra màn hình
    # Nhập chiều dài, chiều rộng HCN (float)
cd = float(input('Nhập chiều dài: '))
cr = float(input('Nhập chiều rộng: '))
    # Tính chu vi, diện tích HCN
cvi = (cd + cr) * 2
dt = cd * cr
    # Hiển thị kết quả
print('Chu vi HCN:', cvi)
print('Diện tích HCN:', dt)
