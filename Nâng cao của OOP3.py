class NhanVien:
    GIOI_HAN_LUONG = 50000000

    def __init__(self, ten, luong_cb, he_so):
        self.__name = ten
        self.__base_pay = luong_cb
        self.__ratio = he_so

    @property
    def ho_ten(self):
        return self.__name

    @ho_ten.setter
    def ho_ten(self, gia_tri):
        if len(gia_tri.strip()) == 0:
            print("❌ Loi: Ten nhan vien khong duoc de trong!")
        else:
            self.__name = gia_tri

    @property
    def muc_luong(self):
        return self.__base_pay

    @muc_luong.setter
    def muc_luong(self, con_so):
        if con_so < 0:
            print("❌ Loi: Muc luong co ban khong the la so am!")
        else:
            self.__base_pay = con_so

    @property
    def he_so(self):
        return self.__ratio

    @he_so.setter
    def he_so(self, hs):
        if hs <= 0:
            print("❌ Loi: He so phai lon hon 0!")
        else:
            self.__ratio = hs

    def tinh_tong_nhan(self):
        return self.__base_pay * self.__ratio

    def hien_thi_chi_tiet(self):
        tong = self.tinh_tong_nhan()
        print("-" * 40)
        print(f"👤 NHAN VIEN: {self.__name.upper()}")
        print(f"💰 Luong co ban: {self.__base_pay:,.0f} VND")
        print(f"📈 He so luong:  {self.__ratio}")
        print(f"💵 Tong thu nhap: {tong:,.0f} VND")
        print("-" * 40)

    def dieu_chinh_luong(self, so_tien_tang):
        du_kien = (self.__base_pay + so_tien_tang) * self.__ratio
        
        if du_kien > NhanVien.GIOI_HAN_LUONG:
            print(f"⚠️  CANH BAO: Luong moi ({du_kien:,.0f}) vuot muc tran {NhanVien.GIOI_HAN_LUONG:,.0f}!")
            return False
        
        self.__base_pay += so_tien_tang
        print(f"✅ Cap nhat thanh cong! Luong moi: {self.tinh_tong_nhan():,.0f} VND")
        return True

# --- TEST ---
nv1 = NhanVien("Nguyen Van A", 10000000, 3.0)
nv1.hien_thi_chi_tiet()

# tang luong lan 1
nv1.dieu_chinh_luong(5000000)

# tang luong lan 2 
nv1.dieu_chinh_luong(10000000)