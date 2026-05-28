"""
BÀI KIỂM TRA ĐÁNH GIÁ NĂNG LỰC ĐẦU VÀO PROJECT
Môn học: Lập trình Python cơ bản
Thời gian làm bài: 45 phút
"""

# Câu 1
print("----Câu 1----")
unit_price = int(input("Nhập đơn giá sản phẩm: "))
quantity = int(input("Nhập số lượng: "))

total_price = unit_price * quantity

if total_price >= 1000000:
    DISCOUNT = total_price * 0.1
else:
    DISCOUNT = 0


print(f"Tổng số tiền khách hàng phải thanh toán là: {int(total_price - DISCOUNT):,}")

# Câu 2
print("----Câu 2----")
BINDING = 1

while True:
    password = input("Nhập mật khẩu để đăng nhập: ")

    if BINDING > 2:
        print("Tài khoản đã bị khóa!")
        break
    elif password != "123456":
        print("Mật khẩu sai, vui lòng nhập lại!")
        BINDING += 1
    else:
        print("Đăng nhập thành công!")
        break

# Câu 3
print("----Câu 3----")
total_products = 0
total_box_true = 0

total_product = int(input("Nhập tổng số lượng sản phẩm: "))
while True:
    number_of_boxes_check = int(input("Nhập số lượng thùng hàng hợp lệ"))

    if number_of_boxes_check < 0:
        print("Số lượng không hợp lệ, bỏ qua thùng này!")
    elif number_of_boxes_check > 0:
        total_box_true += 1
    else:
        break
total_products = total_product * total_box_true

print(f"Tổng số thùng hàng hợp lệ đã đếm: {total_box_true}")
print(f"Tổng số lượng sản phẩm thu được: {total_products}")