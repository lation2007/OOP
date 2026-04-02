class CanBo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ten = ho_ten
        self.tuoi = tuoi
        self.phai = gioi_tinh
        self.dc = dia_chi

    def lay_chuc_vu(self):
        return "Can bo"

    def xem_thong_tin(self):
        print(f"Ho ten: {self.ten} | Tuoi: {self.tuoi} | Phai: {self.phai} | Dia chi: {self.dc}")

class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac

    def lay_chuc_vu(self):
        return "Cong nhan"

    def xem_thong_tin(self):
        super().xem_thong_tin()
        print(f" => Cap bac: {self.bac}/10")

class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh = nganh

    def lay_chuc_vu(self):
        return "Ky su"

    def xem_thong_tin(self):
        super().xem_thong_tin()
        print(f" => Nganh dao tao: {self.nganh}")

class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.job = cong_viec

    def lay_chuc_vu(self):
        return "Nhan vien"

    def xem_thong_tin(self):
        super().xem_thong_tin()
        print(f" => Cong viec: {self.job}")

class QuanLyCanBo:
    def __init__(self):
        self.danh_sach = []

    def nhap_moi(self):
        print("\n--- THEM MOI ---")
        print("1. Cong nhan | 2. Ky su | 3. Nhan vien")
        loai = input("Chon loai: ")
        
        ten = input("Nhap ho ten: ")
        tuoi = int(input("Nhap tuoi: "))
        phai = input("Gioi tinh: ")
        dc = input("Dia chi: ")

        if loai == "1":
            level = int(input("Bac (1-10): "))
            self.danh_sach.append(CongNhan(ten, tuoi, phai, dc, level))
        elif loai == "2":
            major = input("Nganh hoc: ")
            self.danh_sach.append(KySu(ten, tuoi, phai, dc, major))
        elif loai == "3":
            work = input("Cong viec: ")
            self.danh_sach.append(NhanVien(ten, tuoi, phai, dc, work))
        print("Success: Da luu thong tin!")

    def tim_kiem_ten(self):
        key = input("Nhap ten can tim: ").lower()
        found = [cb for cb in self.danh_sach if key in cb.ten.lower()]
        if not found:
            print("Khong tim thay!")
        else:
            for cb in found:
                cb.xem_thong_tin()

    def show_all(self):
        print(f"\n--- DANH SACH ({len(self.danh_sach)} nguoi) ---")
        for i, cb in enumerate(self.danh_sach, 1):
            print(f"{i}.", end=" ")
            cb.xem_thong_tin()

    def menu(self):
        while True:
            print("\n********** MENU QUAN LY **********")
            print("1. Them | 2. Tim kiem | 3. In DS | 4. Thoat")
            chon = input("Moi chon: ")
            if chon == "1": self.nhap_moi()
            elif chon == "2": self.tim_kiem_ten()
            elif chon == "3": self.show_all()
            elif chon == "4": break
            else: print("Nhap sai, moi nhap lai!")

if __name__ == "__main__":
    app = QuanLyCanBo()
    app.menu()