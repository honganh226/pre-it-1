fruits = {"apple", "banana", "cherry"}  #Tạo một set chứa các phần tử: "apple", "banana", "cherry"
fruits.add("orange")    #Thêm phần tử "orange" vào set
fruits.add("banana")  #Thử thêm lại "banana" vào set (quan sát kết quả) => không có gì thay đổi
fruits.discard("apple") #Xóa phần tử "apple" khỏi set
if "mango" not in fruits: #Kiểm tra "mango" có nằm trong set không
    fruits.add("mango") #Nếu không thì thêm vào
print("Set cuối cùng:", fruits) #In ra set cuối cùng