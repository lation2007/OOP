import math

# 1.Thể tích hình cầu 
# V = (4/3) * pi * r^3
r = 5
the_tich = (4/3) * math.pi * (r**3)
print(f"1. Thể tích hình cầu bán kính 5: {the_tich:.2f}")

# 2. Chi phí mua 60 cuốn sách
gia_bia = 24.95
giam_gia = 0.40
gia_sau_giam = gia_bia * (1 - giam_gia)
so_luong = 60
phi_van_chuyen = 3 + (so_luong - 1) * 0.75
tong_chi_phi = (gia_sau_giam * so_luong) + phi_van_chuyen
print(f"2. Tổng chi phí cho 60 cuốn: ${tong_chi_phi:.2f}")

# 3. Tính thời gian về nhà
thoi_gian_chay = (8.25 * 1) + (7.2 * 3) + (8.25 * 1)
gio_khoi_hanh = 6 + (52 / 60) # 6 giờ 52 phút
gio_ve_nha = gio_khoi_hanh + (thoi_gian_chay / 60)
gio_thuc = int(gio_ve_nha)
phut_thuc = int((gio_ve_nha - gio_thuc) * 60)
print(f"3. Thời gian về nhà: {gio_thuc}:{phut_thuc:02d} sáng")