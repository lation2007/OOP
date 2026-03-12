import time
tong_giay = time.time()
giay_trong_ngay = 24 * 60 * 60
so_ngay = int(tong_giay // giay_trong_ngay)
giay_con_lai = tong_giay % giay_trong_ngay
gio = int(giay_con_lai // 3600)
phut = int((giay_con_lai % 3600) // 60)
giay = int(giay_con_lai % 60)
print(f"Số ngày kể từ thời điểm gốc: {so_ngay}")
print(f"Thời gian hiện tại : {gio:02d}:{phut:02d}:{giay:02d}")