date_of_birth = input("Nhập năm sinh: ")

import datetime

current_year = datetime.datetime.now().year

age = current_year - int(date_of_birth)

if age % 2 == 0:
    print("Tuổi tốt")
else:
    print("Tuổi xấu")

# Yêu cầu 2

gender = input("Nhập giới tính (Nam/Nữ): ").strip()
while gender not in ["Nam", "Nữ"]:
    print("Giới tính không hợp lệ. Vui lòng nhập lại.")
    gender = input("Nhập giới tính (Nam/Nữ): ").strip()

if age > 30:
    print("Quá già để kết hôn")
elif (gender == "Nam" and age > 18):
    print("Đủ tuổi lấy vợ")
elif (gender == "Nữ" and age > 16):
    print("Đủ tuổi lấy chồng")
else:
    print("Chưa đủ tuổi kết hôn")
