# 1
phut = 42
giay = 42
tong_giay = phut * 60 + giay
print(f"1. Tổng số giây: {tong_giay} giây")

# 2. 
km = 10
so_dam = km / 1.61
print(f"2. 10 km bằng khoảng {so_dam:.2f} dặm")

# 3.
thoi_gian_phut = phut + (giay / 60)
thoi_gian_tren_dam = thoi_gian_phut / so_dam
phut_thuc = int(thoi_gian_tren_dam)
giay_thuc = (thoi_gian_tren_dam - phut_thuc) * 60
print(f"3a. Tốc độ trung bình: {phut_thuc} phút {int(giay_thuc)} giây mỗi dặm")
thoi_gian_gio = thoi_gian_phut / 60
van_toc = so_dam / thoi_gian_gio
print(f"3b. Vận tốc trung bình: {van_toc:.2f} dặm/giờ")
