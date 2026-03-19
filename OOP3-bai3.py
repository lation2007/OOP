class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac, suc_manh):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac
        self.suc_manh = suc_manh
    def __str__(self):
        return f"Ten: {self.ten:12} | Vu khi: {self.vu_khi:10} | Mau: {self.mau_sac:8} | SM: {self.suc_manh}"
ds_sieu_nhan = []
print("--- NHAP THONG TIN SIEU NHAN ---")
print("(De trong ten de dung nhap)\n")
while True:
    ten_sn = input("Nhap ten: ")
    if not ten_sn:
        break
        
    khi_gioi = input("Nhap vu khi: ")
    mau = input("Nhap mau sac: ")
    chi_so = int(input("Nhap chi so suc manh: "))
    moi = SieuNhan(ten_sn, khi_gioi, mau, chi_so)
    ds_sieu_nhan.append(moi)
    print(f"Da luu {ten_sn} vao danh sach.\n")
print(f"\nTONG CONG CO {len(ds_sieu_nhan)} SIEU NHAN:")
for stt, sn in enumerate(ds_sieu_nhan, 1):
    print(f"{stt}. {sn}")