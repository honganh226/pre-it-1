my_list = [5,10,15,20,25]
print(my_list[0],my_list[-1])
my_list.append(30) ## thêm 30 vào cuối danh sách
my_list.insert(2, 12) ## thêm 12 vào vị trí thứ 2
if 15 in my_list: ## kiểm tra xem 15 có trong danh sách không
   my_list.remove(15) ## nếu có thì xóa 15 khỏi danh sách
my_list[1] = 99 ## thay thế giá trị tại vị trí thứ 1 bằng 99
print(my_list) ## in ra danh sách