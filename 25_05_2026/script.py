patient_name = input("Nhập tên bệnh nhân: ")
gender = input("Nhập giới tính (Nam/Nữ): ")
year_of_birth = int(input("Nhập năm sinh: "))
number_phone = input("Nhập số điện thoại: ")
email = input("Nhập email: ")
symptom = input("Nhập triệu chứng: ")
expense = float(input("Nhập chi phí điều trị: "))

import random

patient_id = random.randint(100, 999)

print("\n ----Thẻ bệnh nhân ----")
print(f"Mã bệnh nhân: BN{year_of_birth}{patient_id}")
print(f"Tên: {patient_name} ({type(patient_name).__name__})")
print(f"Giới tính: {gender} ({type(gender).__name__})")
print(f"Năm sinh: {year_of_birth} ({type(year_of_birth).__name__})")
print(f"Số điện thoại: {number_phone} ({type(number_phone).__name__})")
print(f"Email: {email} ({type(email).__name__})")
print(f"Triệu chứng: {symptom} ({type(symptom).__name__})")
print(f"Chi phí điều trị: {expense} VND ({type(expense).__name__})")