class NhanVien:
    LUONG_MAX = 50000000

    def __init__(self, ten, luong_cb, he_so):
        self.__name = ten
        self.__base_salary = luong_cb
        self.__ratio = he_so

    def get_ten(self):
        return self.__name

    def get_luong_cb(self):
        return self.__base_salary

    def get_he_so(self):
        return self.__ratio

    def set_ten(self, ten_moi):
        self.__name = ten_moi

    def set_luong_cb(self, so_tien):
        if so_tien >= 0:
            self.__base_salary = so_tien
        else:
            print("⚠️ Loi: Luong co ban khong duoc am!")

    def set_he_so(self, chi_so):
        if chi_so > 0:
            self.__ratio = chi_so
        else:
            print("⚠️ Loi: He so phai lon hon 0!")

    def tinh_luong(self):
        return self.__base_salary * self.__ratio

    def in_thong_tin(self):
        print("\n--- 📝 HO SO NHAN VIEN ---")
        print(f"Ho ten: {self.__name}")
        print(f"Luong CB: {self.__base_salary:,.0f} VND")
        print(f"He so: {self.__ratio}")
        print(f"💰 Thuc linh: {self.tinh_luong():,.0f} VND")
        print("-" * 25)

    def tang_luong(self, delta):
        he_so_du_kien = self.__ratio + delta
        luong_du_kien = self.__base_salary * he_so_du_kien
        
        if luong_du_kien > NhanVien.LUONG_MAX:
            print(f"❌ Khong the tang! Luong du kien ({luong_du_kien:,.0f}) vuot muc tran.")
            return False
        
        self.__ratio = he_so_du_kien
        print(f"✅ Da tang he so len {self.__ratio}. Luong moi: {self.tinh_luong():,.0f}")
        return True

# TEST
if __name__ == "__main__":
    nv1 = NhanVien("Nguyen Van A", 10000000, 2.0)
    nv1.in_thong_tin()

    nv1.tang_luong(0.5)
    nv1.tang_luong(3.5) 

    print(f"\nKiem tra ten qua Getter: {nv1.get_ten()}")
    nv1.set_luong_cb(15000000)
    print(f"Sau khi thay doi Luong CB: {nv1.get_luong_cb():,.0f}")