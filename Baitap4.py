my_list = ["An" , "Bình", "Chi", "Dũng"]
my_list.append("Hà")
my_list.insert(2, "Linh")
my_list.remove("Chi")
position_of_Binh=my_list.index("Bình")
my_list[position_of_Binh]="Bình( đã cập nhât)" 
print(my_list) ## output : ['An', 'Bình( đã cập nhât)', 'Linh', 'Dũng', 'Hà']