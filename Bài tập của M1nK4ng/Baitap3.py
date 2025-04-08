students = ["An", "Bình", "Chi", "Dũng"]    #Tạo một list chứa tên các sinh viên: "An", "Bình", "Chi", "Dũng"
students.append("Hà")   #Thêm một sinh viên "Hà" vào cuối
students.insert(1, "Linh")  #Chèn "Linh" vào vị trí thứ 2
students.remove("Chi")  #Xóa sinh viên "Chi"
for i in range(len(students)):  #Đặt điều kiện, Vòng lặp index trong range(4)
    if students[i] == "Bình":   #Nếu index == "Bình"
        students[i] = "Bình (đã cập nhật)"  #Gán index = "Bình (đã cập nhật)"
#Sửa tên "Bình" thành "Bình (đã cập nhật)"
print("Danh sách sinh viên cuối cùng:", students)
