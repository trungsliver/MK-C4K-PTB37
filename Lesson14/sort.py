arr = [64, 25, 12, 22, 11, 90, 34, 78, 56, 43]

# ========= SELECTION SORT ==========
def selection_sort(arr):        # Độ phức tạp: O(n^2)
    # Duyệt từ phần từ đầu tiên đên phần tử cuối cùng
    for i in range(len(arr)):
        # Giả sử phần tử min nằm ở vị trí i
        min_index = i
        # Tìm vị trí phần tử nhỏ nhất trong phần còn lại
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Đổi chỗ arr[i] với phần tử nhỏ nhất tìm được
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print("Selection Sort:", selection_sort(arr))

# ========= BUBBLE SORT ==========
def bubble_sort(arr):           # Độ phức tạp: O(n^2)
    # Duyệt qua tất cả các phần tử trong mảng
    for i in range(len(arr)):
        # So sanh các phần tử cạnh nhau
        for j in range(0, len(arr) - i - 1):
            # Nếu phần tử hiện tại lớn hơn phần tử kế tiếp thì đổi chỗ
            if arr[j] > arr[j + 1]:
                # Đổi chỗ 2 phần tử
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print("Bubble Sort:", bubble_sort(arr))

# ========= INSERTION SORT ==========
    # Giống xếp bài tú lơ khơ trên tay
def insertion_sort(arr):        # Độ phức tạp: O(n^2)
    # Duyệt từ phần tử thứ hai đến phần tử cuối cùng
    for i in range(1, len(arr)):
        # Phần tử cần chèn
        key = arr[i]
        # So sánh key với các phần tử trước nó  
        j = i - 1
        # Dịch chuyển các phần tử lớn hơn key về bên phải
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Chèn key vào vị trí đúng
        arr[j + 1] = key
    return arr

print("Insertion Sort:", insertion_sort(arr))

