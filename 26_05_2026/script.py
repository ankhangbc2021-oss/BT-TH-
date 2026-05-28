"""Bài toán tìm bội chung nhỏ nhất"""

# Start code
A = 13
B = 3

max_val = A if A > B else B
while True:
    if max_val % A == 0 and max_val % B == 0:
        print(f"BCNN: {max_val}")
        break
    max_val += 1
