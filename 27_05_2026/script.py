"""Bài ôn tập"""
# canh = 4
# # Tam giác vuông
# for i in range(canh + 1):  # 0
#     for j in range(canh - i):
#         print(" ", end=" ")
#     for k in range(i):
#         print("*", end=" ")
#     print()

# vuông
# for i in range(4):
#     for j in range(4):
#         print("*", end=" ")
#     print()

# for i in range(canh + 1):
#     for j in range(canh - i + 1):
#         print(" ", end=" ")
#     for k in range(2 * i + 1):
#         print("*", end=" ")
#     print()

N = int(input("Nhập vào 1 số kiểm tra có phải số nguyên tố ko: "))

if N < 2:
    print("Không phải số nguyên tố")
else:
    is_prime = True

    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Là số nguyên tố")
    else:
        print("Không là số nguyên tố")
