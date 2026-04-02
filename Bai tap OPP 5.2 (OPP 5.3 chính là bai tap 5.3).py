BASE_SALARY = 5000000 

class NhanVien:
    def __init__(self, ma, ten, nam, phai, dc, he_so, max_luong):
        self.ma = ma
        self.ten = ten
        self.nam = nam
        self.phai = phai
        self.dc = dc
        self.he_so = he_so if he_so > 0 else 1.0
        self.max_luong = max_luong

    def tinh_luong(self):
        return self.he_so * BASE_SALARY

    def hien_thi(self):
        print(f"ID: {self.ma} | Ten: {self.ten}")
        print(f"NS: {self.nam} | Phai: {self.phai} | DC: {self.dc}")
        print(f"He so: {self.he_so} | Thu nhap: {self.tinh_luong():,.0f} VND")

class CongTacVien(NhanVien):
    def __init__(self, ma, ten, nam, phai, dc, he_so, max_l, thoi_han, phu_cap):
        super().__init__(ma, ten, nam, phai, dc, he_so, max_l)
        self.han_hd = thoi_han
        self.pc_ld = phu_cap

    def tinh_luong(self):
        return super().tinh_luong() + self.pc_ld

    def hien_thi(self):
        print(">>> CONG TAC VIEN <<<")
        super().hien_thi()
        print(f"Thoi han: {self.han_hd} | Phu cap: {self.pc_ld:,.0f} VND")

class NVChinhThuc(NhanVien):
    def __init__(self, ma, ten, nam, phai, dc, he_so, max_l, vi_tri):
        super().__init__(ma, ten, nam, phai, dc, he_so, max_l)
        self.pos = vi_tri

    def hien_thi(self):
        print(">>> NHAN VIEN CHINH THUC <<<")
        super().hien_thi()
        print(f"Vi tri: {self.pos}")

class TruongPhong(NhanVien):
    def __init__(self, ma, ten, nam, phai, dc, he_so, max_l, ngay_bd, phu_cap):
        super().__init__(ma, ten, nam, phai, dc, he_so, max_l)
        self.start_date = ngay_bd
        self.pc_ql = phu_cap

    def tinh_luong(self):
        return super().tinh_luong() + self.pc_ql

    def hien_thi(self):
        print(">>> TRUONG PHONG <<<")
        super().hien_thi()
        print(f"Quan ly tu: {self.start_date} | Phu cap QL: {self.pc_ql:,.0f} VND")

# TEST
if __name__ == "__main__":

    ctv = CongTacVien("CTV01", "Tran Thi B", 2000, "Nu", "Ha Noi", 1.5, 30000000, "6 thang", 1500000)
    nv  = NVChinhThuc("NV01", "Le Van C", 1995, "Nam", "Da Nang", 2.0, 40000000, "Developer")
    tp  = TruongPhong("TP01", "Nguyen Van D", 1985, "Nam", "HCM", 3.0, 50000000, "01/01/2020", 5000000)

    staff_list = [ctv, nv, tp]
    for p in staff_list:
        p.hien_thi()
        print("-" * 30)

    print("\n[ BANG LUONG CHI TIET ]")
    for p in staff_list:
        print(f"{p.ten:<15} : {p.tinh_luong():>12,.0f} VND")