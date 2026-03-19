import math

# --- THU CUNG ---
class ThuCung:
    def __init__(self, ten, loai, mau):
        self.ten = ten
        self.loai = loai
        self.mau = mau

    def phat_am(self, am_thanh):
        print(f"🐾 {self.ten} keu: {am_thanh}! {am_thanh}!")

    def hoat_dong(self, viec_lam):
        print(f"🦴 {self.ten} dang {viec_lam}. Nhin rat dang yeu!")

# --- PHUONG TIEN ---
class XeHoi:
    def __init__(self, nhan_hieu, mau_xe):
        self.nhan_hieu = nhan_hieu
        self.mau_xe = mau_xe
        self.van_toc = 0

    def dieu_khien(self, muc_do):
        self.van_toc += muc_do
        if self.van_toc < 0: self.van_toc = 0
        bieu_tuong = "🚀" if self.van_toc > 80 else "🚗"
        print(f"{bieu_tuong} [{self.nhan_hieu}] Toc do: {self.van_toc} km/h")

    def phanh_gap(self):
        self.van_toc = 0
        print(f"⚠️  NGUY HIEM! Xe {self.nhan_hieu} da dung banh.")

# --- TAI CHINH ---
class NganHang:
    def __init__(self, chu_the, stk, ban_dau=0):
        self.chu_the = chu_the
        self.stk = stk
        self.__quy_tien = ban_dau 

    def nap_tien(self, so_tien):
        self.__quy_tien += so_tien
        print(f"💰 +{so_tien:,} VND | So du moi: {self.__quy_tien:,} VND")

    def lay_tien(self, so_tien):
        if so_tien > self.__quy_tien:
            print(f"❌ Giao dich that bai! So du khong du {so_tien:,} VND")
        else:
            self.__quy_tien -= so_tien
            print(f"💸 -{so_tien:,} VND | Rut tien thanh cong.")

    def xem_so_du(self):
        print(f"💳 TK: {self.chu_the} | So du hien tai: {self.__quy_tien:,} VND")

# --- TEST ---
print("--- DOI TUONG ---")
sn = ThuCung("Lu", "Phu Quoc", "Den")
sn.phat_am("Gau")

xe = XeHoi("VinFast", "Xanh")
xe.dieu_khien(100)
xe.phanh_gap()

tk = NganHang("Tran Van C", "00112233", 2000000)
tk.lay_tien(500000)
tk.xem_so_du()