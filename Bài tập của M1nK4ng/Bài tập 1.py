numbers = [5, 10, 15, 20, 25]   #Tạo một list chứa các số nguyên: 5, 10, 15, 20, 25
print("Phan tu dau tien:", numbers[0])  #In phần tử đầu tiên 
print("Phan tu cuoi cung:", numbers[-1])    #In phần tử cuối cùng
numbers.append(30)  #Thêm số 30 vào cuối list
numbers.insert(1, 12)   #Chèn số 12 vào vị trí thứ 2
numbers.remove(15)  #Xóa phần tử có giá trị là 15
numbers[1] = 99 #Cập nhật phần tử ở vị trí số 1 thành 99
print("List cuoi cung:", numbers)   #In ra list sau khi thực hiện các thao tác