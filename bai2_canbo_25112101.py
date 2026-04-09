from abc import ABC, abstractmethod

# -------------------------------------------------------------------
# 1. CUSTOM EXCEPTIONS
# -------------------------------------------------------------------
class TuoiKhongHopLe(Exception):
    def __init__(self, tuoi):
        self.tuoi = tuoi
        super().__init__(f"Loi: Tuoi {tuoi} khong nam trong pham vi cho phep (18-65).")

class BacKhongHopLe(Exception):
    def __init__(self, bac):
        self.bac = bac
        super().__init__(f"Loi: Bac tho {bac} phai nam trong khoang tu 1 den 10.")

# -------------------------------------------------------------------
# 2. LỚP TRỪU TƯỢNG CANBO 
# -------------------------------------------------------------------
class CanBo(ABC):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.__ho_ten = ho_ten
        self.tuoi = tuoi  # Su dung setter de kiem tra logic
        self.__gioi_tinh = gioi_tinh
        self.__dia_chi = dia_chi

    @property
    def ho_ten(self):
        return self.__ho_ten

    @property
    def tuoi(self):
        return self.__tuoi

    @tuoi.setter
    def tuoi(self, value):
        if not (18 <= value <= 65):
            raise TuoiKhongHopLe(value)
        self.__tuoi = value

    @abstractmethod
    def mo_ta(self):
        """Phuong thuc truu tuong - Cac lop con bat buoc phai ghi de."""
        pass

    def __str__(self):
        # Su dung da hinh: self.mo_ta() se goi dung ham cua lop con tuong ung
        return f"{self.__ho_ten:<15} | {self.__tuoi} tuoi | {self.__gioi_tinh:<5} | {self.mo_ta()}"

    def __repr__(self):
        return f"{self.__class__.__name__}(ten='{self.__ho_ten}', tuoi={self.__tuoi})"

    def __eq__(self, other):
        if not isinstance(other, CanBo):
            return False
        # So sanh dua tren ca Ten va Tuoi
        return self.__ho_ten == other.ho_ten and self.__tuoi == other.tuoi

    def __lt__(self, other):
        # Ho tro sap xep danh sach theo Ho ten (A-Z)
        return self.__ho_ten < other.ho_ten

    def __hash__(self):
        return hash((self.__ho_ten, self.__tuoi))

# -------------------------------------------------------------------
# 3. CÁC LỚP CON CHI TIẾT
# -------------------------------------------------------------------
class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac  # Su dung setter de validate

    @property
    def bac(self):
        return self.__bac

    @bac.setter
    def bac(self, value):
        if not (1 <= value <= 10):
            raise BacKhongHopLe(value)
        self.__bac = value

    def mo_ta(self):
        return f"Cong nhan bac {self.__bac}/10"

class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dt):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.__nganh_dt = nganh_dt

    def mo_ta(self):
        return f"Ky su nganh {self.__nganh_dt}"

class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.__cong_viec = cong_viec

    def mo_ta(self):
        return f"Nhan vien: {self.__cong_viec}"

# -------------------------------------------------------------------
# 4. DEMO
# -------------------------------------------------------------------
if __name__ == "__main__":
    # Khoi tao danh sach can bo
    danh_sach = [
        CongNhan("Nguyen Van A", 30, "Nam", "Ha Noi", 5),
        KySu("Tran Thi B", 28, "Nu", "TP HCM", "CNTT"),
        NhanVien("Le Van C", 35, "Nam", "Da Nang", "Ke toan")
    ]

    print("--- 1. HIEN THI DANH SACH (Da hinh & __str__) ---")
    for cb in danh_sach:
        print(cb)

    print("\n--- 2. SAP XEP THEO TEN (Nho magic method __lt__) ---")
    for cb in sorted(danh_sach):
        print(f"  {cb.ho_ten}")

    print("\n--- 3. KIEM TRA LOGIC BAT LOI (Validation) ---")
    try:
        print(" Dang thu tao Cong nhan 15 tuoi...")
        cn_loi_tuoi = CongNhan("Tre Em", 15, "Nam", "HN", 5)
    except TuoiKhongHopLe as e:
        print(f"  Thong bao: {e}")

    try:
        print(" Dang thu tao Cong nhan bac 12...")
        cn_loi_bac = CongNhan("Tho Ca", 25, "Nu", "HN", 12)
    except BacKhongHopLe as e:
        print(f"  Thong bao: {e}")

    print("\n--- 4. LUU TRU DU LIEU (With Context Manager) ---")
    try:
        with open("danh_sach_can_bo.txt", "w", encoding="utf-8") as f:
            for cb in danh_sach:
                f.write(str(cb) + "\n")
        print(f"  Luu thanh cong {len(danh_sach)} can bo vao file 'danh_sach_can_bo.txt'.")
    except Exception as e:
        print(f"  Loi khi luu file: {e}")