cacngaytrongtuan = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
#Tạo một tuple chứa tên các ngày trong tuần
print("Thứ 2:", cacngaytrongtuan[0])    #In ra thứ 2 theo chỉ số
print("Thứ 6:", cacngaytrongtuan[4])    #In ra thứ 6 theo chỉ số
cacngaytrongtuan_list = list(cacngaytrongtuan) #Chuyển tuple sang list
cacngaytrongtuan_list.append("Funday")  #Thêm một ngày "Funday" vào cuối
updated_cacngaytrongtuans = tuple(cacngaytrongtuan_list)    #Chuyển lại thành tuple
print("Tuple sau khi thêm Funday:", updated_cacngaytrongtuans)  #In kết quả cuối cùng