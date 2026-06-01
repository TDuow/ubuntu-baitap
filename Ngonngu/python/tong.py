n = int(input("Nhap N = "))

tong = 0

for i in range(2, n + 1, 2):
    tong += i

print("Tong cac so chan tu 1 den", n, "la:", tong)
